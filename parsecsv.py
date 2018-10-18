from src.logexception.logframework import MyLogger

myLogger = MyLogger()


def parse_csv_and_get_columns(filename):
    count = 0
    myLogger.logger.info("Read the file")
    csvFile = open(filename, 'r')
    myLogger.logger.info("Read lines from file")
    lines = csvFile.readlines()
    myLogger.logger.info("Loop through lines")
    for line in lines[1:]:
        val = line.split(",")
        test_str_div = val[0] / val[11]
        print(test_str_div)
        test_zero_div = (int(val[0]) / int(val[11]))


if __name__ == "__main__":
    parse_csv_and_get_columns(filename="test.csv")
