list = []
a = int(input("adjon meg számokat"))
list.append(a)
try:
    while a != '':
        a = int(input("adjon meg számokat"))
        list.append(a)
except ValueError:
    print(list)

list = []
while len(list) == 0 or list[len(list)-1] !="":
    list.append(input())
list.remove("")
print(list)


