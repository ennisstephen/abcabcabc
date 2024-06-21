import pytest
import csv
from backend.app import app
from backend.sensor import Sensor

CSV = "data/weather_api_tests.csv"


@pytest.fixture(scope="module")
def dummy_app():
    # Creating a Sensor also initalizes our DB.
    Sensor(["Galway"])
    with app.test_client() as client:
        yield client


@pytest.mark.parametrize(
    "metric, stat, answer, start_date, end_date", csv.reader(open(CSV))
)
def test_valid_scenarios(dummy_app, metric, stat, answer, start_date, end_date):
    url = f"/v1/weather?stats?city=Galway&start_date={start_date}&end_date={end_date}&metric={metric}&stat={stat}"
    response = dummy_app.get(url)
    data = response.json
    assert response.status_code == 200
    assert float(data[stat]) == float(answer)


def test_invalid_metric(dummy_app):
    url = f"/v1/weather?stats?city=Galway&start_date=01-01-2024&end_date=31-12-24&metric=water&stat=AVG"
    response = dummy_app.get(url)
    data = response.json
    assert response.status_code == 400
    assert (
        data["error"]
        == "Invalid metric parameter metric must be of type 'TEMPERATURE', 'HUMIDITY' or 'WIND_KPH'."
    )


def test_invalid_stat(dummy_app):
    url = f"/v1/weather?stats?city=Galway&start_date=01-01-2024&end_date=31-12-24&metric=humidity&stat=HELLO"
    response = dummy_app.get(url)
    data = response.json
    assert response.status_code == 400
    assert (
        data["error"]
        == "Invalid metric parameter stat must be of type 'MIN', 'MAX', 'SUM' or 'AVG'."
    )
