from src.logexception.logframework import MyLogger
from src.logexception.exceptionhandler import CustomInputError, MyZeroDivisionException, DataNotValidException

myLogger = MyLogger().logger


def parse_csv_and_get_columns(filename, error_type):
    myLogger.info("Read the file")
    csv_file = open(filename, 'r')
    if csv_file is None:
        raise CustomInputError
    myLogger.info("Read lines from file")
    lines = csv_file.readlines()
    print(lines)
    myLogger.info("Loop through lines")
    for line in lines:
        print(line)
        val = line.split(",")
        if error_type == 0:
            try:
                test_str_div = val[0] / val[11]
                print(test_str_div)
            except TypeError:
                raise DataNotValidException
                pass
        if error_type == 1:
            try:
                test_zero_div = (int(val[0]) / int(val[11]))
                print(test_zero_div)
            except ZeroDivisionError:
                raise MyZeroDivisionException


if __name__ == "__main__":
    parse_csv_and_get_columns("test.csv", 1)
