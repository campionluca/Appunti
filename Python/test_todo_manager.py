#!/usr/bin/env python3
"""
Test suite per il sistema di gestione task TODO.md

Questo modulo contiene test completi per verificare:
- Parsing del file TODO.md
- Operazioni CRUD
- Filtri e ricerche
- Salvataggio persistente
"""

import unittest
import tempfile
import os
from datetime import datetime
from todo_manager import TodoManager, Task, TaskStatus, TaskPriority


class TestTodoManager(unittest.TestCase):
    """Test case per TodoManager"""
    
    def setUp(self):
        """Crea un file TODO.md temporaneo per i test"""
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md', encoding='utf-8')
        self.temp_file_path = self.temp_file.name
        
        # Contenuto di esempio per il test
        test_content = """# TODO List

## Stato generale
- [ ] Task generale 1 (priorità alta)
- [x] Task generale 2 completata
- [ ] Task generale 3 (priorità bassa)

## Sviluppo
- [ ] Implementare feature A [DEV-01]
- [x] Fix bug critico [DEV-02]
- [ ] Refactor codice [DEV-03]

## Documentazione
- [ ] Scrivere documentazione API
- [ ] Aggiornare README

**Ultimo aggiornamento**: 12 Novembre 2025
**Autore**: Test Suite
"""
        
        self.temp_file.write(test_content)
        self.temp_file.close()
        
        self.manager = TodoManager(self.temp_file_path)
    
    def tearDown(self):
        """Pulisce il file temporaneo"""
        if os.path.exists(self.temp_file_path):
            os.unlink(self.temp_file_path)
    
    def test_load_tasks(self):
        """Test caricamento task dal file"""
        success = self.manager.load_tasks()
        self.assertTrue(success)
        self.assertEqual(len(self.manager.tasks), 8)
        
        # Verifica che le task siano state parsate correttamente
        task = self.manager.tasks[0]
        self.assertEqual(task.content, "Task generale 1 (priorità alta)")
        self.assertEqual(task.status, TaskStatus.PENDING)
        self.assertEqual(task.priority, TaskPriority.HIGH)
        self.assertEqual(task.category, "Stato generale")
        
        # Verifica task completata
        completed_task = self.manager.tasks[1]
        self.assertEqual(completed_task.status, TaskStatus.COMPLETED)
    
    def test_task_id_extraction(self):
        """Test estrazione ID task"""
        self.manager.load_tasks()
        
        # Task con ID
        task_with_id = self.manager.tasks[3]  # [DEV-01]
        self.assertEqual(task_with_id.task_id, "DEV-01")
        self.assertEqual(task_with_id.content, "Implementare feature A [DEV-01]")
        
        # Task senza ID (dovrebbe avere ID generato)
        task_without_id = self.manager.tasks[0]
        self.assertTrue(task_without_id.task_id)
        self.assertNotEqual(task_without_id.task_id, "")
    
    def test_add_task(self):
        """Test aggiunta nuova task"""
        self.manager.load_tasks()
        initial_count = len(self.manager.tasks)
        
        # Aggiungi nuova task
        new_task = self.manager.add_task(
            content="Nuova task di test",
            category="Test",
            priority=TaskPriority.HIGH
        )
        
        self.assertEqual(len(self.manager.tasks), initial_count + 1)
        self.assertEqual(new_task.content, "Nuova task di test")
        self.assertEqual(new_task.category, "Test")
        self.assertEqual(new_task.priority, TaskPriority.HIGH)
        self.assertEqual(new_task.status, TaskStatus.PENDING)
        self.assertTrue(new_task.task_id)
    
    def test_update_task(self):
        """Test aggiornamento task"""
        self.manager.load_tasks()
        task_id = self.manager.tasks[0].task_id
        
        # Aggiorna task
        success = self.manager.update_task(
            task_id,
            content="Task aggiornata",
            status=TaskStatus.COMPLETED,
            priority=TaskPriority.LOW,
            category="Aggiornata"
        )
        
        self.assertTrue(success)
        
        # Verifica aggiornamenti
        updated_task = self.manager.get_task(task_id)
        self.assertEqual(updated_task.content, "Task aggiornata")
        self.assertEqual(updated_task.status, TaskStatus.COMPLETED)
        self.assertEqual(updated_task.priority, TaskPriority.LOW)
        self.assertEqual(updated_task.category, "Aggiornata")
    
    def test_delete_task(self):
        """Test eliminazione task"""
        self.manager.load_tasks()
        initial_count = len(self.manager.tasks)
        task_id = self.manager.tasks[0].task_id
        
        # Elimina task
        success = self.manager.delete_task(task_id)
        self.assertTrue(success)
        self.assertEqual(len(self.manager.tasks), initial_count - 1)
        
        # Verifica che la task sia stata eliminata
        deleted_task = self.manager.get_task(task_id)
        self.assertIsNone(deleted_task)
    
    def test_filter_tasks(self):
        """Test filtraggio task"""
        self.manager.load_tasks()
        
        # Filtra task completate
        completed_tasks = self.manager.filter_tasks(status=TaskStatus.COMPLETED)
        self.assertEqual(len(completed_tasks), 2)  # 2 task completate nel test data
        
        for task in completed_tasks:
            self.assertEqual(task.status, TaskStatus.COMPLETED)
        
        # Filtra per priorità alta
        high_priority_tasks = self.manager.filter_tasks(priority=TaskPriority.HIGH)
        self.assertEqual(len(high_priority_tasks), 1)
        
        # Filtra per categoria
        dev_tasks = self.manager.filter_tasks(category="Sviluppo")
        self.assertEqual(len(dev_tasks), 3)
        
        for task in dev_tasks:
            self.assertEqual(task.category, "Sviluppo")
    
    def test_search_tasks(self):
        """Test ricerca task"""
        self.manager.load_tasks()
        
        # Cerca per parola chiave
        feature_tasks = self.manager.search_tasks("feature")
        self.assertEqual(len(feature_tasks), 1)
        self.assertIn("feature", feature_tasks[0].content.lower())
        
        # Cerca per ID task
        dev_tasks = self.manager.search_tasks("DEV")
        self.assertEqual(len(dev_tasks), 3)
        
        # Cerca case insensitive
        bug_tasks = self.manager.search_tasks("BUG")
        self.assertEqual(len(bug_tasks), 1)
    
    def test_sort_tasks(self):
        """Test ordinamento task"""
        self.manager.load_tasks()
        
        # Ordina per priorità
        sorted_by_priority = self.manager.sort_tasks(self.manager.tasks, "priority")
        priorities = [t.priority for t in sorted_by_priority]
        
        # Verifica che le priorità siano in ordine: HIGH, MEDIUM, LOW
        expected_order = [TaskPriority.HIGH, TaskPriority.MEDIUM, TaskPriority.LOW]
        current_order = []
        
        for priority in priorities:
            if priority not in current_order:
                current_order.append(priority)
        
        self.assertEqual(current_order, expected_order)
    
    def test_save_tasks(self):
        """Test salvataggio task"""
        self.manager.load_tasks()
        
        # Modifica una task
        task_id = self.manager.tasks[0].task_id
        self.manager.update_task(task_id, content="Task modificata per test")
        
        # Salva le modifiche
        success = self.manager.save_tasks()
        self.assertTrue(success)
        
        # Ricarica e verifica che le modifiche siano state salvate
        new_manager = TodoManager(self.temp_file_path)
        new_manager.load_tasks()
        
        saved_task = new_manager.get_task(task_id)
        self.assertEqual(saved_task.content, "Task modificata per test")
    
    def test_get_stats(self):
        """Test statistiche"""
        self.manager.load_tasks()
        
        stats = self.manager.get_stats()
        
        self.assertEqual(stats['total'], 8)
        self.assertEqual(stats['completed'], 2)
        self.assertEqual(stats['pending'], 6)  # 8 totali - 2 completate
        self.assertAlmostEqual(stats['completion_rate'], 25.0)  # 2/8 = 25%
    
    def test_metadata_extraction(self):
        """Test estrazione metadata"""
        self.manager.load_tasks()
        
        self.assertIn('last_updated', self.manager.metadata)
        self.assertIn('author', self.manager.metadata)
        self.assertEqual(self.manager.metadata['author'], 'Test Suite')


