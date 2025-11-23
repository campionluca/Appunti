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
        success = self.manager.loadTasks()
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
        self.manager.loadTasks()
        
        # Task con ID
        task_with_id = self.manager.tasks[3]  # [DEV-01]
        self.assertEqual(task_with_id.taskId, "DEV-01")
        self.assertEqual(task_with_id.content, "Implementare feature A [DEV-01]")
        
        # Task senza ID (dovrebbe avere ID generato)
        task_without_id = self.manager.tasks[0]
        self.assertTrue(task_without_id.taskId)
        self.assertNotEqual(task_without_id.taskId, "")
    
    def test_add_task(self):
        """Test aggiunta nuova task"""
        self.manager.loadTasks()
        initial_count = len(self.manager.tasks)
        
        # Aggiungi nuova task
        new_task = self.manager.addTask(
            content="Nuova task di test",
            category="Test",
            priority=TaskPriority.HIGH
        )
        
        self.assertEqual(len(self.manager.tasks), initial_count + 1)
        self.assertEqual(new_task.content, "Nuova task di test")
        self.assertEqual(new_task.category, "Test")
        self.assertEqual(new_task.priority, TaskPriority.HIGH)
        self.assertEqual(new_task.status, TaskStatus.PENDING)
        self.assertTrue(new_task.taskId)
    
    def test_update_task(self):
        """Test aggiornamento task"""
        self.manager.loadTasks()
        task_id = self.manager.tasks[0].taskId
        
        # Aggiorna task
        success = self.manager.updateTask(
            task_id,
            content="Task aggiornata",
            status=TaskStatus.COMPLETED,
            priority=TaskPriority.LOW,
            category="Aggiornata"
        )
        
        self.assertTrue(success)
        
        # Verifica aggiornamenti
        updated_task = self.manager.getTask(task_id)
        self.assertEqual(updated_task.content, "Task aggiornata")
        self.assertEqual(updated_task.status, TaskStatus.COMPLETED)
        self.assertEqual(updated_task.priority, TaskPriority.LOW)
        self.assertEqual(updated_task.category, "Aggiornata")
    
    def test_delete_task(self):
        """Test eliminazione task"""
        self.manager.loadTasks()
        initial_count = len(self.manager.tasks)
        task_id = self.manager.tasks[0].taskId
        
        # Elimina task
        success = self.manager.deleteTask(task_id)
        self.assertTrue(success)
        self.assertEqual(len(self.manager.tasks), initial_count - 1)
        
        # Verifica che la task sia stata eliminata
        deleted_task = self.manager.getTask(task_id)
        self.assertIsNone(deleted_task)
    
    def test_filter_tasks(self):
        """Test filtraggio task"""
        self.manager.loadTasks()
        
        # Filtra task completate
        completed_tasks = self.manager.filterTasks(status=TaskStatus.COMPLETED)
        self.assertEqual(len(completed_tasks), 2)  # 2 task completate nel test data
        
        for task in completed_tasks:
            self.assertEqual(task.status, TaskStatus.COMPLETED)
        
        # Filtra per priorità alta
        high_priority_tasks = self.manager.filterTasks(priority=TaskPriority.HIGH)
        self.assertEqual(len(high_priority_tasks), 1)
        
        # Filtra per categoria
        dev_tasks = self.manager.filterTasks(category="Sviluppo")
        self.assertEqual(len(dev_tasks), 3)
        
        for task in dev_tasks:
            self.assertEqual(task.category, "Sviluppo")
    
    def test_search_tasks(self):
        """Test ricerca task"""
        self.manager.loadTasks()
        
        # Cerca per parola chiave
        feature_tasks = self.manager.searchTasks("feature")
        self.assertEqual(len(feature_tasks), 1)
        self.assertIn("feature", feature_tasks[0].content.lower())
        
        # Cerca per ID task
        dev_tasks = self.manager.searchTasks("DEV")
        self.assertEqual(len(dev_tasks), 3)
        
        # Cerca case insensitive
        bug_tasks = self.manager.searchTasks("BUG")
        self.assertEqual(len(bug_tasks), 1)
    
    def test_sort_tasks(self):
        """Test ordinamento task"""
        self.manager.loadTasks()
        
        # Ordina per priorità
        sorted_by_priority = self.manager.sortTasks(self.manager.tasks, "priority")
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
        self.manager.loadTasks()
        
        # Modifica una task
        task_id = self.manager.tasks[0].taskId
        self.manager.updateTask(task_id, content="Task modificata per test")
        
        # Salva le modifiche
        success = self.manager.saveTasks()
        self.assertTrue(success)
        
        # Ricarica e verifica che le modifiche siano state salvate
        new_manager = TodoManager(self.temp_file_path)
        new_manager.loadTasks()
        
        saved_task = new_manager.getTask(task_id)
        self.assertTrue(saved_task.content.startswith("Task modificata per test"))
    
    def test_get_stats(self):
        """Test statistiche"""
        self.manager.loadTasks()
        
        stats = self.manager.getStats()
        
        self.assertEqual(stats['total'], 8)
        self.assertEqual(stats['completed'], 2)
        self.assertEqual(stats['pending'], 6)
        self.assertAlmostEqual(stats['completionRate'], 25.0)
    
    def test_metadata_extraction(self):
        """Test estrazione metadata"""
        self.manager.loadTasks()
        
        self.assertIn('lastUpdated', self.manager.metadata)
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
        self.assertTrue(task.taskId)
        self.assertIsInstance(task.createdAt, datetime)
        self.assertIsInstance(task.updatedAt, datetime)
    
    def test_task_markdown_conversion(self):
        """Test conversione task in Markdown"""
        # Task pending
        pending_task = Task("Task pending")
        markdown = pending_task.toMarkdown()
        self.assertRegex(markdown, r"^- \[ \] Task pending \[[^\]]+\]$")
        
        # Task completed
        completed_task = Task("Task completed", status=TaskStatus.COMPLETED)
        markdown = completed_task.toMarkdown()
        self.assertRegex(markdown, r"^- \[x\] Task completed \[[^\]]+\]$")
        
        # Task con ID
        task_with_id = Task("Task with ID [TEST-01]")
        markdown = task_with_id.toMarkdown()
        self.assertEqual(markdown, "- [ ] Task with ID [TEST-01]")
    
    def test_task_status_changes(self):
        """Test cambiamenti di stato"""
        task = Task("Test task")
        
        # Mark as completed
        task.markCompleted()
        self.assertEqual(task.status, TaskStatus.COMPLETED)
        
        # Mark as in progress
        task.markInProgress()
        self.assertEqual(task.status, TaskStatus.IN_PROGRESS)
        
        # Mark as pending
        task.markPending()
        self.assertEqual(task.status, TaskStatus.PENDING)
    
    def test_task_equality(self):
        """Test uguaglianza task"""
        task1 = Task("Test task")
        task2 = Task("Test task")
        
        # Task con stesso contenuto ma ID diverso
        self.assertNotEqual(task1.taskId, task2.taskId)
        self.assertEqual(task1.content, task2.content)


def test_edge_cases():
    """Test casi edge"""
    
    # Test con file vuoto
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md', encoding='utf-8') as f:
        f.write("")
        empty_file = f.name
    
    try:
        manager = TodoManager(empty_file)
        success = manager.loadTasks()
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
        success = manager.loadTasks()
        self.assertTrue(success)
        self.assertEqual(len(manager.tasks), 0)
        self.assertEqual(manager.metadata['author'], 'Test')
    finally:
        os.unlink(metadata_only_file)


if __name__ == "__main__":
    # Esegui i test
    unittest.main(verbosity=2)
