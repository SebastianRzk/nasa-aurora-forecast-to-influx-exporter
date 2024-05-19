import datetime
import decimal

from . import HistoricData, HistoicDataPoint


def parse_historic_k_data(data: list[list]) -> HistoricData:
    index_element = data[0]
    result = []
    timestamp_index = index_element.index("time_tag")
    kp_index = index_element.index("Kp")
    a_running_index = index_element.index("a_running")
    station_count_index = index_element.index("station_count")

    for element in range(1, len(data)):
        element = data[element]
        result.append(
            HistoicDataPoint(
                kp=decimal.Decimal(element[kp_index]),
                timestamp=datetime.datetime.strptime(element[timestamp_index], "%Y-%m-%d %H:%M:%S.%f"),
                a_running=int(element[a_running_index]),
                station_count=int(element[station_count_index])
            )
        )
    return HistoricData(
        points=result
    )
