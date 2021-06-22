import sys
import csv

class CsGo:
    def __init__(self):
        self.file_content = []

    def read(self):
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            for line in reader:
                self.file_content.append(line)
                print(line)


printuj = CsGo()
printuj.read()
