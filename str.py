age = 21
age -= 1
'''
print("Your age is: " + str(age))

height = 168.5

print("Your height is: " + str(height))

print()

print(f"Your age is {age} years old and your height is {height}cm.")
print()

print(type(height))

# multiple assignment
name, age, attractive = "Arhan", 20, True

print(f"{name} {age} {attractive}")

a = b = c = d = (20,)
print(a + b + c + d)
'''

# string methods
"""
name = "arhan Thaker"

print(len(name))
print(name.find("k"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print()
print(name.isdigit())
print(name.isalpha()) # spaces and punctuation return false
print(name.count("a"))
print(name.count("A"))
print(name.replace("a", "x"))
print(name*3)
print()
"""

# type casting
x = 1
y = 2.0
z = "3"

y = int(y)
z = float(z)

print(x)
print(y)
print(z*3)
