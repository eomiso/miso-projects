import tkinter as tk

TITLE = "Simple Todo List"

TASK_LIST = [
    "Process email inbox",
    "Write blog post",
    "Prepare video scripts",
    "Tax accounting",
    "Prepare presentation",
    "Go to the gym",
]

DELETE_BTN_TXT = "Delete"


class TodoList(tk.Tk):
    def __init__(self, task_list: list[str]) -> None:
        super().__init__()
        self.title(TITLE)
        self.geometry("500x300")
        self.create_ui()

        for item in task_list:
            self.task_list.insert(tk.END, item)

    def create_ui(self) -> None:
        self.frame = tk.Frame(self, padx=10, pady=10)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.task_list = tk.Listbox(self.frame, height=10, activestyle="none")
        self.task_list.bind("<FocusOut>", self.on_task_list_focus_out)
        self.task_list.bind("<<ListboxSelect>>", self.on_select_task)
        self.task_list.pack(fill=tk.X)

        self.add_task_button = tk.Button(
            self.frame,
            text="Add task",
            width=6,
            pady=5,
            command=self.add_task,
            state=tk.DISABLED,
        )

        self.my_entry = tk.Entry(self.frame)
        self.my_entry.bind(self.add_task_button, self.add_task)
        self.my_entry.bind("<FocusIn>", self.on_my_entry_focus_in)
        self.my_entry.bind("<FocusOut>", self.on_my_entry_focus_out)
        self.my_entry.pack(fill=tk.X)

        self.del_task_button = tk.Button(
            self.frame,
            text=DELETE_BTN_TXT,
            width=6,
            pady=5,
            command=self.delete_task,
            state=tk.DISABLED,
        )
        self.add_task_button.pack(side=tk.LEFT, anchor=tk.NW)
        self.del_task_button.pack(side=tk.LEFT, anchor=tk.NW)

    def on_write(self, event=None) -> None:
        self.add_task_button.config(state=tk.NORMAL)

    def add_task(self, event=None) -> None:
        task = self.my_entry.get()
        if not task:
            return

        self.task_list.insert(tk.END, task)
        self.task_list.yview(tk.END)
        self.my_entry.delete(0, "end")

    def on_select_task(self, event=None) -> None:
        self.del_task_button.config(state=tk.NORMAL)

    def delete_task(self, event=None) -> None:
        self.task_list.delete(tk.ANCHOR)
        self.del_task_button.config(state=tk.DISABLED)

    def on_my_entry_focus_in(self, event=None) -> None:
        self.add_task_button.config(state=tk.NORMAL)

    def on_my_entry_focus_out(self, event=None) -> None:
        self.add_task_button.config(state=tk.DISABLED)

    def on_task_list_focus_out(self, event=None) -> None:
        self.task_list.selection_clear(0, tk.END)
        self.del_task_button.config(state=tk.DISABLED)


def main():
    app = TodoList(TASK_LIST)
    app.mainloop()


if __name__ == "__main__":
    main()  # pragma: no cover
