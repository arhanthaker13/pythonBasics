character_name = "John Cena"
character_age = "18"
is_male = True;

phrase1 = "HELLO"
phrase2 = "hello HelOO hElIO"

char_age = 18

print("My name is " + character_name + " AND")
print("I am " + character_age + " years old.\n")

character_name = "Mike"

print(f"My name is {character_name} and I'm {char_age} years old.")
print()

if is_male: 
    print("MALE!")
else: 
    print("NOT MALE!")
print()

print(phrase1.lower())
print(phrase1)
print(phrase2.lower())
print(phrase2.upper())
print()

print(phrase1.isupper())
print(phrase1.lower().isupper())
print()

print(len(phrase2))
print(phrase2[0])
# print(phrase2[0, 4])
print(phrase2[5] + "<-- blank space")
print()

print(phrase2.index("h"))
print()

#for instance in enumerate(phrase2):
#    print(f"{phrase2.index("h") }") 

print(phrase1.replace("HELL", "HEAVEN"))
