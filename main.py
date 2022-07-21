import math
import os
import csv
import statistics


def main():
    months = [" ", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    time = input("Enter the time you want to get files: ")
    if "/" in time:
        year = time.split("/")[0]
        month = time.split("/")[1:]
        month = int(month[0])
        month_name = months[month]
        monthly_files(year, month_name)
    else:
        year = time
        month_name = "."
        file_processing(month_name, year)


def monthly_files(year, month_name):
    files_path = r"/home/hamza/Downloads/weatherfiles/weatherfiles/"
    filepaths = [os.path.join(files_path, name) for name in os.listdir(files_path)]
    for path in filepaths:
        if month_name in path:
            if year in path:
                with open(path) as f:
                    cvs_file = csv.reader(f)
                    next(cvs_file)
                    dict_from_csv1 = {rows[0]: rows[3] for rows in cvs_file}
                    # for key, value in dict_from_csv1.items():
                    #     print([key, value])
    for path in filepaths:
        if month_name in path:
            if year in path:
                with open(path) as f:
                    cvs_file = csv.reader(f)
                    next(cvs_file)
                    dict_from_csv = {rows[0]: rows[1] for rows in cvs_file}

    for path in filepaths:
        if month_name in path:
            if year in path:
                with open(path) as f:
                    cvs_file = csv.reader(f)
                    next(cvs_file)
                    dict_from_csv2 = {rows[0]: rows[9] for rows in cvs_file}
    # print(month_name+" "+year)
    average_values(dict_from_csv, dict_from_csv1, dict_from_csv2, month_name, year)


def average_values(dict, dict1, dict2, month, year):
    # res = sum((len(val) for val in dict.values()))
    # print(res)
    # dict[key] = [int(elt) for elt in row[1:] if elt.isdigit()]
    month = month
    year = year
    new_values = [list for key, list in dict.items()]
    for i in range(0, len(new_values)):
        new_values[i] = int(new_values[i])
    first_highest_temprature = max(new_values)
    second_highest_temprature = max(filter(lambda score: score != first_highest_temprature, new_values))

    new_values1 = [list for key, list in dict1.items()]
    for i in range(0, len(new_values1)):
        new_values1[i] = int(new_values1[i])

    first_lowest_temprature = min(new_values1)
    second_lowest_temprature = max(filter(lambda score: score != first_lowest_temprature, new_values1))

    new_values2 = [list for key, list in dict2.items()]
    for i in range(0, len(new_values2)):
        new_values2[i] = int(new_values2[i])

    print("Highest Average: " + str(math.ceil(statistics.mean(new_values))) + "C")
    print("Lowest Average: " + str(math.ceil(statistics.mean(new_values1))) + "C")
    print("Average Mean Humidity: " + str(math.ceil(statistics.mean(new_values2))) + "%")

    first_second(first_highest_temprature, second_highest_temprature, first_lowest_temprature,
                 second_lowest_temprature, month, year)

    # x = type(dict["2009-9-1"][0])

    # print(list)


def first_second(maxT, secondmaxT, minT, secondminT, month, year):
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


def max_temprature(dict):
    temp = max(dict.values())

    key_list = list(dict.keys())
    val_list = list(dict.values())

    # print key with val 100
    position = val_list.index(temp)
    print("Highest " + temp + "C on " + key_list[position])
    # return temp


def min_temprature(dict):
    # print(dict1)
    temp = min(filter(None, dict.values()))
    key_list = list(dict.keys())
    val_list = list(dict.values())

    # print key with val temp
    position = val_list.index(temp)
    print("Minimum " + temp + "C on " + key_list[position])


def max_humidity(dict):
    temp = max(dict.values())
    key_list = list(dict.keys())
    val_list = list(dict.values())

    # print key with val temp
    position = val_list.index(temp)
    print("Maximum " + temp + "% on " + key_list[position])


def first_second_temprature(dict):
    temp = max(dict.values())
    key_list = list(dict.keys())
    val_list = list(dict.values())

    # print key with val temp
    position = val_list.index(temp)
    print(key_list[position])
    for i in range(temp):
        print("+")
    print(temp)


def file_processing(month_name, year):
    files_path = r"/home/hamza/Downloads/weatherfiles/weatherfiles/"
    filepaths = [os.path.join(files_path, name) for name in os.listdir(files_path)]
    for path in filepaths:
        if month_name in path:
            if year in path:
                with open(path) as f:
                    cvs_file = csv.reader(f)
                    next(cvs_file)
                    dict_from_csv1 = {rows[0]: rows[3] for rows in cvs_file}
                    # for key, value in dict_from_csv1.items():
                    #     print([key, value])
    for path in filepaths:
        if month_name in path:
            if year in path:
                with open(path) as f:
                    cvs_file = csv.reader(f)
                    next(cvs_file)
                    dict_from_csv = {rows[0]: rows[1] for rows in cvs_file}

    for path in filepaths:
        if month_name in path:
            if year in path:
                with open(path) as f:
                    cvs_file = csv.reader(f)
                    next(cvs_file)
                    dict_from_csv2 = {rows[0]: rows[9] for rows in cvs_file}
    max_temprature(dict_from_csv)
    min_temprature(dict_from_csv1)
    max_humidity(dict_from_csv2)

    # for key, value in dict_from_csv.items():
    #     fin_max = max(dict_from_csv, key=dict_from_csv.get)
    # print("Maximum value:", fin_max)

    # for line in cvsFile:
    #      print(line)
    # for key, value in mydict.items():
    #     writer.writerow([key, value])


if __name__ == '__main__':
    main()
