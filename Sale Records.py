import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    Fruit_Profit = []
    print("Processing....")

    for row in reader:
        Profit = row[13]
        FRUIT = row[2]
        if FRUIT == "Fruits":
            print(Profit)
            Fruit_Profit.append(float(Profit))
    Fruit_Sum = sum(Fruit_Profit)
    print("THE TOTAL AMOUNT OF PROFIT THE FRUIT CATAGORY IS %f" % Fruit_Sum)
    print("Done")
