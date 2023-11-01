import os
class TaskManager:
    """Clase que administra las tareas"""
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)