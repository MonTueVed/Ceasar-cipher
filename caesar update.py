def encryption(alf):
    print('Введите текст:')
    str = input()
    n = len(alf)//2
    id_low = 97
    id_up = 65   
    itog = []
    mas = str.split(' ')
    for j in mas:
        ans = ''
        slide = len(j)
        if '!' in j:
            slide -= 1
        elif ',' in j:
            slide -= 1
        elif '.' in j:
            slide -= 1
        elif '?' in j:
            slide -= 1
        elif '"' in j:
            slide -= 2
        for i in j:
            sym = i
            if sym.islower():
                c = (ord(sym) + slide - id_low)
                c = c % n
                c += id_low
                ans += chr(c)
            elif sym.isupper():
                c = (ord(sym) + slide - id_up)
                c = c % n
                c += id_up
                ans += chr(c)
            else:
                ans += sym
        itog.append(ans)
         
    return itog

print('Это продвинутая версия шифра Цезаря. Шифрует текст так, что сдвиг равен длине слова. Только для латиницы...')
chars = 'qazwsxedcrfvtgbyhnujmikolp'
chars += chars.upper()
print(*encryption(chars), sep=' ')
print('Press any key to close')
s = input()
