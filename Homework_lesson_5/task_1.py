# Aceasta este prima ta sarcină legată de liste

# Creează o listă goală numită `numbers`

# CODUL TĂU VINE MAI JOS:
numbers = [10, 17, 7, 4, 13, 1]

# CODUL TĂU VINE MAI SUS:

# Acum adaugă numerele de la 1 la 5 în lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers = numbers + list(range(1,6))

# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)

# CODUL TĂU VINE MAI SUS:

# Acum adaugă numărul 6 la lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.append(6)

# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)

# CODUL TĂU VINE MAI SUS:

# Acum șterge numărul 3 din lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.remove(3)

# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)

# CODUL TĂU VINE MAI SUS:

# Acum sortează lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.sort()

# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)

# CODUL TĂU VINE MAI SUS:

# Acum inversează lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.reverse()

# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)

# CODUL TĂU VINE MAI SUS:

# Acum afișează lungimea listei `numbers`

# CODUL TĂU VINE MAI JOS:
print(len(numbers))

# CODUL TĂU VINE MAI SUS:

# Acum selectează primele două elemente din lista `numbers` și afișează-le

# CODUL TĂU VINE MAI JOS:
first = numbers[0]
second = numbers[1]
print(first, second)
#print("Primele doua elemente din lista sunt: ", numbers[:2][0], numbers[:2][1])

# CODUL TĂU VINE MAI SUS:

# Acum selectează ultimele trei elemente din lista `numbers` și afișează-le

# CODUL TĂU VINE MAI JOS:
print("::",numbers[-3])
print(numbers[-2])
print(numbers[-1])

# CODUL TĂU VINE MAI SUS:

# Acum adaugă numărul 3 la poziția 2 în lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.insert(2, 3)  # in cazul in care pozitia e interpretata drept index

# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)

# CODUL TĂU VINE MAI SUS:

# Creează o listă goală numită `numbers2`

# CODUL TĂU VINE MAI JOS:
numbers2 = []

# CODUL TĂU VINE MAI SUS:

# Acum adaugă numerele de la 6 la 10 în lista `numbers2`

# CODUL TĂU VINE MAI JOS:
numbers2 = [6, 10]

# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers2`

# CODUL TĂU VINE MAI JOS:
print(numbers2)

# CODUL TĂU VINE MAI SUS:

# Acum adaugă lista `numbers2` la lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers = numbers + numbers2

# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)

# CODUL TĂU VINE MAI SUS:

# Acum transformă lista `numbers` într-un string și afișează-l

# CODUL TĂU VINE MAI JOS:
string_list = str(numbers)
print(string_list)

# CODUL TĂU VINE MAI SUS:

# Asta a fost tot, ai terminat prima ta sarcină legată de liste
