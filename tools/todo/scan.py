#!/usr/bin/env python3
import argparse
import os
import re
import sys
import json
import hashlib
import datetime
from typing import List, Dict, Any, Tuple


SUPPORTED_EXTENSIONS = {".php", ".js", ".html", ".css"}
KEYWORDS = ["TODO", "FIXME", "NOTE"]


def parse_args():
    parser = argparse.ArgumentParser(
        description="Scanner TODO/FIXME/NOTE per progetti web (php/js/html/css)"
    )
    parser.add_argument(
        "--scan",
        type=str,
        default="",
        help="Percorsi da scansionare separati da ';' o ',' (default: cartella corrente)",
    )
    parser.add_argument(
        "--consolidate",
        action="store_true",
        help="Consolidare con MASTER-TODO.json esistente",
    )
    parser.add_argument(
        "--execute",
        type=int,
        default=0,
        help="Numero di TODO da marcare come completati (e annotare nel codice)",
    )
    parser.add_argument(
        "--output",
        type=str,
        choices=["json", "none"],
        default="json",
        help="Scrive MASTER-TODO.json (json) oppure non scrive (none)",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Genera report HTML in logs/todo_reports/",
    )
    return parser.parse_args()


def is_supported(path: str) -> bool:
    _, ext = os.path.splitext(path)
    return ext.lower() in SUPPORTED_EXTENSIONS


def read_file_lines(path: str) -> List[str]:
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.readlines()
    except Exception:
        return []


def detect_author_and_date(comment: str) -> Tuple[str, str]:
    author = ""
    date = ""
    # Cerca @username o by: Nome
    m = re.search(r"@([A-Za-z0-9_\-\.]+)", comment)
    if m:
        author = m.group(1)
    else:
        m2 = re.search(r"\bby:\s*([^,;\]\)\n]+)", comment, re.IGNORECASE)
        if m2:
            author = m2.group(1).strip()
    # Cerca date in formato YYYY-MM-DD
    m3 = re.search(r"(20\d{2}-\d{2}-\d{2})", comment)
    if m3:
        date = m3.group(1)
    return author, date


def classify_priority(kind: str) -> str:
    kind = kind.upper()
    if kind == "FIXME":
        return "urgent"
    if kind == "TODO":
        return "important"
    return "secondary"


def make_id(record: Dict[str, Any]) -> str:
    h = hashlib.sha256()
    base = f"{record.get('file','')}:{record.get('line',0)}:{record.get('kind','')}:{record.get('text','').strip()}"
    h.update(base.encode("utf-8", errors="replace"))
    return h.hexdigest()[:16]


def scan_file(path: str) -> List[Dict[str, Any]]:
    lines = read_file_lines(path)
    results = []
    # Supporta commenti inline: //, #, <!-- -->, /* */
    for idx, raw in enumerate(lines, start=1):
        line = raw.strip()
        matches = []
        # JS/PHP line comments
        m_slash = re.search(r"//\s*(TODO|FIXME|NOTE)\s*:?(.*)$", line, re.IGNORECASE)
        if m_slash:
            matches.append((m_slash.group(1).upper(), m_slash.group(2)))
        m_hash = re.search(r"#\s*(TODO|FIXME|NOTE)\s*:?(.*)$", line, re.IGNORECASE)
        if m_hash:
            matches.append((m_hash.group(1).upper(), m_hash.group(2)))
        # HTML comments
        m_html = re.search(r"<!--\s*(TODO|FIXME|NOTE)\s*:?(.*?)-->", line, re.IGNORECASE)
        if m_html:
            matches.append((m_html.group(1).upper(), m_html.group(2)))
        # CSS inline (line) or part of block on same line
        m_css = re.search(r"/\*\s*(TODO|FIXME|NOTE)\s*:?(.*?)\*/", line, re.IGNORECASE)
        if m_css:
            matches.append((m_css.group(1).upper(), m_css.group(2)))

        for kind, text in matches:
            author, date = detect_author_and_date(text or "")
            rec = {
                "kind": kind,
                "text": (text or "").strip(),
                "file": os.path.relpath(path, start=os.getcwd()),
                "abs_file": os.path.abspath(path),
                "line": idx,
                "author": author,
                "date": date,
                "priority": classify_priority(kind),
                "status": "pending",
            }
            rec["id"] = make_id(rec)
            results.append(rec)
    return results


def walk_paths(roots: List[str]) -> List[str]:
    files = []
    for root in roots:
        base = os.path.abspath(root)
        if not os.path.exists(base):
            continue
        if os.path.isfile(base):
            if is_supported(base):
                files.append(base)
            continue
        for dirpath, _, filenames in os.walk(base):
            for fn in filenames:
                path = os.path.join(dirpath, fn)
                if is_supported(path):
                    files.append(path)
    return files


def load_master(path: str) -> Dict[str, Any]:
    if not os.path.exists(path):
        return {"items": []}
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            data = json.load(f)
            # Supporta formato legacy: lista pura
            if isinstance(data, list):
                return {"items": data}
            if isinstance(data, dict) and "items" in data:
                return data
            # Altri formati: tenta normalizzazione
            return {"items": data.get("items", []) if isinstance(data, dict) else []}
    except Exception:
        return {"items": []}


