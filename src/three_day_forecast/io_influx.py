import datetime

import influxdb_client

from . import ThreeDayForecast


def convert_three_day_forecast_to_influx_points(forecast: ThreeDayForecast) -> list[influxdb_client.Point]:
    points = []
    today = datetime.datetime.now().date()
    first_measurement = forecast.kp_forecast()[0]
    max_value = first_measurement.kp()

    for kp in forecast.kp_forecast():
        day_delta = kp.start_time().date() - today
        measurement_name = f"three-day-forecast-day-{day_delta.days}"
        points.append(
            influxdb_client.Point(measurement_name=measurement_name)
            .time(kp.start_time()).field("kp", kp.kp())
        )
        if kp.kp() > max_value:
            max_value = kp.kp()

    points.append(
        influxdb_client.Point(measurement_name="three-day-forecast-max-value")
        .time(first_measurement.start_time()).field("kp", max_value)
    )
    return points
