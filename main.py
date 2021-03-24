""" Premier Programme
    en Python
    Debutant"""

# Erreurs et gestions des exceptions

# nom = input("Quel est votre nom?")
# age = input("Quel est votre age?")

# try:
#     age_prochain = int(age) + 1
# except:
#     print("ERREUR: Vous devez rentrer un nombre pour l'age")
# else:
#     print("Hello! " + nom + ", tu as " + str(age) + " ans.")
#     print("L'an prochain tu auras " + str(age_prochain) + " ans.")

# --------------------------------------------------------------------

# Boucle while: "tant que"

# n = 0
# print(n)
# n = 1
# print(n)
# n = n +1
# print(n)

# print("Début de la boucle.")

# while n < 10 :
#     print("Valeur de n: " + str(n))
#     n = n + 1

# print("Fin de la boucle.")

# --------------------------------------------------------------------
# Boucle doit etre correct

# mtp = ""

# while not mtp == "Gwen":
#     mtp = input("Quel est le mot de passe ?")

# print("Mot de passe correct!")

# --------------------------------------------------------------------

# Améliorer le programme avec la boucle

# nom = input("Quel est votre nom?")
# age = 0

# while age == 0:
#     age_str = input("Quel est votre age?")
#     try:
#         age = int(age_str)
#     except:
#         print("ERREUR: Vous devez rentrer un nombre pour l'age")

# # fin de la boucle et affiche ->
# print("Hello! " + nom + ", tu as " + (age_str) + " ans.")
# print("L'an prochain tu auras " + str(age + 1) + " ans.")

# --------------------------------------------------------------------

# Excercie 1 - Faire Fonction de nom et age

# # Demander le nom
# nom = ""

# while nom == "":
#     nom = input("Quel est votre nom?")

# # Demander l'age
# age = 0

# while age == 0:
#     age_str = input("Quel est votre age?")
#     try:
#         age = int(age_str)
#     except:
#         print("ERREUR: Vous devez rentrer un nombre pour l'age")

# # Afficher les résultats
# print("Hello! " + nom + ", tu as " + (age_str) + " ans.")
# print("L'an prochain tu auras " + str(age + 1) + " ans.")

# --------------------------------------------------------------------

# Exercice 1 - Amélioration de notre programme: Fonction

# def demander_nom():
#     reponse_nom = ""

#     while reponse_nom == "":
#         reponse_nom = input("Quel est votre nom?")
#     return reponse_nom


# def demander_age():
#     # Demander l'age
#     age_int = 0

#     while age_int == 0:
#         age_str = input("Quel est votre age?")
#         try:
#             age_int = int(age_str)
#         except:
#             print("ERREUR: Vous devez rentrer un nombre pour l'age")
#     return age_int

# # Demander le nom
# nom = demander_nom()

# # Demander age
# age = demander_age()

# # Afficher les résultats
# print("Hello! " + nom + ", tu as " + str(age) + " ans.")
# print("L'an prochain tu auras " + str(age + 1) + " ans.")

# # --------------------------------------------------------------------

# # Variable Global  d'une fonction mais pas indépendant donc pas judicieux

# def demander_nom():
#     reponse_nom = ""

#     while reponse_nom == "":
#         reponse_nom = input("Quel est votre nom?")
#     return reponse_nom

# age = 0

# def demander_age():
#     # Demander l'age
#     global age
#     while age == 0:
#         age_str = input("Quel est votre age?")
#         try:
#             age = int(age_str)
#         except:
#             print("ERREUR: Vous devez rentrer un nombre pour l'age")

# # Demander le nom
# nom = demander_nom()

# # Demander age
# demander_age()

# # Afficher les résultats
# print("Hello! " + nom + ", tu as " + str(age) + " ans.")
# print("L'an prochain tu auras " + str(age + 1) + " ans.")

# --------------------------------------------------------------------

# # Parametre (ou argument) de la fonction

# def demander_nom():
#     reponse_nom = ""

#     while reponse_nom == "":
#         reponse_nom = input("Quel est votre nom?")
#     return reponse_nom


