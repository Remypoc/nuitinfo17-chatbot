"""
Excel queries
"""
import sys

from data_loader import DataLoader

dataLoader = DataLoader()
personnes = dataLoader.getAllPersons()

def qui_travaille_sur_projet(projet):
    """ Retourne une liste de personne travaillant sur le projet
    Returns:
        (List) Liste de Personne
    """
    projet = projet.upper()
    personnes_concernnees = []
    global personnes
    for person in personnes:
        if person.PROJET == projet:
            personnes_concernnees.append(person)
    print(personnes_concernnees, file=sys.stderr)
    return personnes_concernnees

def qui_est_responsable(nom):
    """ Retourne le responsable ou None de la personne concerné
    Returns:
        (Str) Nom du responsable
     """
    nom = nom.upper()
    global personnes
    for personne in personnes:
        if personne.NOM == nom:
            return personne.responsable
    return None

def qui_sait_faire_competence(competence):
    """ Retourne une liste de personne ayant la compétence
    Returns:
        (List) Liste de Personne
    """
    competence = competence.upper()
    global personnes
    p = []
    for personne in personnes:
        if personne.COMPETENCES == competence:
            p.append(personne)
    return p
