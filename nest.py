rows = int(input("How many rows: "))
coloumns = int(input("How many coloumns: "))
symbol = input("Enter symbol you weant to print: ")

for i in range(rows):
    
    for j in range(coloumns):
        print(symbol, end="")
    print()
        
#loop control

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="") 


for i in range(1, 21):
    
    if i == 13:
        pass
    else:
        print(i)
        