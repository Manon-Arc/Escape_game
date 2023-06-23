import fonctions
import variables
import random
import time
def history():
    print("\nTu es un agent d'élite, spécialisé dans les missions de haut niveau. Cette fois-ci, tu es appelé à résoudre une crise internationale majeure.\nUn scientifique renommé, le Dr. William Hartman, a été enlevé par une organisation criminelle dangereuse.\nIl est sur le point de révéler une découverte scientifique révolutionnaire, susceptible de bouleverser l'équilibre du pouvoir mondial.\nTa mission consiste à pénétrer dans le repaire secret de l'organisation criminelle, situé au cœur d'un bâtiment qui semble désaffecté.\nTu dois libérer le Dr. Hartman, récupérer ses précieuses informations et échapper avant que l'organisation ne s'en rende compte.\nTu disposez de 60 minutes pour parcourir les pièces du repaire, résoudre des énigmes complexes, pirater des systèmes de sécurité et trouver des indices stratégiques.\nSeras-tu capables de neutraliser l'organisation criminelle, sauver le Dr. Hartman et protéger les secrets de l'Opération Hélios ?\nLe sort du monde repose entre tes mains. Le compte à rebours a commencé. Prépares-toi à une mission palpitante et intense !\n")

def rule():
    print(
        "Tu peux maintenant te déplacer et explorer l'environnement n'hésite pas à bien chercher partout, de nombreux indices sont cachés, tu as accès à la liste des commandes avec 'command'\nBonne chance !")
