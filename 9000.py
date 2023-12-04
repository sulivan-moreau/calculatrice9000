historique = []

def ajouter_historique(expression, resultat):
    historique.append((expression, resultat))

def afficher_historique():
    print("\nHistorique des calculs:")
    for i, (expression, resultat) in enumerate(historique, 1):
        print(f"{i}. {expression} = {resultat}")

def effacer_historique():
    historique.clear()
    print("\nHistorique effacé.")

def calculatrice():
    while True:
        print("\nCalculatrice Simple")
        print("1. Addition (+)")
        print("2. Soustraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Afficher l'historique")
        print("6. Effacer l'historique")
        print("7. Quitter")

        choix = input("Choisissez une opération (1-7): ")

        if choix == '7':
            print("Au revoir !")
            break

        if choix in {'1', '2', '3', '4'}:
            try:
                nombre1 = float(input("Entrez le premier nombre : "))
                nombre2 = float(input("Entrez le deuxième nombre : "))
            except ValueError:
                print("Erreur : Veuillez entrer des nombres valides.")
                continue

            if choix == '1':
                resultat = nombre1 + nombre2
                operation = "+"
            elif choix == '2':
                resultat = nombre1 - nombre2
                operation = "-"
            elif choix == '3':
                resultat = nombre1 * nombre2
                operation = "*"
            elif choix == '4':
                if nombre2 != 0:
                    resultat = nombre1 / nombre2
                    operation = "/"
                else:
                    print("Erreur : Division par zéro.")
                    continue

            print(f"Résultat de {nombre1} {operation} {nombre2} = {resultat}")
            ajouter_historique(f"{nombre1} {operation} {nombre2}", resultat)

        elif choix == '5':
            afficher_historique()

        elif choix == '6':
            effacer_historique()

        else:
            print("Erreur : Choix invalide. Veuillez entrer un nombre entre 1 et 7.")

if __name__ == "__main__":
    calculatrice()
