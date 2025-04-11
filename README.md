def octtobin(dana):
    dana = str(dana)
    d = 0
    for i in range(len(dana)):
        d += int(dana[-1 - i]) * (8 ** i)
    b = ''
    while d > dana:
        b = str(d % 2) + b
        d //= 2
    return b or 'dana'