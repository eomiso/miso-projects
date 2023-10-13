from __future__ import annotations

import json
from typing import Annotated

from pydantic import AfterValidator, BaseModel, Field

ZAI_APPLICATION_SERVICE_NAMES = [
    "collector",
    "collector-api-dev",
    "collector-api-bc16bb17-7571-4f11-a7d5-4ea8c05be385",
]


def is_valid_service_name(service_name: str) -> bool:
    if service_name in ZAI_APPLICATION_SERVICE_NAMES:
        return True

    return False


class ApplicationLog(BaseModel):
    datetime: str
    service: Annotated[str, AfterValidator(is_valid_service_name)]
    log: CollectorBody


class CollectorBody(BaseModel):
    user_id: str | None = Field(default=None)
    item_id: str | None = Field(default=None)
    event_type: str | None = Field(default=None)
    event_value: str | None = Field(default=None)
    timestamp: int | float | str
    is_zai_recommendation: bool = Field(default=False)
    from_: str | None = Field(default=None, alias="from")


class TestBody(BaseModel):
    rec_type: str = Field(default=None)


if __name__ == "__main__":
    data = {
        "datetime": "2021-08-17T21:00:00.000Z",
        "service": "collector-api",
        "log": json.dumps(
            {
                "user_id": None,
                "event_type": "item_detail_viewed",
                "event_value": None,
                "timestamp": 1629207600.0,
                "is_zai_recommendation": False,
                "from": None,
            }
        ),
    }

    data2 = {
        "datetime": "2021-08-17T21:00:00.000Z",
        "service": "collector-api",
        "log": {"rec_type": "Subal"},
    }

    data3 = {
        "datetime": "2021-08-17T21:00:00.000Z",
        "service": "collector-api",
        "log": "INFO: hellow",
    }

    import json

    app_log = ApplicationLog.model_validate_json(json.dumps(data))

    print(app_log)
