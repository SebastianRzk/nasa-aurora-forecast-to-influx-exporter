import datetime
import decimal
import re
from datetime import timedelta
from time import time

from . import ThreeDayForecast, KpValue


class TimeSlice:
    def __init__(self, start: time, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"TimeSlice({self.start}-{self.end})"


class TableParser:

    def __init__(self, table_as_str: str):
        self._cells = re.findall("([\S]{3,9}\s\S*)", table_as_str.strip() + " ")
        self._number_of_columns = 3
        self._time_offset = 1
        self._row_size = self._number_of_columns + self._time_offset
        self._number_of_rows = int((len(self._cells) - self._number_of_columns) / self._row_size)

    def columns(self) -> list[str]:
        return self._cells[:3:]

    def get_cells_for_column(self, column_name: str) -> list[str]:
        col_number = self._resolve_column_number(column_name=column_name)
        column = []
        for row_number in range(0, self._number_of_rows):
            column.append(
                self._cells[row_number * self._row_size + self._number_of_columns + self._time_offset + col_number])
        return column

    def _resolve_column_number(self, column_name: str) -> int:
        return self._cells.index(column_name)

    def parsed_timestamps(self, column_name: str, year: str) -> list[TimeSlice]:
        result = []
        for row_index in range(0, self._number_of_rows):
            date_cell = self._cells[row_index * self._row_size + self._number_of_columns]
            month, day = column_name.split(" ")
            result.append(self._create_timeslice(element=date_cell, day=day, month=month, year=year))
        return result

    def _create_timeslice(self, element: str, month: str, day: str, year: str) -> TimeSlice:
        start_hour, end_hour, _timezone = re.findall("(\S\S)-(\S\S)(\S\S)", element)[0]
        start_timestamp = f"{start_hour}:00:00 {year}-{month}-{day}"
        end_timestamp = f"{end_hour}:00:00 {year}-{month}-{day}"

        start_datetime = datetime.datetime.strptime(start_timestamp, "%H:%M:%S %Y-%b-%d")
        end_datetime = (datetime.datetime.strptime(end_timestamp, "%H:%M:%S %Y-%b-%d") - timedelta(seconds=1))
        return TimeSlice(
            start=start_datetime,
            end=end_datetime
        )


def parse_3_day_forecast(website_as_str: str) -> ThreeDayForecast:
    table = website_as_str.split("NOAA Kp index breakdown")[1].split("Rationale")[0]
    headline = table.split("\n")[0]
    year = headline.split(" ")[-1]
    table_without_headline = table[len(headline) + 1::]
    parser = TableParser(table_without_headline)

    kp_values = []

    for column_name in parser.columns():
        row_times = parser.parsed_timestamps(column_name=column_name, year=year)
        column_values = parser.get_cells_for_column(column_name=column_name)
        for row in range(0, len(column_values)):
            cell_time = row_times[row]
            cell_value = column_values[row]
            cell_value = re.findall("(\S+)\s\S*", cell_value)[0]
            kp_values.append(KpValue(
                start_time=cell_time.start,
                end_time=cell_time.end,
                kp=decimal.Decimal(cell_value)
            ))

    return ThreeDayForecast(
        kp_forecast=kp_values
    )
