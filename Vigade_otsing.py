from math import * #Правильный импорт модуля
print("Ruudu karakteristikud")
try:
    a=float(input('Sisesta ruudu külje pikkus => ')) #Преобразование ввода в число с плавающей запятой
    if a>0:
        S=a**2
        print("Ruudu pindala", S)
        P=4*a
        print("Ruudu ümbermõõt", P) 
        di=a*sqrt(2) #Использование sqrt
        print("Ruudu diagonaal", round(di,2))
    else:
        print("külg ei saa olla 0 või vähem.")
except:
    print("Viga! sisesta ainult täisarvud!")
    

print("Ristküliku karakteristikud")
try:
    b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #Преобразование ввода в число с плавающей запятой
    c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #Преобразование ввода в число с плавающей запятой
    if b>0 and c>0:
        S=b*c
        print("Ristküliku pindala", S) #Ошибка с кавычками
        P=2*(b+c) #Правильная формула для периметра
        print("Ristküliku ümbermõõt", P)
        di=sqrt(b**2+c**2) #Ошибка в формуле
        print("Ristküliku diagonaal", round(di))
    else:
        print("b ja c ei saa olla 0 või vähem.")
except:
    print("Viga! sisesta ainult täisarvud!")


print("Ringi karakteristikud")
try:
    r=float(input("Sisesta ringi raadiusi pikkus => ")) #Преобразуем ввод в число с плавающей запятой
    if r>0:
        d=2*r #Формула диаметра окружности, добавлен знак умножить
        print("Ringi läbimõõt", d)
        S=pi*r**2 #Формула площади окружности, после pi не нужны скобки
        print("Ringi pindala", round(S))
        C=2*pi*r #Формула длины окружности, после pi не нужны скобки
        print("Ringjoone pikkus", round(C))
    else:
        print("r ei saa olla 0 või vähem.")
except:
    print("Viga! sisesta ainult täisarvud!")






