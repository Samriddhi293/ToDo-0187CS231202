import json
import os


class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed
        }


class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            self.save_tasks()
            return

        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.tasks = [Task(**task) for task in data]
        except (json.JSONDecodeError, IOError):
            print("⚠ Error loading tasks. Starting with empty list.")
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title):
        self.tasks.append(Task(title))
        self.save_tasks()

    def edit_task(self, index, new_title):
        self.tasks[index].title = new_title
        self.save_tasks()

    def delete_task(self, index):
        self.tasks.pop(index)
        self.save_tasks()

    def toggle_task(self, index):
        self.tasks[index].completed = not self.tasks[index].completed
        self.save_tasks()

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for i, task in enumerate(self.tasks):
            status = "✔5" if task.completed else "✘"
            print(f"{i + 1}. [{status}] {task.title}")


def main():
    todo = ToDoList()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark/Unmark Task")
        print("6. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                todo.show_tasks()

            elif choice == "2":
                title = input("Enter task title: ")
                todo.add_task(title)

            elif choice == "3":
                todo.show_tasks()
                index = int(input("Task number to edit: ")) - 1
                new_title = input("New title: ")
                todo.edit_task(index, new_title)

            elif choice == "4":
                todo.show_tasks()
                index = int(input("Task number to delete: ")) - 1
                todo.delete_task(index)

            elif choice == "5":
                todo.show_tasks()
                index = int(input("Task number to toggle: ")) - 1
                todo.toggle_task(index)

            elif choice == "6":
                print("Exiting...")
                break

            else:
                print("Invalid option.")

        except (IndexError, ValueError):
            print("❌ Invalid input. Try again.")


if __name__ == "__main__":
    main()
