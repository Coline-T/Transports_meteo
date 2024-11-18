import os
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv
import ssl
from pymongo import MongoClient


class APIClient:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self):
        try:
            print(f"Fetching data from API: {self.api_url}")
            response = requests.get(self.api_url)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Failed to fetch data. Status code: {response.status_code}, Response: {response.text}")
                return None
        except Exception as e:
            print(f"Error while fetching data from API: {e}")
            return None


class MongoDBPipeline:
    def __init__(self):
        load_dotenv()

        # Load MongoDB credentials from environment variables
        self.username = os.getenv('MONGO_USERNAME')
        self.password = os.getenv('MONGO_PASSWORD')
        self.cluster_url = os.getenv('MONGO_URI')
        self.database_name = os.getenv('MONGO_DBNAME')

        if not all([self.username, self.password, self.cluster_url, self.database_name]):
            raise ValueError("Missing MongoDB credentials in environment variables.")

        # Connect to MongoDB
        try:
            self.client = MongoClient(self.cluster_url)
            self.db = self.client[self.database_name]
            print("Connected to MongoDB successfully.")
            # Test connection by pinging the database
            self.db.command('ping')
            print("MongoDB connection is active.")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            import traceback
            traceback.print_exc()
            raise

    def insert_data(self, collection_name, data):
        if not data:
            print(f"No data to insert into collection '{collection_name}'.")
            return

        try:
            # Check if data is a list of dictionaries
            if isinstance(data, list) and all(isinstance(d, dict) for d in data):
                print(f"Preparing to insert into '{collection_name}' collection. Data: {data}")
            else:
                print(f"Data format error. Expected a list of dictionaries, got: {type(data)}")
                return

            collection = self.db[collection_name]
            # Try to insert the data into MongoDB
            result = collection.insert_many(data)
            print(f"{len(result.inserted_ids)} documents inserted into '{collection_name}' collection.")
        except Exception as e:
            print(f"Error inserting data into MongoDB: {e}")
            import traceback
            traceback.print_exc()

    def close_connection(self):
        self.client.close()
        print("MongoDB connection closed.")


def main():
    load_dotenv()

    # Fetch weather data
    weather_api_url = os.getenv('URL_METEO')
    pollution_api_url = os.getenv('URL_POLLUTION')

    if not weather_api_url or not pollution_api_url:
        print("API URLs are not defined in the environment variables.")
        return

    weather_client = APIClient(weather_api_url)
    pollution_client = APIClient(pollution_api_url)

    weather_data = weather_client.fetch_data()
    pollution_data = pollution_client.fetch_data()

    if weather_data:
        print("Weather data fetched successfully.")
    else:
        print("Failed to fetch weather data.")

    if pollution_data:
        print("Pollution data fetched successfully.")
    else:
        print("Failed to fetch pollution data.")

    # Save data to MongoDB
    mongo_pipeline = MongoDBPipeline()

    # Insert raw data into MongoDB
    if weather_data:
        mongo_pipeline.insert_data('Météo', [weather_data])  # Insert weather data as a list
    if pollution_data:
        mongo_pipeline.insert_data('Pollution', [pollution_data])  # Insert pollution data as a list

    mongo_pipeline.close_connection()


if __name__ == "__main__":
    main()

