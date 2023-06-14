from __future__ import annotations

from typing import Protocol

from mvp.interfaces import Task
from mvp.model import Model


class IView(Protocol):
    def create_ui(self, presenter: Presenter) -> None:
        ...

    def clear_entry(self) -> None:
        ...

    def get_entry_task(self) -> str:
        ...

    def update_task_list(tasks: list[Task]):
        ...


class Presenter:
    def __init__(self, model: Model, view: IView) -> None:
        self.model = model
        self.view = view

    def handle_add_task(self, event=None) -> None:
        task = self.view.get_entry_task()
        if not task:
            print("No task to add")
            return

        print(task)
        self.model.add_task(task)
        self.view.clear_entry()
        self.update_task_list()

    def handle_delete_task(self, event=None) -> None:
        self.model.delete_task(self.view.selected_task)  # A strong dependency
        self.update_task_list()

    def update_task_list(self) -> None:
        tasks = self.model.get_tasks()
        self.view.update_task_list(tasks)

    def run(self) -> None:
        self.view.create_ui(self)
        self.update_task_list()
        self.view.mainloop()
