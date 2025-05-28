class Livre:
    def __init__(self, titre, auteur, isbn):
        self._titre = titre
        self._auteur = auteur
        self._isbn = isbn
        self._disponible = True

    def afficher_info(self):
        dispo = "Disponible" if self._disponible else "Emprunté"
        print(f"{self._titre} - {self._auteur} - ISBN: {self._isbn} - {dispo}")

    def emprunter(self):
        if self._disponible:
            self._disponible = False
            return True
        return False

    def retourner(self):
        self._disponible = True

    def est_disponible(self):
        return self._disponible
