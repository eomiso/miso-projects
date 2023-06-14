from mvp.model import Model
from mvp.presenter import Presenter
from mvp.view import TodoList


def main() -> None:
    model = Model()
    view = TodoList()
    presenter = Presenter(model, view)
    presenter.run()


if __name__ == "__main__":
    main()  # pragma: no cover
