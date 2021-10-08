start_number_system = 0
start_number = "1111101"
end_number_system = 0
end_number = ""
invalid_value = True
while invalid_value:
    raw_input_data = input("kérem adja meg a cél számrendszert: ")
    if raw_input_data.isnumeric():
         start_number_system = int(raw_input_data)
        if start_number_system > 1:
            invalid_value = False
        else:
            print("A megadott érték nem egy egynél nagyobb pozitív egész szám")
else:
    print("A megadott érték nem egy egynél nagyobb pozitív egész szám")

invalid_value = True
while invalid_value:
    start_number = input("kérem adja meg a cél számrendszert: ")
    if start_number.isnumeric():
        invalid_value = False
    else:
        print("A megadott érték nem csak számjegyeket és betűket tartalmaz.")

number = 0
value = 0
for i in range(len(start_number)):
    if start_number[i].isnumeric():
        value = int(start_number[i])
    else:
        value = ord(start_number[i]) - 65 +10
    number += value * start_number_system ** (len(start_number) - i - 1)

print(number)

while number > 0:
    reminder = number % end_number_system
    if reminder < 10:
        end_number = str(reminder) + end_number
    else:
        end_number = chr(reminder + 65 - 10) + end_number

    number = number // end_number_system
print("a szam értéke a cél szamrendszerben:", end_number)



#elvesztettem a fonalat



