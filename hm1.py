from ast import If
import  array

# 1
def weekend_check(day):
    if (day == 6) | (day == 7):
        print("it's weekend")
    else:
        print("it's not weekend")

weekend_check(3)

# 2
def check_truth(x, y, z):
    if not((x) | (y) | (z)) == ((not x) & (not y) & (not z)) :
        print("True")
    else:
        print("False")

check_truth(True, True, False)
check_truth(0, 0, 1)


# 3
def quarter_definition(x, y):
    if (x > 0) and (y > 0):
        print('quarter equal I')
    elif x < 0 and y > 0:
        print('quarter equal II')
    elif x < 0 and y < 0:
        print('quarter equal III')
    else:
        print('quarter equal IV')

quarter_definition(-10, -20)
quarter_definition(10, -20)
quarter_definition(-10, 20)


# 4
a = int(input("введите первое число: "))
b = int(input("введите второе число: "))
oper = input("введите операцию, которую хотите произвести: ")

if oper == "+":
    print(a+b)
elif oper == "-":
    print(a-b)
elif oper == "/":
    print(a/b)
elif oper == "*":
    print(a*b)
elif oper == "mod":
    print(a%b)
elif oper == "pow":
    print(a**b)
elif oper == "div":
    print(a//b)


# 5
def my_sorted( the_List ):
    result = []
    for element in the_List:
        element_array = []
        length = len(element)
        while len(element_array) != length:
            min_value = min(element)
            element_array.append(min_value)
            element.remove(min_value)
        result.append(element_array)
    print(result)

my_sorted([[7, 3, 6], [2, 1, 5]])

