def bubble_sort():
    elements = [7, 3, 1, 2, 5]
    size = len(elements)
 
    print('Before sorting:', elements)
 
    for i in range(size):
        for j in range(0, size-i-1):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                print(elements)
 
    print('After sorting:', elements)
    
def to_binary(liczba):
    if liczba == 0:
        return '0'
    pom = ''
    while liczba > 0:
        pom = str(liczba % 2) + pom
        liczba //= 2
    return pom

def to_decimal(dana):
    pom = 0
    for i in range(len(dana)):
        check = int(dana[-i-1])
        pom += check * 2 ** i
return def nwd(a, b):
    while b > 0:
        pom = a
        a = b
        b = pom % b
    return a

