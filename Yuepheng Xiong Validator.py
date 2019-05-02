test = "4556737586899855"


# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         print("Processing....")
#
#         for row in reader:
#             old_number = row[0]     # A String object
#             first_num = int(old_number[0])
#              if first_num == 0:   # Scans the first number a certain number or an old/even number
#                 number_lis


def validate(num: str):
    number_list = list(num)
    print(number_list)
    last_num = int(number_list.pop(15))         # Goes through and Deletes that last number in the list (15)
    print(number_list)
    print(last_num)
    reversed_list = reverse(number_list)
    print(reversed_list)
    multiply(number_list)
    print(number_list)


def reverse(string):
    string = string[::-1]
    return string


def multiply(num: list):
    for index in range(len(num)):
        num[index] = int(num[index])
        if index % 2 == 0:
            num[index] *= 2


print(validate(test))


# Notes

# for index in range(len(num)):
