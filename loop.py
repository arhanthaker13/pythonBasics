import time
# while loop

name = None

while not name:
    name  = input("What is your name: ")
    print("PLESE ENTER YOUR NAME!!")

print(f"Hello {name}")


 # In Python, None, empty strings '', empty lists [], and other "falsy" values evaluate to False in a boolean context.

# for loop

for i in range(10, 20+1, 2):
    print(i)


name = "Arhan Thaker"
for i in name:
    print(i)
    
for sec in range(10, 0, -1):
    print(sec)
    time.sleep(1)

print("Happy New Year!")
