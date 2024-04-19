import random
# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
lst = [i for i in range(1, 11)]

# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
for num in lst:
    if num % 2 == 0:
        print(num)

# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i = 1
while i <= 5:
    print(i)
    i += 1
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
dictionary = {"name": "John", "age": 30, "city": "New York"}
for key, val in dictionary.items():
    print(key, val)
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
lst = [[4, 5, 6], [1, 2, 3], [8, 9, 10], [-1, -2, -3]]
for i in range(len(lst)):
    print(lst[i])
    for j in range(len(lst[i])):
        print(lst[i][j], end=" ")
    print()

# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
l = [x for x in range(20, 31)]
for i in range(len(l)):
    print(l[i])

# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
for i, elem in enumerate(l):
    print(f"Indexul: {i}  - valoarea: {elem}")

# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
languages = ["C", "Java", "Python"]
year = [1972, 1995, 1991]
for lan, y in zip(languages, year):
    print(f"{lan} first appeared in {y}.")
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
l = []

for i in range(1, 11):
    l.append(i)

print(l)

# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
while l[0] <= 50:
    l = [x * 2 for x in l]
print(l)
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
l1 = []
x = 1
while x ** 2 <= 100:
    l1.append(x ** 2)
    x += 1
print(l1)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
for i in range(11):
    print(f"7 * {i} = {7 * i}")
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.

# CODUL TĂU VINE MAI JOS:
l2 = []

for i in range(1, 6):
    for j in range(1, 6):
        l2.append([i, j])

print(l2)

# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:
for sublist in l2:
    if sublist[0] < sublist[1]:
        print(sublist)

# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:
l3 = [random.randint(1, 12) for _ in range(5)]
print(l3)

i = 0
while i < len(l3):
    if l3[i] > 10:
        print(l3[i])
        break
    i += 1
if i == len(l3):
    print("Nu există valori mai mari decât 10.")


# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
n = int(input("Dimensiunea patratului: "))
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:
i = 1
while i <= 6:
    for j in range(1, i + 1):
        print(j, end= "")
    i += 1
    print()

# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
i = 1
while i <= 5:
    for j in range(5, i - 1, -1):
        print(j, end="")
    i += 1
    print()

# CODUL TĂU VINE MAI SUS:

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:
string = "abcdefg"
i = 0
while i < len(string):
    print(string[i:])
    i += 1


# CODUL TĂU VINE MAI SUS:

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:
plus = "+"
minus = "-"
lnt = 8
for i in range(lnt):
    if i % 2 == 0:
        for j in range(lnt):
            print(f"{plus}{minus}", end="")
    else:
        for j in range(lnt):
            print(f"{minus}{plus}", end="")
    print()

# CODUL TĂU VINE MAI SUS:

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:
n = 10
k = 1
for i in range(1, n):
    if i <= n // 2:
        for j in range(k, i + 1):
            print(3 ** j, end=" ")
        print()
    else:
        k += 1
        for j in range(k, (n//2) + 1):
            print(3 ** j, end=" ")
        print()

# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.
