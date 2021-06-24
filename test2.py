import sys
import csv
import json


class DoCsv:
    def __init__(self):
        self.file_content = []

    def run_csv(self):
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            for line in reader:
                self.file_content.append(line)

        for line in self.file_content:
            print(line)

        for param in sys.argv[3:]:
            param_list = param.split(",")
            self.file_content[int(param_list[0]) - 1][int(param_list[1]) - 1] = param_list[2]

        with open(sys.argv[2], "w", newline="") as file:
            writer = csv.writer(file)
            for line in self.file_content:
                writer.writerow(line)


printer = DoCsv()
printer.run_csv()
