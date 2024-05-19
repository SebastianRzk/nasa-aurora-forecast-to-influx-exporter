import datetime

import influxdb_client

from . import ThreeDayForecast


def convert_three_day_forecast_to_influx_points(forecast: ThreeDayForecast) -> list[influxdb_client.Point]:
    points = []
    now = datetime.datetime.now().date()

    for kp in forecast.kp_forecast():
        day_delta = kp.start_time().date() - now
        measurement_name = f"three-day-forecast-day-{day_delta.days}"
        points.append(
            influxdb_client.Point(measurement_name=measurement_name)
            .time(kp.start_time()).field("kp", kp.kp())
        )
    return points
