# todo.py

tasks = []  # List to store tasks

def show_menu():
    print("\n--- TODO APP MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print(" Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\n--- Your Tasks ---")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def update_task():
    view_tasks()
    if tasks:
        task_number = int(input("Enter the task number you want to update: "))
        if 1 <= task_number <= len(tasks):
            new_task = input("Enter the new task description: ")
            tasks[task_number - 1] = new_task
            print(" Task updated successfully!")
        else:
            print(" Invalid task number.")

def delete_task():
    view_tasks()
    if tasks:
        task_number = int(input("Enter the task number you want to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f" Task '{deleted_task}' deleted successfully!")
        else:
            print(" Invalid task number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print(" Exiting the app. Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
