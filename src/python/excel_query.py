"""
Excel queries
"""
import sys

from data_loader import DataLoader

dataLoader = DataLoader()
personnes = dataLoader.getAllPersons()

def qui_travaille_sur_projet(projet):
    """ Retourne une liste de personne travaillant sur le projet """
    projet = projet.upper()
    personnes_concernnees = []
    global personnes
    for person in personnes:
        if person.PROJET == projet:
            personnes_concernnees.append(person)
    print(personnes_concernnees, file=sys.stderr)
    return personnes_concernnees

def qui_est_responsable(nom):
    """ Retourne le responsable ou None de la personne concerné """
    nom = nom.upper()
    global personnes
    for personne in personnes:
        if personne.NOM == nom:
            return personne.responsable
    return None
