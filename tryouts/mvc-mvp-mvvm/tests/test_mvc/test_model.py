import sqlite3
from unittest.mock import patch

import pytest

from mvc import model
from mvc.model import Model


@pytest.fixture
def db_with_task() -> tuple[sqlite3.Cursor, str]:
    task = "Test task"
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.execute("create table if not exists tasks (title text)")
    cursor.execute("insert into tasks values (?)", (task,))
    connection.commit()

    yield connection, cursor, task

    connection.close()


@patch("mvc.model.sqlite3.connect")
def test_init(mock_connect):
    Model()
    mock_connect.assert_called_once_with(model.DB_NAME)


def test_get_tasks(db_with_task):
    connection, _, task = db_with_task

    # Check get_tasks
    model = Model(connection)

    # Retrieve all tasks from the database
    tasks = model.get_tasks()

    # Check if the added task is in the database
    assert [task] == tasks


def test_add_task(db_with_task):
    connection, cursor, _ = db_with_task
    model = Model(connection)

    task = "Test task 2"

    # Add the task
    model.add_task(task)

    # Retrieve all tasks from the database
    cursor.execute("select * from tasks")
    tasks = cursor.fetchall()

    # Check if the added task is in the database
    assert (task,) in tasks


def test_delete_task(db_with_task):
    connection, cursor, task = db_with_task

    # Check delete
    model = Model(connection)

    # Delete the task
    model.delete_task(task)

    cursor.execute("select * from tasks")
    tasks = model.get_tasks()

    assert task not in tasks
