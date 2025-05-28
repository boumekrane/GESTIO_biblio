class Utilisateur:
    def __init__(self, nom, identifiant):
        self.nom = nom
        self.identifiant = identifiant
        self.livres_empruntes = []

    def emprunter_livre(self, livre):
        if livre.disponible:
            livre.disponible = False
            self.livres_empruntes.append(livre)
            print(f"{self.nom} a emprunté le livre : {livre.titre}")
        else:
            print(f"Le livre '{livre.titre}' n'est pas disponible.")

    def retourner_livre(self, livre):
        if livre in self.livres_empruntes:
            livre.disponible = True
            self.livres_empruntes.remove(livre)
            print(f"{self.nom} a retourné le livre : {livre.titre}")
        else:
            print(f"{self.nom} n'a pas emprunté le livre : {livre.titre}")
