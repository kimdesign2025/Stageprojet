#---DEFINITION---
class Personne:
    def __init__(self ,nom ="", age=0):
    
        self.nom = nom #creation d'une variable d'instance

        self.age = age #creation d'une variable d'instance

#methode se presenter
    def sepresenter(self):

        information = " Bonjour je m'appele " + self.nom
        if self.age != 0:
            information += " , et j'ai " + str (self.age) +" ans"
            print(information)
        else:
            print(information)

            if self.Est_majeur():
                print("est majeur")
            else:
                print("est mineur")
    #fuction age
    def Est_majeur(self):
        return self.age >= 18
   
    def demander_nom(self):
        self.nom = input("quel est votre nom ?")
        print("vous vous appeler " ,self.nom)
    

#---UTILISATION---
personne1 = Personne("jean", 0) # creation de personne 1
personne2 = Personne("paul" , 17) # creation de personne 2
personne3=Personne()
personne3.demander_nom()
personne1.sepresenter() 
personne2.sepresenter() 


print("est majeur: " , personne1.Est_majeur())
print("est majeur: " , personne2.Est_majeur())
