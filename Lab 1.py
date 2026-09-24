#Ex1: Area of circle
r = float(input("Enter radius: "))
area = 3.14 * r * r
print(f"Area of circle is: {area}")

#Ex2: Celsius to Fahrenheit
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print(f"{c}°C = {f}°F")

#Ex3: Prime number check
x = int(input("Enter a number: "))
if x > 1:
    for i in range(2, x):
        if x % i == 0:
            print(f"{x} is not a prime number")
            break
    else:
        print(f"{x} is a prime number")
else:
    print(f"{x} is not a prime number")

#Ex4: Perfect number check
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum = sum + i
if sum == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")

#Ex5: Find colors in a list
colors = ["red", "green", "blue", "yellow", "purple"]
fav_color = input("What's your favorite color? ")
if fav_color in colors:
    print(f"Your color is at index {colors.index(fav_color)} in the list")
else:
    print("Sorry, I could not find your color")

#Ex6: Using range() function
range1 = range(0, 7)
range2 = range(1, 11, 3) 
range3 = range(5, 0, -1)
range4 = range(6, -3, -2)
print(list(range1))
print(list(range2))
print(list(range3))
print(list(range4))

#Ex7: Function that removes the dollar sign
def remove_dollar_sign(s):
    return s.replace("$", "")
text = input("Enter price with dollar sign: ")
print(remove_dollar_sign(text))

#Ex8: Extracts the even items in a given integer list
def extract_even(lst):
    return [x for x in lst if x % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(extract_even(numbers))

#Ex9: Calculate the factorial of a number (non-negative integer).
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a non-negative integer: "))
print(f"Factorial of {num} is {factorial(num)}")

#Ex10: Get out all of divisors of a number.
def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

num = int(input("Enter a number: "))
print(f"Divisors of {num} are: {get_divisors(num)}")

#Ex11: Compute the distance between two points.
import math

def distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

x1 = float(input("Enter x-coordinate of first point: "))
y1 = float(input("Enter y-coordinate of first point: "))
x2 = float(input("Enter x-coordinate of second point: "))
y2 = float(input("Enter y-coordinate of second point: "))

print(f"Distance between the two points is: {distance(x1, y1, x2, y2)}")