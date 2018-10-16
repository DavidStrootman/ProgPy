import csv

lines = []

with open("gamers.csv", "r", newline="") as file:
    file_reader = csv.reader(file, delimiter=";")

    [lines.append("; ".join(row)) for row in file_reader]
    highest_string_list = max(lines[-2:]).split(";")

    name = highest_string_list[0]
    date = highest_string_list[1].replace(" ", "")
    score = highest_string_list[2].replace(" ", "")

    print("De hoogste score is: " + score + " op " + date + " behaald door " + name)
