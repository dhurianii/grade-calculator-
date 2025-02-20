#Name=input("enter your name:")
#Age=input("enter your age:")
#Color=input("enter your favourite color:")
#print(f"Your name is {Name} and you are {Age} years old and your favourite color is {Color}.")

#Age=int(input("enter your age:"))
#X=(Age*12)
#print(f"you are {X} months old.")

#a = [1, 2, 3]
# b =a
# c = [1, 2, 3]
  
# print(a is  not b)   # True (same object)
# print(a is c)   # False (different objects)
# print(a is not c) # True

# numbers = [1, 2, 3, 4, 5 ,10]

# print(11 in numbers)    # True
# print(10  in numbers)  # True

# a = 5  # 0101
# b = 3  # 0011

# print(a & b)  # AND → 1  (0001)
# print(a | b)  # OR  → 7  (0111)
# print(a ^ b)  # XOR → 6  (0110)
# print(~a)     # NOT → -6 (inverts bits)
# print(a << 1) # Left Shift → 10 (1010)
# print(a >> 1) # Right Shift → 2 (0010)

#num=int(input("enter the number:"))
# b=int(input("enter the number:"))
# sum=(a+b)
# product=(a*b)
# difference=(a-b)
# quoitent=(a/b)
# print(sum ,product,difference,quoitent)
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

# x=input("bool value:")
# y=input("bool value:")
# print(x and y)
# print(x or y)
# print(not x)

# age =int(input("enter your age:"))
# if age>18:
#     print("you are adult.")
# elif age==18:
#     print("you are teenager.")
# else:
#     print("you are child.")
# num=int(input("enter a number:"))
# if num % 2==0:
#     print("even")
# else:
#     print("odd")
# n = 10  # Number of natural numbers
# sum_n = 0  # Initialize sum

# for i in range(5, n + 2):
#     sum_n += i  # Add each number to sum

# print("Sum of first", n, "natural numbers is:", sum_n)
# num = int(input("Enter a number: "))  # Get number from user

# for i in range(1, 11):  # Loop from 1 to 10
#     print(num, "x", i, "=", num * i)  # Print multiplication result

num = int(input("Enter a number: "))  # Get input from user
factorial = 1  # Initialize factorial value
i = 1

while i <= num:
    factorial *= i  # Multiply each number
    i += 1  # Increase counter

print("Factorial of", num, "is:", factorial)
