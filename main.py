from livre import Livre
from utilisateur import Utilisateur
from bibliotheque import Bibliotheque

def menu():
    biblio = Bibliotheque()

    # Données de test
    livre1 = Livre("Python pour les débutants", "Jean Dupont")
    livre2 = Livre("Intelligence Artificielle", "Marie Curie")
    biblio.ajouter_livre(livre1)
    biblio.ajouter_livre(livre2)

    utilisateur1 = Utilisateur("Ali", 1)
    utilisateur2 = Utilisateur("Sana", 2)
    biblio.ajouter_utilisateur(utilisateur1)
    biblio.ajouter_utilisateur(utilisateur2)

    while True:
        print("\n=== Menu ===")
        print("1. Afficher les livres")
        print("2. Afficher les utilisateurs")
        print("3. Emprunter un livre")
        print("4. Retourner un livre")
        print("5. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            biblio.afficher_livres()
        elif choix == "2":
            biblio.afficher_utilisateurs()
        elif choix == "3":
            nom = input("Nom de l'utilisateur : ")
            titre = input("Titre du livre : ")
            utilisateur = next((u for u in biblio.utilisateurs if u.nom == nom), None)
            livre = next((l for l in biblio.livres if l.titre == titre), None)
            if utilisateur and livre:
                utilisateur.emprunter_livre(livre)
            else:
                print("Utilisateur ou livre introuvable.")
        elif choix == "4":
            nom = input("Nom de l'utilisateur : ")
            titre = input("Titre du livre : ")
            utilisateur = next((u for u in biblio.utilisateurs if u.nom == nom), None)
            livre = next((l for l in biblio.livres if l.titre == titre), None)
            if utilisateur and livre:
                utilisateur.retourner_livre(livre)
            else:
                print("Utilisateur ou livre introuvable.")
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    menu()
