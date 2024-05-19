import datetime

import influxdb_client

from . import ThreeDayForecast


def convert_three_day_forecast_to_influx_points(forecast: ThreeDayForecast) -> list[influxdb_client.Point]:
    points = []

    now = datetime.datetime.strptime('00:00:00 2024-May-13', '%H:%M:%S %Y-%b-%d')

    for kp in forecast.kp_forecast():
        kp_date_normalized = datetime.datetime.strptime(
            f'00:00:00 {kp.start_time().year}-{kp.start_time().month}-{kp.start_time().day}'
            , '%H:%M:%S %Y-%m-%d')
        day_delta = kp_date_normalized - now
        measurement_name = f"three-day-forecast-day-{day_delta.days}"
        points.append(
            influxdb_client.Point(measurement_name=measurement_name)
            .time(kp.start_time()).field("kp", kp.kp())
        )
    return points
