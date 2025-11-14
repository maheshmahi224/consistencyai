tasks = []

def show_tasks():
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added.")

def delete_task():
    show_tasks()
    num = int(input("Enter task number to delete: "))
    if 0 < num <= len(tasks):
        tasks.pop(num - 1)
        print("Task deleted.")
    else:
        print("Invalid number.")

def main():
    while True:
        print("\n1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()
