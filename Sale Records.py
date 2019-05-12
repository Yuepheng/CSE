import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    Fruit_Profit = []
    Household_Profit = []
    Office_Supplies_Profit = []
    Clothes_Profit = []
    Meat_Profit = []
    Beverages_Profit = []
    Cosmetics_Profit = []
    Personal_Care_Profit = []
    Baby_Food_Profit = []
    Cereal_Profit = []
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
        MEAT = row[2]
        if MEAT == "Meat":
            Meat_Profit.append(float(Profit))
        BEVERAGES = row[2]
        if BEVERAGES == "Beverages":
            Beverages_Profit.append(float(Profit))
        COSMETICS = row[2]
        if COSMETICS == "Cosmetics":
            Cosmetics_Profit.append(float(Profit))
        PERSONAL_CARE = row[2]
        if PERSONAL_CARE == "Personal Care":
            Personal_Care_Profit.append(float(Profit))
        BABY_FOOD = row[2]
        if BABY_FOOD == "Baby Food":
            Baby_Food_Profit.append(float(Profit))
        CEREAL = row[2]
        if CEREAL == "Cereal":
            Cereal_Profit.append(float(Profit))

    Cereal_sum = sum(Cereal_Profit)
    Baby_Food_sum = sum(Baby_Food_Profit)
    Personal_Care_sum = sum(Personal_Care_Profit)
    Cosmetics_sum = sum(Cosmetics_Profit)
    Beverages_sum = sum(Beverages_Profit)
    Meat_sum = sum(Meat_Profit)
    Clothes_sum = sum(Clothes_Profit)
    Office_Supplies_sum = sum(Office_Supplies_Profit)
    Household_sum = sum(Household_Profit)
    Fruit_Sum = sum(Fruit_Profit)
    print("THE TOTAL AMOUNT OF PROFIT THE FRUIT CATEGORY IS %f" % Fruit_Sum)
    print("THE TOTAL AMOUNT OF PROFIT THE HOUSEHOLD CATEGORY IS %f" % Household_sum)
    print("THE TOTAL AMOUNT OF PROFIT THE OFFICE SUPPLY CATEGORY IS %f" % Office_Supplies_sum)
    print("THE TOTAL AMOUNT OF PROFIT THE CLOTHES CATEGORY IS %f" % Clothes_sum)
    print("THE TOTAL AMOUNT OF PROFIT THE MEAT CATEGORY IS %f" % Meat_sum)
    print("The total amount of profit the beverage category has is %f" % Beverages_sum)
    print("The total amount of profit that the Cosmetics Category made is %f" % Cosmetics_sum)
    print("The total amount of profit the Personal Care category made is %f" % Personal_Care_sum)
    print("The Total amount of profit the Baby Food category made is %f" % Baby_Food_sum)
    print("The total amount of profit the Cereal Category made is %f" % Cereal_sum)
    print("Done")
