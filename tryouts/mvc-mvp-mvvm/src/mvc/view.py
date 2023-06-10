import tkinter as tk
from typing import Callable

from mvc.interfaces import Task
from mvc.model import Model

TITLE = "Todo List"

DELETE_BTN_TXT = "Delete"

LEFT_BUTTON_CLICK = "<Button-1>"


class TodoList(tk.Tk):
    def __init__(self, model: Model) -> None:
        super().__init__()
        self.model = model
        self.title(TITLE)
        self.geometry("500x300")
        self.create_ui()
        self.update_task_list()

    def create_ui(self) -> None:
        self.frame = tk.Frame(self, padx=10, pady=10)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.task_list = tk.Listbox(self.frame, height=10, activestyle="none")
        self.task_list.bind("<FocusOut>", self.on_task_list_focus_out)
        self.task_list.bind("<<ListboxSelect>>", self.on_select_task)
        self.task_list.pack(fill=tk.X)

        self.my_entry = tk.Entry(self.frame)
        self.my_entry.bind("<FocusIn>", self.on_my_entry_focus_in)
        self.my_entry.bind("<FocusOut>", self.on_my_entry_focus_out)
        self.my_entry.pack(fill=tk.X)

        self.add_task_button = tk.Button(
            self.frame,
            text="Add task",
            width=6,
            pady=5,
            state=tk.DISABLED,
        )

        self.del_task_button = tk.Button(
            self.frame,
            text=DELETE_BTN_TXT,
            width=6,
            pady=5,
            state=tk.DISABLED,
        )
        self.add_task_button.pack(side=tk.LEFT, anchor=tk.NW)
        self.del_task_button.pack(side=tk.LEFT, anchor=tk.NW)

    def bind_add_task(self, callback: Callable[[tk.Event], None]) -> None:
        self.my_entry.bind(self.add_task_button, callback)

    def bind_delete_task(self, callback: Callable[[tk.Event], None]) -> None:
        self.del_task_button.bind(LEFT_BUTTON_CLICK, callback)

    def get_entry_task(self) -> Task:
        task = Task(title=self.my_entry.get())
        return task

    def clear_entry(self) -> None:
        self.my_entry.delete(0, tk.END)

    def on_write(self, event=None) -> None:
        self.add_task_button.config(state=tk.NORMAL)

    def on_select_task(self, event=None) -> None:
        self.del_task_button.config(state=tk.NORMAL)

    def on_my_entry_focus_in(self, event=None) -> None:
        self.add_task_button.config(state=tk.NORMAL)

    def on_my_entry_focus_out(self, event=None) -> None:
        self.add_task_button.config(state=tk.DISABLED)

    def on_task_list_focus_out(self, event=None) -> None:
        self.task_list.selection_clear(0, tk.END)
        self.del_task_button.config(state=tk.DISABLED)

    def update_task_list(self) -> None:
        self.task_list.delete(0, tk.END)
        for item in self.model.get_tasks():
            self.task_list.insert(tk.END, item)
