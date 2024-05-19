import influxdb_client

from . import Status


def convert_status_to_influx_pojnts(status: list[Status]) -> influxdb_client.Point:
    point = influxdb_client.Point(measurement_name="influx_importer_status")
    for statu in status:
        named_status = "is_ok"
        if not statu.is_ok:
            named_status = "failed"
        point.field(statu.name, named_status)
    return point
