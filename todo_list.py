# add task
# show task
# delete task


def show_tasks(tasks):
    if not tasks:
        print('\nNo tasks in your to-do list.')
    else:
        print("\nYour Tasks: ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"{task} add to your to-do list.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("ENter the number of the task to delete: "))- 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"{removed_task} removed from your to-do list.")
        else:
            print("Invalid Task")
    except ValueError:
        print("Please enter a Valid Number")


def todo_list():
    tasks = []
    while True:
        print('\nOption: 1. View Tasks 2. Add Task 3. Delete Task 4. Exit')
        choice = input("Choose an option: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Exiting the To-Do List App.")
            break
        else:
            print("Invalid choice. Try again")

todo_list()