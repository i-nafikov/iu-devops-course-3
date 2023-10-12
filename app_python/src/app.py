from flask import Flask
from datetime import datetime
from zoneinfo import ZoneInfo
from waitress import serve

import logging
logging.basicConfig(
    format="%(asctime)-s  %(levelname)-8s: %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S"
)
logger = logging.getLogger("waitress")
logger.setLevel(logging.INFO)

app = Flask(__name__)


@app.route("/")
def current_time():
    moscow_zone_info = ZoneInfo("Europe/Moscow")
    time: datetime = datetime.now(tz=moscow_zone_info)
    time_str: str = time.strftime("%H:%M:%S")

    logger.info(msg="Moscow time was sent")
    return "Moscow Time: " + time_str


if __name__ == "__main__":
    serve(app=app, port="8080")
