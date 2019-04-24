import csv


with open("Book1.csv", 'r') as old_csv:     # Allows us to open another file and access its Data
    reader = csv.reader(old_csv)        # Goes through and reads the information in that CSV
    for row in reader:
        old_number = row[0]
        # print(int(old_number) + 1)
        print(old_number)
