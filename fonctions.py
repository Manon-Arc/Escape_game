import fonctions
import variables
import random
def history():
    print("\nTu es un agent d'élite, spécialisé dans les missions de haut niveau. Cette fois-ci, tu es appelé à résoudre une crise internationale majeure.\nUn scientifique renommé, le Dr. William Hartman, a été enlevé par une organisation criminelle dangereuse.\nIl est sur le point de révéler une découverte scientifique révolutionnaire, susceptible de bouleverser l'équilibre du pouvoir mondial.\nTa mission consiste à pénétrer dans le repaire secret de l'organisation criminelle, situé au cœur d'un bâtiment qui semble désaffecté.\nTu dois libérer le Dr. Hartman, récupérer ses précieuses informations et échapper avant que l'organisation ne s'en rende compte.\nTu disposez de 60 minutes pour parcourir les pièces du repaire, résoudre des énigmes complexes, pirater des systèmes de sécurité et trouver des indices stratégiques.\nSeras-tu capables de neutraliser l'organisation criminelle, sauver le Dr. Hartman et protéger les secrets de l'Opération Hélios ?\nLe sort du monde repose entre tes mains. Le compte à rebours a commencé. Prépares-toi à une mission palpitante et intense !\n")

def rule():
    print(
        "Tu peux maintenant te déplacer et explorer l'environnement n'hésite pas à bien chercher partout, de nombreux indices sont cachés, tu as accès à la liste des commandes avec 'command'\nBonne chance !")
def command():
    print("\nSe déplacer -> 'go'\nExplorer -> 'explore'\nInteragir -> 'interact'\nOu tu es -> 'where'\nCarte -> map\nAfficher l'inventaire -> inventory\nUtiliser un objet de ton inventaire -> 'use' ")

def go():
    piece = input('Où veux-tu aller ? :')
    if piece in variables.map:
        variables.room = piece
        print("Tu es maintenant ici : " + variables.room)
        entry()
    elif piece == "rester" and variables.room == "extérieur":
        fonctions.snap()
    else:
     print("Tu ne peux pas aller dans cette piece")

def where():
    print("Tu es ici : " + variables.room)

def inventory():
    if len(variables.inventory) == 0:
        print("Ton inventaire est vide...")
    else:
        print("Tu as : " + ', '.join(variables.inventory) + " dans ton inventaire")

def equiper(obj):
    variables.main_equipe = obj

def map():
    print("Tu peux aller là : " + ', '.join(variables.map))

def explore():
    match variables.room:
        case "extérieur":
            if variables.attempts_ext == 0:
                print("l'entrée principal semble condamnée...")
                variables.attempts_ext =+ 1
            else:
                print("Il y a une porte derrière")
        case "Hall 1":
            if variables.attempts_hall1 == 0:
                print("Des caméras surveilles la zone un peu plus loin ")
                variables.attempts_hall1 =+ 1
            if variables.attempts_hall1 == 1:
                variables.attempts_hall1 =+ 1
                print("On peut compter 4 caméras ainsi que 5 cartons numérotés de 1 à 5")
            else:
                print("Le carton 1 semble plus grand que les autres")

