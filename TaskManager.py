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

    def list_tasks(self):
        if not self.tasks:
            return "No tasks found."
        return "\n".join(self.tasks)
    def save_tasks_to_file(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')
    def load_tasks_from_file(self, filename):
        if os.path.isfile(filename):
            with open(filename, 'r') as file:
                self.tasks = file.read().splitlines()
