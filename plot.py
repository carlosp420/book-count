import csv

import pygal


__author__ = 'carlosp420'


def plot():
    years, data = get_data()

    line_chart = pygal.Bar()
    line_chart.title = "Books read per year"
    line_chart.x_labels = years
    line_chart.add('Books per year', data)
    line_chart.render_to_file('books_per_year.svg')


def get_data():
    count = dict()
    years = []
    with open("books.csv", "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='"')

        for row in reader:
            if 'Author' in row:
                continue
            if row and row[-1] not in count:
                count[row[-1]] = 1
                years.append(row[-1])
            elif row:
                count[row[-1]] += 1

    years.sort()
    data = [count[year] for year in years]
    return years, data


if __name__ == '__main__':
    plot()
