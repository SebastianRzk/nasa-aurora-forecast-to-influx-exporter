import datetime
import decimal

from status import Status


def historic_k_status() -> Status:
    return Status("k_index")


class HistoicDataPoint:
    def __init__(self, kp: decimal.Decimal, a_running: int, station_count: int, timestamp: datetime.datetime):
        self.kp = kp
        self.a_running = a_running
        self.station_count = station_count
        self.timestamp = timestamp

    def __repr__(self):
        return f"HistoricDataPoint(timestamp={self.timestamp}, kp={self.kp}, a_running={self.a_running}, station_count={self.station_count})"


class HistoricData:
    def __init__(self, points: list[HistoicDataPoint]):
        self.points = points

    def __repr__(self):
        return f"HistoricData({self.points})"
