tasks = []

def display_menu():
    print("1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. Display Tasks")
    print("5. Exit")

while True:
    display_menu()
    choice = input("Enter your choice: ")

# Handle Add Choice

    if choice == '1':
        task = input("Enter task description: ")
        tasks.append(task)
        print("Task added!")

# Handle Update Choice

    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks to update.")
        else:
            for index, task in enumerate(tasks):
                print(f"{index+1}. {task}")
            task_index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter new task description: ")
            tasks[task_index] = new_task
            print("Task updated!")

# Handle Delete Choice

    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index+1}. {task}")
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            print(f"Task '{deleted_task}' deleted!")
        else:
            print("Invalid task number.")   

# Handle Display Choice

    elif choice == '4':
        if len(tasks) == 0:
            print("No tasks to display.")
        else:
            print("Tasks:")
            for index, task in enumerate(tasks):
                print(f"{index+1}. {task}")

# Handle Exit Choice

    elif choice == '5':
        print("Exiting the To-Do List application.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")