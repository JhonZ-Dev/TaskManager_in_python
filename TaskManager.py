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
        else:
            print("Task not found.")

    def list_tasks(self):
        if not self.tasks:
            return "No tasks found."
        else:
            return "\n".join(self.tasks)

    def save_tasks_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write("\n".join(self.tasks))

    def load_tasks_from_file(self, filename):
        if os.path.isfile(filename):
            with open(filename, 'r') as file:
                self.tasks = file.read().splitlines()
                print("Tasks loaded from file.")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_file = "tasks.txt"

    # Cargar tareas desde el archivo si existe
    task_manager.load_tasks_from_file(task_file)

    while True:
        print("Options:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. List tasks")
        print("4. Save tasks to file")
        print("5. Quit")

        choice = input("Select an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            task_manager.add_task(task)
            print("Task added.")

        elif choice == "2":
            task = input("Enter the task to remove: ")
            task_manager.remove_task(task)

        elif choice == "3":
            tasks = task_manager.list_tasks()
            print("Tasks:")
            print(tasks)

        elif choice == "4":
            task_manager.save_tasks_to_file(task_file)
            print("Tasks saved to file.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please select a valid option.")
