from abc import ABC, abstractmethod
from typing import Any


## Meta Class for Strategies
class InferenceStrategy(ABC):
    # @abstractmethod
    # def __init__(self) -> None:
    #     ...

    @abstractmethod
    def __call__(
        self,
        user_history: list[str],
        recommender_input: list[str],
        candidate_items: list[str],
        **kwargs: Any,
    ):
        ...


class ChildStrategy(InferenceStrategy):
    def __init__(self) -> None:
        pass

    # def __call__(self) -> None:
    #     pass
