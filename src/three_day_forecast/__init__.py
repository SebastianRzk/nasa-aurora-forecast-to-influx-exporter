from datetime import datetime
from decimal import Decimal

from status import Status


def three_day_forecast_status() -> Status:
    return Status("three_day_forecast")


class KpValue:
    def __init__(self, start_time: datetime, end_time: datetime, kp: Decimal):
        self._start_time = start_time
        self._end_time = end_time
        self._kp = kp

    def start_time(self) -> datetime:
        return self._start_time

    def end_time(self) -> datetime:
        return self._end_time

    def kp(self) -> Decimal:
        return self._kp

    def __repr__(self):
        return f"KpValue({self.start_time()} - {self._end_time} {self._kp})"


class ThreeDayForecast:
    def __init__(self, kp_forecast: list[KpValue]):
        self._kp_forecast = kp_forecast

    def kp_forecast(self) -> list[KpValue]:
        return self._kp_forecast

    def __repr__(self):
        return f"ThreeDayForecast(kp_forecast={self.kp_forecast()})"
