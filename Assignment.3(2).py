import math

num=int(input("enter a number: "))

if num>0:
    square_root = math.sqrt(num)
    sine = math.sin(num)
    logarithm = math.log(num, 10)
    print(f"Square root: {square_root}\nLogarithm: {logarithm}\nSine: {sine}")
else:
    print("number is negative")




