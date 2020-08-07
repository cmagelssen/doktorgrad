from moduler import Trening, Utovere
import pandas as pd
import numpy as np
import random
# Class used for testing
class Lageutover:
    @staticmethod
    def rydd():
        path = "/Users/cmagelssen/Desktop/testing/data/pilot1.csv"
        global df
        df = pd.read_csv(path, skiprows=2, decimal=".")
        df = Trening.dnfCountandReplace(df, LagreCsv=True)
        df = Trening.changeDataType(df)
        df = Trening.renameCommentToCourse(df)
        return df

    @staticmethod
    def findBestRunForEachBibAndCourse():
        global groupby
        groupby = Trening.findBestRun(df) #I burde droppe en rank i denne
        return groupby

    @staticmethod
    def allokereIGrupper():
        df1 = groupby.sort_values(by='PRESTASJON', ascending=True)
        mask = np.arange(len(df1)) % 2
        global group1
        group1 = df1.loc[mask == 0]
        global group2
        group2 = df1.loc[mask == 1]
        return group1, group2

    @staticmethod
    def velgerGR1():
        grupper = ['RANDOM', 'BLOCKED']
        for i in group1['BIB#'].unique():
            velger = random.sample(grupper, k=1)
        group1['GRUPPE'] = velger
        return group1

    @staticmethod
    def velgerGR2():
        grupper = ['RANDOM', 'BLOCKED']
        for i in group2['BIB#'].unique():
            velger = random.sample(grupper, k=1)
        group2['GRUPPE'] = velger
        return group2
    #
    @staticmethod
    def lageDataFrames():
        global dfJoinedRandom
        hentRandom = group1.query('GRUPPE == "RANDOM"')
        hentRandom2 = group2.query('GRUPPE == "RANDOM"')
        dfJoinedRandom = pd.concat([hentRandom, hentRandom2])

        global dfJoinedBlocked
        hentBlocked = group1.query('GRUPPE == "BLOCKED"')
        hentBlocked2 = group2.query('GRUPPE == "BLOCKED"')
        dfJoinedBlocked = pd.concat([hentBlocked, hentBlocked2])

        return dfJoinedRandom, dfJoinedBlocked

class Randomgruppe:
    @staticmethod
    def createDict():
        unike = [n for n in dfJoinedRandom['BIB#'].unique()]
        global bibNumberR
        bibNumberR = {bibNumberR: unike for bibNumberR in unike}
        return bibNumberR

    def lagExcelFiler():
        with pd.ExcelWriter('random.xlsx') as writer:
            for key in bibNumberR.keys():
                dataramme = Utovere.allokeringRandom()
                df = dataramme
                df.to_excel(writer, sheet_name=str(key))

class Blockedgruppe:
    @staticmethod
    def createDict():
        unike = [n for n in dfJoinedBlocked['BIB#'].unique()]
        global bibNumberB
        bibNumberB = {bibNumberB: unike for bibNumberB in unike}
        return bibNumberB

    def lagExcelFiler():
        with pd.ExcelWriter('blocked.xlsx') as writer:
            for key in bibNumberB.keys():
                dataramme = Utovere.allokeringBlocked()
                df = dataramme
                df.to_excel(writer, sheet_name=str(key))


Lageutover.rydd()
Lageutover.findBestRunForEachBibAndCourse()
Lageutover.allokereIGrupper()
Lageutover.velgerGR1()
Lageutover.velgerGR2()
Lageutover.lageDataFrames()



Randomgruppe.createDict()
Randomgruppe.lagExcelFiler()
Blockedgruppe.createDict()
Blockedgruppe.lagExcelFiler()
