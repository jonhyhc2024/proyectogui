import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        # Lista de tareas
        self.tasks = []

        # Configuración de la interfaz
        self.setup_ui()

    def setup_ui(self):
        # Entrada de texto para nuevas tareas
        self.task_entry = tk.Entry(self.root, width=30)
        self.task_entry.pack(pady=10)

        # Botón para añadir tarea
        self.add_task_btn = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.add_task_btn.pack(pady=10)

        # Lista de tareas
        self.tasks_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=50, height=10)
        self.tasks_listbox.pack(pady=10)

        # Botones para eliminar y marcar como completada
        self.delete_task_btn = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_btn.pack(side=tk.LEFT, padx=20)

        self.complete_task_btn = tk.Button(self.root, text="Marcar Completada", command=self.complete_task)
        self.complete_task_btn.pack(side=tk.RIGHT, padx=20)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            self.tasks_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index[0]]
        else:
            messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna tarea.")

    def complete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]] + " (Completada)"
            self.tasks[selected_task_index[0]] = task
            self.tasks_listbox.delete(selected_task_index)
            self.tasks_listbox.insert(selected_task_index, task)
        else:
            messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna tarea.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()