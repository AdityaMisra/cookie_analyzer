from dataclasses import dataclass
from datetime import datetime


@dataclass
class CookieDetails:
    cookie_id: str
    time: datetime

    def __init__(self, cookie_id: str, time_str: str) -> None:
        super().__init__()
        self.cookie_id = cookie_id
        self.time = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S%z")
