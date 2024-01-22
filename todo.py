import tkinter as tk
from tkinter import Entry, Button, Listbox, Scrollbar

class ToDoListGUI:
    """A simple ToDo list GUI using Tkinter."""
    def __init__(self, root):
        self.root = root
        self.root.title("ToDo List")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        window_width = 400
        window_height = 300

        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        self.tasks = []

        self.task_entry = Entry(root, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        add_button = Button(root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = Listbox(root, width=40, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        scrollbar = Scrollbar(root, command=self.task_listbox.yview)
        scrollbar.grid(row=1, column=2, sticky='ns')
        self.task_listbox.config(yscrollcommand=scrollbar.set)

        done_button = Button(root, text="Mark as Done", command=self.mark_done)
        done_button.grid(row=2, column=0, columnspan=2, pady=10)

        quit_button = Button(root, text="Quit", command=root.destroy)
        quit_button.grid(row=3, column=0, columnspan=2, pady=10)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task and task not in self.tasks:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        elif task:
            print(f'Task "{task}" already in the list.')

    def mark_done(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            task = self.tasks[task_index]
            self.task_listbox.delete(task_index)
            print(f'Task "{task}" marked as done.')
        else:
            print("Please select a task to mark as done.")

def main():
    root = tk.Tk()
    todo_gui = ToDoListGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
