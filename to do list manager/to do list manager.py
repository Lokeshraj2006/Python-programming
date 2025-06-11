import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    desc, status = line.rsplit(" | ", 1)
                    tasks.append({"desc": desc, "completed": status == "done"})
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            status = "done" if task["completed"] else "todo"
            f.write(f"{task['desc']} | {status}\n")

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{idx}. {status} {task['desc']}")

def add_task(tasks):
    desc = input("Enter task description: ").strip()
    if desc:
        tasks.append({"desc": desc, "completed": False})
        print("Task added.")
    else:
        print("Empty description. Task not added.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: "))
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            print(f"Deleted: {removed['desc']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def mark_completed(tasks):
    display_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark as completed: "))
        if 1 <= idx <= len(tasks):
            tasks[idx - 1]["completed"] = True
            print(f"Marked as completed: {tasks[idx - 1]['desc']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Manager")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task as completed")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            mark_completed(tasks)
            save_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()