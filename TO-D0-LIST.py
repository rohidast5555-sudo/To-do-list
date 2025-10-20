print("-- Welcome to the Professional To-Do List Manager --")

TODO_FILE = "todo-list"

def load_tasks():
        try:
            with open( "TODO_FILE", "r") as file:
                return [line.strip() for line in file.readlines() if line.strip()]
        except FileNotFoundError:
            return []

def save_task(todo_list):

        with open("TODO_FILE", "w") as file:
            for task in todo_list:
                file.write(task + '\n')

def add_task(todo_list):
    task = input("Enter your task:")
    if task.strip():
        todo_list.append(task)
        save_task(todo_list)
        print(f"add task {task} successfully!")
    else:
        print("Please enter a valid task!")

def view_task(todo_list):
    if todo_list:
        print("Your to-do list")
        print("*" * 20)
        for i ,task in enumerate(todo_list , 1):
            print(f"{i}.{task}")
        print(f"\n Total task: {len(todo_list)}")
    else:
        print("Your to-do list is empty!")

def remove_task(todo_list):
    view_task(todo_list)
    try:
        task_num = int(input("Enter you task number: "))
        if 1 <= task_num <= len(todo_list):
            remove = todo_list.pop(task_num - 1)
            save_task(todo_list)
            print(f"your remove task is {remove}")
        else:
            print("your number is not valid")
    except ValueError:
        print("Enter a valid valid number please!")

def clear_task(todo_list):
    if todo_list:
        clear_task = input("Are you sure you want to clear all tasks? (y/n): ")
        if clear_task.lower() == 'y':
            todo_list.clear()
            save_task(todo_list)
            print("All tasks have been cleared!")
    else:
        print("you task is empty!")


def main():
    todo_list = load_tasks()
    while True:
        print( "\n" + "=" * 40 )
        print("         TO DO LIST MANAGER")
        print("=" * 40)
        print("1.Add task")
        print("2.view tasks")
        print("3.remove task")
        print("4.clear all task")
        print("Exit")
        print("-" * 40)

        choice = int((input("Enter your choice (1-5):")).strip())
        if choice == 1:
            add_task(todo_list)
        elif choice == 2:
            view_task(todo_list)
        elif choice == 3:
            remove_task(todo_list)
        elif choice == 4:
            clear_task(todo_list)
        elif choice == 5:
            print("have nice day!😉")
            print("Goodbye")
            break
        else:
            print("enter a valid number between (1-5)")


if __name__ == "__main__":
        main()
