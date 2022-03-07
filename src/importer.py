import csv


def import_data():
    filename = 'activities.csv'
    data = []
    with open(filename) as csv_file:
        raw_data = csv.reader(csv_file, delimiter=',')

        for row in raw_data:
            data.append(row)

    return data


if __name__ == '__main__':
    print(import_data())
