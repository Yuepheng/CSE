import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    print("Processing....")

    for row in reader:
        Profit = row[13]
        FRUIT = row[2]
        if FRUIT == "Fruits":
            print(Profit)
            print(FRUIT)
    print("Done")
