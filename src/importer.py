import csv
import numpy as np


def clean_data(data):
    # Convert to correct data types
    for row in range(len(data)):
        for atr in range(len(data[row])):
            # Try to replace string with int
            try:
                data[row][atr] = int(data[row][atr])
            except ValueError:
                # Try to replace string with float
                try:
                    data[row][atr] = float(data[row][atr])
                except ValueError:
                    continue


def partition(data, filter):
    part = {}
    bins = []
    for element in data[filter]:
        if element not in bins:
            bins.append(element)

    for bin in bins:
        part[bin] = {}
        for atr in data.keys():
            if atr != filter:
                part[bin][atr] = []
                for element in range(len(data[atr])):
                    if data[filter][element] == bin:
                        part[bin][atr].append(data[atr][element])
                part[bin][atr] = np.array(part[bin][atr])


    return part


class Data:
    def __init__(self):
        self.file_name = 'activities.csv'
        self.__data = []
        with open(self.file_name) as csv_file:
            raw_data = csv.reader(csv_file, delimiter=',')
            self.headers = next(raw_data)
            self.types = next(raw_data)
            for row in raw_data:
                self.__data.append(row)

        self.__data = np.array(self.__data).T

        clean_data(self.__data)

        # Reformat the data into the correct np types
        data = {}
        for i in range(len(self.headers)):
            if self.types[i] == 'int':
                data[self.headers[i]] = []
                for element in self.__data[i]:
                    if element == '':
                        element = -1
                    data[self.headers[i]].append(int(element))
                data[self.headers[i]] = np.array(data[self.headers[i]])

            elif self.types[i] == 'float':
                data[self.headers[i]] = []
                for element in self.__data[i]:
                    if element == '':
                        element = -1.0
                    data[self.headers[i]].append(float(element))
                data[self.headers[i]] = np.array(data[self.headers[i]])

            elif self.types[i] == 'string':
                data[self.headers[i]] = np.array(self.__data[i])

        self.__data = data

    def get_data(self, headers, omit_nones=True):
        # Create array of flags to be included
        include = [True for i in range(len(self.__data['Activity ID']))]
        filtered_data = {}

        if omit_nones:
            for header in headers:
                for atr in range(len(self.__data[header])):
                    if self.__data[header][atr] == '':
                        include[atr] = False

        for header in headers:
            filtered_data[header] = []
            for atr in range(len(self.__data[header])):
                if include[atr]:
                    filtered_data[header].append(self.__data[header][atr])

        return filtered_data


if __name__ == '__main__':
    data_set = Data()
    data = data_set.get_data(['Activity ID', 'Perceived Exertion', 'Activity Gear'])
    print(data)
