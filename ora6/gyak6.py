name = input("add meg a nevedet gec:")
gender = input("add meg a nemedet genyoo (f-nő, m- férfi):")
if gender == "f":
    print(name, "asszony")
elif gender == "m":
    print(name, "ur")
else:
    print("nem")