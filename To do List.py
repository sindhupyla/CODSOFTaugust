# Define an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

# Function to list all tasks
def list_tasks():
    if tasks:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("Your To-Do List is empty.")

# Function to mark a task as done
def mark_task_done(task_index):
    if 1 <= task_index <= len(tasks):
        task = tasks[task_index - 1]
        print(f"Task '{task}' marked as done!")
        del tasks[task_index - 1]
    else:
        print("Invalid task index.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Mark a task as done")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        task_index = int(input("Enter the task number to mark as done: "))
        mark_task_done(task_index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")