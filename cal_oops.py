def div(number_1, number_2):
    """division of numbers"""
    try:
        Result = number_1 / number_2
    except ZeroDivisionError as err:
        print('Error', err)
    else:
        print('Result')


def mul(number_1, number_2):
    """multiplication of numbers"""
    return number_1 / number_2




def modulo(number_1, number_2):
    """modulus of numbers"""
    return number_1 % number_2


def add(number_1, number_2):
    """addition of numbers"""
    return number_1 + number_2


def sub(number_1, number_2):
    """Subtraction of two numbers"""
    return number_1 - number_2


class Calculators():
    """class is created"""


if __name__ == "__main__":
    mycalculator = Calculators()
    ch = 1
    while ch!=0:
        print("1:add")
        print("2:sub")
        print("3:mul")
        print("4:div")
        print("5:modulo")
        ch = int(input("select operation"))
        num3 = int(input("enter the first number"))
        num4 = int(input("enter the second value"))

        if ch == 1:
            print("calculate:", add(num3, num4))
        elif ch == 2:
            print("calculate:", sub(num3, num4))
        elif ch == 3:
            print("calculate:", mul(num3, num4))
        elif ch == 4:
            print("calculate:", div(num3, num4))
        elif ch == 5:
            print("calculate:", modulo(num3, num4))
        else:
            print("Enter valid option")

