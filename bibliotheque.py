from livre import Livre
from utilisateur import Utilisateur

class Bibliotheque:
    def __init__(self):
        self.livres = []
        self.utilisateurs = []

    def ajouter_livre(self, titre, auteur, isbn):
        livre = Livre(titre, auteur, isbn)
        self.livres.append(livre)
        print("Livre ajouté.")

    def enregistrer_utilisateur(self, nom, identifiant):
        utilisateur = Utilisateur(nom, identifiant)
        self.utilisateurs.append(utilisateur)
        print("Utilisateur inscrit.")

    def lister_livres(self):
        for livre in self.livres:
            livre.afficher_info()

    def chercher_utilisateur(self, identifiant):
        for u in self.utilisateurs:
            if u.identifiant == identifiant:
                return u
        return None

    def chercher_livre(self, isbn):
        for l in self.livres:
            if l._isbn == isbn:
                return l
        return None

    def emprunter_livre(self, identifiant, isbn):
        utilisateur = self.chercher_utilisateur(identifiant)
        livre = self.chercher_livre(isbn)
        if utilisateur and livre:
            utilisateur.emprunter_livre(livre)

    def rendre_livre(self, identifiant, isbn):
        utilisateur = self.chercher_utilisateur(identifiant)
        livre = self.chercher_livre(isbn)
        if utilisateur and livre:
            utilisateur.rendre_livre(livre)

    def afficher_utilisateurs(self):
        for u in self.utilisateurs:
            print(f"{u.nom} - {u.identifiant}")
            u.afficher_livres_empruntes()