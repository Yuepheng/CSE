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
    NorthAmerica_Profit = []
    print("Processing....")

    for row in reader:
        Profit = row[13]
        FRUIT = row[2]
        if FRUIT == "Fruits":
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
        VEGGIES = row[2]
        if VEGGIES == "Vegetables":
            Veggies_Profit.append(float(Profit))
        SNACKS = row[2]
        if SNACKS == "Snacks":
            Snacks_Profit.append(float(Profit))
        SUBSAHARAN = row[0]
        if SUBSAHARAN == "Sub-Saharan Africa":
            SubSaharan_Africa_Profit.append(float(Profit))
        MIDDLEEASTANDNORTHAFRICA = row[0]
        if MIDDLEEASTANDNORTHAFRICA == "Middle East and North Africa":
            MiddleEastandNorthAfrica_Profit.append(float(Profit))
        AUSTRALIAOCEANIA = row[0]
        if AUSTRALIAOCEANIA == "Australia and Oceania":
            AustraliaOceania_Profit.append(float(Profit))
        EUROPE = row[0]
        if EUROPE == "Europe":
            Europe_Profit.append(float(Profit))
        ASIA = row[0]
        if ASIA == "Asia":
            Asia_Profit.append(float(Profit))
        CENTRALAMERICAANDCARIBBEAN = row[0]
        if CENTRALAMERICAANDCARIBBEAN == "Central America and the Caribbean":
            CentralAmericaAndCaribbean_Profit.append(float(Profit))
        NORTHAMERICA = row[0]
        if NORTHAMERICA == "North America":
            NorthAmerica_Profit.append(float(Profit))

    NorthAmerica_sum = sum(NorthAmerica_Profit)
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

    ItemCategorySum = [Fruit_Sum, Household_sum, Office_Supplies_sum, Clothes_sum, Meat_sum, Beverages_sum,
                       Cosmetics_sum, Personal_Care_sum, Baby_Food_sum, Cereal_sum, Veggies_sum, Snacks_sum]

    RegionProfitSum = [SubSaharan_Africa_sum, MiddleEastandNorthAfrica_sum, AustraliaOceania_sum, Europe_sum,
                       CentralAmericaAndCaribbean_Sum, Asia_sum]

    RegionOfProfit = ["Sub-Saharan Africa", "Middle East and North Africa", "Australia and Oceania", "Europe",
                      "Asia", "Central America and the Caribbean", "North America"]

    ItemCategoryType = ["Fruit", "Household", "Office Supplies", "Clothes", "Meat", "Beverages", "Cosmetics",
                        "Personal Care", "Baby Care", "Cereal", "Vegetables", "Snacks"]

    index = ItemCategorySum.index(max(ItemCategorySum))
    index2 = RegionProfitSum.index(max(RegionProfitSum))

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
    print("AND The Category with the MOST AMOUNT OF PROFIT is....... %s!!!!!!!!!!!!!!!!" % ItemCategoryType[index])
    print()
    print()
    print("New List about the profit from Regions.")
    print("The total Profit of the Sub Saharan Africa Region is % f" % SubSaharan_Africa_sum)
    print("The total profit of the Middle East and North Africa region is %f" % MiddleEastandNorthAfrica_sum)
    print("The total Profit of the Australia And Oceania region is %f" % AustraliaOceania_sum)
    print("The total amount of Profit the Europe region is %f" % Europe_sum)
    print("The total amount of Profit the Asia region has is %f" % Asia_sum)
    print("The total amount of Profit the Central America and Caribbean region is %f" % CentralAmericaAndCaribbean_Sum)
    print("The total amount of Profit North America made is %f" % NorthAmerica_sum)
    print("Done")
