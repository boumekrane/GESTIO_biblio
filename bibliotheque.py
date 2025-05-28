from livre import Livre
from utilisateur import Utilisateur

class Bibliotheque:
    def __init__(self):
        self.livres = []
        self.utilisateurs = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def ajouter_utilisateur(self, utilisateur):
        self.utilisateurs.append(utilisateur)

    def afficher_livres(self):
        print("Liste des livres :")
        for livre in self.livres:
            print(f"  - {livre}")

    def afficher_utilisateurs(self):
        print("Liste des utilisateurs :")
        for utilisateur in self.utilisateurs:
            print(f"  - {utilisateur.nom} (ID: {utilisateur.identifiant})")
