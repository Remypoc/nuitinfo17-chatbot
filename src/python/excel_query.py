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
    """ Retourne la personne responsable du projet
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

def comment_joindre_responsable_projet(projet):
    """ Retourne le responsable ou None du projet concerné """
    projet = projet.upper()
    global personnes
    for personne in personnes:
        if personne.PROJET == projet:
            return personne
    return None

def comment_contacter_personne(nom):
    """ Comment contacter une personne """
    nom = nom.upper()
    global personnes
    for personne in personnes:
        if personne.NOM == nom:
            return personne
    return None

def competences_liees_au_projet(projet):
    """ Retourne les compétences liés à un projet donné """
    projet = projet.upper()
    competences = []
    global personnes
    for personne in personnes:
        if personne.PROJET == projet:
            competences.append(personne.competences)
    return competences

def role_de_personne(nom):
    """ Retourne le role d'une personne donnée """
    nom = nom.upper()
    global personnes
    for personne in personnes:
        if personne.NOM == nom:
            return personne.role
    return None

def de_quoi_personne_est_responsable(nom):
    """ Retourne les personnes sous la responsabilité d'une autre personne """
    nom = nom.upper()
    responsable_de = []
    global personnes
    for personne in personnes:
        if personne.RESPONSABLE == nom:
            responsable_de.append(personne.nom)
    return responsable_de


def quel_responsable_projet(projet):
    """ Retourne la personne responsable du projet
    Returns:
        (Personne) Pesonne
    """
    projet = projet.upper()
    global personnes
    p = None
    for personne in personnes:
        if personne.PROJET == projet:
            if p is None or p.niveau > personne.niveau:
                if personne.RESPONSABLE != 'Aucun':
                    for p_tmp in personnes:
                        if p_tmp.NOM == personne.RESPONSABLE:
                            p = p_tmp
                else:
                    p = personne

    return p


def qui_est_personne(nom):
    """ Retourne des informations sur la personne.
    Returns:
        (Str) Informations sur la personne concerné
    """
    nom = nom.upper()
    global personnes
    inf = None
    p = None
    for personne in personnes:
        if personne.NOM == nom:
            p = personne
            break
    if p is not None:
        inf = "<div href='{url}'>{nom}</div>".format(
            url=personne.complements, nom=personne.nom)

    return inf
