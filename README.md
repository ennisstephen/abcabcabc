#  My Random Repo
N.B. Sensor requires https://www.weatherapi.com/ API key to work, reach out to me if needed. App will work fine without this, as it will load 1 month of Galway weather data from CSV.
30 days of Galway weather data for May 2024, will be preloaded into the app on start up, this is for testing purposes and also to play around with the app.
##  Installation
1.  **Clone the repository:**
```bash
git clone https://github.com/ennisstephen/My_Random_Repo.git
  ```
2.  **Start virtual env and download dependencies**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3.  **Run App**
```bash
python run.py
```
4. **Run tests**
```bash
pytest --verbose
```
5. **Example queries**
```
http://localhost:5000/v1/weather?stat=AVG&metric=TEMPERATURE&city=Galway&start_date=2024-05-01&end_date=2025-05-31

{
  "AVG": "17.02",
  "city": "GALWAY",
  "end_date": "2025-05-31",
  "metric": "TEMPERATURE",
  "start_date": "2024-05-01"
}

http://localhost:5000/v1/weather?stat=MAX&metric=HUMIDITY&city=Galway&start_date=2024-05-01&end_date=2025-05-31

{
  "MAX": "85",
  "city": "GALWAY",
  "end_date": "2025-05-31",
  "metric": "HUMIDITY",
  "start_date": "2024-05-01"
}

http://localhost:5000/v1/weather?stat=AVG&metric=WIND_KPH&city=Galway&start_date=2024-05-01&end_date=2025-05-31

{
  "AVG": "4.42",
  "city": "GALWAY",
  "end_date": "2025-05-31",
  "metric": "WIND_KPH",
  "start_date": "2024-05-01"
}
```
*I have included an OpenAPI spec if you need more comprehensive documentation*

6. **Happy Hacking!**
