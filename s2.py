import csv
import os
import re


a = []


def make_dir(path_sc2: str) -> None:
    if not os.path.isdir(path_sc2):
        os.mkdir(path_sc2)


def work_file(date_1: str, date_2: str, list1_years: list, path_to_csv: str) -> None:
    '''Принимает имя пути, записывает в список'''
    name_file = path_to_csv + '/lab2/' + date_1[0:10] + "_" + date_2[0:10] + ".csv"
    print("create file: ", name_file)
    with open(name_file, 'w', newline='', encoding='utf-8') as namefile:
        writer = csv.writer(namefile)
        for i in reversed(range(len(list1_years))):
            writer.writerow(list1_years[i])


def run_2(path_to_csv: str=os.path.join("C:/", "Users", "79171", "PyCharmProjects", "lab2")) -> None:
    '''Основная функция работы скрипта'''
    path_sc2 = path_to_csv + "/lab2"
    make_dir(path_sc2)
    set1 = set()
    list1_years = []
    with open(path_to_csv + '/dataset.csv', 'r',  encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            set1.add(row[0][:4])
    set1 = sorted(list(set1))
    n = len(set1)

    with open(path_to_csv + '/dataset.csv', 'r', encoding='utf-8') as csvfile:
        file_reader = list(csv.reader(csvfile))
        for i in range(n):
            for j in range(len(file_reader)):
                if (file_reader[j][0][:4] == set1[i]): list1_years.append(file_reader[j])
            print(list1_years[0][0][:4])
            date_2 = str(re.sub(r'[-]', '', list1_years[0][0]))
            date_1 = str(re.sub(r'[-]', '', list1_years[-1][0]))
            work_file(date_1, date_2, list1_years, path_to_csv)
            list1_years = []