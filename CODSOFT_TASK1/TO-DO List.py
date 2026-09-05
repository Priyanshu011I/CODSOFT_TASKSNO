import json
import os
from datetime import datetime


DATA_FILE = "tasks.json"


# -----------------------------
# File Handling
# -----------------------------

def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
    except OSError as error:
        print(f"\nError saving tasks: {error}")


# -----------------------------
# Utility Functions
# -----------------------------

def generate_task_id(tasks):
    """Generate a unique task ID."""
    if not tasks:
        return 1

    return max(task["id"] for task in tasks) + 1


def get_task_by_id(tasks, task_id):
    """Find a task using its ID."""
    for task in tasks:
        if task["id"] == task_id:
            return task

    return None


def get_valid_priority():
    """Get a valid priority from the user."""
    while True:
        priority = input("Enter priority (Low/Medium/High): ").strip().capitalize()

        if priority in ["Low", "Medium", "High"]:
            return priority

        print("Invalid priority. Please choose Low, Medium, or High.")


def get_valid_date():
    """Get a valid due date."""
    while True:
        date_input = input(
            "Enter due date (YYYY-MM-DD) or press Enter to skip: "
        ).strip()

        if not date_input:
            return "Not Set"

        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


def display_task(task):
    """Display a single task."""
    status = "Completed" if task["completed"] else "Pending"

    print("-" * 60)
    print(f"ID       : {task['id']}")
    print(f"Title    : {task['title']}")
    print(f"Priority : {task['priority']}")
    print(f"Due Date : {task['due_date']}")
    print(f"Status   : {status}")
    print("-" * 60)


# -----------------------------
# Task Operations
# -----------------------------

def add_task(tasks):
    """Add a new task."""
    print("\n" + "=" * 60)
    print("ADD NEW TASK")
    print("=" * 60)

    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    priority = get_valid_priority()
    due_date = get_valid_date()

    task = {
        "id": generate_task_id(tasks),
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("\nTask added successfully!")


def view_tasks(tasks):
    """Display all tasks."""
    print("\n" + "=" * 60)
    print("ALL TASKS")
    print("=" * 60)

    if not tasks:
        print("No tasks available.")
        return

    for task in tasks:
        display_task(task)


def mark_task_completed(tasks):
    """Mark a task as completed."""
    print("\n" + "=" * 60)
    print("MARK TASK AS COMPLETED")
    print("=" * 60)

    if not tasks:
        print("No tasks available.")
        return

    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    task = get_task_by_id(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    if task["completed"]:
        print("This task is already completed.")
        return

    task["completed"] = True
    save_tasks(tasks)

    print("Task marked as completed!")


def update_task(tasks):
    """Update an existing task."""
    print("\n" + "=" * 60)
    print("UPDATE TASK")
    print("=" * 60)

    if not tasks:
        print("No tasks available.")
        return

    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    task = get_task_by_id(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    print(f"\nCurrent title: {task['title']}")
    new_title = input(
        "Enter new title (press Enter to keep current): "
    ).strip()

    if new_title:
        task["title"] = new_title

    print(f"Current priority: {task['priority']}")
    change_priority = input(
        "Do you want to change priority? (y/n): "
    ).strip().lower()

    if change_priority == "y":
        task["priority"] = get_valid_priority()

    print(f"Current due date: {task['due_date']}")
    change_date = input(
        "Do you want to change due date? (y/n): "
    ).strip().lower()

    if change_date == "y":
        task["due_date"] = get_valid_date()

    save_tasks(tasks)

    print("\nTask updated successfully!")


def delete_task(tasks):
    """Delete a task."""
    print("\n" + "=" * 60)
    print("DELETE TASK")
    print("=" * 60)

    if not tasks:
        print("No tasks available.")
        return

    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    task = get_task_by_id(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    print(f"\nTask: {task['title']}")

    confirmation = input(
        "Are you sure you want to delete this task? (y/n): "
    ).strip().lower()

    if confirmation == "y":
        tasks.remove(task)
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Deletion cancelled.")


def search_tasks(tasks):
    """Search tasks by title."""
    print("\n" + "=" * 60)
    print("SEARCH TASKS")
    print("=" * 60)

    if not tasks:
        print("No tasks available.")
        return

    keyword = input("Enter keyword to search: ").strip().lower()

    results = [
        task for task in tasks
        if keyword in task["title"].lower()
    ]

    if not results:
        print("No matching tasks found.")
        return

    print(f"\nFound {len(results)} matching task(s):")

    for task in results:
        display_task(task)


# -----------------------------
# Statistics
# -----------------------------

def show_statistics(tasks):
    """Display task statistics."""
    print("\n" + "=" * 60)
    print("TASK STATISTICS")
    print("=" * 60)

    total = len(tasks)
    completed = sum(task["completed"] for task in tasks)
    pending = total - completed

    print(f"Total Tasks     : {total}")
    print(f"Completed Tasks : {completed}")
    print(f"Pending Tasks   : {pending}")

    if total > 0:
        completion_rate = (completed / total) * 100
        print(f"Completion Rate : {completion_rate:.2f}%")


# -----------------------------
# Main Menu
# -----------------------------

def display_menu():
    """Display the main menu."""
    print("\n")
    print("=" * 60)
    print("              TO-DO LIST APPLICATION")
    print("=" * 60)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Search Tasks")
    print("7. Task Statistics")
    print("8. Exit")
    print("=" * 60)


def main():
    """Main application function."""
    tasks = load_tasks()

    print("\nWelcome to the To-Do List Application!")

    while True:
        display_menu()

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            mark_task_completed(tasks)

        elif choice == "4":
            update_task(tasks)

        elif choice == "5":
            delete_task(tasks)

        elif choice == "6":
            search_tasks(tasks)

        elif choice == "7":
            show_statistics(tasks)

        elif choice == "8":
            print("\nThank you for using the To-Do List Application!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select a number from 1 to 8.")


if __name__ == "__main__":
    main()