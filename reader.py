
from sys import argv, stdin, stdout

with open("deniro.csv") as file:
    for line in file:
        stdout.write(file.readline())
