import requests

import influx_adapter
from historic_k_index import historic_k_status
from historic_k_index.io_influx import convert_historic_data_to_influx_points
from historic_k_index.parser import parse_historic_k_data
from status import Status
from status.to_influx import convert_status_to_influx_pojnts
from three_day_forecast import three_day_forecast_status
from three_day_forecast.io_influx import convert_three_day_forecast_to_influx_points
from three_day_forecast.parser import parse_3_day_forecast
from env import get_from_env


def save_three_day_forecast(influx_port: influx_adapter.InfluxWriter) -> Status:
    try:
        forecast = requests.get(get_from_env("DATA_SOURCE") + "/text/3-day-forecast.txt").text
        three_day_forecast = parse_3_day_forecast(forecast)
        three_day_forecast_influx = convert_three_day_forecast_to_influx_points(three_day_forecast)
        influx_port.write_points(three_day_forecast_influx)
    except:
        return three_day_forecast_status().failed()
    return three_day_forecast_status().everything_worked_as_expected()


def save_historic_k_value(influx_port: influx_adapter.InfluxWriter) -> Status:
    try:
        historic_data_json = requests.get(get_from_env("DATA_SOURCE") + "/products/noaa-planetary-k-index.json").json()
        historic_data = parse_historic_k_data(historic_data_json)
        historic_data_influx = convert_historic_data_to_influx_points(historic_data)
        influx_port.write_points(historic_data_influx)
    except:
        return historic_k_status().failed()
    return historic_k_status().everything_worked_as_expected()


def save_stats(influx_port: influx_adapter.InfluxWriter, status: list[Status]):
    status_influx = convert_status_to_influx_pojnts(status)
    influx_port.write_points([status_influx])


influx_writer = influx_adapter.InfluxWriter()
status = [
    save_three_day_forecast(influx_port=influx_writer),
    save_historic_k_value(influx_port=influx_writer)]
save_stats(status=status, influx_port=influx_writer)
