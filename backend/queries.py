import sqlite3


class Queries:
    def __init__(self, db_name="weather_data.db"):
        self.db_name = db_name
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row

    def disconnect(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def get_records_by_city(self, stat, metric, city, start_date, end_date):
        try:
            self.connect()
            cursor = self.conn.cursor()
            query_string = f"SELECT {stat}({metric}) as my_value FROM weather_data WHERE UPPER(region)=? AND date BETWEEN ? AND ?"
            cursor.execute(query_string, (city, start_date, end_date))
            records = cursor.fetchone()

            if not records[0]:
                return "no data found"

            formatted_number = "{:.2f}".format(records[0]).rstrip("0").rstrip(".")
            return {
                "city": city,
                "start_date": start_date,
                "end_date": end_date,
                "metric": metric,
                stat: str(formatted_number),
            }
        finally:
            self.disconnect()
