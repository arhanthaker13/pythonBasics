"""
name = input("What is your name: ")
age = int(input("What is your age: "))

print(f"Hello {name}")
print(f"You are {age} years old")

"""

# indexing

name = "Arhan Thaker"

first_name = name[:5]
last_name = name[6:]
funky_name = name[::2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

# string slicing

website1 = "http://google.com"
website2 = "http://github.com"

web_name = slice(7, -4)

print(website1[web_name])
print(website2[web_name])
