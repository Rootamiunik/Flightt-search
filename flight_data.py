import requests
import keys
from dotenv import load_dotenv
import os


load_dotenv()

LOCATION_ENDPOINT_TEQUILA = os.getenv("LOCATION_ENDPOINT_TEQUILA")
TEQUILA_HEADER = os.getenv("TEQUILA_HEADER")


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self) -> None:
        self.place = ''

    def server_get(self):
        self.server_request = requests.get(url=LOCATION_ENDPOINT_TEQUILA,params={'term':self.place,'location_types':'airport',},headers=TEQUILA_HEADER)
        return self.server_request.json()

