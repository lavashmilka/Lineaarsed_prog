# #Ulesanne 1
# try:
#     arv=input("Sisesta arv:")
#     if arv.isnumeric():
#         arv=int(arv)
#         if arv>0:
#             if arv%2==0:
#                 print("Paaris arv")
#             else:
#                  print("Paaritu")
#         else:
#             print("Negatiivne arv")
# except:
#     print("Kirjuta numbreid")
    
# #Ulesanne 2
# try:
#    nurk1=float(input("Esimene nurk"))
#    nurk2=float(input("Teine nurk"))
#    nurk3=float(input("Kolmas nurk"))
#    if nurk1>0 and nurk2>0 and nurk3>0:
#        print("Nurgad on positiivsed")
#        if nurk1+nurk2+nurk3==180:
#            print("See on kolmnur")
#            if nurk1==nurk2 and nurk2==nurk3:
#                print("Võrgkülgne kolmnurk")
#            elif nurk1==nurk2 or nurk2==nurk3 or nurk1==nurk3:
#                print("Võrdvaarne kolmnurk")
#            else:
#                print("Erikülgne kolmnurk")
#        else:
#             print("See ei ole kolmnurk")
#    else:
#         print("Negatiivsed nurgad ei soobi")
# except:
#     print("Sisesta ujukomaarvud")

# #Ulesanne 3
# try:
#     soov=input("Kas tahad dekodeerida?").lower()
#     if soov=="jah":
#        try:
#            nr=int(input("Päeva number: "))
#            if nr in range(1,8):
#                if nr==1:
#                    print("Esmaspäev")
#                elif nr==2:
#                    print("Teisipäev")
#                elif nr==3:
#                    print("Kolmapäev")
#                elif nr==4:
#                    print("Neljapäev")
#                elif nr==5:
#                    print("Reede")
#                elif nr==6:
#                    print("Laupäev")
#                elif nr==7:
#                    print("Pühapäev")
#        except:
#             print("Numbrit vahemikust 1-7")
#     else:
#         print("ok")
# except:
#     print("Mul on vaja vastus Jah või Ei")
    
# #Ulesanne 4
# päev=int(input("Sünnipäev"))
# kuu=int(input("Sünnikuu"))
# if (kuu==3 and päev>=21) or (kuu==4 and päev<=19):
#        märk="Jäär"
# elif (kuu==4 and päev>=20) or (kuu==5 and päev<=20):
#        märk="Sõnn"
# elif (kuu==5 and päev>=21) or (kuu==6 and päev<=21):
#        märk="Kaksikud"
# elif (kuu==6 and päev>=22) or (kuu==7 and päev<=22):
#        märk="Vähk"
# elif (kuu==7 and päev>=23) or (kuu==8 and päev<=22):
#        märk="Lõvi"
# elif (kuu==8 and päev>=23) or (kuu==9 and päev<=22):   
#        märk="Neitsi"
# elif (kuu==9 and päev>=23) or (kuu==10 and päev<=22):
#        märk="Kaalud"
# elif (kuu==10 and päev>=23) or (kuu==11 and päev<=21):
#        märk="Skorpion"
# elif (kuu==11 and päev>=22) or (kuu==12 and päev<=21):
#        märk="Ambur"
# elif (kuu==12 and päev>=22) or (kuu==1 and päev<=19):
#        märk="Kaljukits"
# elif (kuu==1 and päev>=20) or (kuu==2 and päev<=18):
#        märk="Veevalaja"
# elif (kuu==2 and päev>=19) or (kuu==3 and päev<=20):
#        märk="Kaalad"
       
# print(f"{märk}")

# #Ulesanne 5
# user_input = input("Введите число: ")
# try:
#     number = float(user_input)  # Пробуем преобразовать в число
#     if number==int(number):  # Если число целое
#         print(f"Целое число: {int(number)}, 50% от него: {int(number) * 0.5}")
#     else:  # Если число дробное
#         print(f"Дробное число: {number}, 70% от него: {number * 0.7}")
# except ValueError:  # Если ошибка преобразования, значит это текст
#     print(f"Вы ввели текст: {user_input}")

# #Ulesanne 6
# answer = input("Хотите решить квадратное уравнение? (да/нет): ")
# if answer == "да":
#     a = float(input("Введите коэффициент a: "))
#     b = float(input("Введите коэффициент b: "))
#     c = float(input("Введите коэффициент c: "))

#     # Вычисляем дискриминант
#     D = b**2 - 4*a*c
#     print(f"Дискриминант D = {D:.2f}")

#     if D > 0:
#         x1 = (-b + D**0.5) / (2 * a)
#         x2 = (-b - D**0.5) / (2 * a)
#         print(f"Уравнение имеет два корня: x1 = {x1:.2f}, x2 = {x2:.2f}")
#     elif D == 0:
#         x = -b / (2 * a)
#         print(f"Уравнение имеет один корень: x = {x:.2f}")
#     else:
#         print("Уравнение не имеет действительных корней.")

# else:
#     print("До свидания!")


# from random import choice

# word = 'ABCDEFG'
# print(choice(word)) # => C

# fruit = ['apple', 'banana', 'cherry', 'watermelon']
# print(choice(fruit)) # => cherry


from random import *
sõnad=["Võilill","Nartsiss","Rukkilill","Lill","Liilia"]
salasõna=choice(sõnad)
k=len(salasõna)
katsed=6
while katsed>0:
    print("_ "*k)
    print(f"On jäänud {katsed} katset")
    katsed-=1
    sõna=input("Sisesta oma variant: ").capitalize()
    if len(sõna)!=k:
        print(f"Sõna peab olema {k} tähte pikk!")
        continue
    if sõna==salasõna:
     print("Hurraa!!")
     break
     tulemus=""
     i=0
     while i<k:
         täht=sõna[i]
         if täht==salasõna[i]:
             tulemus+=f"[{täht}]"
         elif täht in salasõna:
             tulemus+=f"({täht})"
         else:
             tulemus+=f" {täht} "
             i+=1
             print(tulemus)
             katsed-=1
             if katsed==0:
                 print(f"Kahjuks kaotasid! Õige sõna oli: {salasõna}")


