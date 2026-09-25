import math
def ex1():
    r = float(input("enter circle radius: "));
    area = (r**2) * 3.14 ;
    print(area);

def ex2():
    c = float(input("enter the temperature in C: "));
    f = c * 1.8 + 32;
    print(f);

def ex3():
    num = int(input("Enter a positive integer: "))
    if num <= 1:
        is_prime = False
    is_prime = True    

    for i in range(2, int(math.sqrt(num))+1):
        if (num % i == 0):
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number!")
    else:
        print(f"{num} is NOT a prime number.")

def ex4():
    num = int(input("enter a number: "))
    if (num < 0):
        print("Not a positive integer.")
        return
    divisors = [1]
    for i in range (2, int(num/2)+1):
        if (num % i == 0):
            divisors.append(i)

    sum = 0
    for i in divisors:
        sum += 1
    if sum == num:
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")                

def ex5():
    colors = ["red", "green", "blue", "yellow", "brown"]
    favorite_color = input("What is your favorite color: ")

    if favorite_color in colors:
        index = colors.index(favorite_color)
        print(f"Your color is at index {index} in my lists")
    else:
        print(f"Sorry")


def ex6():
    range1 = list(range(0,7))
    range2 = list(range(1,11,3))
    range3 = list(range(5,0,-1))
    range4 = list(range(6,-3,-2))

    print("range 1: ",range1)
    print("range 2: ",range2)
    print("range 3: ",range3)
    print("range 4: ",range4)


def ex7():
    user_input = input("Enter a string with a dollar sign($): ")
    clean_text = user_input.replace("$", "")
    print(clean_text)



def ex8():
    user_input = list(input("Enter a list of integer: ").split())
    extract_even = []
    for i in user_input:
        if int(i) % 2 == 0:
            extract_even.append(i)
    print(f"The string of even number is {extract_even}")

def ex9():
    num = int(input("Enter a number: "))
    
    if num < 0:
        print("Error: cannot enter a number less than 0")
    else:
        factorial_num = 1
        for i in range(2, num + 1):
            factorial_num *= i 
        print(f"The factorial of {num} is {factorial_num}")


def ex10():
    num = int(input("Enter a positive integer: "))
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    print(f"The divisors of {num} are {divisors}")


def ex11():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"The distance between points is {distance:.2f}")

def ex12():
    m = int(input("Enter number of rows (m): "))
    n = int(input("Enter number of columns (n): "))
    
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

ex1()
ex2()
ex3()
ex4()
ex5()
ex6()
ex7()
ex8()
ex9()
ex10()
ex11()
ex12()
