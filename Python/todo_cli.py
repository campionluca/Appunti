#!/usr/bin/env python3
"""
Interfaccia CLI per la gestione delle task del file TODO.md

Questo modulo fornisce un'interfaccia a riga di comando completa per:
- Visualizzare le task
- Aggiungere, modificare, eliminare task
- Filtrare, ordinare e cercare task
- Gestire lo stato delle task
"""

import argparse
import sys
from typing import List
from todo_manager import TodoManager, Task, TaskStatus, TaskPriority


class TodoCLI:
    """Classe per l'interfaccia CLI del gestore TODO"""
    
    def __init__(self, file_path: str):
        self.manager = TodoManager(file_path)
        self.manager.load_tasks()
    
    def run(self):
        """Avvia l'interfaccia CLI"""
        parser = argparse.ArgumentParser(description='Gestione task TODO.md')
        subparsers = parser.add_subparsers(dest='command', help='Comandi disponibili')
        
        # Comando list
        list_parser = subparsers.add_parser('list', help='Lista task')
        list_parser.add_argument('--status', choices=['pending', 'completed', 'in_progress'], 
                               help='Filtra per stato')
        list_parser.add_argument('--priority', choices=['alta', 'media', 'bassa'], 
                               help='Filtra per priorità')
        list_parser.add_argument('--category', help='Filtra per categoria')
        list_parser.add_argument('--sort', choices=['priority', 'status', 'category', 'content'],
                               default='priority', help='Ordina per')
        list_parser.add_argument('--limit', type=int, help='Limita numero di task')
        
        # Comando add
        add_parser = subparsers.add_parser('add', help='Aggiungi task')
        add_parser.add_argument('content', help='Contenuto della task')
        add_parser.add_argument('--category', help='Categoria della task')
        add_parser.add_argument('--priority', choices=['alta', 'media', 'bassa'], 
                               default='media', help='Priorità della task')
        
        # Comando update
        update_parser = subparsers.add_parser('update', help='Aggiorna task')
        update_parser.add_argument('task_id', help='ID della task da aggiornare')
        update_parser.add_argument('--content', help='Nuovo contenuto')
        update_parser.add_argument('--category', help='Nuova categoria')
        update_parser.add_argument('--priority', choices=['alta', 'media', 'bassa'], 
                                 help='Nuova priorità')
        update_parser.add_argument('--status', choices=['pending', 'completed', 'in_progress'], 
                                 help='Nuovo stato')
        
        # Comando delete
        delete_parser = subparsers.add_parser('delete', help='Elimina task')
        delete_parser.add_argument('task_id', help='ID della task da eliminare')
        
        # Comando search
        search_parser = subparsers.add_parser('search', help='Cerca task')
        search_parser.add_argument('query', help='Query di ricerca')
        
        # Comando stats
        subparsers.add_parser('stats', help='Mostra statistiche')
        
        # Comando mark
        mark_parser = subparsers.add_parser('mark', help='Cambia stato task')
        mark_parser.add_argument('task_id', help='ID della task')
        mark_parser.add_argument('status', choices=['completed', 'in_progress', 'pending'], 
                               help='Nuovo stato')
        
        # Comando categories
        subparsers.add_parser('categories', help='Lista categorie')
        
        args = parser.parse_args()
        
        if not args.command:
            self._show_usage()
            return
        
        try:
            if args.command == 'list':
                self._handle_list(args)
            elif args.command == 'add':
                self._handle_add(args)
            elif args.command == 'update':
                self._handle_update(args)
            elif args.command == 'delete':
                self._handle_delete(args)
            elif args.command == 'search':
                self._handle_search(args)
            elif args.command == 'stats':
                self._handle_stats()
            elif args.command == 'mark':
                self._handle_mark(args)
            elif args.command == 'categories':
                self._handle_categories()
            
            # Salva sempre le modifiche
            self.manager.save_tasks()
            
        except Exception as e:
            print(f"Errore: {e}", file=sys.stderr)
            sys.exit(1)
    
    def _handle_list(self, args):
        """Gestisce il comando list"""
        # Filtra task
        status_map = {
            'pending': TaskStatus.PENDING,
            'completed': TaskStatus.COMPLETED,
            'in_progress': TaskStatus.IN_PROGRESS
        }
        
        priority_map = {
            'alta': TaskPriority.HIGH,
            'media': TaskPriority.MEDIUM,
            'bassa': TaskPriority.LOW
        }
        
        status = status_map[args.status] if args.status else None
        priority = priority_map[args.priority] if args.priority else None
        
        tasks = self.manager.filter_tasks(
            status=status,
            priority=priority,
            category=args.category
        )
        
        # Ordina task
        tasks = self.manager.sort_tasks(tasks, args.sort)
        
        # Applica limite
        if args.limit:
            tasks = tasks[:args.limit]
        
        self._display_tasks(tasks)
    
    def _handle_add(self, args):
        """Gestisce il comando add"""
        priority_map = {
            'alta': TaskPriority.HIGH,
            'media': TaskPriority.MEDIUM,
            'bassa': TaskPriority.LOW
        }
        
        task = self.manager.add_task(
            content=args.content,
            category=args.category,
            priority=priority_map[args.priority]
        )
        
        print(f"Task aggiunta: {task.task_id}")
        print(f"Contenuto: {task.content}")
        if task.category:
            print(f"Categoria: {task.category}")
        print(f"Priorità: {task.priority.value}")
    
    def _handle_update(self, args):
        """Gestisce il comando update"""
        update_data = {}
        
        if args.content:
            update_data['content'] = args.content
        if args.category:
            update_data['category'] = args.category
        if args.priority:
            priority_map = {
                'alta': TaskPriority.HIGH,
                'media': TaskPriority.MEDIUM,
                'bassa': TaskPriority.LOW
            }
            update_data['priority'] = priority_map[args.priority]
        if args.status:
            status_map = {
                'pending': TaskStatus.PENDING,
                'completed': TaskStatus.COMPLETED,
                'in_progress': TaskStatus.IN_PROGRESS
            }
            update_data['status'] = status_map[args.status]
        
        if not update_data:
            print("Nessun campo da aggiornare specificato")
            return
        
        success = self.manager.update_task(args.task_id, **update_data)
        if success:
            print(f"Task {args.task_id} aggiornata")
        else:
            print(f"Task {args.task_id} non trovata")
    
    def _handle_delete(self, args):
        """Gestisce il comando delete"""
        success = self.manager.delete_task(args.task_id)
        if success:
            print(f"Task {args.task_id} eliminata")
        else:
            print(f"Task {args.task_id} non trovata")
    
    def _handle_search(self, args):
        """Gestisce il comando search"""
        tasks = self.manager.search_tasks(args.query)
        self._display_tasks(tasks)
    
    def _handle_stats(self):
        """Gestisce il comando stats"""
        stats = self.manager.get_stats()
        
        print("=== STATISTICHE ===")
        print(f"Task totali: {stats['total']}")
        print(f"Completate: {stats['completed']} ({stats['completion_rate']:.1f}%)")
        print(f"In progress: {stats['in_progress']}")
        print(f"Pending: {stats['pending']}")
        
        # Statistiche per categoria
        categories = {}
        for task in self.manager.tasks:
            if task.category:
                categories[task.category] = categories.get(task.category, 0) + 1
        
        if categories:
            print("\n=== TASK PER CATEGORIA ===")
            for category, count in sorted(categories.items()):
                print(f"{category}: {count}")
    
    def _handle_mark(self, args):
        """Gestisce il comando mark"""
        task = self.manager.get_task(args.task_id)
        if not task:
            print(f"Task {args.task_id} non trovata")
            return
        
        status_map = {
            'completed': TaskStatus.COMPLETED,
            'in_progress': TaskStatus.IN_PROGRESS,
            'pending': TaskStatus.PENDING
        }
        
        task.status = status_map[args.status]
        task.updated_at = datetime.now()
        
        print(f"Task {args.task_id} contrassegnata come {args.status}")
    
    def _handle_categories(self):
        """Gestisce il comando categories"""
        categories = set()
        for task in self.manager.tasks:
            if task.category:
                categories.add(task.category)
        
        if categories:
            print("=== CATEGORIE ===")
            for category in sorted(categories):
                print(f"- {category}")
        else:
            print("Nessuna categoria trovata")
    
    def _display_tasks(self, tasks: List[Task]):
        """Visualizza le task in formato tabellare"""
        if not tasks:
            print("Nessuna task trovata")
            return
        
        # Header della tabella
        print(f"{'ID':<15} {'STATO':<12} {'PRIORITÀ':<8} {'CATEGORIA':<20} CONTENUTO")
        print("-" * 80)
        
        for task in tasks:
            status_icon = "✓" if task.status == TaskStatus.COMPLETED else "↻" if task.status == TaskStatus.IN_PROGRESS else "◯"
            priority_icon = "❗" if task.priority == TaskPriority.HIGH else "🔶" if task.priority == TaskPriority.MEDIUM else "🔷"
            
            # Tronca il contenuto se troppo lungo
            content_preview = task.content[:50] + "..." if len(task.content) > 50 else task.content
            
            print(f"{task.task_id:<15} {status_icon:<11} {priority_icon:<7} {task.category[:18]:<20} {content_preview}")
        
        print(f"\nTotale: {len(tasks)} task")
    
    def _show_usage(self):
        """Mostra l'utilizzo del programma"""
        print("""
Gestione Task TODO.md - Interfaccia CLI

Utilizzo:
  todo_cli.py <comando> [opzioni]

Comandi disponibili:
  list      - Lista task (con filtri e ordinamento)
  add       - Aggiungi nuova task
  update    - Aggiorna task esistente
  delete    - Elimina task
  search    - Cerca task per contenuto
  stats     - Mostra statistiche
  mark      - Cambia stato task
  categories - Lista categorie

Esempi:
  todo_cli.py list --status pending --priority alta
  todo_cli.py add "Implementare nuova feature" --category "Sviluppo" --priority alta
  todo_cli.py update TASK_ID --content "Nuovo contenuto" --status completed
  todo_cli.py search "database"
  todo_cli.py stats
""")


def main():
    """Funzione principale"""
    if len(sys.argv) == 1:
        # Modalità interattiva semplice
        cli = TodoCLI("TODO.md")
        cli._show_usage()
    else:
        # Modalità comandi
        cli = TodoCLI("TODO.md")
        cli.run()


if __name__ == "__main__":
    main()