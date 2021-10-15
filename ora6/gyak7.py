a, b = 0, 0
is_number = False
while not is_number:
    try:
        a = int(input("kezdőérték:"))
        is_number = True
    except ValueError:
        print("invalid érték")

is_number = False
while not is_number:
    try:
        b = int(input("kezdőérték:"))
        is_number = True
    except ValueError:
        print("invalid érték")

sum = 0
for number in range(a, b +1):
    if number % 3 == 0 and number % 5 == 0:
        sum += number
print(sum)