# Aceasta este sarcina pentru lecția despre polimorfism, metode speciale și compoziție a claselor în Python.

from sigmoid_check.python_odyssey.lesson_15.lesson_15 import Lesson15
from functools import reduce

# Această temă pentru acasă necesită instalarea librăriei `sigmoid_check` cu versiunea cel puțin 0.0.8
# Pentru a instala această librărie, rulați următorul cod în terminal:
# pip install sigmoid_check==0.0.8

# VERIFICATION PROCESS
session = Lesson15()
# VERIFICATION PROCESS

"""
ISTORIA DIN SPATE
După toată munca depusă pentru proiectul de la DARWIN și TechSolutions, ai primit o ofertă de la cei de la Microsoft, 
aceștia lucrează la crearea unui algoritm care le va permite procesarea a unor cantități mari de date.
"""

"""
Primul pas în crearea algoritmului este implementarea unor containere de date care va permite stocarea și 
manipularea datelor într-un mod mai simplu
și eficient. Trebuie să creezi o clasă nouă `DataContainer`. 
Pentru a manipula datele vom folosi metodele speciale ale clasei.

Clasa va primi ca parametru o listă de numere integer.
- __init__ initializează clasa cu lista de numere.
- __str__ va returna lista de numere sub formă de string.
- __len__ va returna numărul de elemente din listă.
- __getitem__ va permite accesarea elementelor din listă folosind indexul (e.g., container[0]).
- __setitem__ va permite modificarea elementelor din listă folosind indexul (e.g., container[0] = 5).
- __add__ va permite combinarea a două instanțe de `DataContainer` într-o singură instanță.
"""

# CODUL TĂU VINE MAI JOS:
class DataContainer:
    def __init__(self, number_list: list):
        self.number_list = number_list

    def __str__(self):
        return f"{self.number_list}"
    
    def __len__(self):
        return len(self.number_list)
    
    def __getitem__(self, index):
        return self.number_list[index]
    
    def __setitem__(self, index, valoare):
        self.number_list[index] = valoare

    def __add__(self, other_list):
        return self.number_list + other_list.number_list
    
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_1(DataContainer))
# VERIFICATION PROCESS

"""
Acum avem nevoie de o modalitate de a calcula suma și produsul containerului de date. 
Pentru aceasta creează două clase noi care vor moșteni clasa `DataContainer`.
- `SumaContainer` va calcula suma elementelor din listă.
- `ProdusContainer` va calcula produsul elementelor din listă.
Ambele clase vor avea metoda `calculate` care va returna suma sau produsul elementelor.
"""

# CODUL TĂU VINE MAI JOS:
class SumaContainer(DataContainer):
    def calculate(l: DataContainer):
        return sum(l)
    
class ProdusContainer(DataContainer):
    def calculate(l: DataContainer):
        return reduce((lambda x, y: x * y), l)

# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_2(SumaContainer, ProdusContainer, DataContainer))
# VERIFICATION PROCESS

"""
Pentru ca instrumentul pe care îl folosim să fie complet vom mai avea nevoie de careva adiții.
Creează o clasă `DataAnalysis` care va primi ca input o listă de obiecte de tipul `DataContainer`.
- __init__ va inițializa clasa cu lista de obiecte.
- `add_container` va permite adăugarea unui nou container în listă.
- `__call__` va returna o listă cu valorile maxime ale fiecărui container.
"""

# CODUL TĂU VINE MAI JOS:
class DataAnalysis:
    def __init__(self, object_list = []):
        self.object_list = object_list

    def add_container(self, obj: DataContainer):
        self.object_list.append(obj)

    def __call__(self):
        max_values_list =[max(container.number_list) for container in self.object_list] 
        return max_values_list


# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_3(DataAnalysis, DataContainer))
# VERIFICATION PROCESS

"""
Pe lângă elementul de analiză a datelor, Microsoft a mai cerut și un element de statistică.
Creează o clasă `DataStatistics` care va primi ca input o listă de obiecte de tipul `DataContainer`.
- __init__ va inițializa clasa cu lista de obiecte.
- `add_container` va permite adăugarea unui nou container în listă.
- `mean` va returna media aritmetică a elementelor din toate containerele.
- `median` va returna mediana elementelor din toate containerele.
- `min` va returna valoarea minimă din toate containerele.
- `sum` va returna suma elementelor din toate containerele.
"""

# CODUL TĂU VINE MAI JOS:
class DataStatistics:
    def __init__(self, object_list=[]):
        self.object_list = object_list

    def add_container(self, obj: DataContainer):
        self.object_list.append(obj)

    def mean(self):
        sum = 0
        number = 0
        for lst in self.object_list:
            sum += SumaContainer.calculate(lst)
            number += len(lst)
        return sum / number
        
    def median(self):
        all = [number for lst in self.object_list for number in lst.number_list]
        if len(all) % 2 != 0:
            return all[len(all)//2]
        return (all[len(all)//2] + all[len(all)//2 - 1]) / 2
    
    def min(self):
        all = [number for lst in self.object_list for number in lst.number_list]
        return min(all)
    
    def sum(self):
        sum = 0
        for lst in self.object_list:
            sum += SumaContainer.calculate(lst)
        return sum


# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_4(DataStatistics, DataContainer))
# VERIFICATION PROCESS

"""
Iar pe ultima sută de metri, Microsoft a cerut și un element de filtrare a datelor.

Creează o clasă `DataFilter` care va primi ca input o listă de obiecte de tipul `DataContainer`.
- __init__ va inițializa clasa cu lista de obiecte.
- `add_container` va permite adăugarea unui nou container în listă.
- `filter_zeros` va returna o listă cu toate elementele care sunt diferite de 0.
- `filter_negatives` va returna o listă cu toate elementele care sunt mai mari sau egale cu 0.
- `filter_positives` va returna o listă cu toate elementele care sunt mai mici sau egale cu 0.
- `filter_under_mean` va returna o listă cu toate elementele care sunt mai mari decât media aritmetică a 
tuturor elementelor calculate cu metoda `mean` din clasa `DataStatistics`.
"""

# CODUL TĂU VINE MAI JOS:
class DataFilter:
    def __init__(self, object_list=[]):
        self.object_list = object_list

    def add_container(self, obj):
        self.object_list.append(obj)
    
    def return_all(self):
        all = [number for lst in self.object_list for number in lst.number_list]
        return all

    def filter_zeros(self):
        all = self.return_all()
        return [number for number in all if number != 0]
    
    def filter_negatives(self):
        all = self.return_all()
        return [number for number in all if number < 0]
    
    def filter_positives(self):
        all = self.return_all()
        return [number for number in all if number >= 0]
    
    def filter_under_mean(self):
        all = self.return_all()
        data_stat = DataStatistics()
        data_stat.add_container(all)
        return list(filter(lambda x: x > data_stat.mean(), all))

# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_5(DataFilter, DataStatistics, DataContainer))
print(session.get_completion_percentage())
# VERIFICATION PROCESS