import tkinter as tk
from unittest import mock
from unittest.mock import MagicMock, Mock, patch

import simple_todolist
from simple_todolist import TodoList


def test_mock_TodoList():
    with patch.object(simple_todolist, "TodoList") as MockTodoList:
        print()
        print(f"       class:{MockTodoList}")
        print(f"return_value:{MockTodoList.return_value}")


def test_TodoList_init():
    task_list = ["Task 1", "Task 2"]
    with patch.object(tk.Listbox, "insert") as mock_insert:
        _ = TodoList(task_list)

    expected_calls = [mock.call(tk.END, "Task 1"), mock.call(tk.END, "Task 2")]
    mock_insert.assert_has_calls(expected_calls, any_order=False)


def test_create_ui():
    todo_list = TodoList([])

    # We can check that the correct variables were set
    assert isinstance(todo_list.frame, tk.Frame)
    assert isinstance(todo_list.task_list, tk.Listbox)
    assert isinstance(todo_list.my_entry, tk.Entry)
    assert isinstance(todo_list.add_task_button, tk.Button)
    assert isinstance(todo_list.del_task_button, tk.Button)


def test_on_write():
    todo_list = TodoList([])

    todo_list.add_task_button = Mock()

    todo_list.on_write()

    todo_list.add_task_button.config.assert_called_with(state=tk.NORMAL)


def test_add_task():
    listbox_mock = Mock()
    listbox_mock.inset = Mock()

    todo_list = TodoList([])

    # Replace the actual Listbox with the mock
    todo_list.task_list = listbox_mock

    todo_list.my_entry.get = MagicMock(return_value="New task")
    todo_list.my_entry.delete = Mock()

    todo_list.add_task()

    listbox_mock.insert.assert_called_with(tk.END, "New task")
    listbox_mock.yview.assert_called_with(tk.END)
    todo_list.my_entry.delete.assert_called_with(0, "end")


def test_add_task_with_empty():
    listbox_mock = Mock()
    listbox_mock.inset = Mock()

    todo_list = TodoList([])

    # Replace the actual Listbox with the mock
    todo_list.task_list = listbox_mock

    todo_list.my_entry.get = MagicMock(return_value="")
    todo_list.my_entry.delete = Mock()

    todo_list.add_task()

    listbox_mock.insert.assert_not_called()
    listbox_mock.yview.assert_not_called()
    todo_list.my_entry.delete.assert_not_called()


def test_on_select_task():
    todo_list = TodoList([])
    todo_list.del_task_button = Mock()

    todo_list.on_select_task()
    todo_list.del_task_button.config.assert_called_with(state=tk.NORMAL)


def test_delete_task():
    todo_list = TodoList([])
    todo_list.task_list = Mock()
    todo_list.del_task_button = Mock()

    todo_list.delete_task()

    # Check if the "delete" method of the Listbox is called with the expected parameters.
    todo_list.task_list.delete.assert_called_with(tk.ANCHOR)

    # Check if the config method of the del_task_button is called with the expected parameters.
    todo_list.del_task_button.config.assert_called_with(state=tk.DISABLED)


def test_on_my_entry_focus_in():
    todo_list = TodoList([])

    todo_list.add_task_button = Mock()

    todo_list.on_my_entry_focus_in()

    todo_list.add_task_button.config.assert_called_with(state=tk.NORMAL)


def test_on_my_entry_focus_out():
    todo_list = TodoList([])

    todo_list.add_task_button = Mock()

    todo_list.on_my_entry_focus_out()
    todo_list.add_task_button.config.assert_called_with(state=tk.DISABLED)


def test_on_task_list_focus_out():
    todo_list = TodoList([])

    # Mock the task_list and del_task_button widgets
    task_list_mock = Mock()
    del_task_button_mock = Mock()

    todo_list.task_list = task_list_mock
    todo_list.del_task_button = del_task_button_mock

    # Replace the actual task_list and del_task_button with our mocks
    todo_list.task_list = task_list_mock
    todo_list.del_task_button = del_task_button_mock

    todo_list.on_task_list_focus_out()

    # Check if te "selection_clear" and "config" methods are called with the expected parameters.
    task_list_mock.selection_clear.assert_called_with(0, tk.END)
    del_task_button_mock.config.assert_called_with(state=tk.DISABLED)


def test_main():
    class ListMatcher:
        def __eq__(self, other):
            return isinstance(other, list)

    with patch.object(simple_todolist, "TodoList") as MockTodoList:
        simple_todolist.main()
        MockTodoList.assert_called_with(ListMatcher())
