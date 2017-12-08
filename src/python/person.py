class Personne:

    def __init__(self, nom=None, contact=None, role=None, responsable=None,
                 niveau=None, equipe=None, competences=None, projet=None,
                 complements=None):
        self.nom = nom
        self.NOM = nom.upper()
        self.contact = contact
        self.CONTACT = contact.upper()
        self.role = role
        self.ROLE = role.upper()
        self.responsable = responsable
        self.RESPONSABLE = responsable.upper()
        self.niveau = niveau
        self.NIVEAU = niveau
        self.equipe = equipe
        self.EQUIPE = equipe.upper()
        self.competences = competences
        self.COMPETENCES = competences.upper()
        self.projet = projet
        self.PROJET = projet.upper()
        self.complements = complements
        self.COMPLEMENTS = complements.upper()

    def __str__(self):
        return self.nom

    def pretty_print(self):
        return ("Personne:\n name = %s\ncontact = %s\nrole = %s\n"
               "responsable = %s\n niveau=%d\n...\n") % (self.nom, self.contact, self.role, self.responsable, self.niveau)

    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    person = Personne("Albert", "Dupontel", "Aucun", "")
    print(person.nom)
    print(person.contact)
    print(person.role)
    print(person.responsable)
    print(person.projet)