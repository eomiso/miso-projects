from unittest.mock import patch

from mvc.main import main


@patch("mvc.main.Controller")  # Beware of the order of the patches
@patch("mvc.main.Model")
@patch("mvc.main.TodoList")
def test_main(mock_view, mock_model, mock_controller):
    main()

    assert mock_model.called
    mock_view.assert_called_with(mock_model())
    mock_controller.assert_called_with(mock_model(), mock_view())
