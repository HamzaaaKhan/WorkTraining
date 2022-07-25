import sys
from csv import reader
import datetime
from math import ceil
import os
from statistics import mean


def main(argv):
    months = [" ", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    length = len(sys.argv)
    option = sys.argv[length - 2]
    date = sys.argv[length - 1]
    print(date)
    if option == "-e":

        date = sys.argv[length - 1]
        year_month = datetime.datetime.strptime(date, "%Y")
        year = str(year_month.year)
        month = year
        file_parsing(year, month, option)

    elif option == "-a":
        year_month = datetime.datetime.strptime(date, "%Y/%m")
        year = str(year_month.year)
        month = year_month.month
        month_name = months[month]
        file_parsing(year, month_name, option)

    elif option == "-c":

        year_month = datetime.datetime.strptime(date, "%Y/%m")
        year = str(year_month.year)
        month = year_month.month
        month_name = months[month]
        file_parsing(year, month_name, option)


def get_first_second_temprature(dict1, dict2, month, year):
    new_values = [list for key, list in dict1.items()]
    for i in range(0, len(new_values)):
        new_values[i] = int(new_values[i])
    new_values.sort()
    first_highest_temprature = new_values[-1]
    second_highest_temprature = new_values[-2]

    new_values1 = [list for key, list in dict2.items()]
    for i in range(0, len(new_values1)):
        new_values1[i] = int(new_values1[i])

    new_values1.sort(reverse=True)
    first_lowest_temprature = new_values1[-1]
    second_lowest_temprature = new_values1[-2]

    first_second_low_high_temprature(first_highest_temprature, second_highest_temprature,
                                     first_lowest_temprature, second_lowest_temprature, month, year)


def first_second_low_high_temprature(maxT, secondmaxT, minT, secondminT, month, year):
    print(" ")

    print(month + " " + year)

    print("01 ", end="")
    for i in range(maxT):
        print("+", end="")
    print(" " + str(maxT) + "C")

    print("01 ", end="")
    for i in range(secondmaxT):
        print("+", end="")
    print(" " + str(secondmaxT) + "C")

    print("02 ", end="")
    for i in range(minT):
        print("+", end="")
    print(" " + str(minT) + "C")

    print("02 ", end="")
    for i in range(secondminT):
        print("+", end="")
    print(" " + str(secondminT) + "C")


def monthly_average_values(dict, dict1, dict2, ):
    new_values = [list for key, list in dict.items()]
    for i in range(0, len(new_values)):
        new_values[i] = int(new_values[i])

    new_values1 = [list for key, list in dict1.items()]
    for i in range(0, len(new_values1)):
        new_values1[i] = int(new_values1[i])

    new_values2 = [list for key, list in dict2.items()]
    for i in range(0, len(new_values2)):
        new_values2[i] = int(new_values2[i])

    print("Highest Average: " + str(ceil(mean(new_values))) + "C")
    print("Lowest Average: " + str(ceil(mean(new_values1))) + "C")
    print("Average Mean Humidity: " + str(ceil(mean(new_values2))) + "%")


def yearly_values(dict1, dict2, dict3):
    max_temprature = max(dict1.values())
    key_list = list(dict1.keys())
    val_list = list(dict1.values())

    # print key with val temp
    position = val_list.index(max_temprature)
    print("Highest: " + max_temprature + "C on " + key_list[position])

    min_temprature = max(dict2.values())
    key_list = list(dict2.keys())
    val_list = list(dict2.values())

    # print key with val temp
    position = val_list.index(min_temprature)
    print("Lowest: " + min_temprature + "C on " + key_list[position])

    max_humidity = max(dict1.values())
    key_list = list(dict1.keys())
    val_list = list(dict1.values())

    # print key with val temp
    position = val_list.index(max_humidity)
    print("Humidity: " + max_humidity + "% on " + key_list[position])


def file_processing(i, files_list):
    index = i
    files_list = files_list
    files_path = "/home/hamza/Downloads/weatherfiles/weatherfiles/"
    filepaths = [os.path.join(files_path, name) for name in os.listdir(files_path)]
    print(files_path)
    for i in files_list:
        if i in files_list:
            with open(i) as f:
                csv_file = reader(f)
                next(csv_file)
                dict_rows_key = {rows[0]: rows[9] for rows in csv_file}
    return dict_rows_key


def file_parsing(year, month_name, option):
    year = year
    month = month_name
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    files_list = [None] * 12
    j = 0
    if option == "-e":
        list_length = len(files_list)

        for i in range(list_length):
            files_list[i] = ("Murree_weather_" + year + "_" + months[j] + ".txt")
            j = j + 1

    else:
        files_list[0] = "Murree_weather_" + year + "_" + months[j] + ".txt"
    dict_max_temprature = file_processing(1, files_list)
    dict_min_temprature = file_processing(3, files_list)
    dict_humidity = file_processing(9, files_list)
    if year != month_name:
        monthly_average_values(dict_max_temprature, dict_min_temprature,
                               dict_humidity)

    elif option == "-a":
        yearly_values(dict_max_temprature, dict_min_temprature, dict_humidity)
    elif option == "-c":
        get_first_second_temprature(dict_max_temprature, dict_min_temprature, month, year)


if __name__ != '__main__':
    pass
else:
    main(sys.argv[1])
