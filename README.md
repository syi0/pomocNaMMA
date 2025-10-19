def sito(n):
    pierwsze = [True]*n
    pierwsze[0] = pierwsze[1] = False
    for i in range (2, int(n**0.5)+1):
        if pierwsze[i]:
            for j in range (i*i, n, i):
                pierwsze[j] = False
    return [i for i, is_prime in enumerate(pierwsze) if is_prime]
    
print(sito(10))

def wstawianie(tab):
    for i in range(1, len(tab)):
        klucz = tab[i]
        j = i-1
        while j>=0 and tab[j]>klucz:
            tab[j+1] = tab[j]
            j -= 1
            tab[j+ 1] = klucz
tablica = [5,7,9,2,3,0]
wstawianie(tablica)
print(tablica)
            
def wybieranie(tab):
    n = len(tab)
    for i in range(n - 1):
        min_i = i
        for j in range(i + 1, n):
            if tab[j] < tab[min_i]:
                min_i = j
        tab[i], tab[min_i] = tab[min_i], tab[i]
    return tab

print(wybieranie([5, 2, 4, 1]))
        
def szybkie(tab):
    if len(tab) <= 1:
        return tab
    pivot = tab[len(tab)//2]
    mniejsze = [x for x in tab if x < pivot]
    rowne = [x for x in tab if x == pivot]
    wieksze = [x for x in tab if x > pivot]
    return szybkie(mniejsze) + rowne + szybkie(wieksze)

print(szybkie([7,3,5,6,2,1,0]))

def scalanie(tab):
    if len(tab) <= 1:
        return tab
    srodek = len(tab) // 2
    lewa = scalanie(tab[:srodek])
    prawa = scalanie(tab[srodek:])
    wynik = []
    i = j = 0
    while i < len(lewa) and j < len(prawa):
        if lewa[i] <= prawa[j]:
            wynik.append(lewa[i]); i += 1
        else:
            wynik.append(prawa[j]); j += 1
    wynik.extend(lewa[i:])
    wynik.extend(prawa[j:])
    return wynik

print(scalanie([8, 3, 5, 2, 9]))  
