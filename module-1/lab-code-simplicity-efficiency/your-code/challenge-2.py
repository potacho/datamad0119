"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
"""
def RandomStringGenerator(l=12, a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']):
    p = 0
    s = ''
    while p<l:
        import random
        s += random.choice(a)
        p += 1
    return s

def BatchStringGenerator(n, a=8, b=12):
    r = []
    for i in range(n):
        c = None
        if a < b:
            import random
            c = random.choice(range(a, b))
        elif a == b:
            c = a
        else:
            import sys
            sys.exit('Incorrect min and max string lengths. Try again.')
        r.append(RandomStringGenerator(c))
    return r

a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

print(BatchStringGenerator(int(n), int(a), int(b)))
"""

"""
Mejoras: 
1) Sacar los import y no duplicarlos (line 53,54)
2) Eliminar los valores default de las variables de las funciones
3) Cambiar la función random.choice() por random.sample() para eliminar el loop while
4) Usar la función .join() para convertir en un str la lista de listas con 1 valor alfanumérico que genera el random.sample()
5) Sacamos fuera del loop for la condición de si b es menor que a que despliega el error.
6) Convertimos la parte que genera la condición para crear el valor c en una list comprehension (line 62)
7) Convertimos el loop for que genera la lista que retorna la función en una list comprehension (line 63)
"""



import random as rd
import sys     

def RandomStringGenerator(l, a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']):
    return ''.join(rd.sample(a, l))

def BatchStringGenerator(n,a,b):
    if a > b: 
         sys.exit('Incorrect min and max string lengths. Try again.')
    c = rd.choice(range(a,b)) if a < b else b
    return [RandomStringGenerator(c) for _ in range(n)]

a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

print(BatchStringGenerator(int(n), int(a), int(b)))
