import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    Fruit_Profit = []
    Household_Profit = []
    Office_Supplies_Profit = []
    Clothes_Profit = []
    print("Processing....")

    for row in reader:
        Profit = row[13]
        FRUIT = row[2]
        if FRUIT == "Fruits":
            print(Profit)
            Fruit_Profit.append(float(Profit))
        HOUSEHOLD = row[2]
        if HOUSEHOLD == "Household":
            Household_Profit.append(float(Profit))
        OFFICE_SUPPLIES = row[2]
        if OFFICE_SUPPLIES == "Office Supplies":
            Office_Supplies_Profit.append(float(Profit))
        CLOTHES = row[2]
        if CLOTHES == "Clothes":
            Clothes_Profit.append(float(Profit))

    Clothes_sum = sum(Clothes_Profit)
    Office_Supplies_sum = sum(Office_Supplies_Profit)
    Household_sum = sum(Household_Profit)
    Fruit_Sum = sum(Fruit_Profit)
    print("THE TOTAL AMOUNT OF PROFIT THE FRUIT CATEGORY IS %f" % Fruit_Sum)
    print("THE TOTAL AMOUNT OF PROFIT THE HOUSEHOLD CATEGORY IS %f" % Household_sum)
    print("THE TOTAL AMOUNT OF PROFIT THE OFFICE SUPPLY CATEGORY IS %f" % Office_Supplies_sum)
    print("THE TOTAL AMOUNT OF PROFIT THE CLOTHES CATEGORY IS %f" % Clothes_sum)
    print("Done")
