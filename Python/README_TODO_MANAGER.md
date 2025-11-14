# Sistema di Gestione Task TODO.md

Un sistema completo in Python per gestire le task del file `TODO.md` con funzionalità CRUD, interfaccia CLI, filtri avanzati e salvataggio persistente.

## ✨ Funzionalità

- **📖 Parsing avanzato**: Legge e interpreta il file TODO.md mantenendo la struttura originale
- **🔄 Operazioni CRUD complete**: Crea, leggi, aggiorna, elimina task
- **🎯 Interfaccia CLI intuitiva**: Comandi semplici e potenti per gestire le task
- **🔍 Ricerca e filtri**: Cerca per contenuto, filtra per stato, priorità, categoria
- **📊 Statistiche**: Monitora il progresso con metriche dettagliate
- **💾 Salvataggio persistente**: Mantiene l'integrità del file originale
- **✅ Testing completo**: Suite di test per garantire affidabilità

## 🚀 Installazione

Il sistema richiede solo Python 3.7+ (nessuna dipendenza esterna):

```bash
# Clona o copia i file nella tua directory di progetto
cd /percorso/del/tuo/progetto

# I file necessari:
# - todo_manager.py   # Core del sistema
# - todo_cli.py       # Interfaccia CLI
# - test_todo_manager.py # Test suite
```

## 📖 Utilizzo

### Interfaccia CLI Principale

```bash
# Mostra aiuto
python todo_cli.py

# Lista tutte le task
python todo_cli.py list

# Lista task pending con priorità alta
python todo_cli.py list --status pending --priority alta

# Aggiungi nuova task
python todo_cli.py add "Implementare nuova feature" --category "Sviluppo" --priority alta

# Aggiorna task
python todo_cli.py update TASK_ID --content "Nuovo contenuto" --status completed

# Elimina task
python todo_cli.py delete TASK_ID

# Cerca task
python todo_cli.py search "database"

# Mostra statistiche
python todo_cli.py stats

# Cambia stato task
python todo_cli.py mark TASK_ID completed
```

### Esempi Pratici

```bash
# Filtra task di sviluppo in progress
python todo_cli.py list --category "Sviluppo" --status in_progress

# Ordina task per categoria
python todo_cli.py list --sort category

# Limita risultati
python todo_cli.py list --limit 5

# Cerca task relative al database
python todo_cli.py search "MySQL"
```

## 🏗️ Architettura

### File Principali

- **`todo_manager.py`** - Core del sistema:
  - `TodoManager`: Classe principale per la gestione delle task
  - `Task`: Modello dati per una singola task
  - `TaskStatus`: Enum per gli stati (pending, completed, in_progress)
  - `TaskPriority`: Enum per le priorità (alta, media, bassa)

- **`todo_cli.py`** - Interfaccia a riga di comando
- **`test_todo_manager.py`** - Suite di test completa

### Flusso di Lavoro

1. **Caricamento**: Parsing del file TODO.md e estrazione task
2. **Elaborazione**: Operazioni CRUD sulle task in memoria
3. **Salvataggio**: Scrittura delle modifiche nel file originale
4. **Persistenza**: Mantenimento della struttura e metadata

## 🔧 API del Sistema

### TodoManager Class

```python
# Inizializzazione
manager = TodoManager("TODO.md")
manager.load_tasks()

# Operazioni CRUD
manager.add_task("Contenuto", category="Categoria", priority=TaskPriority.HIGH)
manager.update_task(task_id, content="Nuovo contenuto", status=TaskStatus.COMPLETED)
manager.delete_task(task_id)

# Filtri e Ricerche
manager.filter_tasks(status=TaskStatus.PENDING, priority=TaskPriority.HIGH)
manager.search_tasks("query")
manager.sort_tasks(tasks, "priority")

# Utility
manager.get_stats()
manager.save_tasks()
```

### Task Class

```python
task = Task("Contenuto task")
task.mark_completed()
task.mark_in_progress()
task.mark_pending()
task.to_markdown()  # Conversione in formato Markdown
```

## 🧪 Testing

Esegui la suite di test completa:

```bash
python test_todo_manager.py
```

I test coprono:
- Parsing del file TODO.md
- Operazioni CRUD
- Filtri e ricerche
- Salvataggio persistente
- Casi edge e error handling

## 📋 Formato File TODO.md

Il sistema supporta il formato standard:

```markdown
# Titolo TODO

## Categoria 1
- [ ] Task pending
- [x] Task completata
- [ ] Task con priorità alta (priorità alta)

## Categoria 2
- [ ] Task con ID [PROJ-01]
- [ ] Altra task

**Ultimo aggiornamento**: 12 Novembre 2025
**Autore**: Nome Autore
```

## 🎨 Personalizzazione

### Aggiungere Nuovi Filtri

```python
# Esempio: filtro per data
class TodoManager:
    def filter_by_date(self, start_date, end_date):
        return [t for t in self.tasks if start_date <= t.created_at <= end_date]
```

### Estendere le Proprietà Task

```python
class ExtendedTask(Task):
    def __init__(self, content, tags=None, **kwargs):
        super().__init__(content, **kwargs)
        self.tags = tags or []
```

## ⚠️ Gestione Errori

Il sistema include robusta gestione errori:

- **File non trovato**: Messaggio descrittivo e graceful degradation
- **Task non esistente**: Validazione degli ID e feedback chiaro
- **Formato non valido**: Parsing tollerante agli errori
- **Salvataggio fallito**: Backup automatico e recovery

## 🔄 Integrazione

### Con Altri Strumenti

```python
# Integrazione con sistema di notifiche
def send_notification(task):
    # Implementa notifiche email/Slack/etc.
    pass

# Hook per task completate
for task in manager.filter_tasks(status=TaskStatus.COMPLETED):
    send_notification(task)
```

### Automatizzazione

```bash
# Script automatico per daily report
python todo_cli.py stats > daily_report.txt

# Automazione CI/CD
python todo_cli.py list --status pending --priority alta | wc -l
```

## 📊 Metriche e Statistiche

Il sistema traccia:
- Task totali, completate, in progress, pending
- Tasso di completamento
- Distribuzione per categoria
- Distribuzione per priorità
- Andamento temporale

## 🚦 Roadmap

- [ ] Interfaccia web con Flask/FastAPI
- [ ] Sincronizzazione cloud
- [ ] Integrazione calendar
- [ ] Plugin per editor (VSCode, PyCharm)
- [ ] API RESTful
- [ ] Mobile app

## 🤝 Contributi

1. Fork il progetto
2. Crea un branch per la feature
3. Commit delle modifiche
4. Push del branch
5. Crea una Pull Request

## 📄 Licenza

Questo progetto è rilasciato sotto licenza MIT.

## 🆘 Supporto

Per problemi o domande:
1. Controlla la documentazione
2. Crea una issue su GitHub
3. Contatta il maintainer

---

**Sviluppato con ❤️ per migliorare la produttività**