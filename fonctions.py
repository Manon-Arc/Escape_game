import fonctions
import variables
import random
def history():
    print("\nTu es un agent d'élite, spécialisé dans les missions de haut niveau. Cette fois-ci, tu es appelé à résoudre une crise internationale majeure.\nUn scientifique renommé, le Dr. William Hartman, a été enlevé par une organisation criminelle dangereuse.\nIl est sur le point de révéler une découverte scientifique révolutionnaire, susceptible de bouleverser l'équilibre du pouvoir mondial.\nTa mission consiste à pénétrer dans le repaire secret de l'organisation criminelle, situé au cœur d'un bâtiment qui semble désaffecté.\nTu dois libérer le Dr. Hartman, récupérer ses précieuses informations et échapper avant que l'organisation ne s'en rende compte.\nTu disposez de 60 minutes pour parcourir les pièces du repaire, résoudre des énigmes complexes, pirater des systèmes de sécurité et trouver des indices stratégiques.\nSeras-tu capables de neutraliser l'organisation criminelle, sauver le Dr. Hartman et protéger les secrets de l'Opération Hélios ?\nLe sort du monde repose entre tes mains. Le compte à rebours a commencé. Prépares-toi à une mission palpitante et intense !\n")

def rule():
    print(
        "Tu peux maintenant te déplacer et explorer l'environnement n'hésite pas à bien chercher partout, de nombreux indices sont cachés, tu as accès à la liste des commandes avec 'command'\nBonne chance !")
def command():
    print("\nSe déplacer -> 'go'\nExplorer -> 'explore'\nInteragir -> 'interact'\nOu tu es -> 'where'\nCarte -> map\nAfficher l'inventaire -> inventory\nUtiliser un objet de ton inventaire -> 'use'\nVoir ce que tu as d'équipé -> 'main' ")

def go():
    piece = input('Où veux-tu aller ? :')
    if piece in variables.map and variables.room != piece:
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

def en_main():
    print("Tu as" + variables.main_equipe + "d'équipé")

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
                print("Des caméras surveilles la zone un peu plus loin")
                variables.attempts_hall1 += 1
                print(variables.attempts_hall1)
            elif variables.attempts_hall1 == 1:
                print("On peut compter 4 caméras ainsi que 5 cartons numérotés de 1 à 5")
                variables.attempts_hall1 += 1
                print(variables.attempts_hall1)
            else:
                print("Le carton 1 semble plus grand que les autres")
        case "Entrepôt":
            if variables.garde != 0:
                print("Tu aperçois une échelle ainsi qu'une porte au loin (et pas un porte-au-loin lol HP la ref)")
            else:
                print("La voie est libre tu peux avancer")
        case "Echafaudage":
            variables.inventory.append("feuille")
            print("Tu as mis la main sur une feuille, ça doit faire un sacré moment qu'elle est là.")
        case "Couloir secondaire":
            print("Il n'y a qu'une porte, si on en crois les panneaux elle mène à la salle des archives ")
        case "Salle des archives":
            print("Il y a pleins d'étagères remplis de caisses poussiéreuses mais un dossier attire ton attention")

def interact():
    match variables.room:
        case "Extérieur":
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
            elif (obj_hall1 != "carton 1" or obj_hall1 != "carton 2" or obj_hall1 != "carton 3" or obj_hall1 != "carton 4" or obj_hall1 != "carton 5"):
                print("Tu ne peux pas intéragir avec ça")
            else:
                if obj_hall1 == "carton 1":
                    if variables.etat_carton_1 == "prendre":
                        if not "carton" in variables.inventory:
                            variables.inventory.append("carton")
                            print("Tu as récupéré le carton")
                        else:
                            print("Le carton est déjà dans ton inventaire")

                    if variables.attempts_carton_hall1 < 4 and variables.etat_carton_1 == "ferme":
                        variables.etat_carton_1 = "prendre"
                        variables.attempts_carton_hall1 += 1
                        print("Le carton est vide...")

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
                        variables.inventory.append("flechette")
                        variables.attempts_carton_hall1 += 1
                        variables.etat_carton_4 = "ferme"
                        print("Tu viens de trouver 2 fléchettes et les ajoute à ton inventaire")

                if obj_hall1 == "carton 5":
                    if variables.attempts_carton_hall1 < 4 and variables.etat_carton_5 == "ouvert":
                        variables.attempts_carton_hall1 += 1
                        print("Tu as déjà ouvert le " + obj_hall1)
                    else:
                        variables.inventory.append("flechette")
                        variables.attempts_carton_hall1 += 1
                        variables.etat_carton_5 = "ferme"
                        print("Tu viens de trouver une fléchette et l'ajoute à ton inventaire")
        case "Entrepôt":
            obj_entrepot = input('Avec quoi veux-tu intéragir ? :')
            if obj_entrepot == "echelle" and variables.dilemme == "non":
                variables.map.append("Echafaudage")
                variables.room = "Echafaudage"
                variables.dilemme = "oui"
                print("L'échelle ta conduit en haut d'un échafaudage, t'es fort à cache-cache toi non ? Le garde t'as perdu de vue ")
            elif obj_entrepot == "porte" and variables.dilemme == "non":
                variables.map.append("Couloir principal")
                variables.room = "Couloir principal"
                variables.dilemme = "oui"
                print("La porte ta mené dans le couloir principal")
                entry()
            elif obj_entrepot == "trappe":
                variables.map.append("Couloir secondaire")
                variables.room = "Couloir secondaire"
                print("La trappe ta conduit jusqu'au couloir secondaire")
                entry()
            elif (obj_entrepot == "echelle" or obj_entrepot == "porte") and variables.dilemme == "oui":
                print("Tu ne peux plus intéragir avec ça")
        case "Couloir secondaire":
            obj_couloiresec = input('Avec quoi veux-tu intéragir ? :')
            if obj_couloiresec == "porte":
                variables.map.append("Salle des archives")
                print("La porte s'ouvre en un grincement bruyant")
        case "Salle des archives":
            obj_sallearchives = input('Avec quoi veux-tu intéragir ? :')
            if obj_sallearchives == "dossier":
                variables.inventory.append("doc_Dr")
                print("Tu viens de trouver un des documents du Dr Hartman ! Il est maintenant dans ton inventaire ")


