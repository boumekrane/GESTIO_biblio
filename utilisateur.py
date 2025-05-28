class Utilisateur:
    def __init__(self, nom, identifiant):
        self.nom = nom
        self.identifiant = identifiant
        self.livres_empruntes = []

    def emprunter_livre(self, livre):
        if livre.emprunter():
            self.livres_empruntes.append(livre)
            print(f"{self.nom} a emprunté {livre._titre}")
        else:
            print("Le livre n'est pas disponible.")

    def rendre_livre(self, livre):
        if livre in self.livres_empruntes:
            livre.retourner()
            self.livres_empruntes.remove(livre)
            print(f"{self.nom} a rendu {livre._titre}")
        else:
            print("Ce livre n'est pas dans la liste d'emprunts.")

    def afficher_livres_empruntes(self):
        if not self.livres_empruntes:
            print(f"{self.nom} n’a emprunté aucun livre.")
        for livre in self.livres_empruntes:
            livre.afficher_info()
