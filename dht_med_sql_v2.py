import sqlite3
import  Adafruit_DHT
from time import sleep
import datetime


sensor = Adafruit_DHT.DHT11
pin = 4

query = """INSERT INTO temp_hum (DATETIME, TEMPERATURE, HUMIDITY) 
VALUES(?,?,?)"""

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    conn = sqlite3.connect('temp_hum.db')
    cur = conn.cursor()
    cur.execute(""" CREATE TABLE IF NOT EXISTS temp_hum (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    DATETIME text,
                    TEMPERATURE real,
                    HUMIDITY real   
                    )""")
    if humidity is not None and temperature is not None:
        x = datetime.datetime.now()
        data = (x,temperature, humidity)
        try:
            cur.execute(query,data)
            rowid = cur.lastrowid
            print(f'id of last row insert = {rowid}')
            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
            print(f"could not insert {e}")
        finally:
            conn.close()
        print(f"Temp={temperature}*C Humidity={humidity}%")
        sleep(10)
    else:
        print('Failed to get reading. Try again!')