def save_master(path: str, data: Dict[str, Any]):
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def consolidate(master: Dict[str, Any], found_items: List[Dict[str, Any]]) -> Dict[str, Any]:
    by_id = {item["id"]: item for item in master.get("items", [])}
    for item in found_items:
        if item["id"] in by_id:
            # Aggiorna metadati (file/line potrebbero cambiare)
            existing = by_id[item["id"]]
            existing.update({
                "file": item["file"],
                "abs_file": item["abs_file"],
                "line": item["line"],
                "priority": item["priority"],
            })
        else:
            by_id[item["id"]] = item
    # Filtra elementi non più presenti: mantieni ma aggiungi flag missing
    current_ids = {i["id"] for i in found_items}
    for iid, itm in by_id.items():
        itm["missing"] = iid not in current_ids
    return {"items": list(by_id.values())}


def mark_completed_in_source(item: Dict[str, Any]) -> bool:
    path = item.get("abs_file", "")
    line_no = item.get("line", 0)
    if not os.path.exists(path) or line_no <= 0:
        return False
    lines = read_file_lines(path)
    if not lines:
        return False
    idx = line_no - 1
    stamp = datetime.date.today().isoformat()
    marker = f" [COMPLETATO {stamp}]"
    try:
        lines[idx] = lines[idx].rstrip("\n") + marker + "\n"
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        return True
    except Exception:
        return False


def execute_items(master: Dict[str, Any], count: int) -> int:
    if count <= 0:
        return 0
    pending = [i for i in master.get("items", []) if i.get("status") == "pending" and not i.get("missing")]
    done = 0
    for item in pending[:count]:
        ok = mark_completed_in_source(item)
        if ok:
            item["status"] = "completed"
            item["completed_at"] = datetime.datetime.now().isoformat(timespec="seconds")
            done += 1
    return done


def generate_report(master: Dict[str, Any]) -> str:
    out_dir = os.path.join("logs", "todo_reports")
    os.makedirs(out_dir, exist_ok=True)
    stamp = datetime.date.today().isoformat()
    out_path = os.path.join(out_dir, f"report_{stamp}.html")
    items = master.get("items", [])
    total = len(items)
    completed = sum(1 for i in items if i.get("status") == "completed")
    pending = sum(1 for i in items if i.get("status") == "pending")
    urgent = sum(1 for i in items if i.get("priority") == "urgent")

    def row(i: Dict[str, Any]) -> str:
        return (
            f"<tr>"
            f"<td>{i.get('kind')}</td>"
            f"<td>{i.get('priority')}</td>"
            f"<td>{i.get('status')}</td>"
            f"<td>{i.get('file')}:{i.get('line')}</td>"
            f"<td>{html_escape(i.get('text',''))}</td>"
            f"<td>{html_escape(i.get('author',''))}</td>"
            f"<td>{i.get('date','')}</td>"
            f"</tr>"
        )

    html = f"""
<!doctype html>
<html lang=\"it\">
<head>
  <meta charset=\"utf-8\"/>
  <title>Report TODO/FIXME/NOTE - {stamp}</title>
  <style>
    body {{ font-family: system-ui, Arial, sans-serif; margin: 20px; }}
    h1 {{ margin-top: 0; }}
    table {{ border-collapse: collapse; width: 100%; }}
    th, td {{ border: 1px solid #ddd; padding: 6px 8px; }}
    th {{ background: #f7f7f7; text-align: left; }}
    .summary span {{ display: inline-block; margin-right: 12px; }}
  </style>
  </head>
<body>
  <h1>Report TODO/FIXME/NOTE</h1>
  <div class=\"summary\">
    <span><strong>Totale:</strong> {total}</span>
    <span><strong>Pending:</strong> {pending}</span>
    <span><strong>Completati:</strong> {completed}</span>
    <span><strong>Urgenti:</strong> {urgent}</span>
  </div>
  <table>
    <thead>
      <tr><th>Tipo</th><th>Priorità</th><th>Stato</th><th>File:Linea</th><th>Testo</th><th>Autore</th><th>Data</th></tr>
    </thead>
    <tbody>
      {''.join(row(i) for i in items)}
    </tbody>
  </table>
</body>
</html>
"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    return out_path


def html_escape(s: str) -> str:
    if s is None:
        s = ""
    return (
        str(s).replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\"", "&quot;")
        .replace("'", "&#39;")
    )


def main():
    args = parse_args()
    if args.scan:
        raw_roots = re.split(r"[;,]", args.scan)
        roots = [r.strip() for r in raw_roots if r.strip()]
    else:
        roots = ["."]

    files = walk_paths(roots)
    found = []
    for fp in files:
        found.extend(scan_file(fp))

    master_path = os.path.join(os.getcwd(), "MASTER-TODO.json")
    master = load_master(master_path)
    if args.consolidate:
        master = consolidate(master, found)
    else:
        master = {"items": found}

    # Esecuzione (marcatura completato)
    done = 0
    if args.execute > 0:
        done = execute_items(master, args.execute)

    if args.output == "json":
        save_master(master_path, master)

    report_path = ""
    if args.report:
        report_path = generate_report(master)

    print(json.dumps({
        "scanned_files": len(files),
        "found_items": len(found),
        "executed": done,
        "master_path": master_path if args.output == "json" else "",
        "report_path": report_path,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
