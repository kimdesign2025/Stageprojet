def info_personne(nom, age):
    print("vous vous appelle " + nom + " et vous avez " + str(age) + " et vous aurez " + str(age + 1)  + " l'annee prochain ")
    
    if age <=18:
        print("vous etes mineur ")
    else:
        print("vous etes majeur")

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

nom1 = demander_nom()
nom2 = demander_nom()

age1 = demander_age()
age2 = demander_age()

info_personne(nom1, age1)
info_personne(nom2, age2)