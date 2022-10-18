from audioop import mul
from unicodedata import decimal
import math
from unittest import result

# 1
# number = float(input("Enter the number: "))
# sum = 0
# some_number = int(number)
# another_number = 0

# if number - some_number != 0:
#     cnumber = some_number
#     print("cnum: ", cnumber)
#     vnumber = number - some_number
#     print("vnum: ", vnumber)
#     while cnumber > 0:
#         sum += cnumber % 10
#         cnumber = cnumber // 10
#     while round(vnumber, 3) != 0:
#         another_number = vnumber * 10
#         some_number = int(another_number)
#         sum += some_number
#         vnumber = another_number - some_number
# else:  # иначе
#     while number > 0:
#         sum += number % 10
#         number = number // 10

# print(sum)


# 2
# n_number = int(input("Enter the number: "))
# mult = 1
# result_str = ""
# for num in range(n_number):
#     mult = mult * (num + 1)
#     print("Произведение #", num + 1, "=", mult)


# 3
string1 = str(input("enter some text:")).lower()
string2 = str(input("and some else:")).lower()

coincidence = 0

for i in list(string1):
    for n in list(string2):
        if i == n:
            coincidence += 1
print(coincidence)
