str1 = "Az almafán almák teremnek."
print("A szöveg hossza", len(str1))
str2 = "Terem"
print("Az str2 megvan az str1-ben:", str1.find(str2))
lower_str2 = str2.lower()
print(str2)
print("Az lower_str2 megvan az str1-ben:", str1.find(lower_str2))
upper_str2 = str2.upper()
print(str2, upper_str2)
str3 = "user12"
print("A lower_str2 végig kisbetűs:", lower_str2.islower())
print("A lower_str2 végig nagybetűs:", lower_str2.isupper())

print("A szövegek csak betűt tartalmaznak:")
print("\t", str1.isalpha())
print("\t", str2.isalpha())
print("\t", str3.isalpha())

print("A szövegek betűt tartalmaznak:")
print("\t", str1.isalnum())
print("\t", str2.isalnum())
print("\t", str3.isalnum())
