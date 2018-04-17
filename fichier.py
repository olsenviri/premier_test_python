
#__Premier test avec python ( notion des conditions)
#__ Programme effectuer par VIRI REICH
#__Teste si une annee est bissextile ou pas
#__date de creation: 13_04_2018

#_____________________________________________________


print("\n Ce programme ecrit en python teste si une annee est bissextile ou non");

  
bissextile = False

    
annee = input("\nveuillez saisir une annee: ")
annee = int(annee)




if annee % 400 == 0 :  #si le reste de la division de année par 400 est 0 
            bissextile = True

elif annee % 100 == 0:
         bissextile = False

elif annee % 4 == 0:
           bissextile = True

else:
          bissextile = False

if bissextile:
        print(annee, " est une annee bissextile")

else:
       print(annee, " n'est pa une annee bissextile")


    





