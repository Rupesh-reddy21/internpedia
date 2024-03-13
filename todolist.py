import os
def load_tasks():
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                task, status = line.strip().split(",")
                tasks.append((task, status == "done"))
    return tasks
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task, done in tasks:
            status = "done" if done else "undone"
            file.write(f"{task},{status}\n")
def view_tasks(tasks):
    print("\nTasks:")
    if not tasks:
        print("No tasks.")
    else:
        for i, (task, done) in enumerate(tasks, start=1):
            status = "Done" if done else "Undone"
            print(f"{i}. {task} - {status}")
def add_task(tasks):
    task = input("\nEnter the new task: ")
    tasks.append((task, False))
    save_tasks(tasks)
    print("Task added successfully.")
def mark_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to mark (0 to cancel): ")) - 1
        if task_index == -1:
            return
        if 0 <= task_index < len(tasks):
            task, done = tasks[task_index]
            tasks[task_index] = (task, not done)
            save_tasks(tasks)
            print("Task marked successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to remove (0 to cancel): ")) - 1
        if task_index == -1:
            return
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            save_tasks(tasks)
            print("Task removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
def display_menu():
    print("\nMenu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done/undone")
    print("4. Remove task")
    print("5. Quit")
def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Thank you for using the To-Do List application!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
if __name__ == "__main__":
    main()