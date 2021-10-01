i = 1
while i <= 10:
    print(i, end= " ")
    i += 1
print()

for b in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(b, end= " ")
print()
for l in range(1, 11):
    print(l, end= " ")
print()


# 2. feladat


j = 1
while j <= 11:
    print(j, end= " ")
    j += 2
print()
k = 1
while k <= 6:
    print(2 * k - 1, end= " ")
    k += 1
print()
for o in range(1, 12, 2):
    print(o, end= " ")

print()

#3.feladat
a1 = 0
a2 = 1
print(a1, a2, end= " ")
p = 0
while p < 8:
    an = a1 + a2
    a1= a2
    a2 = an
    print(an, end=" ")
    p += 1

