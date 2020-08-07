import random
import pandas as pd

people = []


# create a dict

class Utovere:
    def __init__(self, bib):
        self.navn = bib
        people.append(self)

    #def allokeringTilGruppe(self):

    @staticmethod
    def allokeringRandom(printToCSV=False):
        dn = []
        for i in range(3):
            loype = ['STRAIGHT-GLIDING', 'STRAIGHT-GLIDING', 'LØYPE 1', 'LØYPE 1', 'LØYPE 1', 'LØYPE 2', 'LØYPE 2', 'LØYPE 2', 'LØYPE 3', 'LØYPE 3', 'LØYPE 3']
            dn.append(['STRAIGHT-GLIDING'] + random.sample(loype, len(loype)))
        df = pd.DataFrame(dn).transpose()
        df = df.rename(
            columns={0: "Treningsdag 1", 1: "Treningsdag 2", 2: "Treningsdag 3"}
        )
        if printToCSV == True:
            df.to_csv(
                'bra.csv'
            )
        return df

    @staticmethod
    def allokeringBlocked(printToCSV=False):
        dn = []
        for i in range(1):
            loype = ['LØYPE 1', 'LØYPE 2', 'LØYPE 3']
            dn.append(random.sample(loype, len(loype)))
        df = pd.DataFrame(dn)
        df = df.rename(columns={0: "Treningsdag 1", 1: "Treningsdag 2", 2: "Treningsdag 3"})
        return df

    # @staticmethod
    # def lagExcelFiler():
    #     with pd.ExcelWriter('index.xlsx') as writer:
    #         dataliste = []
    #         for person in people:
    #             dataramme = Utovere.allokeringRandom()
    #             df = dataramme
    #             df.to_excel(writer, sheet_name=person.navn)
#
# delegates = {bib: Utovere(bib) for bib in people}

# Christian = Utovere('Christian', 'HSG')
# beate = Utovere('BHJBHUBJBHJ', 'HSG')
# Simen= Utovere('Simen', 'HSG')
# Bra = Utovere('Bra', 'HSG')

#Utovere.lagExcelFiler()