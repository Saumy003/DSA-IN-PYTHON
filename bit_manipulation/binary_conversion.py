""" Introduction to Bit Manipulation
    1. Binary Conversion
 """

# i.convert decimal to binary 

def covert_to_binary(num:int)->str:
    result = ""

    while num > 0:
        if num % 2 == 1:
            result += "1"
        else:
            result += "0"
        
        num = num//2
    result = result[: : -1]
    return result

print("binary number is:", covert_to_binary(13))         #1101


# ii. convert binary to decimal

def convert_to_decimal(x:str)->int:
    decimal_number = 0
    power = 0
    index = len(x) - 1

    while index >= 0:
        num = int(x[index]) * (2**power)
        decimal_number += num
        index -= 1
        power += 1
    return decimal_number

print("Decimal number is:", convert_to_decimal("1101"))   #13