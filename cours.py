# review:
# cree un fonction appelée greet
# def greet(name):
#     print(f"bonjour {name}!")
#     print("bien venu au jour  9")
#     print("on va revise les fonction")
# ecrire  trois lignre d'instruction d'impression
# greet("balouka")
# appele la fonction greet et run  le code

# une fonction qui permet de faire plusieur entre
    #fonction appeler entre
# value = input("entre le nom : ")
# def input_value(name) :
#     print(f"bonjour {name}")
# input_value(value)
# import  math
#
# longeur = int(input("entre la longeur : "))
# largeur =  int(input("entrer la larguer :"))
# cover = 5
#
# def calcul(longeur, largeur, cover) :
#     suface = longeur * largeur
#     number_cans =math.ceil( suface / cover)
#     print(f'le nombre de pot de painture a utiliser est de : {number_cans}')
# calcul(longeur, largeur, cover)

# verifier si un nombre est premier
n = int(input("antre un nombre: "))

def premier_check(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("it is a prime number")
    else:
        print ("it is not a prime number")
premier_check(number= n)