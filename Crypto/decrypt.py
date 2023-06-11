import collections

def freq_lettres(fichier):
    with open(fichier, 'r') as f:
        texte = f.read()
        # Créer un dictionnaire avec des compteurs pour chaque lettre de l'alphabet
        compteurs = collections.Counter(texte)
        # Boucle sur chaque lettre de l'alphabet et afficher sa fréquence
        return compteurs

fichier = './student/cipher.txt'
compteur = freq_lettres(fichier)
print(compteur)