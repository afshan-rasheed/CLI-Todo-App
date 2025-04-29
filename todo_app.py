class TodoApp:
    def __init__(self):
        self.tasks = []

    @staticmethod
    def show_menu():
        print("\n--- Todo App ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

    @staticmethod
    def get_choice():
        return input("Enter your choice (1-5): ")

    def add_task(self):
        task = input("Enter the task: ")
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found!")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def update_task(self):
        self.view_tasks()
        task_no = input("Enter task number to update: ")
        if task_no.isdigit():
            task_no = int(task_no)
            if 1 <= task_no <= len(self.tasks):
                new_task = input("Enter new task: ")
                self.tasks[task_no - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number!")
        else:
            print("Invalid input! Please enter a number.")

    def delete_task(self):
        self.view_tasks()
        task_no = input("Enter task number to delete: ")
        if task_no.isdigit():
            task_no = int(task_no)
            if 1 <= task_no <= len(self.tasks):
                deleted = self.tasks.pop(task_no - 1)
                print(f"Task '{deleted}' deleted successfully!")
            else:
                print("Invalid task number!")
        else:
            print("Invalid input! Please enter a number.")


# Application entry
def main():
    app = TodoApp()
    while True:
        TodoApp.show_menu()
        choice = TodoApp.get_choice()

        if choice == '1':
            app.add_task()
        elif choice == '2':
            app.view_tasks()
        elif choice == '3':
            app.update_task()
        elif choice == '4':
            app.delete_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-5.")


if __name__ == "__main__":
    main()

