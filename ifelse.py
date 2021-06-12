
def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    elif num1 == num2 and num1 == num3:
        return num1
    else:
        return num3

print(max_num(11,11,12))