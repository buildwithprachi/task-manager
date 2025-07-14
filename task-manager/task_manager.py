import json

def save():
    with open ("tasks.json", "w") as file:
        json.dump(tasks,file)
    
def load():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

load()

from datetime import datetime, date

def menu():
    print("Task manager📝")
    print("1. View Tasks")
    print("2. Add Tasks")
    print("3. Mark as complete")
    print("4. Delete Task")
    print("5. Exit")

def view():
    if not tasks:
        print("No tasks yet!")
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task['done'] else "❌"
        deadline = task.get("deadline", "N/A")
        
        if deadline != "N/A":
            try:
                deadline_date = datetime.strptime(deadline, "%Y-%m-%d").date()
                today = date.today()
                if deadline_date < today:
                    reminder = "🔴 Overdue"
                elif deadline_date == today:
                    reminder = "🟡 Due Today"
                else:
                    reminder = "🟢 On Time"
            except:
                reminder = "🚧 Invalid Date"
        else:
            reminder = "_"

        print(f"{i}. {task['title']} [{status}] | Deadline: {deadline} | {reminder}")

def add():
    new = input("Enter the task: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    task = {"title": new, "done": False, "deadline": deadline}
    tasks.append(task)
    save()
    print("Task added✔️")

def mark():
    view()
    try:
        no = int(input("Enter the number of task to be marked done: "))
        tasks[no-1]["done"] = True
        save()
        print("Task marked as done!")
    except:
        print("Invalid task number!")

def delete():
    view()
    tsk = int(input("Enter the number task to be deleted: "))
    tasks.pop(tsk-1)
    save()
    print("Task deleted!🚮")

while True:
    menu()
    choice = int(input("Choose an option from 1 to 5: "))
    if choice == 1:
        view()
    elif choice == 2:
        add()
    elif choice == 3:
        mark()
    elif choice == 4:
        delete()
    elif choice == 5:
        print("Exiting. Bye :)")
        break
    else:
        print("Invalid choice.")