class TestTask(unittest.TestCase):
    """Test case per la classe Task"""
    
    def test_task_creation(self):
        """Test creazione task"""
        task = Task("Test task content")
        
        self.assertEqual(task.content, "Test task content")
        self.assertEqual(task.status, TaskStatus.PENDING)
        self.assertEqual(task.priority, TaskPriority.MEDIUM)
        self.assertEqual(task.category, "")
        self.assertTrue(task.task_id)
        self.assertIsInstance(task.created_at, datetime)
        self.assertIsInstance(task.updated_at, datetime)
    
    def test_task_markdown_conversion(self):
        """Test conversione task in Markdown"""
        # Task pending
        pending_task = Task("Task pending")
        markdown = pending_task.to_markdown()
        self.assertEqual(markdown, "- [ ] Task pending")
        
        # Task completed
        completed_task = Task("Task completed", status=TaskStatus.COMPLETED)
        markdown = completed_task.to_markdown()
        self.assertEqual(markdown, "- [x] Task completed")
        
        # Task con ID
        task_with_id = Task("Task with ID [TEST-01]")
        markdown = task_with_id.to_markdown()
        self.assertEqual(markdown, "- [ ] Task with ID [TEST-01]")
    
    def test_task_status_changes(self):
        """Test cambiamenti di stato"""
        task = Task("Test task")
        
        # Mark as completed
        task.mark_completed()
        self.assertEqual(task.status, TaskStatus.COMPLETED)
        
        # Mark as in progress
        task.mark_in_progress()
        self.assertEqual(task.status, TaskStatus.IN_PROGRESS)
        
        # Mark as pending
        task.mark_pending()
        self.assertEqual(task.status, TaskStatus.PENDING)
    
    def test_task_equality(self):
        """Test uguaglianza task"""
        task1 = Task("Test task")
        task2 = Task("Test task")
        
        # Task con stesso contenuto ma ID diverso
        self.assertNotEqual(task1.task_id, task2.task_id)
        self.assertEqual(task1.content, task2.content)


def test_edge_cases():
    """Test casi edge"""
    
    # Test con file vuoto
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md', encoding='utf-8') as f:
        f.write("")
        empty_file = f.name
    
    try:
        manager = TodoManager(empty_file)
        success = manager.load_tasks()
        self.assertTrue(success)
        self.assertEqual(len(manager.tasks), 0)
    finally:
        os.unlink(empty_file)
    
    # Test con file contenente solo metadata
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md', encoding='utf-8') as f:
        f.write("""**Ultimo aggiornamento**: 2023
**Autore**: Test
""")
        metadata_only_file = f.name
    
    try:
        manager = TodoManager(metadata_only_file)
        success = manager.load_tasks()
        self.assertTrue(success)
        self.assertEqual(len(manager.tasks), 0)
        self.assertEqual(manager.metadata['author'], 'Test')
    finally:
        os.unlink(metadata_only_file)


if __name__ == "__main__":
    # Esegui i test
    unittest.main(verbosity=2)