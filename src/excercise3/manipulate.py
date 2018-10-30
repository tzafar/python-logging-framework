import pandas as pd
import numpy as np

flights_file = pd.read_csv('data/flights.csv')
airports_data = pd.read_csv('data/airports.csv')


def replace_nan_with_mean():
    flights_file.AIR_SYSTEM_DELAY = flights_file.AIR_SYSTEM_DELAY.fillna(flights_file.AIR_SYSTEM_DELAY.mean())
    print(flights_file.AIR_SYSTEM_DELAY)


def get_descriptions():
    numeric_data = flights_file._get_numeric_data()
    print(numeric_data.describe())


def remove_outliers():
    print("Number of rows before removing the outliers: {0}".format(flights_file.YEAR.count()))
    required_data = flights_file[flights_file.DEPARTURE_DELAY.abs() < (flights_file.DEPARTURE_DELAY.std() * 3)]
    print("Number of rows before removing the outliers: {0}".format(required_data.YEAR.count()))
    print(required_data)


# def remove_outliers_from_quantitative_columns():
#     print("Number of rows before removing the outliers: {0}".format(flights_file.YEAR.count()))
#     numeric_data = flights_file.apply(lambda x: x if x is str else x if flights_file.std() > x else 0)
#     print("Number of rows after removing the outliers: {0}".format(numeric_data.YEAR.count()))
#     print(numeric_data)

def log_of_a_column():
    print(flights_file.YEAR)
    print(np.log(flights_file.YEAR))


def new_column():
    flights_file['ROUTE'] = flights_file.ORIGIN_AIRPORT + ' - ' + flights_file.DESTINATION_AIRPORT
    print(flights_file.ROUTE)


def normlaize_all_columns():
    pass


def sigmoid_func():
    flights_file['sigmoid'] = 1 / (1 + np.exp(-flights_file.ARRIVAL_DELAY))
    print(flights_file.sigmoid)


def left_join_airports():
    result_data = flights_file.merge(airports_data, how='left', left_on='ORIGIN_AIRPORT', right_on='IATA_CODE')
    print(result_data)


def all_numeric_log_transformed():
    numeric_data_log = np.log(flights_file._get_numeric_data())
    print(numeric_data_log)


def percentage_delay_for_each():
    pass


def mean_departure_delay_for_each_arline():
    df = flights_file[['AIRLINE', 'DEPARTURE_DELAY']].groupby('AIRLINE').mean()
    print(df.head())


def mean_geohash_for_each_arline():
    df = flights_file.merge(airports_data, how='left', left_on='ORIGIN_AIRPORT', right_on='IATA_CODE')
    fd = df[['AIRLINE', 'LONGITUDE', 'LATITUDE']].groupby('AIRLINE').mean()
    print(fd.head())


def flights_leaving_before_1200():
    pass


def percentage_flights_leaving_before_1200():
    pass


def number_of_flights_for_each_route():
    flights_file['ROUTE'] = flights_file.ORIGIN_AIRPORT + ' - ' + flights_file.DESTINATION_AIRPORT
    df = flights_file[['ROUTE', 'YEAR']].groupby('ROUTE').count()
    print(df.head())


def for_each_airline_percentage_of_each_route():
    pass


def pca_to_reduce_variable():
    pass


# replace_nan_with_mean()
# get_descriptions()
# remove_outliers()
# remove_outliers_from_quantitative_columns()
# log_of_a_column()
# new_column()
# sigmoid_func()
# left_join_airports()
# all_numeric_log_transformed()
# mean_departure_delay_for_each_arline()
# mean_geohash_for_each_arline()
#number_of_flights_for_each_route()
