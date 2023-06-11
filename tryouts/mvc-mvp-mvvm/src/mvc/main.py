from mvc.controller import Controller
from mvc.model import Model
from mvc.view import TodoList


def main() -> None:
    model = Model()
    view = TodoList(model)
    controller = Controller(model, view)
    controller.run()


if __name__ == "__main__":
    main()  # pragma: no cover
