import os
class TaskManager:
    """Clase que administra las tareas"""
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)