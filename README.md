# nasa-aurora-forecast-to-influx-exporter


Export NASA's aurora forecast to InfluxDb to design your own aurora dashboard (e.g. with Grafana) and create your own alerts.

So you never miss the northern lights in your area again.


## Features

Exports the following values:

* Three day forecast (kp value)
* Current and past (7 days) values ​​(kp values, number of stations, a running)
* Maximum value of the forecast (required for alerts)

Additional features

* Pre-build images for amd64
* Example docker-compose.yml for self-building and for using the pre-built images
* Data updated every 4 hours
* Overwrite data if the forecast changes during the day
* Save each day of a 3-day forecast for retrospective analysis