# def demander_age(nom_personne):
#     # Demander l'age
#     age_int = 0

#     while age_int == 0:
#         age_str = input(nom_personne + "Quel est votre age?")
#         try:
#             age_int = int(age_str)
#         except:
#             print("ERREUR: Vous devez rentrer un nombre pour l'age")
#     return age_int

# # Demander le nom pour person 1 et person 2
# nom1 = demander_nom()
# nom2 = demander_nom()

# # Demander age pour nom 1 et nom 2
# age1 = demander_age(nom1)
# age2 = demander_age(nom2)

# # Afficher les résultats de nom 1 avec age 1
# print("Hello! " + nom1 + ", tu as " + str(age1) + " ans.")
# print("L'an prochain " + nom1 + ", tu auras " + str(age1 + 1) + " ans.")

# # Afficher les résultats de nom 2 avec age 2
# print("Hello! " + nom2 + ", tu as " + str(age2) + " ans.")
# print("L'an prochain " + nom2 + ", tu auras " + str(age2 + 1) + " ans.")

# --------------------------------------------------------------------

# Exercice 3 - Fonction et paramétres

# afficher_information_personne
# Paramètres : nom, age,

# def afficher_information_personne(nom, age):
#     print("Hello! " + nom + ", tu as " + str(age) + " ans.")
#     print("L'an prochain " + nom + ", tu auras " + str(age + 1) + " ans.")

# def demander_nom():
#     reponse_nom = ""

#     while reponse_nom == "":
#         reponse_nom = input("Quel est votre nom?")
#     return reponse_nom


# def demander_age(nom_personne):
#     # Demander l'age
#     age_int = 0

#     while age_int == 0:
#         age_str = input(nom_personne + "Quel est votre age?")
#         try:
#             age_int = int(age_str)
#         except:
#             print("ERREUR: Vous devez rentrer un nombre pour l'age")
#     return age_int

# # Demander le nom pour person 1 et person 2
# nom1 = demander_nom()
# nom2 = demander_nom()

# # Demander age pour nom 1 et nom 2
# age1 = demander_age(nom1)
# age2 = demander_age(nom2)

# afficher_information_personne(nom1, age1)
# afficher_information_personne(nom2, age2)

# --------------------------------------------------------------------

# # Condition ET / OU

# # age == 17 -> Vous êtes presque majeur
# # age == 18 -> Vous êtes tout juste : Félicitation
# # elif -> else if
# # age > 60 : Vous êtes sénior
# # age < 10 : Vous êtes un enfant
# # adolescent si age >= 12 et age < 18
# # age >= 12 and age < 18
# # Bebe si age == 1 ou age == 2

# def afficher_information_personne(nom, age):
#     print()
#     print("Hello! " + nom + ", tu as " + str(age) + " ans.")
#     print("L'an prochain " + nom + ", tu auras " + str(age + 1) + " ans.")

# # == égal
# # < inférieur
# # <= inférieur ou égal
# # > supérieur
# # >= supérieur ou égal
# # True /False (Boolean)

#     if age == 17:
#         print("Vous êtes presque majeur") 
#     elif age == 1 or age == 2:
#         print("Vous êtes un baby")
#     elif age < 10:
#         print("Vous êtes un enfant")
#     elif 12 <= age < 18:
#         print("Vous êtes un adolescent")
#     elif age == 18:
#         print("Vous êtes tout juste : Félicitation")
#     elif age > 60:
#         print("Vous êtes sénior")
#     elif age >= 18:
#         print("Vous êtes majeur")
#     else:
#         print("Vous êtes mineur")

# def demander_nom():
#     reponse_nom = ""

#     while reponse_nom == "":
#         reponse_nom = input("Quel est votre nom?")
#     return reponse_nom


# def demander_age(nom_personne):
#     # Demander l'age
#     age_int = 0

#     while age_int == 0:
#         age_str = input(nom_personne + "Quel est votre age?")
#         try:
#             age_int = int(age_str)
#         except:
#             print("ERREUR: Vous devez rentrer un nombre pour l'age")
#     return age_int

