def make_negative(number):
    if number==0:
        return 0
    elif number>0:
        return -number
    return number
print(make_negative(0))
print(make_negative(23))
print(make_negative(-12))
# another short
def make_negative(number):
    return -abs(number)
# if you give abs() a number, it’ll hand you back its distance from zero on the number line. Positive numbers remain unchanged, while negative ones flip their sign
# eg: # Example 1: Absolute value of an integer
# my_number = -20
# absolute_number = abs(my_number)
# print("Absolute value:", absolute_number)  # Output: 20

# # Example 2: Absolute value of a floating-point number
# my_float = -7.25
# absolute_float = abs(my_float)
# print("Absolute value:", absolute_float)  # Output: 7.25

# # Example 3: Absolute value of a complex number
# my_complex = 3 + 5j
# absolute_complex = abs(my_complex)
# print("Magnitude (absolute value) of complex number:", absolute_complex)

make_negative(number=int(input("Enter the number ")))