def interact():
    match variables.room:
        case "extérieur":
            obj_ext = input('Avec quoi veux-tu intéragir ? :')
            if obj_ext == "porte":
                if not "Hall 1" in variables.map:
                    variables.map.append("Hall 1")
                    print("La porte s'ouvre, tu peux entrer.")
                else:
                    print("Tu as déjà intéragit avec la porte...")
            else:
                print("Tu ne peux pas intéragir avec ça...")

        case "Hall 1":
            obj_hall1 = input('Avec quoi veux-tu intéragir ? :')
            if (obj_hall1 == "carton 1" or obj_hall1 == "carton 2" or obj_hall1 == "carton 3" or obj_hall1 == "carton 4" or obj_hall1 == "carton 5") and variables.attempts_carton_hall1 == 4:
                print("Tu ne peux plus ouvrir de cartons")
            else:
                if obj_hall1 == "carton 1":
                    if variables.etat_carton_1 == "prendre":
                        if not "carton" in variables.inventory:
                            variables.inventory.append("carton")
                            print("Tu as récupéré le carton")
                            print(variables.attempts_carton_hall1)
                        else:
                            print("Le carton est déjà dans ton inventaire")
                            print(variables.attempts_carton_hall1)

                    if variables.attempts_carton_hall1 < 4 and variables.etat_carton_1 == "ferme":
                        variables.etat_carton_1 = "prendre"
                        variables.attempts_carton_hall1 += 1
                        print("Le carton est vide...")
                        print(variables.attempts_carton_hall1)

                if obj_hall1 == "carton 2":
                    if variables.attempts_carton_hall1 < 4 and variables.etat_carton_2 == "ouvert":
                        variables.attempts_carton_hall1 += 1
                        print("Tu as déjà ouvert le " + obj_hall1)
                    else:
                        variables.inventory.append("flechette")
                        variables.attempts_carton_hall1 += 1
                        variables.etat_carton_2 = "ferme"
                        print("Tu viens de trouver une fléchette et l'ajoute à ton inventaire")


                if obj_hall1 == "carton 3":
                    if variables.attempts_carton_hall1 < 4 and variables.etat_carton_3 == "ouvert":
                        variables.attempts_carton_hall1 += 1
                        print("Tu as déjà ouvert le " + obj_hall1)
                    else:
                        variables.inventory.append("flechette")
                        variables.attempts_carton_hall1 += 1
                        variables.etat_carton_3 = "ferme"
                        print("Tu viens de trouver une fléchette et l'ajoute à ton inventaire")

                if obj_hall1 == "carton 4":
                    if variables.attempts_carton_hall1 < 4 and variables.etat_carton_4 == "ouvert":
                        variables.attempts_carton_hall1 += 1
                        print("Tu as déjà ouvert le " + obj_hall1)
                    else:
                        variables.inventory.append("flechette")
                        variables.attempts_carton_hall1 += 1
                        variables.etat_carton_4 = "ferme"
                        print("Tu viens de trouver une fléchette et l'ajoute à ton inventaire")

                if obj_hall1 == "carton 5":
                    if variables.attempts_carton_hall1 < 4 and variables.etat_carton_5 == "ouvert":
                        variables.attempts_carton_hall1 += 1
                        print("Tu as déjà ouvert le " + obj_hall1)
                    else:
                        variables.inventory.append("flechette")
                        variables.attempts_carton_hall1 += 1
                        variables.etat_carton_5 = "ferme"
                        print("Tu viens de trouver une fléchette et l'ajoute à ton inventaire")

def use():
    match variables.room:
        case "Hall 1":
            use_object = input("Que veux-tu utiliser ?")
            if use_object in variables.inventory:
                if use_object == "flechette" and variables.camera > 0:
                    detruire_cam = input("Veux-tu tenter de détruire une caméra ?")
                    if detruire_cam == "oui":
                        if random.randint(1,10) >= 7:
                            variables.camera -= 1
                            variables.inventory.remove("flechette")
                            print("Tu as détruit une caméra !")
                        else:
                            variables.inventory.remove("flechette")
                            print("Raté... tu as perdu une flechette")
                if use_object == "carton":
                    cache_carton = input("Veux-tu te cacher/déguiser à l'aide du carton ?")
                    if cache_carton == "oui":
                        equiper(use_object)
                        print("Tu peux avancer en toute discretion")
            else:
                print("Tu n'as pas cet objet dans ton inventaire")
def entry():
    match variables.room:
        case "Hall 1":
            print("Il fait sombre et humide, on entend la chute de gouttes d'eau résonner...")
            variables.map.append("Entrepôt")

def snap():
    with open("asset/snap.txt", "r") as fichier:
        lignes = fichier.readlines()

    for ligne in lignes:
        print(ligne.strip())


def bim():
    with open("asset/bim.txt", "r") as fichier:
        lignes = fichier.readlines()

    for ligne in lignes:
        print(ligne.strip())

def return_ta_win():
    bim()
    print("Le Dr. William Hartman s'est échappé sans votre aide. Félicitation vous n'avez servi à rien !")