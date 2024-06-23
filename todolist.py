import sys

# List to hold the tasks
tasks = []

def display_menu():
    print("\nTo-Do List Application")
    print("======================")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("\nEnter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("\nChoose an option: ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()