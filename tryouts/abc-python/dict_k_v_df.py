import collections
from datetime import date

import pandas as pd

df1: pd.DataFrame = pd.DataFrame(
    {
        "id": [1, 2],
        "value": ["foo", "boo"],
        "date": [date(2020, 1, 1), date(2020, 1, 2)],
    }
)

df2: pd.DataFrame = pd.DataFrame(
    {
        "id": [2, 3],
        "value": ["xoo", "bar"],
        "date": [date(2020, 1, 2), date(2020, 1, 3)],
    }
)

additional_df1: pd.DataFrame = pd.DataFrame(
    {
        "id": [1, 2],
        "value": ["koo", "soo"],
        "date": [date(2023, 1, 1), date(2023, 1, 2)],
    }
)

additional_df2: pd.DataFrame = pd.DataFrame(
    {
        "id": [1, 2],
        "value": ["zaa", "faa"],
        "date": [date(2022, 4, 3), date(2022, 4, 5)],
    }
)


if __name__ == "__main__":
    import pdb

    pdb.set_trace()
