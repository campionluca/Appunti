#!/usr/bin/env python3
import json
import os
import sys
import uuid
import time
import datetime
import threading
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
WEB_DIR = os.path.join(os.path.dirname(__file__), "web")
DB_PATH = os.path.join(os.path.dirname(__file__), "tasks_db.json")
BACKUP_DIR = os.path.join(ROOT, "logs", "task_backups")

lock = threading.Lock()
SUBSCRIBERS = set()


def now_iso():
    return datetime.datetime.now().isoformat(timespec="seconds")


def ensure_dirs():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    os.makedirs(BACKUP_DIR, exist_ok=True)
    os.makedirs(WEB_DIR, exist_ok=True)


def load_db():
    ensure_dirs()
    if not os.path.exists(DB_PATH):
        data = {
            "version": "1.0",
            "last_updated": now_iso(),
            "tasks": []
        }
        save_db(data)
        return data
    with open(DB_PATH, "r", encoding="utf-8", errors="replace") as f:
        return json.load(f)


def save_db(data):
    data["last_updated"] = now_iso()
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def sse_headers(handler):
    handler.send_response(200)
    handler.send_header("Content-Type", "text/event-stream")
    handler.send_header("Cache-Control", "no-cache")
    handler.send_header("Connection", "keep-alive")
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.end_headers()


def sse_send(wfile, event, payload):
    try:
        body = json.dumps(payload, ensure_ascii=False)
        wfile.write(f"event: {event}\n".encode("utf-8"))
        wfile.write(f"data: {body}\n\n".encode("utf-8"))
        try:
            wfile.flush()
        except Exception:
            pass
        return True
    except Exception:
        return False


def broadcast(event, payload):
    stale = []
    for wfile in list(SUBSCRIBERS):
        ok = sse_send(wfile, event, payload)
        if not ok:
            stale.append(wfile)
    for s in stale:
        try:
            SUBSCRIBERS.remove(s)
        except KeyError:
            pass