def use():
    use_object = input("Que veux-tu utiliser ?")
    if use_object in variables.inventory:
        match variables.room:
            case "Hall 1":
                if use_object == "flechette" and variables.camera > 0:
                    detruire_cam = input("Veux-tu tenter de détruire une caméra ?")
                    if detruire_cam == "oui":
                        if random.randint(1,10) <= 7:
                            variables.camera -= 1
                            variables.inventory.remove("flechette")
                            print("Tu as détruit une caméra !")
                        else:
                            variables.inventory.remove("flechette")
                            print("Raté... tu as perdu une flechette")
                elif use_object == "carton":
                    cache_carton = input("Veux-tu te cacher/déguiser à l'aide du carton ?")
                    if cache_carton == "oui":
                        equiper(use_object)
                        print("Tu peux avancer en étant plus discret")
                else:
                    print("Tu n'as pas cet objet dans ton inventaire")
            case "Entrepôt":
                if use_object == "flechette" and variables.garde > 0:
                    eliminer_garder = input("Veux-tu tenter d'éliminer un garde ?")
                    if eliminer_garder == "oui":
                        if random.randint(1,2) == 1:
                            variables.garde -= 1
                            variables.inventory.remove("flechette")
                            print("Tu as éliminé un garde !")
                        else:
                            variables.inventory.remove("flechette")
                            print("Raté... tu as perdu une flechette")
                if use_object == "feuille":
                    print("C'est un plan de la pièce, on dirait qu'elle indique une trappe dans l'Entrepôt...")
            case "Echafaudage":
                if use_object == "feuille":
                    print("C'est un plan de la pièce, on dirait qu'elle indique une trappe dans l'Entrepôt...")
def entry():
    match variables.room:
        case "Extérieur":
            print("Il pleut tu ferais mieux de re rentrer")
        case "Hall 1":
            print("Il fait sombre et humide, on entend la chute de gouttes d'eau résonner...")
            if not "Entrepôt" in variables.map:
                variables.map.append("Entrepôt")
        case "Entrepôt":
            if variables.entreé_entrepot == 0:
                if variables.camera == 0:
                    variables.entreé_entrepot +=1
                    variables.map.append("Couloir secondaire")
                    print("Il n'y a personne, tu peux avancer ")
                if variables.main_equipe == "carton" and variables.camera > 0:
                    if random.randint(1,2) == 1:
                        variables.entreé_entrepot += 1
                        variables.map.append("Couloir secondaire")
                        print("Il n'y a personne, tu peux avancer ")
                    else:
                        variables.garde += 1
                        variables.entreé_entrepot += 1
                        print("Il y a un garde, tu es repéré !")
                if variables.camera > 0 and variables.main_equipe != "carton":
                    variables.garde += 1
                    variables.entreé_entrepot +=1
                    print("Il y a un garde, tu es repéré !")
        case "Echafaudage":
            print("Tu surplombes tout l'entrepôt de ta hauteur")
        case "Couloir secondaire":
            print("C'est très étroit ici")
        case "Couloir principal":
            print("Ce couloir est si long que tu n'en vois pas le bout, un frisson te parcourt...")
        case "Salle des archives":
            print("*Tousse Tousse* cette poussière...")
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