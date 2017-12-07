class Personne:

    def __init__(self, nom=None, contact=None, role=None, responsable=None, niveau=None, equipe=None, 
    competences=None, projet=None, complements=None):
        self.nom = nom
        self.contact = contact
        self.role = role
        self.responsable = responsable
        self.niveau = niveau
        self.equipe = equipe
        self.competences = competences
        self.projet = projet
        self.complements = complements

    def __str__(self):
        return "Person : " + "nom = " + self.nom + ", contact = " + self.contact

if __name__ == "__main__":
    person = Personne("Albert", "Dupontel", "Aucun", "")
    print(person.nom)
    print(person.contact)
    print(person.role)
    print(person.responsable)
    print(person.projet)