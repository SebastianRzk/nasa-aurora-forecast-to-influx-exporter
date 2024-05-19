import influxdb_client

from . import HistoricData


def convert_historic_data_to_influx_points(historic_data: HistoricData) -> list[influxdb_client.Point]:
    result = []
    for point in historic_data.points:
        result.append(
            influxdb_client.Point(measurement_name="k_index")
            .time(point.timestamp).field("kp", point.kp).field("a_running", point.a_running).field("station_count",
                                                                                                   point.station_count)
        )
    return result
