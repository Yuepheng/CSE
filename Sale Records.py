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
    Veggies_Profit = []
    Snacks_Profit = []
    SubSaharan_Africa_Profit = []
    MiddleEastandNorthAfrica_Profit = []
    AustraliaOceania_Profit = []
    Europe_Profit = []
    Asia_Profit = []
    CentralAmericaAndCaribbean_Profit = []
    print("Processing....")

    for row in reader:
        Profit = row[13]
        FRUIT = row[2]
        if FRUIT == "Fruits":
            print(Profit)
            Fruit_Profit.append(float(Profit))
        HOUSEHOLD = row[2]
        if HOUSEHOLD == "Household":
            print(Profit)
            Household_Profit.append(float(Profit))
        OFFICE_SUPPLIES = row[2]
        if OFFICE_SUPPLIES == "Office Supplies":
            print(Profit)
            Office_Supplies_Profit.append(float(Profit))
        CLOTHES = row[2]
        if CLOTHES == "Clothes":
            print(Profit)
            Clothes_Profit.append(float(Profit))
        MEAT = row[2]
        if MEAT == "Meat":
            print(Profit)
            Meat_Profit.append(float(Profit))
        BEVERAGES = row[2]
        if BEVERAGES == "Beverages":
            print(Profit)
            Beverages_Profit.append(float(Profit))
        COSMETICS = row[2]
        if COSMETICS == "Cosmetics":
            print(Profit)
            Cosmetics_Profit.append(float(Profit))
        PERSONAL_CARE = row[2]
        if PERSONAL_CARE == "Personal Care":
            print(Profit)
            Personal_Care_Profit.append(float(Profit))
        BABY_FOOD = row[2]
        if BABY_FOOD == "Baby Food":
            print(Profit)
            Baby_Food_Profit.append(float(Profit))
        CEREAL = row[2]
        if CEREAL == "Cereal":
            print(Profit)
            Cereal_Profit.append(float(Profit))
        VEGGIES = row[2]
        if VEGGIES == "Vegetables":
            print(Profit)
            Veggies_Profit.append(float(Profit))
        SNACKS = row[2]
        if SNACKS == "Snacks":
            print(Profit)
            Snacks_Profit.append(float(Profit))
        SUBSAHARAN = row[0]
        if SUBSAHARAN == "Sub-Saharan Africa":
            print(Profit)
            SubSaharan_Africa_Profit.append(float(Profit))
        MIDDLEEASTANDNORTHAFRICA = row[0]
        if MIDDLEEASTANDNORTHAFRICA == "Middle East and North Africa":
            print(Profit)
            MiddleEastandNorthAfrica_Profit.append(float(Profit))
        AUSTRALIAOCEANIA = row[0]
        if AUSTRALIAOCEANIA == "Australia and Oceania":
            print(Profit)
            AustraliaOceania_Profit.append(float(Profit))
        EUROPE = row[0]
        if EUROPE == "Europe":
            print(Profit)
            Europe_Profit.append(float(Profit))
        ASIA = row[0]
        if ASIA == "Asia":
            print(Profit)
            Asia_Profit.append(float(Profit))
        CENTRALAMERICAANDCARIBBEAN = row[0]
        if CENTRALAMERICAANDCARIBBEAN == "Central America and the Caribbean":
            print(Profit)
            CentralAmericaAndCaribbean_Profit.append(float(Profit))

    Asia_sum = sum(Asia_Profit)
    CentralAmericaAndCaribbean_Sum = sum(CentralAmericaAndCaribbean_Profit)
    Europe_sum = sum(Europe_Profit)
    AustraliaOceania_sum = sum(AustraliaOceania_Profit)
    MiddleEastandNorthAfrica_sum = sum(MiddleEastandNorthAfrica_Profit)
    SubSaharan_Africa_sum = sum(SubSaharan_Africa_Profit)
    Snacks_sum = sum(Snacks_Profit)
    Veggies_sum = sum(Veggies_Profit)
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
    print("The total amount of profit the Vegetables category made is %f" % Veggies_sum)
    print("The total amount of Profit the Snacks Category made is %f" % Snacks_sum)
    print("AND The Category with the MOST AMOUNT OF PROFIT is.......................... THE COSMETICS CATEGORY!!!!!!!!")
    print()
    print()
    print("New List about the profit from Regions.")
    print("The total Profit of the Sub Saharan Africa Region is % f" % SubSaharan_Africa_sum)
    print("The total profit of the Middle East and North Africa region is %f" % MiddleEastandNorthAfrica_sum)
    print("The total Profit of the Australia And Oceania region is %f" % AustraliaOceania_sum)
    print("The total amount of Profit the Europe region is %f" % Europe_sum)
    print("The total amount of Profit the Asia region has is %f" % Asia_sum)
    print("The total amount of Profit the Central America and Caribbean region is %f" % CentralAmericaAndCaribbean_Sum)
    print("Done")
