#To Do List
tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added done")

def delete_task():
    if len(tasks) == 0:
        print("no tasks to delete")
    else:
        print("Task")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        
        choice = int(input("Enter the task number to delete: "))
        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print("Task deleted done")
        else:
            print("Invalid task number")


def view_task():
    if len(tasks) == 0:
        print("no task")
    else:
        print("List of tasks: ")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")


def main():
    while True:
        print("\n To-Do-List Application")
        print("1. Add task")
        print("2. Delete task")
        print("3. View")
        print("4. Quit")

        choice = int(input("Enter your choice:"))
        if choice == 1:
            add_task()
        elif choice == 2:
            delete_task()
        elif choice == 3:
            view_task()
        elif choice == 4:
            print("Ok")
            break
        else:
            print("Invalid choice")

if _name=="main_":
    main()
