import os
import json

# File where tasks are stored
TASKS_FILE = "tasks.json"

# Load tasks from JSON file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Show all tasks
def view_tasks(tasks):
    if not tasks:
        print("\n📌 No tasks yet!\n")
        return
    print("\n Your To-Do List:")
    for idx, task in enumerate(tasks, 1):
        status = "✔️ Done" if task["done"] else "❌ Not Done"
        print(f"{idx}. {task['title']} [{status}] (Priority: {task['priority']})")
    print()

# Add a task
def add_task(tasks):
    title = input("Enter task title: ")
    priority = input("Enter priority (High/Medium/Low): ").capitalize()
    tasks.append({"title": title, "done": False, "priority": priority})
    save_tasks(tasks)
    print("  Task added!\n")

# Mark task as completed
def mark_done(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter task number to mark as done: "))
        tasks[task_no - 1]["done"] = True
        save_tasks(tasks)
        print("🎉 Task marked as done!\n")
    except (ValueError, IndexError):
        print(" Invalid task number!\n")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_no - 1)
        save_tasks(tasks)
        print(f" Deleted task: {removed['title']}\n")
    except (ValueError, IndexError):
        print("Invalid task number!\n")

# Search tasks
def search_tasks(tasks):
    keyword = input("Enter keyword to search: ").lower()
    results = [task for task in tasks if keyword in task["title"].lower()]
    if results:
        print("\n Search Results:")
        for idx, task in enumerate(results, 1):
            status = "✔️ Done" if task["done"] else "❌ Not Done"
            print(f"{idx}. {task['title']} [{status}] (Priority: {task['priority']})")
        print()
    else:
        print(" No matching tasks found!\n")

# Main app loop
def main():
    tasks = load_tasks()
    while True:
        print("====== To-Do List App ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Search Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            search_tasks(tasks)
        elif choice == "6":
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("⚠️ Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
