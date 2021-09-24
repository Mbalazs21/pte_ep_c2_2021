number = -21
if number < 10:
    print("ez a sz kissebb mint 10")
else:
    print("Ez a szám nagyobb vagy engyelnő 10el")

if number > 100:
    print("Ez a szám nagyobb mint 100")
else:
    print("Ez a szám nem nagyobb mint 100")

if number % 2 > 0:
    print("páratlan")
else:
    print("páros")

number2 = 200
if number % number2 == 0:
    print("A", number2, "osztója a", number)
else:

    if number2 % number ==0:
        print("A", number, "osztója a", number2)
    else:
        print("Egyik sem osztója a másiknak")

str = "alma"
if str[0] == str[-1]:
    print("az első és az utcsó megegyezik")
else:
    print("nem egyezik meg")


if number > 0:
    print("pozitív")
else:
    if number < 0:
        print("negga")
    else:
        print("nulla")

if number > 0:
    print("pozitív")
elif number < 0:
    print("negga")
else:
    print("nulla")

str = "alma"
if str[0].isupper():
    print("nagybetűvel kezdődik")
else:
    print("nem nagybetűvel kezdődik")

str2 = "almafa"
str = "almaszár"
if str[0:5] == str2[0:5]:
    print("Az első 5 karakter azonos")
else:
    print("nem azonos első 5 karakter ")