def command():
    print("\nSe déplacer -> 'go'\nExplorer -> 'explore'\nInteragir -> 'interact'\nOu tu es -> 'where'\nCarte -> 'map'\nAfficher l'inventaire -> 'inventory'\nUtiliser un objet de ton inventaire -> 'use'\nVoir ce que tu as d'équipé -> 'main' ")

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
            print("Il n'y a qu'une porte, si on en crois les panneaux elle mène à la salle des archives")
        case "Salle des archives":
            if variables.attempts_sallearchive == 0:
                variables.attempts_sallearchive +=1
                print("Il y a pleins d'étagères remplis de caisses poussiéreuses mais un dossier attire ton attention")
            elif variables.attempts_sallearchive == 1:
                variables.attempts_sallearchive +=1
                print("Tu sens un léger courant d'air")
            else:
                print("Tu te rend compte que ça vient d'une ventilation")
        case "Couloir principal":
            if variables.garde != 0:
                cachette = input("Il y a un casier et un placard ou veux-tu te cacher")
                if cachette == "casier":
                    variables.garde -= 1
                    print("Le garde s'éloigne, t'as eu chaud !")
                elif cachette == "placard":
                    print("Le placard est plein tu ne peux pas te cacher ici...\nLe garde t'a attrapé c'est fini pour toi...")
                    loose()
            else:
                if not "Ascenseur" in variables.map:
                    variables.map.append("Ascenseur")
                print("Au bout du couloir tu aperçois un ascenseur à travers le hublot d'une porte")

        case "Sas":
            print("Il y a 2 placards au fond de la piece ainsi qu'une porte")
        case "Ascenseur":
            if variables.attempts_ascenseur == 0:
                variables.attempts_ascenseur += 1
                print("Il y a des boutons pour changer d'étage")
            else:
                print("Quelque chose semble dépasser du boitier de commande...")
        case "Laboratoire":
            print("Vous remarquez une porte peut-être faudrait-il une clé ?")
            print("En faisant de tour du laboratoire, vous relevez la présence de pas mal de choses :\n-carton,\n-box,\n- casier,\n- becher,\n- caisse à outil,\n- pierre étrange,\n- microscope")
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
            if obj_sallearchives == "ventilation":
                variables.map.append("Conduit")
                variables.room = "Conduit"
                print("Tu te faufiles à travers le conduit")
                time.sleep(2)
                vitesse = input("Préfères-tu te déplacer de façon rapide ou lente dans le conduit ? :")
                if vitesse == "rapide":
                    if random.randint(1,2) == 1:
                        variables.map.append("Salle de réunion")
                        variables.room = "Salle de réunion"
                        print("Le conduit se met à trembler : *Boum* Les filles je suis tombééééééhhh")
                        entry()
                    else:
                        variables.map.append("Couloir principal")
                        variables.room = "Couloir principal"
                        print("Le conduit débouche dans le couloir principal")
                elif vitesse == "lente":
                    variables.map.append("Couloir principal")
                    variables.room = "Couloir principal"
                    print("Le conduit débouche dans le couloir principal")
        case "Sas":
            obj_sas = input('Avec quoi veux-tu intéragir ? :')
            if obj_sas == "placard 2":
                variables.inventory.append("uniforme")
                print("Tu viens de récupérer un uniforme de gardes, avec un peu de chance tu pourras l'utiliser pour rester sous couverture")
            elif obj_sas == "placard 1":
                print("C'est vide...")
            elif obj_sas == "porte":
                if not "Couloir principal" in variables.map:
                    variables.map.append("Couloir principal")
                    variables.room = "Couloir principal"
                    print("La porte s'ouvre")
                    entry()
                else:
                    print("Tu as déjà ouvert la porte")
            else :
                print("Tu ne peux pas intéragir avec ça")
        case "Ascenseur":
            obj_ascenseur = input('Avec quoi veux-tu intéragir ? :')
            if obj_ascenseur == "boutons":
                if random.randint(1,4) == 1:
                    print("*Monte au 3e...*")
                    time.sleep(0.5)
                    print("...")
                    time.sleep(0.5)
                    print("*Redescend*, mince quelqu'un a du appeler l'ascenseur !")
                    time.sleep(0.5)
                    print("*Porte s'ouvre...")
                    if variables.main_equipe == "uniforme":
                        if random.randint(1,2) == 1:
                            print("Des gardes arrivent du bout du couloir, et te font signe\nTu rappuies rapidement sur le bouton et la porte se ferme, heureusement que tu portais l'uniforme")
                            variables.map = []
                            variables.map.append("Laboratoire")
                            variables.room == "Laboratoire"
                            print("*Monte au 3e...*")
                            time.sleep(2)
                            entry()
                        else:
                            print("*Des gardes arrivent du bout du couloir*, Mais, tu n'es pas Michel ! *PewPewPew* ")
                            loose()
                else:
                    variables.map = []
                    variables.map.append("Laboratoire")
                    variables.room == "Laboratoire"
                    print("*Monte au 3e...*")
                    time.sleep(2)
                    entry()
            elif obj_ascenseur == "boitier de commande":
                variables.inventory.append("doc_Dr")
                print("Tu viens de trouver un des documents du Dr Hartman ! Il est maintenant dans ton inventaire ")
        case "Laboratoire":
            obj_labo = input('Avec quoi veux-tu intéragir ? :')
            if obj_labo == "carton":
                print("Il y a une poule")
                time.sleep(2)
                print("Cote cote 🤌")
            elif obj_labo == "box":
                print("Il n'y a rien ici")
            elif obj_labo == "casier":
                print("Ce casier m'a l'air louche")
                time.sleep(1)
                print("on dirait qu'il y a quelque chose")
                time.sleep(1)
                print("...")
                time.sleep(1.5)
                print("...")
                time.sleep(1.5)
                print("QU'EST-CE QUE C'EST ?!!")
                time.sleep(3)
                print("En fait non y'a rien")
                time.sleep(1)
                print("Je rigooooleuuu UwU")
                time.sleep(1)
                print("T'es bo kiss kiss <3")
            elif obj_labo == "becher":
                print("BOUH !!! ToT")
            elif obj_labo == "caisse à outils":
                print("Cette utilitaire est vide")
            elif obj_labo == "pierre etrange":
                korogu()
            elif obj_labo == "microscope":
                variables.inventory.append("mot")
                print("Tu as trouvé un mot plier près de l'appareil, il est maintenant dans ton inventaire")
            elif obj_labo == "porte":
                variables.map.append("Toit")
                print("La porte était déjà déverouillé... SORRY ;)\nTu arrives dans une cage d'escalier avec un accès direct au toit")
            else:
                print("Tu ne peux pas intéragir avec ça")

