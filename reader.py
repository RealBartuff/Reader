
import csv
import pickle
import json

from sys import argv

file_content = []
main_file = argv[1]

def load_csv(main_file):
    with open(main_file, "r") as file:
        reader = csv.reader(file)
        for line in reader:
            file_content.append(line)
        return file_content

def load_json(main_file):
    reader = main_file.read()
    file_content_2 = json.loads(reader)

def save_csv(main_file, file_content):
    with open(main_file, "w", newline="") as file:
        writer = csv.writer(file)
        for line in file_content:
            writer.writerow(line)


for param in argv[3:]:
    param_list = param.split(",")
    file_content[int(param_list[0])-1][int(param_list[1])-1] = param_list[2]


def save_json(main_file, file_content):
    with open(main_file, "w", newline="") as file:
        file_content_json = json.dumps(file_content)
        file.write(file_content_json)

def ext(main_file, file_content):
    main_file_list = main_file.split(".")
    extension = main_file_list[-1]
    if extension == "csv":
        save_csv(main_file, file_content)
    elif extension == "json":
        save_json(main_file, file_content)


"""with open(argv[2], "w") as file:
    print(json.dumps(file_content))
    file_content_json = json.dumps(file_content)
    file.write(file_content_json)"""
