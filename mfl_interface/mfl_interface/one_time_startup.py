import mysql.connector
import environ
from django.core.management import call_command
import requests
import json


def create_db():
    env = environ.Env()
    # reading .env file
    environ.Env.read_env()

    dataBase = mysql.connector.connect(
        host="localhost",
        user=env("DATABASE_USER"),
        passwd=env("DATABASE_PASSWORD")
    )

    # preparing a cursor object
    cursorObject = dataBase.cursor()


    # drop if exists database
    cursorObject.execute("DROP DATABASE IF EXISTS testingautodb")

    # creating database
    cursorObject.execute("CREATE DATABASE IF NOT EXISTS testingautodb")
    call_command("migrate", interactive=False)

    # fetch the facility data
    response = requests.get('http://ip-api.com/json')
    data = json.loads(response.content)

    # save fetched data in the db
    cursorObject.execute("USE testingautodb")
    add_facility_data = "insert into facilities_ipdata(city, country, lat, lon) value(%s, %s, %s, %s)"
    data = (data['city'], data['country'], data['lat'], data['lon'])
    cursorObject.execute(add_facility_data, data)

    dataBase.commit()

    cursorObject.close()
    dataBase.close()