def use():
    use_object = input("Que veux-tu utiliser ?")
    if use_object == "ma bite":
        print("Ce n'est pas très approprié...")
    elif use_object in variables.inventory:
        if use_object == "uniforme":
            if variables.main_equipe != "uniforme":
                variables.main_equipe = "uniforme"
                print("Tu es déguisé")
            else:
                print("Tu es déjà déguisé")
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
                            print("Tu as éliminé un garde ! C'est ciao !")
                        else:
                            variables.inventory.remove("flechette")
                            print("Raté... tu as perdu une flechette")
                if use_object == "feuille":
                    print("C'est un plan de la pièce, on dirait qu'elle indique une trappe dans l'Entrepôt...")
            case "Echafaudage":
                if use_object == "feuille":
                    print("C'est un plan de la pièce, on dirait qu'elle indique une trappe dans l'Entrepôt...")
            case "Laboratoire":
                if use_object == "mot":
                    print("Je ne pense pas qu'il y ai de bonnes ou de mauvaise situation,\nsi je devais résumer ma vie avec vous aujourd'hui c'est avant tout des rencontres des gens qui m'ont tendu la mains a des moments ou je ne m'y attendais pas")
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
                        print("Bah frérot je suis presque sur que les cartons ça bouge pas à la base tu es repéré, court ta mère!")
                if variables.camera > 0 and variables.main_equipe != "carton":
                    variables.garde += 1
                    variables.entreé_entrepot +=1
                    print("Il y a un garde, ouaieuh t'es dans la merde !")
        case "Echafaudage":
            print("Tu surplombes tout l'entrepôt de ta hauteur")
        case "Couloir secondaire":
            print("C'est très étroit ici")
        case "Couloir principal":
            print("Ce couloir est si long que tu n'en vois pas le bout, un frisson te parcourt...")
        case "Salle des archives":
            print("*Tousse Tousse* Quelle poussière...")
        case "Salle de réunion":
            if random.randint(1,100) == 1:
                variables.map.append("Sas")
                variables.room = "Sas"
                print("BUUUUUUUUT *Ils ne t'ont pas entendu tu en profites pour t'enfuir vers la porte*")
            else:
                print("Les gardes ton vue c'est fini pour toi...")
                loose()
        case "Sas":
            print("♫ Sas-en va et Sas-revient ♫ (référence au 'Sas') C'est sen-sas-ionnel ce jeu de mot non ? ^_^ (encore lol tavu)")
        case "Ascenseur":
            print("*Musique d'ascenseur*")
        case "Laboratoire":
            print("Une atmosphère pessante règne dans cette pièce\nLes murs décrépis et les fenêtres brisées témoignent de l'usure du temps et de l'absence d'activité humaine depuis des années.")
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

def korogu():
    with open("asset/korogu.txt", "r") as fichier:
        lignes = fichier.readlines()

    for ligne in lignes:
        print(ligne.strip())
    print("nyah   ha   haaa !!!!")
    time.sleep(0.5)
    print(...)
    time.sleep(0.5)
    print("tou roututu tututuuuu")
    time.sleep(0.5)
    print("Tu as trouvé un korogu !!!")

def migraculous():
    if random.randint(1,2) == 1:
        with open("asset/lady_beurre.txt", "r") as fichier:
            lignes = fichier.readlines()

        for ligne in lignes:
            print(ligne.strip())
        print("♫ Migraculous porte-bonheurt lady magique et laby-beurre ♫")
    else:
        with open("asset/gras_noir.txt", "r") as fichier:
            lignes = fichier.readlines()

        for ligne in lignes:
            print(ligne.strip())
        print("♫ C'est moi gras noir, toujours présent, j'ai les doigts gras vive l'saucisson ♫")

def return_ta_win():
    bim()
    print("Le Dr. William Hartman s'est échappé sans votre aide. Félicitation vous n'avez servi à rien !")

def loose():
    print("Ton parcours s'achève ici, mais n'abandonne pas pour autant. Retente ta chance et explore les multiples voies qui te mèneront à d'autres fins captivantes.\nLe jeu n'est pas encore terminé, il te reste encore beaucoup à découvrir.")
    snap()