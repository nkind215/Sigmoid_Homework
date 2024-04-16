# Aceasta este sarcina pentru lecția 7 legată de comentarii, continuarea liniilor și instrucțiuni condiționale.

# Creați o variabilă numită number și atribuiți-i o valoare întreagă.

# CODUL TĂU VINE MAI JOS:
number = 8
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este pozitiv și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number > 0:
    print("Numarul este pozitiv.")
else: 
    print("Numarul este negativ sau egal cu zero.")

# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este par și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number % 2 == 0:
    print("Numarul este par.")

# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este impar și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number % 2 != 0:
    print("Numarul este impar.")

# CODUL TĂU VINE MAI SUS:

# Creați o variabilă text și atribuiți-i un șir de caractere.

# CODUL TĂU VINE MAI JOS:
text = "Aceasta este o linie de cod in Python sau Java."

# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Python" in text:
    print("Cuvantul 'Python' se regaseste in variabila 'text'.")
else:
    print("Cuvantul 'Python' nu se regaseste in variabila 'text'.")

# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Java" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Java" in text:
    print("Textul contine cuvantul 'Java'.")
else:
    print("Textul nu contine cuvantul 'Java'.")

# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.
# în cazul în care nu conține, verificați dacă conține cuvântul "Java" și afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Python" in text:
    print("Textul contine cuvantul 'Python'. Cuvantul 'Java' nu a fost verificat.")
elif "Java" in text:
    print("Textul contine cuvantul 'Java', insa nu si cuvantul 'Python'.")
else:
    print("Textul nu contine niciunul dintre cuvintele 'Java' sau 'Python'.")

# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și cuvântul "Java" și afișați un mesaj corespunzător.
# În cazul în care conține doar unul dintre ele, afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Python" in text and "Java" in text:
    print("Cuvintele 'Python' si 'Java' se regasesc in variabila 'text'.")
elif "Python" in text or 'Java' in text:
    print("Textul contine doar unul dintre cuvintele 'Python' sau 'Java'.")
else:
    print("Textul nu contine niciunul dintre cuvintele 'Java' sau 'Python'.")

# CODUL TĂU VINE MAI SUS:

# Extrageți de la tastatură utilizând funcția input un număr de la 1 la 5 și atribuiți-l variabilei number.
# Folosiți o instrucțiune condițională pentru a printa un mesaj corespunzător în funcție de numărul introdus.
# pentru 1 - printați "Unu"
# pentru 2 - printați "Doi"
# pentru 3 - printați "Trei"
# pentru 4 - printați "Patru"
# pentru 5 - printați "Cinci"

# CODUL TĂU VINE MAI JOS:
number = input("Introduceti un numar intreg de la 1 la 5: ")
if number == "1":
    print("Unu")
elif number == "2":
    print("Doi")
elif number == "3":
    print("Trei")
elif number == "4":
    print("Patru")
elif number == "5":
    print("Cinci")

# CODUL TĂU VINE MAI SUS:


