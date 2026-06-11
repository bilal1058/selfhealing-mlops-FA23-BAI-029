import time
import requests
from prometheus_client import start_http_server, Gauge

APP_URL = "http://13.207.67.12:32500/api/latest-confidence"

confidence_gauge = Gauge(
    "prediction_confidence_score",
    "Latest model prediction confidence score"
)

def poll_confidence():
    while True:
        try:
            response = requests.get(APP_URL, timeout=3)
            data = response.json()
            confidence = float(data.get("confidence", 1.0))
        except Exception:
            confidence = 1.0

        confidence_gauge.set(confidence)
        time.sleep(5)

if __name__ == "__main__":
    start_http_server(8000)
    poll_confidence()
