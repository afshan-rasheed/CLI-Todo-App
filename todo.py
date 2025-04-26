# todo.py

tasks = []  # List to store tasks

def show_menu():
    print("\n--- TODO APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("✅ Task added.")

def view_tasks():
    if not tasks:
        print("⚠️ No tasks yet!")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def update_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to update: "))
        if 0 < task_num <= len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[task_num - 1] = new_task
            print("✅ Task updated.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 0 < task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"✅ Deleted task: {deleted_task}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

while True:
    show_menu()
    choice = input("Enter choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("👋 Exiting... Bye!")
        break
    else:
        print("⚠️ Invalid choice. Try again.")
