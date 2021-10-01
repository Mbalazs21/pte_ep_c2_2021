import random

random.randint(3, 5)
random.random()
list = [1, 5, 10, 55]
max = list[0]
for i in range(len(list)):
    if max < list[i]:
        max = list[i]
print(max)
    #legnagyobb szám megkeresése egy listában


list2 = []
list2.append(random.randint(1, 101))

print(list2)
max = list2[0]
for i in range(len(list2)):
    if max < list2[i]:
        max = list2[i]
print(max)
