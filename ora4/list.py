my_list = [1, 2.5, "alma", False]
print("A lista hossza:", len(my_list))
print("A len() függvény visszatérési értékének típusa", type(len(my_list)))

print("A lista tartalmazza-e a 2.5 ös értéket:", 2.5 in my_list)
print("Az in operátor eredményének típusa:", type(2.5 in my_list))

print("A lista tartalmazza-e a 2 értéket:", 2 in my_list)
print("Az in operátor típusa:", type(2 in my_list))

try:
    print("A 2.5 érték pozíciója a listában:", my_list.index(2))
    print("Az index() metódus visszatérési értékének típusa:", type(my_list.index(2)))
except ValueError:
    print("hiba")

print("A lista 4. elemének a lekérdezése:", my_list[3])
print("A lista 1. értékének a típusa:", my_list[0])

my_list[2] = "körte"
print(my_list)

my_list.append(5)
my_list.extend([1, 2, 3])
print(my_list)



my_list.insert(0, "start")
print(my_list)



del(my_list[7])
print(my_list)

while 1 in my_list:
    my_list.remove(1)
print(my_list)


my_list = [4, 7, 1, 4.5, 7, 6]


my_list.sort()
print("A sort ()metódus visszatérési értékének típusát:", type(my_list.sort()))