def backup_db(data):
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(BACKUP_DIR, f"tasks_backup_{ts}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return path


def json_response(handler, status, payload, headers=None):
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.send_header("Access-Control-Allow-Headers", "Content-Type")
    handler.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
    if headers:
        for k, v in headers.items():
            handler.send_header(k, v)
    handler.end_headers()
    handler.wfile.write(body)


def read_json(handler):
    length = int(handler.headers.get("Content-Length", "0") or 0)
    if length <= 0:
        return {}
    raw = handler.rfile.read(length)
    try:
        return json.loads(raw.decode("utf-8"))
    except Exception:
        return {}


def find_task(tasks, tid):
    for t in tasks:
        if t.get("id") == tid:
            return t
    return None


class TaskHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Serve static files from WEB_DIR by default
        if path.startswith("/api/"):
            return path
        # map to web dir
        rel = path.lstrip("/") or "index.html"
        return os.path.join(WEB_DIR, rel)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.end_headers()

    def do_GET(self):
        if self.path.startswith("/api/"):
            self.handle_api_get()
        else:
            super().do_GET()

    def do_POST(self):
        if self.path.startswith("/api/"):
            self.handle_api_post()
        else:
            super().do_POST()

    def do_PUT(self):
        if self.path.startswith("/api/"):
            self.handle_api_put()
        else:
            self.send_error(405, "Method Not Allowed")

    def do_DELETE(self):
        if self.path.startswith("/api/"):
            self.handle_api_delete()
        else:
            self.send_error(405, "Method Not Allowed")

    def handle_api_get(self):
        parsed = urlparse(self.path)
        if parsed.path == "/api/tasks":
            with lock:
                data = load_db()
            return json_response(self, 200, data)
        elif parsed.path == "/api/events":
            # Server-Sent Events for realtime updates
            sse_headers(self)
            SUBSCRIBERS.add(self.wfile)
            # send initial hello and last_updated
            with lock:
                data = load_db()
            sse_send(self.wfile, "hello", {"last_updated": data.get("last_updated")})
            try:
                while True:
                    # keep-alive comment every 15s
                    try:
                        self.wfile.write(b": ping\n\n")
                        self.wfile.flush()
                    except Exception:
                        break
                    time.sleep(15)
            finally:
                try:
                    SUBSCRIBERS.remove(self.wfile)
                except KeyError:
                    pass
            return
        elif parsed.path == "/api/changes":
            qs = parse_qs(parsed.query)
            since = (qs.get("since", [""])[0])
            with lock:
                data = load_db()
            # naive: return all tasks and last_updated for simplicity
            return json_response(self, 200, {"last_updated": data.get("last_updated"), "tasks": data.get("tasks", [])})
        elif parsed.path == "/api/backup":
            with lock:
                data = load_db()
                path = backup_db(data)
            return json_response(self, 200, {"backup_path": os.path.relpath(path, ROOT)})
        else:
            self.send_error(404, "Not Found")

    def handle_api_post(self):
        parsed = urlparse(self.path)
        if parsed.path == "/api/tasks":
            payload = read_json(self)
            required = ["title", "description", "priority", "deadline", "assignee"]
            for r in required:
                if not payload.get(r):
                    return json_response(self, 400, {"error": f"Campo mancante: {r}"})
            task = {
                "id": uuid.uuid4().hex[:12],
                "title": payload["title"],
                "description": payload["description"],
                "priority": payload.get("priority", "media"),
                "deadline": payload.get("deadline", ""),
                "assignee": payload.get("assignee", ""),
                "project": payload.get("project", "Generale"),
                "status": payload.get("status", "da_fare"),
                "type": payload.get("type", "Generico"),
                "history": [{"ts": now_iso(), "action": "create", "by": payload.get("assignee", "system")}],
                "time_tracking": [],
                "comments": [],
                "created_at": now_iso(),
                "updated_at": now_iso(),
            }
            with lock:
                data = load_db()
                data["tasks"].append(task)
                save_db(data)
            broadcast("update", {"type": "create", "task": {"id": task["id"], "status": task["status"], "project": task.get("project")}, "last_updated": data.get("last_updated")})
            return json_response(self, 201, task)

        # actions on task
        if parsed.path.startswith("/api/tasks/") and parsed.path.endswith("/start"):
            tid = parsed.path.split("/")[3]
            with lock:
                data = load_db()
                task = find_task(data["tasks"], tid)
                if not task:
                    return json_response(self, 404, {"error": "Task non trovata"})
                task["time_tracking"].append({"start": now_iso(), "end": None, "duration_seconds": 0})
                task["history"].append({"ts": now_iso(), "action": "time_start", "by": task.get("assignee","")})
                task["updated_at"] = now_iso()
                save_db(data)
            broadcast("update", {"type": "time_start", "task": {"id": tid}})
            return json_response(self, 200, task)

        if parsed.path.startswith("/api/tasks/") and parsed.path.endswith("/stop"):
            tid = parsed.path.split("/")[3]
            with lock:
                data = load_db()
                task = find_task(data["tasks"], tid)
                if not task:
                    return json_response(self, 404, {"error": "Task non trovata"})
                # close last open session
                sessions = task.get("time_tracking", [])
                if sessions and sessions[-1]["end"] is None:
                    sessions[-1]["end"] = now_iso()
                    try:
                        dt_start = datetime.datetime.fromisoformat(sessions[-1]["start"])
                        dt_end = datetime.datetime.fromisoformat(sessions[-1]["end"])
                        sessions[-1]["duration_seconds"] = int((dt_end - dt_start).total_seconds())
                    except Exception:
                        sessions[-1]["duration_seconds"] = 0
                task["history"].append({"ts": now_iso(), "action": "time_stop", "by": task.get("assignee","")})
                task["updated_at"] = now_iso()
                save_db(data)
            broadcast("update", {"type": "time_stop", "task": {"id": tid}})
            return json_response(self, 200, task)

        if parsed.path.startswith("/api/tasks/") and parsed.path.endswith("/comment"):
            tid = parsed.path.split("/")[3]
            payload = read_json(self)
            with lock:
                data = load_db()
                task = find_task(data["tasks"], tid)
                if not task:
                    return json_response(self, 404, {"error": "Task non trovata"})
                task.setdefault("comments", []).append({
                    "author": payload.get("author", ""),
                    "text": payload.get("text", ""),
                    "ts": now_iso(),
                })
                task["history"].append({"ts": now_iso(), "action": "comment", "by": payload.get("author","")})
                task["updated_at"] = now_iso()
                save_db(data)
            broadcast("update", {"type": "comment", "task": {"id": tid}})
            return json_response(self, 200, task)

        return self.send_error(404, "Not Found")

    def handle_api_put(self):
        parsed = urlparse(self.path)
        if parsed.path.startswith("/api/tasks/"):
            tid = parsed.path.split("/")[3]
            payload = read_json(self)
            with lock:
                data = load_db()
                task = find_task(data["tasks"], tid)
                if not task:
                    return json_response(self, 404, {"error": "Task non trovata"})
                before = task.copy()
                for k in ["title","description","priority","deadline","assignee","project","status","type"]:
                    if k in payload:
                        task[k] = payload[k]
                task["history"].append({"ts": now_iso(), "action": "update", "by": payload.get("actor",""), "diff": {
                    k: {"old": before.get(k), "new": task.get(k)} for k in payload.keys()
                }})
                task["updated_at"] = now_iso()
                save_db(data)
            broadcast("update", {"type": "update", "task": {"id": tid}})
            return json_response(self, 200, task)
        return self.send_error(404, "Not Found")

    def handle_api_delete(self):
        parsed = urlparse(self.path)
        if parsed.path.startswith("/api/tasks/"):
            tid = parsed.path.split("/")[3]
            with lock:
                data = load_db()
                before_count = len(data["tasks"])
                data["tasks"] = [t for t in data["tasks"] if t.get("id") != tid]
                after_count = len(data["tasks"])
                save_db(data)
            if after_count < before_count:
                broadcast("update", {"type": "delete", "task": {"id": tid}})
                return json_response(self, 200, {"deleted": tid})
            return json_response(self, 404, {"error": "Task non trovata"})
        return self.send_error(404, "Not Found")


def run(port=8003):
    ensure_dirs()
    os.chdir(ROOT)  # for relative backup paths
    server = ThreadingHTTPServer(("", port), TaskHandler)
    print(f"Task server running on http://localhost:{port}/")
    print(f"Static web dir: {WEB_DIR}")
    server.serve_forever()


if __name__ == "__main__":
    p = 8003
    if len(sys.argv) > 1:
        try:
            p = int(sys.argv[1])
        except Exception:
            pass
    run(p)

