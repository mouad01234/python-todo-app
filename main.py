import tkinter as tk
from tkinter import simpledialog
import json

try:
    with open("tasks.json") as f:
        tasks = json.load(f)
except:
    tasks = []

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def display_tasks():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task['done'] else "❌"
        listbox.insert(tk.END, f"{status} {task['title']} - {task['description']}")

def add_task():
    title = simpledialog.askstring("Title", "Enter task title:")
    if title:
        desc = simpledialog.askstring("Description", "Enter task description:")
        tasks.append({"title": title, "description": desc or "", "done": False})
        save_tasks()
        display_tasks()

def edit_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = tasks[index]
        new_title = simpledialog.askstring("Edit Title", "New title:", initialvalue=task['title'])
        if new_title:
            new_desc = simpledialog.askstring("Edit Description", "New description:", initialvalue=task['description'])
            task['title'] = new_title
            task['description'] = new_desc or ""
            save_tasks()
            display_tasks()

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        save_tasks()
        display_tasks()

def toggle_done():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]['done'] = not tasks[index]['done']
        save_tasks()
        display_tasks()
root = tk.Tk()
root.title("To-Do Manager")
root.geometry("500x450")
root.configure(bg="#1e1e1e")

tk.Label(root, text="To-Do Manager", font=("Arial", 20, "bold"), fg="#e91e63", bg="#1e1e1e").pack(pady=10)

btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Add Task", width=12, bg="#4caf50", fg="white", command=add_task).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Edit Task", width=12, bg="#2196f3", fg="white", command=edit_task).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete Task", width=12, bg="#f44336", fg="white", command=delete_task).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Toggle Done", width=12, bg="#ff9800", fg="white", command=toggle_done).grid(row=0, column=3, padx=5)

listbox = tk.Listbox(root, width=65, height=15, bg="#2e2e2e", fg="white", selectbackground="#e91e63", font=("Arial", 12))
listbox.pack(pady=10)

display_tasks()
root.mainloop()
