import csv

name = input("What is ur name?")

home = input("where is your home?")

with open("students.csv", "a") as file:
    writer = csv.DictReader(file, fieldnames = ["name", "home"])
    writer.writerow({"name": name, "home" : home})