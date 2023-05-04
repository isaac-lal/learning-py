# freeCodeCamp.org: Learn Python - Full Course for Beginners [Tutorial] (2:41:21)

print(2**3) # 2^3

def raise_to_power(base_num, pow_num):
    result = 1

    for index in range(pow_num):
        result *= base_num

    return result

print(raise_to_power(2, 3))