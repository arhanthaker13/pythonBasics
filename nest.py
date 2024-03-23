rows = int(input("How many rows: "))
coloumns = int(input("How many coloumns: "))
symbol = input("Enter symbol you weant to print: ")

for i in range(rows):
    
    for j in range(coloumns):
        print(symbol, end="")
    print()
        