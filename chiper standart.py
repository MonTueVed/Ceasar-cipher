def encryption(alf, slide):
    print('Введи текст:')
    s = input()
    n = len(alf)//2
    if n == 32:
        id_low = 1072
        id_up = 1040
    elif n == 26:
        id_low = 97
        id_up = 65
    ans = ''
    for i in range(len(s)):
        sym = s[i]
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
    return ans

def decryption(alf, slide):
    print('Введи текст:')
    s = input()
    n = len(alf)//2
    if n == 32:
        id_low = 1072
        id_up = 1040
    elif n == 26:
        id_low = 97
        id_up = 65
    ans = ''
    for i in range(len(s)):
        sym = s[i]
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
    return ans

print('Что делаем? Шифруем? y-ШИФРУЕМ, n-ДЕШИФРУЕМ')
s1 = input()
print('Какой язык? rus-РУССКИЙ, eng-АНГЛИЙСКИЙ')
s2 = input()

if s2 == 'rus':
    chars = 'йфяцычувскамепинртгоьшлбщдюзжхэъ'
    chars += chars.upper()
if s2 == 'eng':
    chars = 'qazwsxedcrfvtgbyhnujmikolp'
    chars += chars.upper()
if s1 == 'y':
    print('какой сдвиг?')
    slide = int(input())
    print('Зашифрованный текст: ', encryption(chars, slide))
if s1 == 'n':
    print('какой сдвиг?')
    slide = int(input())
    print(decryption(chars, slide))

print('Press any key to close')
s = input()
