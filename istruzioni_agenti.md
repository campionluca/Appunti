# Istruzioni per Agenti AI - Gestione TODO.md

## Panoramica

Questo documento fornisce istruzioni dettagliate per gli agenti AI configurati nel file `agent_instructions.json` su come gestire i loro file TODO.md personali seguendo un processo strutturato in 5 fasi.

## Fase 1: Lettura Attenta del File TODO.md

### Percorso del File
- **Posizione assoluta**: `C:\Users\campi\Documents\SCUOLA\Appunti\MASTER-TODO.md`
- **Posizione relativa**: `./MASTER-TODO.md` (dalla directory principale del progetto)
- **Formato previsto**: File Markdown con struttura gerarchica

### Struttura del File TODO.md
Il file deve seguire questo formato:

```markdown
# MASTER TODO - [Nome Progetto]

## 📊 Stato Generale
- Complezione complessiva: X%
- Task completate: Y/Z
- Priorità alta: A task
- Priorità media: B task  
- Priorità bassa: C task

## 🚀 Build e Distribuzione
- [ ] TASK-ID: Descrizione breve (Priorità)

## 🧠 Contenuti (Priorità Alta)
- [ ] CONTENT-01: Modulo 00 - Fondamenti Python
- [ ] CONTENT-02: Modulo 01 - Controllo del Flusso
- [x] CONTENT-03: Modulo 02 - Funzioni

## 📚 Documentazione
- [ ] DOC-01: Documentazione tecnica

## 🔧 Refactoring
- [ ] REFACTOR-01: Uniformare indentazione
```

## Fase 2: Analisi di Tutte le Task

### Categorie di Task
1. **Task di Contenuto** (CONTENT-XX): Creazione/modifica contenuti didattici
2. **Task di Documentazione** (DOC-XX): Documentazione tecnica e spiegazioni
3. **Task di Refactoring** (REFACTOR-XX): Miglioramenti del codice esistente
4. **Task di Test** (TEST-XX): Validazione e testing
5. **Task di Formattazione** (FORMAT-XX): Standardizzazione formattazione

### Metadati Obbligatori per Ogni Task
- **ID Task**: Identificativo univoco (es: CONTENT-01)
- **Descrizione**: Descrizione chiara e concisa
- **Priorità**: Alta/Media/Bassa
- **Stato**: [ ], [x], [-] (completata, in corso, bloccata)
- **Dipendenza**: Task da completare prima di questa
- **Tempo stimato**: Tempo previsto per completamento

## Fase 3: Identificazione Priorità e Dipendenze

### Gerarchia delle Priorità
1. **Priorità Alta**: Task critiche per la funzionalità base
   - Compilazione LaTeX senza errori
   - Contenuti didattici principali
   - Sicurezza e gestione errori

2. **Priorità Media**: Miglioramenti funzionali
   - Documentazione aggiuntiva
   - Esempi di codice
   - Refactoring minore

3. **Priorità Bassa**: Ottimizzazioni e abbellimenti
   - Formattazione estetica
   - Commenti aggiuntivi
   - Ottimizzazioni prestazioni

### Analisi delle Dipendenze
Utilizzare questa tabella per identificare le dipendenze:

| Task ID | Dipende da | Blocca | Tipo Dipendenza |
|---------|------------|--------|-----------------|
| CONTENT-02 | CONTENT-01 | - | Sequenziale |
| TEST-01 | CONTENT-01 | - | Validazione |
| FORMAT-01 | - | MULTIPLE | Prerequisito |

## Fase 4: Preparazione Ambiente di Lavoro

### Requisiti di Sistema
- **LaTeX Distribution**: MiKTeX o TeX Live installato
- **Python**: Versione 3.8+ per script di automazione
- **Strumenti di Build**: latexmk, xelatex
- **Editor**: VS Code con estensione LaTeX Workshop

### Struttura Directory
```
C:\Users\campi\Documents\SCUOLA\Appunti\
├── MASTER-TODO.md
├── agent_instructions.json
├── capitoli\
│   ├── 00_fondamenti_python.tex
│   ├── 01_controllo_flusso.tex
│   └── ...
├── build\
├── output\
└── scripts\
```

### Configurazione Agente
Verificare la configurazione nel file `agent_instructions.json`:
- **agent_name**: Nome identificativo dell'agente
- **processing_type**: Tipo di elaborazione (content, build, test)
- **target_directory**: Directory di lavoro assegnata
- **work_parameters**: Parametri specifici per il lavoro

## Fase 5: Esecuzione delle Task

### Ordine di Esecuzione Corretto
1. **Task di Sistema**: Setup ambiente e dipendenze
2. **Task di Build**: Compilazione LaTeX senza errori
3. **Task di Contenuto**: Creazione contenuti principali
4. **Task di Test**: Validazione e testing
5. **Task di Documentazione**: Documentazione tecnica
6. **Task di Refactoring**: Miglioramenti codice
7. **Task di Formattazione**: Standardizzazione estetica

### Processo di Esecuzione
Per ogni task seguire questo flusso:

```python
def execute_task(task_id):
    # 1. Verifica prerequisiti
    if not check_prerequisites(task_id):
        return False
    
    # 2. Esegui task principale
    result = perform_task_work(task_id)
    
    # 3. Verifica risultati
    if not validate_results(task_id, result):
        handle_errors(task_id)
        return False
    
    # 4. Aggiorna stato
    update_task_status(task_id, "completed")
    
    # 5. Documenta cambiamenti
    document_changes(task_id)
    
    return True
```

## Gestione Errori e Task Incomplete

### Tipologie di Errori
1. **Errori di Compilazione**: Errori LaTeX/blocchi di build
2. **Errori di Contenuto**: Contenuti mancanti o incompleti
3. **Errori di Formattazione**: Standard non rispettati
4. **Errori di Dipendenza**: Task prerequisite non completate

### Procedure di Gestione Errori

#### Per Errori di Compilazione:
```markdown
- [ ] TASK-ID: Descrizione task
  - ❌ ERRORE: Messaggio di errore dettagliato
  - 🔧 AZIONE: Azione correttiva specifica
  - ⏱️ TEMPO: Tempo stimato per fix
  - 📋 STATO: In lavorazione
```

#### Per Task Incomplete:
- **Marcare come [-]**: Task iniziata ma non completata
- **Documentare motivo**: Perché la task non può essere completata
- **Stimare tempo residuo**: Quando sarà possibile completare
- **Identificare blocchi**: Cosa sta bloccando il completamento

## Segnalazione Stato di Avanzamento

### Formato di Reporting
Utilizzare questo template per i report:

```markdown
## 📈 Report Avanzamento - [Data]

### 📊 Statistiche Generali
- Task totali: X
- Completate: Y (Z%)
- In corso: A
- Bloccate: B
- In attesa: C

### 🎯 Task Completate
1. **TASK-ID**: Breve descrizione completamento
   - ⏱️ Tempo impiegato: Xh Ym
   - 📋 Changes: Elenco modifiche apportate

### 🚧 Task in Corso
1. **TASK-ID**: Stato attuale e progresso
   - 📈 Progresso: X%
   - ⏱️ Tempo rimanente: Yh Zm

### ⚠️ Task Bloccate
1. **TASK-ID**: Motivo blocco e azioni necessarie
   - 🔒 Blocco: Descrizione dettagliata blocco
   - 🆘 Aiuto richiesto: Cosa serve per sbloccare
```

### Frequenza di Reporting
- **Report Giornaliero**: Ogni 24 ore di lavoro attivo
- **Report per Task Completa**: Immediatamente al completamento
- **Report di Blocco**: Immediatamente al verificarsi di blocchi
- **Report Settimanale**: Riepilogo complessivo settimanale

## Tempistiche Previste per Completamento

### Stime Temporali Standard

#### Task di Contenuto (per modulo):
- **Setup base**: 1-2 ore
- **Contenuti principali**: 4-8 ore  
- **Esempi codice**: 2-4 ore
- **Esercizi**: 3-6 ore
- **Documentazione**: 2-3 ore
- **Testing**: 1-2 ore

#### Task Tecniche:
- **Setup ambiente**: 1-3 ore
- **Configurazione build**: 2-4 ore
- **Refactoring codice**: 1-2 ore per file
- **Formattazione**: 30min-1h per file

### Timeline di Riferimento

#### Per Modulo Completo (CONTENT-XX):
```
Giorno 1: Setup e contenuti base (6-8 ore)
Giorno 2: Esempi ed esercizi (6-8 ore)  
Giorno 3: Documentazione e testing (4-6 ore)
Giorno 4: Revisione e finalizzazione (2-4 ore)
```

#### Per Progetto Completo:
- **Moduli base (00-04)**: 5-7 giorni lavorativi
- **Moduli intermedi (05-10)**: 7-10 giorni lavorativi
- **Moduli avanzati (11-15)**: 8-12 giorni lavorativi
- **Moduli NAO (16-18)**: 6-9 giorni lavorativi
- **Task tecniche**: 3-5 giorni lavorativi

## Metriche di Successo

### Qualità del Lavoro
- **0 errori di compilazione**
- **100% task completate** secondo standard
- **Documentazione completa** per ogni modifica
- **Tempo di esecuzione** entro il 120% della stima

### Performance dell'Agente
- **Efficienza**: Task completate/tempo impiegato
- **Accuratezza**: Errori commessi/task completate  
- **Produttività**: Task completate/giorno lavorativo
- **Affidabilità**: Task completate senza bisogno di rework

## Integrazione con agent_instructions.json

### Parametri di Configurazione Rilevanti
Nel file `agent_instructions.json`, prestare attenzione a:

```json
{
  "work_parameters": {
    "todo_integration": {
      "enabled": true,
      "todo_file_path": "MASTER-TODO.md",
      "sync_interval": 1800,
      "status_mapping": {
        "completed": [],
        "in_progress": ["C", "HTMLCSS", "Java","Python", "PHP"], 
        "pending": ["new_courses"]
      }
    }
  }
}
```

### Sincronizzazione Automatica
- **Interval