#!/usr/bin/env python3
"""
Sistema di gestione delle task per il file TODO.md

Questo modulo fornisce funzionalità complete per:
- Parsing del file TODO.md
- Operazioni CRUD sulle task
- Interfaccia CLI
- Salvataggio persistente
- Filtraggio, ordinamento e ricerca
"""

import re
import os
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from enum import Enum


class TaskStatus(Enum):
    """Enum per lo stato delle task"""
    PENDING = "pending"
    COMPLETED = "completed"
    IN_PROGRESS = "in_progress"


class TaskPriority(Enum):
    """Enum per la priorità delle task"""
    HIGH = "alta"
    MEDIUM = "media" 
    LOW = "bassa"


class Task:
    """Classe che rappresenta una singola task"""
    
    def __init__(self, 
                 content: str, 
                 status: TaskStatus = TaskStatus.PENDING,
                 priority: TaskPriority = TaskPriority.MEDIUM,
                 category: str = "",
                 task_id: str = "",
                 created_at: Optional[datetime] = None,
                 updated_at: Optional[datetime] = None):
        self.content = content.strip()
        self.status = status
        self.priority = priority
        self.category = category.strip()
        self.task_id = task_id or self._generate_id()
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
    
    def _generate_id(self) -> str:
        """Genera un ID univoco basato sul contenuto, timestamp e random"""
        import time
        import random
        
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        content_hash = hash(self.content[:20]) % 10000
        random_part = random.randint(1000, 9999)
        
        return f"{timestamp}_{abs(content_hash)}_{random_part}"
    
    def mark_completed(self):
        """Contrassegna la task come completata"""
        self.status = TaskStatus.COMPLETED
        self.updated_at = datetime.now()
    
    def mark_in_progress(self):
        """Contrassegna la task come in progress"""
        self.status = TaskStatus.IN_PROGRESS
        self.updated_at = datetime.now()
    
    def mark_pending(self):
        """Contrassegna la task come pending"""
        self.status = TaskStatus.PENDING
        self.updated_at = datetime.now()
    
    def to_markdown(self) -> str:
        """Converte la task in formato Markdown"""
        status_char = "x" if self.status == TaskStatus.COMPLETED else " "
        
        # Gestione delle task con ID (es: [BUILD-01])
        if re.search(r"\[.*-\d+\]", self.content):
            return f"- [{status_char}] {self.content}"
        else:
            return f"- [{status_char}] {self.content}"
    
    def __str__(self) -> str:
        return f"{self.task_id}: {self.content} ({self.status.value})"
    
    def __repr__(self) -> str:
        return f"Task(content='{self.content}', status={self.status}, priority={self.priority})"


