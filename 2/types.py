input_data = input("kérek egy egyész számot: ")
try:
    int_number = int(input_data)
    print("A kapott szám 3 szorosa:", 3 * int_number)
    print(type(input_data))
    print(type(int_number))

except ValueError:
    print("Ez nem egyész szam")

input_data = input("kérek egy valós számot")
try:
    float_number = float(input_data)
    print("A kapott szám 3 szorosa:", 3 * float_number)
    print(type(input_data))
    print(type(float_number))
    str_number = str(float_number)
    print(type(str_number), str_number)
except ValueError:
    print("valós számot kértem")