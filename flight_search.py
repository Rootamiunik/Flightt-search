import requests
import pandas
import datetime as dt
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv
import os

load_dotenv()

#----------------Constant--------------------#
TEQUILA_API_KEY = os.getenv('TEQUILA_API_KEY')
LOCATION_ENDPOINT_TEQUILA = os.getenv('LOCATION_ENDPOINT_TEQUILA')
SEARCH_ENDPOINT_TREQUILA = os.getenv('SEARCH_ENDPOINT_TREQUILA')
TEQUILA_HEADER = {
    'apikey':TEQUILA_API_KEY,
    'Content-Encoding': 'gzip',
}


class FlightSearch:
    def __init__(self) -> None:
        self.raw_data = pandas.read_csv('data.csv').to_dict('list')
        self.iata_codes = self.raw_data['IataCode']
        self.time_data = str(dt.date(dt.datetime.now().year ,dt.datetime.now().month , dt.datetime.now().day) + relativedelta(months=5)).split('-')
        self.formated_time_list = [i for i in self.time_data[::-1]]

        self.date_from = dt.datetime.now().date().strftime('%d/%m/%Y')
        self.date_to = '/'.join(self.formated_time_list)

        print(self.date_from)
        print(self.date_to)
        
    def search(self):
        for each_iata_code in self.iata_codes:
            
            query = {
                "fly_from": 'KTM',
                "fly_to": each_iata_code,
                "date_from": self.date_from,
                "date_to": self.date_to,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 0,
                "curr": "GBP"
            }
            
            server_request = requests.get(SEARCH_ENDPOINT_TREQUILA,params=query,headers=TEQUILA_HEADER)
            server_request.raise_for_status()
            print(server_request.json())
            break


FlightSearch()
    