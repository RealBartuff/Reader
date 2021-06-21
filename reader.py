
import csv
import pickle
import json

from sys import argv

"""
def jj():
    data = argv[2:]
    with open(argv[1], "a") as file:
        json.dump(data, file)
        

def pickle_process():
    data = argv[2:]
    with open(argv[1], "a") as file:
        pickle.dump(data, file)


def csv_process():"""

with open(argv[1], "r") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)

with open(argv[2], "a") as file:
    writer = csv.writer(file)
    writer.writerow(argv[3:])
