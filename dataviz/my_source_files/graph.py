from collections import Counter
import csv
import matplotlib.pyplot as plt
import numpy.numarray as na
from parse import parse, MY_FILE

def visualize_days(parsed_data):
    """Visualize data by day of week"""

    # make a new variable, 'counter', from iterating through each
    # line of data in the parsed data, and count how many incidents
    # happen on each day of the week
    counter = Counter(item["DayOfWeek"] for item in parsed_data)

    # separate the x-axis data (the days of the week) from the
    # 'counter' variable from the y-axis data (the number of
    # incidents for each day)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday", "Sunday"]
    data_list = [counter[day] for day in days]
    day_tuple = tuple([day[:-3] for day in days])

    # with that y-axis data, assign it to a matplotlib plot instance
    plt.plot(data_list)

    # create the amount of ticks needed for our x-axis, and assign
    # the labels
    plt.xticks(range(len(day_tuple)), day_tuple)

    # show the plot!
    plt.show()
   
def visualize_type(parsed_data):
    """Visualize data by category in a bar graph"""
    
    counter = Counter(item["Category"] for item in parsed_data)

    labels = tuple(k for (k, v) in counter.most_common())
    values = tuple(v for (k, v) in counter.most_common())

    xlocations = na.array(range(len(labels))) + 0.5

    width = 0.5
    plt.bar(xlocations, values, width=width)
    plt.xticks(xlocations + width / 2, labels, rotation=90)
    plt.subplots_adjust(bottom=0.4)
    plt.rcParams['figure.figsize'] = 12, 8
    plt.show()


def main():
    visualize_days(parse(MY_FILE, ','))
    visualize_type(parse(MY_FILE, ','))

if __name__ == '__main__':
    main()
