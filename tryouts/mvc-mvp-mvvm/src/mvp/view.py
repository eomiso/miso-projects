import tkinter as tk
from typing import Protocol

from mvp.interfaces import Task

TITLE = "Todo List"

DELETE_BTN_TXT = "Delete"

LEFT_BUTTON_CLICK = "<Button-1>"


class IPresenter(Protocol):
    def handle_add_task(self, event=None) -> None:
        ...

    def handle_delete_task(self, event=None) -> None:
        ...


class TodoList(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title(TITLE)
        self.geometry("500x300")

    # In the MVP pattern, instead of using bindings,
    # we use the reference to the presenter(controller)
    def create_ui(self, presenter: IPresenter) -> None:
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
        self.my_entry.bind("<Return>", presenter.handle_add_task)
        self.del_task_button.bind(LEFT_BUTTON_CLICK, presenter.handle_delete_task)
        self.add_task_button.pack(side=tk.LEFT, anchor=tk.NW)
        self.del_task_button.pack(side=tk.LEFT, anchor=tk.NW)

    def get_entry_task(self) -> Task:
        task = Task(title=self.my_entry.get())
        return task

    def clear_entry(self) -> None:
        self.my_entry.delete(0, tk.END)

    def on_write(self, event=None) -> None:
        self.add_task_button.config(state=tk.NORMAL)

    @property
    def selected_task(self) -> Task:
        title = self.task_list.get(self.task_list.curselection())
        return Task(title=title)

    def on_select_task(self, event=None) -> None:
        self.del_task_button.config(state=tk.NORMAL)

    def on_my_entry_focus_in(self, event=None) -> None:
        self.add_task_button.config(state=tk.NORMAL)

    def on_my_entry_focus_out(self, event=None) -> None:
        self.add_task_button.config(state=tk.DISABLED)

    def on_task_list_focus_out(self, event=None) -> None:
        self.task_list.selection_clear(0, tk.END)
        self.del_task_button.config(state=tk.DISABLED)

    def update_task_list(self, tasks: list[Task]) -> None:
        self.task_list.delete(0, tk.END)
        for task in tasks:
            item = task.title
            self.task_list.insert(tk.END, item)
