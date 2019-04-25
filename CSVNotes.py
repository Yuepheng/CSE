import csv


# with open("Book1.csv", 'r') as old_csv:     # Allows us to open another file and access its Data
#     reader = csv.reader(old_csv)        # Goes through and reads the information in that CSV
#     for row in reader:
#         old_number = row[0]
#         # print(int(old_number) + 1)
#         print(old_number)


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing....")

        for row in reader:
            old_number = row[0]     # A String object
            first_num = int(old_number[0])
            # print(int(old_number) + 1)
            if first_num == 4:   # Scans the first number a certain number or an old/even number
                writer.writerow(row)
    print("Done")
