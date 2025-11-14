// Simple client for tools/tasks/server.py
const apiBase = location.origin; // server serves static from /tools/tasks/web and api under /api

const state = {
  tasks: [],
  filters: {
    project: '', status: '', priority: '', type: '', q: '',
  },
  view: 'list',
  notified: new Set(),
};

function qs(id) { return document.getElementById(id); }
function qsa(sel) { return Array.from(document.querySelectorAll(sel)); }
function toast(msg) {
  const el = qs('toast');
  el.textContent = msg;
  el.classList.add('show');
  setTimeout(() => el.classList.remove('show'), 2000);
}

async function api(path, opts={}) {
  const res = await fetch(`${apiBase}${path}`, {
    headers: { 'Content-Type': 'application/json' },
    ...opts,
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

function applyFilters(tasks) {
  const f = state.filters;
  const q = f.q.trim().toLowerCase();
  return tasks.filter(t => {
    if (f.project && t.project !== f.project) return false;
    if (f.status && t.status !== f.status) return false;
    if (f.priority && t.priority !== f.priority) return false;
    if (f.type && t.type !== f.type) return false;
    if (q && !(`${t.title} ${t.description}`.toLowerCase().includes(q))) return false;
    return true;
  });
}

function prioBadge(p) {
  const map = { alta: 'prio-alta', media: 'prio-media', bassa: 'prio-bassa' };
  return `<span class="badge ${map[p]||''}">${p}</span>`;
}

function deadlineText(d) {
  if (!d) return '';
  const dt = new Date(d);
  const days = Math.ceil((dt - new Date()) / (1000*60*60*24));
  if (days <= 3) return `<span class="deadline-soon">${dt.toLocaleDateString()}</span>`;
  return dt.toLocaleDateString();
}

function renderList() {
  const tbody = qs('list-body');
  tbody.innerHTML = '';
  for (const t of applyFilters(state.tasks)) {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${t.title}</td>
      <td>${prioBadge(t.priority)}</td>
      <td>${deadlineText(t.deadline)}</td>
      <td>${t.assignee||''}</td>
      <td>${t.project||''}</td>
      <td>${t.status}</td>
      <td>${t.type||''}</td>
      <td class="actions">
        <button data-act="edit">Modifica</button>
        <button data-act="advance">Avanza</button>
        <button data-act="delete">Elimina</button>
      </td>
    `;
    tr.dataset.id = t.id;
    tbody.appendChild(tr);
  }
}

function renderBoard() {
  for (const id of ['da_fare','in_corso','completato']) qs(`col-${id}`).innerHTML='';
  for (const t of applyFilters(state.tasks)) {
    const el = document.createElement('div');
    el.className = 'card';
    el.innerHTML = `
      <div class="title">${t.title} ${prioBadge(t.priority)}</div>
      <div class="meta">${t.project||''} • ${t.assignee||''} • ${deadlineText(t.deadline)}</div>
      <div class="actions">
        <button data-act="edit">Modifica</button>
        <button data-act="advance">Avanza</button>
        <button data-act="delete">Elimina</button>
      </div>
    `;
    el.dataset.id = t.id;
    qs(`col-${t.status}`).appendChild(el);
  }
}

function setView(v) {
  state.view = v;
  qsa('.view').forEach(e => e.classList.remove('active'));
  qs(`view-${v}`).classList.add('active');
  qsa('.views button').forEach(b => b.classList.toggle('active', b.dataset.view === v));
  if (v === 'list') renderList(); else renderBoard();
}

function collectForm() {
  return {
    title: qs('task-title').value.trim(),
    description: qs('task-desc').value.trim(),
    priority: qs('task-prio').value,
    deadline: qs('task-deadline').value,
    assignee: qs('task-assignee').value.trim(),
    project: qs('task-project').value.trim(),
    type: qs('task-type').value,
    status: qs('task-status').value,
  };
}

function fillForm(t) {
  qs('task-id').value = t?.id || '';
  qs('task-title').value = t?.title || '';
  qs('task-desc').value = t?.description || '';
  qs('task-prio').value = t?.priority || 'media';
  qs('task-deadline').value = t?.deadline || '';
  qs('task-assignee').value = t?.assignee || '';
  qs('task-project').value = t?.project || '';
  qs('task-type').value = t?.type || 'Sviluppo';
  qs('task-status').value = t?.status || 'da_fare';
}

async function loadTasks() {
  const data = await api('/api/tasks');
  state.tasks = data.tasks || [];
  const projects = [...new Set(state.tasks.map(t => t.project).filter(Boolean))].sort();
  const projSel = qs('filter-project');
  projSel.innerHTML = '<option value="">Tutti i progetti</option>' + projects.map(p=>`<option>${p}</option>`).join('');
  if (state.view === 'list') renderList(); else renderBoard();
  notifyDeadlines();
}

async function saveTask() {
  const id = qs('task-id').value;
  const payload = collectForm();
  if (!payload.title || !payload.description) { toast('Titolo/descrizione obbligatori'); return; }
  const path = id ? `/api/tasks/${id}` : '/api/tasks';
  const method = id ? 'PUT' : 'POST';
  await api(path, { method, body: JSON.stringify(payload) });
  qs('dlg-task').close();
  toast('Task salvata');
  await loadTasks();
}

async function delTask(id) {
  await api(`/api/tasks/${id}`, { method: 'DELETE' });
  toast('Task eliminata');
  await loadTasks();
}

async function advanceTask(id) {
  const t = state.tasks.find(x => x.id === id);
  if (!t) return;
  const order = ['da_fare','in_corso','completato'];
  const next = order[Math.min(order.indexOf(t.status)+1, order.length-1)];
  await api(`/api/tasks/${id}`, { method: 'PUT', body: JSON.stringify({ status: next }) });
  toast('Stato aggiornato');
  await loadTasks();
}

async function doBackup() {
  const res = await api('/api/backup', { method: 'POST' });
  toast(`Backup creato: ${res.file}`);
}

function wireEvents() {
  qs('btn-new').addEventListener('click', () => { fillForm(null); qs('dlg-task').showModal(); });
  qs('btn-backup').addEventListener('click', () => { doBackup(); });
  qs('btn-save').addEventListener('click', (e) => { e.preventDefault(); saveTask(); });
  qsa('.views button').forEach(b => b.addEventListener('click', () => setView(b.dataset.view)));
  qs('search').addEventListener('input', e => { state.filters.q = e.target.value; (state.view==='list'?renderList:renderBoard)(); });
  qs('filter-project').addEventListener('change', e => { state.filters.project = e.target.value; (state.view==='list'?renderList:renderBoard)(); });
  qs('filter-status').addEventListener('change', e => { state.filters.status = e.target.value; (state.view==='list'?renderList:renderBoard)(); });
  qs('filter-priority').addEventListener('change', e => { state.filters.priority = e.target.value; (state.view==='list'?renderList:renderBoard)(); });
  qs('filter-type').addEventListener('change', e => { state.filters.type = e.target.value; (state.view==='list'?renderList:renderBoard)(); });

  // Delegated actions for list and board
  document.body.addEventListener('click', (e) => {
    const btn = e.target.closest('button');
    if (!btn) return;
    const act = btn.dataset.act;
    const tr = e.target.closest('[data-id]');
    if (!act || !tr) return;
    const id = tr.dataset.id;
    if (act === 'edit') { const t = state.tasks.find(x=>x.id===id); fillForm(t); qs('dlg-task').showModal(); }
    else if (act === 'delete') { if (confirm('Eliminare la task?')) delTask(id); }
    else if (act === 'advance') { advanceTask(id); }
  });
}

function setupRealtime() {
  try {
    const es = new EventSource('/api/events');
    es.onmessage = (ev) => {
      // generic update -> reload list
      loadTasks();
    };
    es.addEventListener('update', () => loadTasks());
    es.addEventListener('hello', () => {});
  } catch (e) {
    // Fallback: poll every 20s
    setInterval(loadTasks, 20000);
  }
}

function notifyDeadlines() {
  const soon = applyFilters(state.tasks).filter(t => {
    if (!t.deadline || t.status === 'completato') return false;
    const dt = new Date(t.deadline);
    const days = Math.ceil((dt - new Date()) / (1000*60*60*24));
    return days <= 1; // entro 24 ore
  });
  for (const t of soon) {
    if (!state.notified.has(t.id)) {
      toast(`Scadenza imminente: "${t.title}" (${deadlineText(t.deadline)})`);
      state.notified.add(t.id);
    }
  }
}

window.addEventListener('DOMContentLoaded', async () => {
  wireEvents();
  await loadTasks();
  setupRealtime();
});
