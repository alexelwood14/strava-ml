import csv


def clean_data(data):
    # Convert to correct data types
    for row in range(1, len(data)):
        for atr in range(len(data[row])):
            try:
                data[row][atr] = int(data[row][atr])
            except ValueError:
                try:
                    data[row][atr] = float(data[row][atr])
                except ValueError:
                    continue


def import_data():
    filename = 'activities.csv'
    data = []
    with open(filename) as csv_file:
        raw_data = csv.reader(csv_file, delimiter=',')

        for row in raw_data:
            data.append(row)

    return data


if __name__ == '__main__':
    data = import_data()
    clean_data(data)
    print(data)
