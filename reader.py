"""
import os
import json

from sys import argv, stdin, stdout

data = argv[2:]
with open(argv[1], "a") as file:
    json.dump(data, file)


    if argv[1] != "deniro.csv":
        print("No such file or directory in: ", os.path.abspath("venv"))
        print(os.system("DIR"))
    for line in file:
        stdout.write(file.readline())"""

import csv

from sys import argv

with open(argv[1], "r") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)

with open(argv[1], "a") as file:
    writer = csv.writer(file)
    writer.writerow(argv[3:])
    