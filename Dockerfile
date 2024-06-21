FROM python:3.10.14-alpine
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

CMD ["python", "run.py"]
