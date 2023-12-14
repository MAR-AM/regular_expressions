import re

def recherche(chaine, mot):
    pattern = re.compile(fr'\b{re.escape(mot)}\b')
    
    if pattern.search(chaine):
        print(f"Le mot '{mot}' existe dans la chaîne.")
        return True
    else:
        print(f"Le mot '{mot}' n'existe pas dans la chaîne.")
        return False


def contient_chiffres(chaine):
    # Utilisation de re.search pour rechercher des chiffres dans la chaîne
    return bool(re.search(r'\d', chaine))


def remplace(chaine):
    return re.sub(r'\s', '-', chaine)



def telephone(numero):
    # Utilisation de re.match pour vérifier le format du numéro
    pattern = re.compile(r'\d{2}-\d{3}\d{4}')
    if pattern.search(numero):
        print("Le numéro de téléphone est au format attendu.")
        return True
    else:
        print("Le numéro de téléphone n'est pas au format attendu.")
        return False


def email(email):
    # Utilisation de re.match pour valider le format de l'e-mail
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if  pattern.search(email):
        print("L'adresse e-mail est au format attendu.")
        return True
    else:
        print("L'adresse e-mail n'est pas au format attendu.")
        return False






