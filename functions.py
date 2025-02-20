# def greet(name):
#     print("Hello, welcome to Python!",name)

# greet("aniket") # Calling the function

# def add(a, b):
#     return a + b  # Returns sum

# result = add(5, 3)
# print("Sum:", result)

# def greet(name="hero"):
#     print("Hello,", name)

# greet()  # Uses default value
# greet("Rahul")  # Uses given argument

# def person_info(name, age):
#     print("Name:", name)
#     print("Age:", age)

# person_info(age=20, name="Neha")  # Order doesn't matter

def add_numbers(*numbers):
    return sum(numbers)

print(add_numbers(1, 2, 3, 4, 5))  # Sum of all arguments
