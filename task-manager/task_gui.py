import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkfont
import json
import os

root = tk.Tk()
root.title("Task Manager📝")
root.geometry("400x450")
root.configure(bg="#a7c7e7")

custom_font = ("Calibri", 11)
tasks = []

def load_tasks():
    global tasks
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    else:
        tasks = []

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

from datetime import datetime

def add_task():
    task_title = entry.get()
    deadline = date.get()
    if task_title :
        task = {"title": task_title, "done": False, "deadline": deadline}
        tasks.append(task)
        save_tasks()
        update_listbox()
        entry.delete(0, tk.END)
        date.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def update_listbox():
    listbox.delete(0, tk.END)
    today = datetime.today().date()

    for task in tasks:
        status = "☑️" if task["done"] else "⏳"
        deadline_str = task.get("deadline", "")
        reminder = ""
        if deadline_str:
            try:
                deadline_date = datetime.strptime(deadline_str, "%Y-%m-%d").date()
                if not task["done"]:
                    if deadline_date < today:
                        reminder = "🔴 Overdue"
                    elif deadline_date == today:
                        reminder = "🟡 Due Today"
                    else:
                        reminder = f"📆 Due {deadline_date}"
            except ValueError:
                reminder = "🚧 Invalid Date"
        
        listbox.insert(tk.END, f"{task["title"]} {status}{reminder}") 

def mark_complete():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]['done'] = True
        update_listbox()

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_listbox()

def  sort_task():
    def get_deadline(task):
        try:
            return datetime.strptime(task['deadline'], "%Y-%m-%d")
        except:
            return datetime.messagebox
    
    tasks.sort(key=get_deadline)
    update_listbox()

entry_label = tk.Label(root, text="Enter Task:", bg="#d9d9d9", font=custom_font)
entry_label.pack()

entry = tk.Entry(root, width = 30, bg="#b0bec5", relief="groove", font=custom_font)
entry.pack(pady=10)

deadline_label = tk.Label(root, text="Deadline (YYYY-MM-DD):", bg="#d9d9d9", font=custom_font)
deadline_label.pack()

date = tk.Entry(root, width = 20, bg="#b0bec5", relief="groove", font=custom_font)
date.pack(pady=5)

add_button = tk.Button(root, text="➕ Add Task", bg="#b8e8fc", fg="#444444", relief="groove", font=custom_font, command=add_task)
add_button.pack(pady=5)

mark_button = tk.Button(root, text="☑️ Mark Complete", bg="#b8e8fc", fg="#444444", relief="groove", font=custom_font, command=mark_complete)
mark_button.pack(pady=5)

delete_button = tk.Button(root, text="🚮 Delete Task", bg="#b8e8fc", fg="#444444", relief="groove", font=custom_font, command=delete_task)
delete_button.pack(pady=5)

sort_button = tk.Button(root, text="📆 Sort by Deadline", bg="#b8e8fc", fg="#444444", relief="groove", font=custom_font, command=sort_task)
sort_button.pack(pady=5)

listbox = tk.Listbox(root, width=40, height=10, bg="#cdeac0", relief="groove", font=custom_font)
listbox.pack(pady=10)

load_tasks()
update_listbox()

root.mainloop() 