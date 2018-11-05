import pandas as pd
import numpy as np
import hashlib


class DataManager:
    def __init__(self):
        self.flights = pd.read_csv('../data/flights.csv')
        self.airlines = pd.read_csv('../data/airlines.csv')

    def get_first_20_rows(self,column_name):
        return self.flights.head(20)[column_name].to_json()

    def get_airline_data_by_name(self,name):
        return self.airlines[self.airlines.IATA_CODE == name].to_json()

    def update_airline_code(self,old_code, new_code):
        return self.airlines['AIRLINE'].str.replace(old_code, new_code).to_json()

