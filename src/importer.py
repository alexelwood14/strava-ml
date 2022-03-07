import csv
import numpy as np


def clean_data(data):
    # Convert to correct data types
    for row in range(1, len(data)):
        for atr in range(len(data[row])):
            # Try to replace string with int
            try:
                data[row][atr] = int(data[row][atr])
            except ValueError:
                # Try to replace string with float
                try:
                    data[row][atr] = float(data[row][atr])
                except ValueError:
                    # Change missing data to None primitive
                    if data[row][atr] == '':
                        data[row][atr] = None


def import_data():
    filename = 'activities.csv'
    data = []
    with open(filename) as csv_file:
        raw_data = csv.reader(csv_file, delimiter=',')
        headers = next(raw_data)
        for row in raw_data:
            data.append(row)

    return headers, np.array(data).T


if __name__ == '__main__':
    headers, data = import_data()
    clean_data(data)
    print(data)
    print(headers)
