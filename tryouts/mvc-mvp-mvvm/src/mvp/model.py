import sqlite3

from mvp.interfaces import Task

DB_NAME = "tasks.db"


class Model:
    def __init__(self, connection=None) -> None:
        if connection is None:
            self.connection = sqlite3.connect(DB_NAME)
        else:
            self.connection = connection
        self.cursor = self.connection.cursor()
        self.cursor.execute("create table if not exists tasks (title text)")

    def add_task(self, task: Task) -> None:
        title = task.title
        self.cursor.execute("insert into tasks values (?)", (title,))
        self.connection.commit()

    def delete_task(self, task: Task) -> None:
        title = task.title
        self.cursor.execute("delete from tasks where title = ?", (title,))
        self.connection.commit()

    def get_tasks(self) -> list[Task]:
        self.cursor.execute("select * from tasks")
        tasks = self.cursor.fetchall()

        return [Task(title=task[0]) for task in tasks]
