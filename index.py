import requests
import mysql.connector
from datetime import datetime

def create_connection():
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'weather_db'
    )
    return connection

def get_description(latitude, longitude):
    api_key = "2c1238469dd9438b960dcd1667a0b800"
    url = f"https://api.opencagedata.com/geocode/v1/json?key={api_key}&q={latitude}%2C+{longitude}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            description = data['results'][0]['formatted']
            return description
        else:
            return "No description available."
    else:
        print("Failed to fetch location description.")
        return None

def get_weather_data(latitude, longitude):
    description = get_description(latitude, longitude)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relative_humidity_2m"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        temperature = data['hourly']['temperature_2m'][0]
        humidity = data['hourly']['relative_humidity_2m'][0]
        timestamp = data['hourly']['time'][0]

        return {
                'latitude': latitude,
                'longitude': longitude,
                'temperature': temperature,
                'description': description,
                'humidity' : humidity,
                'timestamp': timestamp
            }
    else:
        print("Failed to fetch weather data")
        return None
    
def insert_weather_data(weather_data):
    connection = create_connection()
    cursor = connection.cursor()

    insert_query = '''
    INSERT INTO weather_data (city, temperature, description, humidity, timestamp)
        VALUES (%s, %s, %s, %s, %s)
    '''

    data_tuple = (
          f"{weather_data['latitude']}, {weather_data['longitude']}",
        weather_data['temperature'],
        weather_data['description'],
        weather_data['humidity'],
        weather_data['timestamp']
    )

    cursor.execute(insert_query, data_tuple)
    connection.commit()
    cursor.close()
    connection.close()

    print(f"Data for coordinates ({weather_data['latitude']}, {weather_data['longitude']}) inserted successfully.")

#Insira as coordenadas nas variáveis abaixo

latitude = -3.0987967
longitude = -60.0233903

weather_data = get_weather_data(latitude, longitude)
if weather_data:
    insert_weather_data(weather_data)