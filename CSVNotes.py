import csv


def validate(num: str):
    if is_first_num_odd(num) and is_second_num_even(num):
        return True
    return False


def divisible_by_one(num: str):
    first_num = int(num[1])     # This is the first number
    if first_num % 5 == 0:      # For Every Number that can be multiplied by         % = Module
        return True             # A list of the first 2 numbers being odd then even
    return False


def multiply2(num: str):
    second_num = int(num[0])  # This is the first number
    if second_num % 2 == 0:  # For Every Number that can be multiplied by 3        % = Module
        return True
    return False


def is_first_num_odd(num: str):
    first_num = int(num[0])
    if first_num % 2 == 1:
        return True
    return False


def is_second_num_even(num: str):
    second_number = int(num[1])
    if second_number % 2 == 0:
        return True
    return False


# with open("Book1.csv", 'r') as old_csv:     # Allows us to open another file and access its Data
#     reader = csv.reader(old_csv)        # Goes through and reads the information in that CSV
#     for row in reader:
#         old_number = row[0]
#         # print(int(old_number) + 1)
#         print(old_number)


# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         print("Processing....")
#
#         for row in reader:
#             old_number = row[0]     # A String object
#             first_num = int(old_number[0])
#             # print(int(old_number) + 1)
#             if first_num == 4:   # Scans the first number a certain number or an old/even number
#                 writer.writerow(row)
#     print("Done")


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing....")

        for row in reader:
            old_number = row[0]     # A String object
            if validate(old_number):   # Scans the first number a certain number or an old/even number
                writer.writerow(row)
            # print(int(old_number) + 1)
            # print(old_number)
    print("Done")
