import pandas
from flight_data import FlightData


class DataManager():
    def __init__(self,obj:object) -> None:
        self.flightdata = obj()
        self.panda_obj = pandas.read_csv('data.csv')
        self.raw_data = self.panda_obj.to_dict('list')

        self.city = self.raw_data['City']
        self.iata()

    
    def iata(self):
        self.iatacode = []
        for i in range(len(self.city)):
            self.flightdata.place = self.city[i]
            self.iatacode.append(self.flightdata.server_get()['locations'][0]['id'])
            
        self.raw_data['IataCode'] = self.iatacode
        pandas.DataFrame(self.raw_data).to_csv('data.csv')



    
