def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("quelle est votre nom ? ")
    return reponse_nom

def demander_age():
    age_int = 0

    while age_int == 0:
        age_str = input("quelle est votre age ? ")
        try:
            age_int = int(age_str) 
        except:
            print("erreur vous devez entre un nombre")
    return age_int

nom = demander_nom()

age = demander_age()

print("vous vous appelle " + nom + " et vous avez " + str(age) + " et vous aurez " + str(age + 1)  + " l'annee prochain ")




#essai while
# mot_de_passe = ""
# while not mot_de_passe == "TOTO":
#     mot_de_passe = input("quelle est le mot de passe ")
#     print("le mot de passe est incorrect")
# print("le mot de passe est correct vous avez acces au compte")