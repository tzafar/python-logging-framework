import pandas as pd

flights_file = pd.read_csv('data/flights.csv')


def drop_a_column():
    flights_file.drop(["DAY_OF_WEEK"], axis=1)
    flights_file.rename(index=str, columns={"WHEELS_OFF": "HAS_WHEELS"})
    print(flights_file)


def print_a_column():
    print(flights_file.DESTINATION_AIRPORT)


def get_a_range_of_rows():
    new_object = flights_file['DESTINATION_AIRPORT']
    print(new_object[0:10])


def make_horizontal_chinks_of_data_and_then_combine():
    chunk_size = len(flights_file) // 4
    chunk1 = flights_file[0:chunk_size]
    chunk2 = flights_file[chunk_size:chunk_size * 2]
    chunk3 = flights_file[chunk_size * 2:chunk_size * 3]
    chunk4 = flights_file[chunk_size * 3:chunk_size * 4]
    combined_chunks_list = [chunk1, chunk2, chunk3, chunk4]
    combined_chunks = pd.concat(combined_chunks_list)


def get_rows_by_a_column_value():
    chunk_aa = flights_file[flights_file.AIRLINE == 'AA']
    chunk_aa_delay = chunk_aa[(chunk_aa.DEPARTURE_DELAY < 10) & (chunk_aa.DESTINATION_AIRPORT == 'PBI')]
    print(chunk_aa_delay)


def add_column_and_put_conditional_value():
    flights_file['has_A'] = flights_file['AIRLINE'].apply(lambda x: 1 if 'A' in x else 0)
    print(flights_file)


def get_random_sample():
    flights_file.sample(200)


def normalization():
    flights_file['dd'] = (flights_file.DEPARTURE_DELAY - flights_file.DEPARTURE_DELAY.min())/ (flights_file.DEPARTURE_DELAY.max() - flights_file.DEPARTURE_DELAY.min())
    print("normalization output:")
    print(flights_file['dd'])


def binarise_column():
    print("Binarising the column")
    final_data = flights_file.merge(pd.get_dummies(flights_file['ORIGIN_AIRPORT']))
    print("Binarise column output: ")
    print(final_data)


drop_a_column()
print_a_column()
normalization()
get_a_range_of_rows()
make_horizontal_chinks_of_data_and_then_combine()
get_rows_by_a_column_value()
add_column_and_put_conditional_value()
get_random_sample()
normalization()
binarise_column()