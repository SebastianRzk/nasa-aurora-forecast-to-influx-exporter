import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

from env import get_from_env


class InfluxWriter:
    def __init__(self):
        self._bucket = get_from_env('INFLUX_BUCKET_NAME')
        self._org = get_from_env('INFLUX_ORG_NAME')
        self._token = get_from_env('INFLUX_AUTH_TOKEN')
        # Store the URL of your InfluxDB instance
        url = get_from_env('INFLUX_URL')
        client = influxdb_client.InfluxDBClient(
            url=url,
            token=self._token,
            org=self._org
        )
        # Write script
        self._write_api = client.write_api(write_options=SYNCHRONOUS)

    def write_point(self, point: influxdb_client.Point):
        self._write_api.write(bucket=self._bucket, org=self._org, record=point)

    def write_points(self, points: list[influxdb_client.Point]):
        for point in points:
            self.write_point(point)
