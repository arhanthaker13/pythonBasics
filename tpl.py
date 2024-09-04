'''
student =("Bro", 21, "Male")

print(student.count("Bro"))
print(student.index("Male"))

for x in student:
    print(x)

if "Bro" in student:
    print("TRUE")
'''

#set

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}

utensils.update(dishes)

for x in utensils:
    print(x)
    
# set.add(x), set.remove(x), set.clear()
 