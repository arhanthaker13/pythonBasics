# lists

food = ["pizza", "hotdog", "burger", "sphagetti"]

food[0] = "sushi"

#print(food[0])

food.append("ice cream")
food.remove("hotdog")
food.pop()
food.insert(0, "taco")
food.sort()
#food.clear()

for i in food:
    print(i, end=" ")
    