class TodoManager:
    """Classe principale per la gestione delle task"""
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.tasks: List[Task] = []
        self.categories: List[str] = []
        self.metadata: Dict[str, str] = {}
    
    def load_tasks(self) -> bool:
        """Carica le task dal file TODO.md"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            self._parse_todo_file(content)
            return True
        except FileNotFoundError:
            print(f"File {self.file_path} non trovato.")
            return False
        except Exception as e:
            print(f"Errore durante il caricamento: {e}")
            return False
    
    def _parse_todo_file(self, content: str):
        """Parsa il contenuto del file TODO.md"""
        self.tasks = []
        self.categories = []
        self.metadata = {}
        
        # Estrai metadata (ultimo aggiornamento, autore)
        metadata_pattern = r"\*\*Ultimo aggiornamento\*\*: (.+?)\n\*\*Autore\*\*: (.+?)\n"
        metadata_match = re.search(metadata_pattern, content, re.IGNORECASE)
        if metadata_match:
            self.metadata['last_updated'] = metadata_match.group(1)
            self.metadata['author'] = metadata_match.group(2)
        
        # Parsa il contenuto linea per linea
        lines = content.split('\n')
        current_category = ""
        
        for line in lines:
            line = line.strip()
            
            # Se è un'intestazione di categoria
            if line.startswith('## '):
                current_category = line[3:].strip()
                if current_category not in self.categories:
                    self.categories.append(current_category)
            
            # Se è una task
            elif line.startswith('- ['):
                # Estrai stato e contenuto
                match = re.match(r"- \[(.)\] (.+)", line)
                if match:
                    status_char, task_content = match.groups()
                    status = TaskStatus.COMPLETED if status_char.lower() == 'x' else TaskStatus.PENDING
                    
                    # Estrai priorità dalla task content
                    priority = self._extract_priority(task_content)
                    task_id = self._extract_task_id(task_content)
                    
                    task = Task(
                        content=task_content,
                        status=status,
                        priority=priority,
                        category=current_category,
                        task_id=task_id
                    )
                    self.tasks.append(task)
    
    def _extract_priority(self, task_content: str) -> TaskPriority:
        """Estrae la priorità dalla task content"""
        content_lower = task_content.lower()
        if 'priorità alta' in content_lower or '(alta)' in content_lower:
            return TaskPriority.HIGH
        elif 'priorità media' in content_lower or '(media)' in content_lower:
            return TaskPriority.MEDIUM
        elif 'priorità bassa' in content_lower or '(bassa)' in content_lower:
            return TaskPriority.LOW
        else:
            return TaskPriority.MEDIUM
    
    # Il metodo _extract_category è stato rimosso perché la categoria
    # viene ora gestita durante il parsing linea per linea
    
    def _extract_task_id(self, task_content: str) -> str:
        """Estrae l'ID della task se presente"""
        id_pattern = r"\[(.*?-\d+)\]"
        match = re.search(id_pattern, task_content)
        if match:
            return match.group(1)
        return ""
    
    def save_tasks(self) -> bool:
        """Salva le task nel file TODO.md"""
        try:
            # Ricostruisci l'intero contenuto del file
            content_lines = []
            
            # Aggiungi l'intestazione
            content_lines.append("# TODO List")
            content_lines.append("")
            
            # Raggruppa le task per categoria
            tasks_by_category = {}
            for task in self.tasks:
                if task.category not in tasks_by_category:
                    tasks_by_category[task.category] = []
                tasks_by_category[task.category].append(task)
            
            # Aggiungi le task per categoria
            for category in self.categories:
                if category in tasks_by_category:
                    content_lines.append(f"## {category}")
                    for task in tasks_by_category[category]:
                        content_lines.append(task.to_markdown())
                    content_lines.append("")
            
            # Aggiungi metadata
            today = datetime.now().strftime("%d %B %Y")
            content_lines.append(f"**Ultimo aggiornamento**: {today}")
            content_lines.append("**Autore**: Sistema di Gestione Task")
            
            # Scrivi il contenuto
            with open(self.file_path, 'w', encoding='utf-8') as file:
                file.write('\n'.join(content_lines))
            
            return True
        except Exception as e:
            print(f"Errore durante il salvataggio: {e}")
            return False
    
    # Il metodo _update_metadata è stato rimosso perché i metadata
    # vengono ora gestiti durante la ricostruzione del file
    
    # Operazioni CRUD
    def add_task(self, content: str, category: str = "", priority: TaskPriority = TaskPriority.MEDIUM) -> Task:
        """Aggiunge una nuova task"""
        task = Task(content=content, category=category, priority=priority)
        self.tasks.append(task)
        return task
    
    def get_task(self, task_id: str) -> Optional[Task]:
        """Restituisce una task per ID"""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None
    
    def update_task(self, task_id: str, **kwargs) -> bool:
        """Aggiorna una task esistente"""
        task = self.get_task(task_id)
        if not task:
            return False
        
        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)
        
        task.updated_at = datetime.now()
        return True
    
    def delete_task(self, task_id: str) -> bool:
        """Elimina una task"""
        task = self.get_task(task_id)
        if not task:
            return False
        
        self.tasks.remove(task)
        return True
    
    # Filtri e ricerche
    def filter_tasks(self, 
                    status: Optional[TaskStatus] = None,
                    priority: Optional[TaskPriority] = None,
                    category: Optional[str] = None) -> List[Task]:
        """Filtra le task in base a criteri"""
        filtered = self.tasks
        
        if status:
            filtered = [t for t in filtered if t.status == status]
        if priority:
            filtered = [t for t in filtered if t.priority == priority]
        if category:
            filtered = [t for t in filtered if t.category.lower() == category.lower()]
        
        return filtered
    
    def search_tasks(self, query: str) -> List[Task]:
        """Cerca task contenenti la query"""
        query = query.lower()
        return [t for t in self.tasks if query in t.content.lower()]
    
    def sort_tasks(self, tasks: List[Task], by: str = "priority") -> List[Task]:
        """Ordina le task"""
        if by == "priority":
            priority_order = {TaskPriority.HIGH: 0, TaskPriority.MEDIUM: 1, TaskPriority.LOW: 2}
            return sorted(tasks, key=lambda t: priority_order[t.priority])
        elif by == "status":
            status_order = {TaskStatus.COMPLETED: 0, TaskStatus.IN_PROGRESS: 1, TaskStatus.PENDING: 2}
            return sorted(tasks, key=lambda t: status_order[t.status])
        elif by == "category":
            return sorted(tasks, key=lambda t: t.category)
        else:
            return sorted(tasks, key=lambda t: t.content)
    
    # Statistiche
    def get_stats(self) -> Dict[str, int]:
        """Restituisce statistiche sulle task"""
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t.status == TaskStatus.COMPLETED])
        in_progress = len([t for t in self.tasks if t.status == TaskStatus.IN_PROGRESS])
        pending = len([t for t in self.tasks if t.status == TaskStatus.PENDING])
        
        return {
            'total': total,
            'completed': completed,
            'in_progress': in_progress,
            'pending': pending,
            'completion_rate': (completed / total * 100) if total > 0 else 0
        }


def main():
    """Funzione principale per testing"""
    file_path = "TODO.md"
    manager = TodoManager(file_path)
    
    if manager.load_tasks():
        print(f"Caricate {len(manager.tasks)} task")
        
        # Esempio: mostra statistiche
        stats = manager.get_stats()
        print(f"Completate: {stats['completed']}/{stats['total']} ({stats['completion_rate']:.1f}%)")
        
        # Esempio: filtra task completate
        completed_tasks = manager.filter_tasks(status=TaskStatus.COMPLETED)
        print(f"\nTask completate:")
        for task in completed_tasks[:3]:  # Mostra solo prime 3
            print(f"  - {task.content}")


if __name__ == "__main__":
    main()