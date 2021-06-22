
import csv
import pickle
import json

from sys import argv


file_content = []
with open(argv[1], "r") as file:
    reader = csv.reader(file)
    for line in reader:
        file_content.append(line)

for line in file_content:
    print(line)

for param in argv[3:]:
    param_list = param.split(",")
    file_content[int(param_list[0])-1][int(param_list[1])-1] = param_list[2]

with open(argv[2], "w", newline="") as file:
    writer = csv.writer(file)
    for line in file_content:
        writer.writerow(line)
