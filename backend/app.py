from datetime import datetime
from flask import Flask, jsonify, request
from backend.queries import Queries

app = Flask(__name__)


@app.route("/v1/weather", methods=["GET"])
def query_stats():
    metric = request.args.get("metric")
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    city = request.args.get("city")
    stat = request.args.get("stat")

    if city:
        city = city.upper()
    else:
        city = "GALWAY"

    if not stat or stat.upper() not in ["MIN", "MAX", "SUM", "AVG"]:
        return (
            jsonify(
                {
                    "error": "Invalid metric parameter stat must be of type 'MIN', 'MAX', 'SUM' or 'AVG'."
                }
            ),
            400,
        )

    if not metric or metric.upper() not in ["TEMPERATURE", "HUMIDITY", "WIND_KPH"]:
        return (
            jsonify(
                {
                    "error": "Invalid metric parameter metric must be of type 'TEMPERATURE', 'HUMIDITY' or 'WIND_KPH'."
                }
            ),
            400,
        )

    if not start_date or not end_date:
        current_date = datetime.now().date().isoformat()
        start_date = current_date
        end_date = current_date

    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    queries = Queries()
    records = queries.get_records_by_city(stat, metric, city, start_date, end_date)

    return jsonify(records), 200
