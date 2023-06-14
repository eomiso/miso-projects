from unittest.mock import patch

from mvp.main import main


@patch("mvp.main.Presenter")
@patch("mvp.main.Model")
@patch("mvp.main.TodoList")
def test_main(mock_view, mock_model, mock_presenter):
    main()

    assert mock_view.called
    assert mock_model.called
    mock_presenter.assert_called_with(mock_model(), mock_view())
