import fonctions
import variables

def main():
    fonctions.history()
    fonctions.rule()
    while True:
        if variables.fin == True:
            break
        user = input('Que veux-tu faire ? : ')
        match user:
            case "command":
                fonctions.command()
            case "go":
                fonctions.go()
            case "where":
                fonctions.where()
            case "map":
                fonctions.map()
            case "inventory":
                fonctions.inventory()
            case "explore":
                fonctions.explore()
            case "interact":
                fonctions.interact()
            case "main":
                fonctions.en_main()
            case "rien":
                fonctions.snap()
                break
            case "use":
                fonctions.use()
            case "terminer le travail":
                if variables.final == True:
                    fonctions.terminer_le_travail()
            case "return ta mere":
                fonctions.return_ta_win()
                break
            case "ma bite":
                print("Ce n'est pas très approprié...")
            case _:
                fonctions.command()


if __name__ == '__main__':
    main()