# # Demander le nom pour person 1
# nom1 = demander_nom()

# # Demander age pour nom 1
# age1 = demander_age(nom1)

# afficher_information_personne(nom1, age1)

# --------------------------------------------------------------------

# # Boucle "for"

# # age == 17 -> Vous êtes presque majeur
# # age == 18 -> Vous êtes tout juste : Félicitation
# # elif -> else if
# # age > 60 : Vous êtes sénior
# # age < 10 : Vous êtes un enfant
# # adolescent si age >= 12 et age < 18
# # age >= 12 and age < 18
# # Bebe si age == 1 ou age == 2

# def afficher_information_personne(nom, age):
#     print()
#     print("Hello! " + nom + ", tu as " + str(age) + " ans.")
#     print("L'an prochain " + nom + ", tu auras " + str(age + 1) + " ans.")

# # == égal
# # < inférieur
# # <= inférieur ou égal
# # > supérieur
# # >= supérieur ou égal
# # True /False (Boolean)

#     if age == 17:
#         print("Vous êtes presque majeur") 
#     elif age == 1 or age == 2:
#         print("Vous êtes un baby")
#     elif age < 10:
#         print("Vous êtes un enfant")
#     elif 12 <= age < 18:
#         print("Vous êtes un adolescent")
#     elif age == 18:
#         print("Vous êtes tout juste : Félicitation")
#     elif age > 60:
#         print("Vous êtes sénior")
#     elif age >= 18:
#         print("Vous êtes majeur")
#     else:
#         print("Vous êtes mineur")

# def demander_nom():
#     reponse_nom = ""

#     while reponse_nom == "":
#         reponse_nom = input("Quel est votre nom?")
#     return reponse_nom


# def demander_age(nom_personne):
#     # Demander l'age
#     age_int = 0

#     while age_int == 0:
#         age_str = input(nom_personne + "Quel est votre age?")
#         try:
#             age_int = int(age_str)
#         except:
#             print("ERREUR: Vous devez rentrer un nombre pour l'age")
#     return age_int

# # Demander le nom pour person 1
# nom1 = demander_nom()

# # Demander age pour nom 1
# age1 = demander_age(nom1)

# afficher_information_personne(nom1, age1)

# la boucle for
# for i in range(0, 3):
#     nom = "personne" + str(i + 1)
#     age = demander_age(nom)
#     afficher_information_personne(nom, age)

# ou

# NB_PERSONNES = 3

# NB_PERSONNES 

# # la boucle for
# for i in range(0, NB_PERSONNES):
#     nom = "personne" + str(i + 1)
#     age = demander_age(nom)
#     afficher_information_personne(nom, age)

# # --------------------------------------------------------------------

# # Nombre à virgule et paramétres optionnel 

# # age == 17 -> Vous êtes presque majeur
# # age == 18 -> Vous êtes tout juste : Félicitation
# # elif -> else if
# # age > 60 : Vous êtes sénior
# # age < 10 : Vous êtes un enfant
# # adolescent si age >= 12 et age < 18
# # age >= 12 and age < 18
# # Bebe si age == 1 ou age == 2

# def afficher_information_personne(nom, age, taille=0):
#     print()
#     print("Hello! " + nom + ", tu as " + str(age) + " ans.")
#     print("L'an prochain " + nom + ", tu auras " + str(age + 1) + " ans.")

# # == égal
# # < inférieur
# # <= inférieur ou égal
# # > supérieur
# # >= supérieur ou égal
# # True /False (Boolean)

#     if age == 17:
#         print("Vous êtes presque majeur") 
#     elif age == 1 or age == 2:
#         print("Vous êtes un baby")
#     elif age < 10:
#         print("Vous êtes un enfant")
#     elif 12 <= age < 18:
#         print("Vous êtes un adolescent")
#     elif age == 18:
#         print("Vous êtes tout juste : Félicitation")
#     elif age > 60:
#         print("Vous êtes sénior")
#     elif age >= 18:
#         print("Vous êtes majeur")
#     else:
#         print("Vous êtes mineur")

