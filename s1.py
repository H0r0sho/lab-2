import csv
import os


def make_dir(path_fol: str, path_sc1: str) -> None:
    if not os.path.isdir(path_fol): os.mkdir(path_fol)
    if not os.path.isdir(path_sc1): os.mkdir(path_sc1)

def run_1(path_to_csv: str=os.path.join("C:/", "Users", "79171", "PyCharmProjects", "lab2")) -> None:
    path_fol, path_sc1 = "lab2", "lab2/s1"
    make_dir(path_fol, path_sc1)
    list1 = []
    with open(path_to_csv + '/dataset.csv', 'r', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            list1.append(row)

    with open(path_to_csv + "/lab2/X.csv", 'w', newline='', encoding='utf-8') as csvfile_x:
        for i in reversed(range(0, len(list1))):
            all_data = [list1[i][0][0:10]]
            writer = csv.writer(csvfile_x)
            writer.writerow(all_data)

    with open(path_to_csv + "/lab2/Y.csv", 'w', newline='', encoding='utf-8') as csvfile_y:
        for i in range(0, len(list1)):
            all_data = [list1[i][0][12:]]
            writer = csv.writer(csvfile_y)
            writer.writerow(all_data)