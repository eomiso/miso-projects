import sqlite3
import tkinter as tk
from unittest import mock
from unittest.mock import MagicMock, Mock, patch

import pytest

from mvc import view
from mvc.interfaces import Task
from mvc.model import Model
from mvc.view import TodoList

TASK_LIST = ["Task 1", "Task 2"]


@pytest.fixture(scope="session")
def mock_model():
    connection = sqlite3.connect(":memory:")
    model = Model(connection)
    for task in TASK_LIST:
        model.add_task(task)

    yield model

    connection.close()


@pytest.fixture(scope="function")
def mock_todolist(mock_model):
    todolist = TodoList(mock_model)
    yield todolist


def test_mock_TodoList():
    with patch.object(view, "TodoList") as MockTodoList:
        print()
        print(f"       class:{MockTodoList}")
        print(f"return_value:{MockTodoList.return_value}")


@patch("mvc.view.tk.Listbox.insert", autospec=True)
def test_TodoList_init(mock_insert, mock_model):
    task_list = TodoList(mock_model).task_list
    expected_calls = [
        mock.call(task_list, tk.END, "Task 1"),
        mock.call(task_list, tk.END, "Task 2"),
    ]
    mock_insert.assert_has_calls(expected_calls, any_order=False)


def test_create_ui(mock_todolist):
    # We can check that the correct variables were set
    assert isinstance(mock_todolist.frame, tk.Frame)
    assert isinstance(mock_todolist.task_list, tk.Listbox)
    assert isinstance(mock_todolist.my_entry, tk.Entry)
    assert isinstance(mock_todolist.add_task_button, tk.Button)
    assert isinstance(mock_todolist.del_task_button, tk.Button)

    # And we can check some of their properties
    assert mock_todolist.task_list["height"] == 10
    assert mock_todolist.task_list["activestyle"] == "none"
    assert mock_todolist.del_task_button["text"] == view.DELETE_BTN_TXT
    assert mock_todolist.del_task_button["state"] == tk.DISABLED


def test_bind_add_task(mock_todolist):
    callback = MagicMock()
    mock_todolist.my_entry.bind = MagicMock()

    # Act
    mock_todolist.bind_add_task(callback)

    mock_todolist.my_entry.bind.assert_called_with(
        mock_todolist.add_task_button, callback
    )


def test_bind_delete_task(mock_todolist):
    callback = MagicMock()
    mock_todolist.del_task_button = MagicMock()
    mock_todolist.del_task_button.bind = MagicMock()

    # Act
    mock_todolist.bind_delete_task(callback)

    mock_todolist.del_task_button.bind.assert_called_with(
        view.LEFT_BUTTON_CLICK, callback
    )


def test_get_entry_task(mock_todolist):
    mock_todolist.my_entry.get = Mock(return_value="Task 1")
    task = mock_todolist.get_entry_task()
    assert task == Task(title="Task 1")


def test_clear_entry(mock_todolist):
    mock_todolist.my_entry.delete = Mock()
    mock_todolist.clear_entry()

    mock_todolist.my_entry.delete.assert_called_with(0, tk.END)


def test_on_write(mock_todolist):
    mock_todolist.add_task_button = Mock()

    mock_todolist.on_write()

    mock_todolist.add_task_button.config.assert_called_with(state=tk.NORMAL)


def test_on_select_task(mock_todolist):
    mock_todolist.del_task_button = Mock()

    mock_todolist.on_select_task()
    mock_todolist.del_task_button.config.assert_called_with(state=tk.NORMAL)


def test_on_my_entry_focus_in(mock_todolist):
    mock_todolist.add_task_button = Mock()

    mock_todolist.on_my_entry_focus_in()

    mock_todolist.add_task_button.config.assert_called_with(state=tk.NORMAL)


def test_on_my_entry_focus_out(mock_todolist):
    mock_todolist.add_task_button = Mock()

    mock_todolist.on_my_entry_focus_out()
    mock_todolist.add_task_button.config.assert_called_with(state=tk.DISABLED)


def test_on_task_list_focus_out(mock_todolist):
    # Mock the task_list and del_task_button widgets
    task_list_mock = Mock()
    del_task_button_mock = Mock()

    mock_todolist.task_list = task_list_mock
    mock_todolist.del_task_button = del_task_button_mock

    # Replace the actual task_list and del_task_button with our mocks
    mock_todolist.task_list = task_list_mock
    mock_todolist.del_task_button = del_task_button_mock

    mock_todolist.on_task_list_focus_out()

    # Check if te "selection_clear" and "config" methods are called with the expected parameters.
    task_list_mock.selection_clear.assert_called_with(0, tk.END)
    del_task_button_mock.config.assert_called_with(state=tk.DISABLED)
