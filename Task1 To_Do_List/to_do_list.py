import tkinter as tk
from tkinter import messagebox

tasks = []

# Function to add a new task
def add_task():
    task_name = entry_name.get().strip()
    if not task_name:
        messagebox.showinfo("Info", "Empty field found. Please enter your task.")
        return
    tasks.append({"task": task_name, "status": "Incomplete"})
    update_task_listbox()
    messagebox.showinfo("Success", "Task added successfully.")

# Function to view all tasks
def view_tasks():
    if not tasks:
        messagebox.showinfo("Info", "No tasks to display.")
    else:
        task_details = ""
        for i, task in enumerate(tasks, start=1):
            task_details += f"{i}. {task['task']} - Status: {task['status']}\n"
        messagebox.showinfo("Task List", task_details)

# Function to update a task
def update_task():
    selected_index = listbox_tasks.curselection()
    if not selected_index:
        messagebox.showinfo("Info", "Please select a task.")
        return
    choice = selected_index[0]
    new_task_name = entry_name.get().strip()
    if not new_task_name:
        messagebox.showinfo("Info", "Empty field found. Please enter the updated task name.")
        return
    tasks[choice]['task'] = new_task_name
    update_task_listbox()
    messagebox.showinfo("Success", "Task updated successfully.")

# Function to delete a task
def delete_task():
    selected_index = listbox_tasks.curselection()
    if not selected_index:
        messagebox.showinfo("Info", "Please select a task.")
        return
    choice = selected_index[0]
    del tasks[choice]
    update_task_listbox()
    messagebox.showinfo("Success", "Task deleted successfully.")

# Function to mark a task as complete
def mark_task_complete():
    selected_index = listbox_tasks.curselection()
    if not selected_index:
        messagebox.showinfo("Info", "Please select a task.")
        return
    choice = selected_index[0]
    tasks[choice]['status'] = "Complete"
    update_task_listbox()
    messagebox.showinfo("Success", "Task marked as complete.")

# Function to update the task listbox
def update_task_listbox():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        listbox_tasks.insert(tk.END, f"{task['task']} - Status: {task['status']}")

# Main function
def main():
    global entry_name, listbox_tasks

    root = tk.Tk()
    root.title("To-Do List")

    frame_task_list = tk.Frame(root)
    frame_task_list.grid(row=0, column=0, padx=10, pady=10, sticky='w')

    label_task_entry = tk.Label(frame_task_list, text="Enter task below :")
    label_task_entry.grid(row=0, column=0, padx=5, pady=5, sticky='w')

    entry_name = tk.Entry(frame_task_list)
    entry_name.grid(row=1, column=0, padx=5, pady=5, sticky='w')

    button_add_task = tk.Button(frame_task_list, text="Add Task", command=add_task)
    button_add_task.grid(row=2, column=0, padx=5, pady=5, sticky='w')

    listbox_tasks = tk.Listbox(root, height=10, width=50)
    listbox_tasks.grid(row=1, column=0, padx=10, pady=10, sticky='w')

    scrollbar_tasks = tk.Scrollbar(root)
    scrollbar_tasks.grid(row=1, column=1, sticky='ns')
    scrollbar_tasks.config(command=listbox_tasks.yview)
    listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)

    button_view_tasks = tk.Button(root, text="View Tasks", command=view_tasks)
    button_view_tasks.grid(row=2, column=0, padx=10, pady=5, sticky='w')

    button_update_task = tk.Button(root, text="Update Task", command=update_task)
    button_update_task.grid(row=3, column=0, padx=10, pady=5, sticky='w')

    button_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
    button_delete_task.grid(row=4, column=0, padx=10, pady=5, sticky='w')

    button_mark_complete = tk.Button(root, text="Mark Task as Complete", command=mark_task_complete)
    button_mark_complete.grid(row=5, column=0, padx=10, pady=5, sticky='w')

    root.mainloop()

if __name__ == "__main__":
    main()
