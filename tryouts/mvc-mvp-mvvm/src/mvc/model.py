import sqlite3

DB_NAME = "tasks.db"


class Model:
    def __init__(self, connection=None) -> None:
        if connection is None:
            self.connection = sqlite3.connect(DB_NAME)
        else:
            self.connection = connection
        self.cursor = self.connection.cursor()
        self.cursor.execute("create table if not exists tasks (title text)")

    def add_task(self, task: str) -> None:
        self.cursor.execute("insert into tasks values (?)", (task,))
        self.connection.commit()

    def delete_task(self, task: str) -> None:
        self.cursor.execute("delete from tasks where title=?", (task,))
        self.connection.commit()

    def get_tasks(self) -> list[str]:
        self.cursor.execute("select * from tasks")
        tasks = self.cursor.fetchall()

        return [task[0] for task in tasks]
