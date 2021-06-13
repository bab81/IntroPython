
print(2**3)

def raise_to_power(base_num, power):
    result = 1
    for i in range(power):
        result *= base_num

    return result

print(raise_to_power(2,4))