#     # Afficher la taille
#     #taille = 1.75 -> float
#     if not taille == 0:
#         print("Votre taille : " + str(taille) + " m")


# def demander_nom():
#     reponse_nom = ""

#     while reponse_nom == "":
#         reponse_nom = input("Quel est votre nom?")
#     return reponse_nom


# def demander_age(nom_personne):
#     # Demander l'age
#     age_int = 0

#     while age_int == 0:
#         age_str = input(nom_personne + "Quel est votre age?")
#         try:
#             age_int = int(age_str)
#         except:
#             print("ERREUR: Vous devez rentrer un nombre pour l'age")
#     return age_int

# # # Demander le nom pour person 1
# # nom1 = demander_nom()

# # # Demander age pour nom 1
# # age1 = demander_age(nom1)

# # afficher_information_personne(nom1, age1)

# # la boucle for
# # for i in range(0, 3):
# #     nom = "personne" + str(i + 1)
# #     age = demander_age(nom)
# #     afficher_information_personne(nom, age)

# # ou

# NB_PERSONNES = 1

# NB_PERSONNES 

# # la boucle for
# for i in range(0, NB_PERSONNES):
#     nom = "personne" + str(i + 1) #car index commence à 0
#     age = demander_age(nom)
#     afficher_information_personne(nom, age)

# --------------------------------------------------------------------

# Les chaines formatées

# age == 17 -> Vous êtes presque majeur
# age == 18 -> Vous êtes tout juste : Félicitation
# elif -> else if
# age > 60 : Vous êtes sénior
# age < 10 : Vous êtes un enfant
# adolescent si age >= 12 et age < 18
# age >= 12 and age < 18
# Bebe si age == 1 ou age == 2

def afficher_information_personne(nom, age, taille=0):
    print()
    # print("Hello! " + nom + ", tu as " + str(age) + " ans.")
    # ou
    # print(f"Hello! {nom}, tu as {age} ans.")
    # ou
    print("Hello! %s, tu as %s ans." %(nom, age))
    # print("L'an prochain " + nom + ", tu auras " + str(age + 1) + " ans.")
    # ou
    print("L'an prochain, tu auras %s ans." % (age + 1))

# == égal
# < inférieur
# <= inférieur ou égal 
# > supérieur
# >= supérieur ou égal
# True /False (Boolean)

    if age == 17:
        print("Vous êtes presque majeur") 
    elif age == 1 or age == 2:
        print("Vous êtes un baby")
    elif age < 10:
        print("Vous êtes un enfant")
    elif 12 <= age < 18:
        print("Vous êtes un adolescent")
    elif age == 18:
        print("Vous êtes tout juste : Félicitation")
    elif age > 60:
        print("Vous êtes sénior")
    elif age >= 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")

    # Afficher la taille
    #taille = 1.75 -> float
    if not taille == 0:
        print("Votre taille : " + str(taille) + " m")


def demander_nom():
    reponse_nom = ""

    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom?")
    return reponse_nom


def demander_age(nom_personne):
    # Demander l'age
    age_int = 0

    while age_int == 0:
        age_str = input(nom_personne + "Quel est votre age?")
        try:
            age_int = int(age_str)
        except:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age_int

# # Demander le nom pour person 1
# nom1 = demander_nom()

# # Demander age pour nom 1
# age1 = demander_age(nom1)

# afficher_information_personne(nom1, age1)

# la boucle for
# for i in range(0, 3):
#     nom = "personne" + str(i + 1)
#     age = demander_age(nom)
#     afficher_information_personne(nom, age)

# ou

NB_PERSONNES = 1

NB_PERSONNES 

# la boucle for
for i in range(0, NB_PERSONNES):
    nom = "personne" + str(i + 1) #car index commence à 0
    age = demander_age(nom)
    afficher_information_personne(nom, age)

# afficher sur plusieurs lignes

print("""
    Vous mettez 
        ce que vous 
            vouler
""")

print("toto", 20, "ans", "taille:", 1.70)