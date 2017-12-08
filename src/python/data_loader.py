"""
Load data from excel
"""

from openpyxl import load_workbook
from person import Personne

class DataLoader:

    def getAllPersons(self):
        persons = []
        filename = 'ressources/Data_GOT.xlsx'
        wb = load_workbook(filename)
        ws = wb.worksheets[0]
        for row in ws.iter_rows(row_offset=1, max_col=9, max_row=29):
            persons.append(
                Personne(row[0].value, row[1].value, row[2].value, row[3].value,
                         row[4].value, row[5].value, row[6].value,
                         row[7].value, row[8].value))
        return persons

if __name__ == "__main__":
    d = DataLoader()
    persons = d.getAllPersons()
    for person in persons:
        print(person)
