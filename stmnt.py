# if else format

age = int(input("How old are you?: "))

if age == 100:
    print("You are century old")
elif age >= 18:
    print("You are an adult")
elif 0 < age < 18:
    print("You are a child")
else:
    print("You are not born yet")
    