# To-Do List App using Python Lists

# Empty list to store tasks
tasks = []

def show_tasks():
    """Display all tasks with their status."""
    if not tasks:
        print("\n✅ No tasks available!\n")
        return
    print("\n📋 To-Do List:")
    for idx, task in enumerate(tasks, start=1):
        status = "✅ Done" if task[1] else "❌ Pending"
        print(f"{idx}. {task[0]} - {status}")
    print("\n")

def add_task(task_name):
    """Add a new task to the list."""
    tasks.append([task_name, False])
    print(f"\n✅ Task '{task_name}' added successfully!\n")

def remove_task(index):
    """Remove a task by index."""
    try:
        removed_task = tasks.pop(index - 1)
        print(f"\n🗑️ Task '{removed_task[0]}' removed!\n")
    except IndexError:
        print("\n⚠️ Invalid task number!\n")

def mark_complete(index):
    """Mark a task as complete."""
    try:
        tasks[index - 1][1] = True
        print(f"\n✅ Task '{tasks[index - 1][0]}' marked as completed!\n")
    except IndexError:
        print("\n⚠️ Invalid task number!\n")

# Main Menu
while True:
    print("\n📌 To-Do List Menu:")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Complete")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        task_name = input("\nEnter the task: ")
        add_task(task_name)
    elif choice == "3":
        show_tasks()
        index = int(input("Enter task number to remove: "))
        remove_task(index)
    elif choice == "4":
        show_tasks()
        index = int(input("Enter task number to mark complete: "))
        mark_complete(index)
    elif choice == "5":
        print("\n👋 Exiting... Have a productive day!\n")
        break
    else:
        print("\n⚠️ Invalid choice! Please enter a number between 1-5.\n")
