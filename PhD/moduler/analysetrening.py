import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class Trening:

    @staticmethod
    def loadData(fileName):
        df = pd.read_csv(fileName, skiprows=2, decimal=".")
        return df

    @staticmethod
    def dnfCountandReplace(df, LagreCsv=False):
        filt = df['FINISH'] == 'DNF'
        dnf = df[filt]
        dnf = dnf.replace('DNF', 1)
        df.replace('DNF', np.NaN, inplace=True)
        df.dropna(subset=['FINISH'], inplace=True)
        if LagreCsv == True:
            dnf.to_csv('kanskje.csv')
        return df

    @staticmethod
    def changeDataType(df):
        df["FINISH"] = df["FINISH"].str.replace(',', '.').astype(float)
        df["INTER 1"] = df["INTER 1"].str.replace(',', '.').astype(float)
        df["SECTION IM4-FINISH"] = df["SECTION IM4-FINISH"].str.replace(',', '.').astype(float)
        df["COMMENT"] = df['COMMENT'].astype(int)
        df["COMMENT"] = df['COMMENT'].astype(str)
        df["COMMENT"] = df['COMMENT'].str.replace('1', 'COURSE 1')
        df["COMMENT"] = df['COMMENT'].str.replace('2', 'COURSE 2')
        df["COMMENT"] = df['COMMENT'].str.replace('9', 'STRAIGHT-GLIDING')
        pd.to_numeric(df['FINISH'], downcast='float', errors='raise')
        pd.to_numeric(df['INTER 1'], downcast='float', errors='raise')
        pd.to_numeric(df['SECTION IM4-FINISH'], downcast='float', errors='raise')
        return df

    @staticmethod
    def renameCommentToCourse(df):
        df.rename(columns={'COMMENT': 'COURSE'}, inplace=True)
        return df

    @staticmethod
    def findBestRun(df):
        grupper = df.groupby(['BIB#', 'COURSE'])
        bestruns = grupper['FINISH'].apply(lambda x: x.nsmallest(2).mean()).reset_index()
        global df1
        df1 = bestruns.pivot('BIB#', 'COURSE', 'FINISH').reset_index()
        df1['MEAN'] = df1['COURSE 1'].add(df1['COURSE 2']).div(2)
        df1['PRESTASJON'] = df1['MEAN'].div(df1['STRAIGHT-GLIDING'])
        return df1

    @staticmethod
    def allocateGroups(df1):
        df1 = df1.sort_values(by='PRESTASJON', ascending=True)
        mask = np.arange(len(df1)) % 2
        group1 = df1.loc[mask == 0]
        group2 = df1.loc[mask == 1]
        return group1,group2


    @staticmethod
    def groupDataAndFindTwoBestRunsForEachCourse(df):
        global cool
        cool = df.groupby(['BIB#', 'COURSE'])['FINISH'].nsmallest(2).reset_index(ascending=False)
        return cool


    @staticmethod
    def calculateSpeed(df):
        # (x2 - x1) / (t2 - t1)
        x2 = 2
        x1 = 0
        t1 = 0
        for i in df['INTER 1']:
            df['ENTRANCESPEED'] = (x2 - x1) / (df['INTER 1'] - t1)
        return df











    # def __init__(self, Path):
    #     self.path = Path
    #     self.df = None
    #
    # def getDF(self, df):
    #     return self.df
    #
    # def loadData(self, fileName= "pilot1.csv"):
    #     filePath = str(self.path + fileName)
    #     self.df = pd.read_csv(filePath, skiprows=2, decimal=".")
    #     return self.df
    #
    # def dnfCountandReplace(self, df):
    #     filt = self.df['FINISH'] == 'DNF'
    #     dnf = self.df[filt]
    #     dnf = dnf.replace('DNF', 1)
    #     dnf.to_csv('faenta.csv')
    #     self.df.replace('DNF', np.NaN, inplace=True)
    #     self.df.dropna(subset=['FINISH'], inplace=True)
    #     return self.df
    #
    # def changeDataType(self, df):
    #     self.df["FINISH"] = self.df["FINISH"].str.replace(',', '.').astype(float)
    #     self.df["INTER 1"] = self.df["INTER 1"].str.replace(',', '.').astype(float)
    #     self.df["SECTION IM4-FINISH"] = self.df["SECTION IM4-FINISH"].str.replace(',', '.').astype(float)
    #     self.df["COMMENT"] = self.df['COMMENT'].astype(str)
    #     self.df["COMMENT"] = self.df['COMMENT'].str.replace('1', 'COURSE 1').astype(str)
    #     self.df["COMMENT"] = self.df['COMMENT'].str.replace('2', 'COURSE 2').astype(str)
    #     self.df["COMMENT"] = self.df['COMMENT'].str.replace('9', 'STRAIGHT-GLIDING').astype(str)
    #     pd.to_numeric(self.df['FINISH'], downcast='float', errors='raise')
    #     pd.to_numeric(self.df['INTER 1'], downcast='float', errors='raise')
    #     pd.to_numeric(self.df['SECTION IM4-FINISH'], downcast='float', errors='raise')
    #     return self.df
    #
    #
    # def renameCommentToCourse(self, df):
    #     self.df.rename(columns={'COMMENT': 'COURSE'}, inplace=True)
    #     return self.df
    #
    # def groupData(self, df):
    #     self.df.groupby(['BIB#', 'COURSE'])['FINISH']
    #     return self.df
    #
    # def findTwoFastestRunsbyGroup(self, df):
    #     self.df['FINISH'].nsmallest(2)
    #     return self.df
    #
    # def parseToCSV(self, df):
    #     self.df.to_csv('cool.csv')
    #
    # def calculateSpeed(self, df):
    #     # (x2 - x1) / (t2 - t1)
    #     x2 = 2
    #     x1 = 0
    #     t1 = 0
    #     for i in self.df['INTER 1']:
    #         self.df['ENTRANCESPEED'] = (x2 - x1) / (self.df['INTER 1'] - t1)
    #     return df

#
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# class Trening:
#     def __init__(self, Path):
#         self.path = Path
#         self.df = None
#
#     def getDF(self, df):
#         return self.df
#
#     def loadData(self, fileName= "pilot1.csv"):
#         filePath = str(self.path + fileName)
#         self.df = pd.read_csv(filePath, skiprows=2, decimal=".")
#         return self.df
#
#     def dnfCountandReplace(self, df):
#         filt = self.df['FINISH'] == 'DNF'
#         dnf = self.df[filt]
#         dnf = dnf.replace('DNF', 1)
#         dnf.to_csv('faenta.csv')
#         self.df.replace('DNF', np.NaN, inplace=True)
#         self.df.dropna(subset=['FINISH'], inplace=True)
#         return self.df
#
#     def changeDataType(self, df):
#         self.df["FINISH"] = self.df["FINISH"].str.replace(',', '.').astype(float)
#         self.df["INTER 1"] = self.df["INTER 1"].str.replace(',', '.').astype(float)
#         self.df["SECTION IM4-FINISH"] = self.df["SECTION IM4-FINISH"].str.replace(',', '.').astype(float)
#         self.df["COMMENT"] = self.df['COMMENT'].astype(str)
#         self.df["COMMENT"] = self.df['COMMENT'].str.replace('1', 'COURSE 1').astype(str)
#         self.df["COMMENT"] = self.df['COMMENT'].str.replace('2', 'COURSE 2').astype(str)
#         self.df["COMMENT"] = self.df['COMMENT'].str.replace('9', 'STRAIGHT-GLIDING').astype(str)
#         pd.to_numeric(self.df['FINISH'], downcast='float', errors='raise')
#         pd.to_numeric(self.df['INTER 1'], downcast='float', errors='raise')
#         pd.to_numeric(self.df['SECTION IM4-FINISH'], downcast='float', errors='raise')
#         return self.df
#
#
#     def renameCommentToCourse(self, df):
#         self.df.rename(columns={'COMMENT': 'COURSE'}, inplace=True)
#         return self.df
#
#     def groupData(self, df):
#         self.df.groupby(['BIB#', 'COURSE'])['FINISH']
#         return self.df
#
#     def findTwoFastestRunsbyGroup(self, df):
#         self.df['FINISH'].nsmallest(2)
#         return self.df
#
#     def parseToCSV(self, df):
#         self.df.to_csv('cool.csv')
#
#     def calculateSpeed(self, df):
#         # (x2 - x1) / (t2 - t1)
#         x2 = 2
#         x1 = 0
#         t1 = 0
#         for i in self.df['INTER 1']:
#             self.df['ENTRANCESPEED'] = (x2 - x1) / (self.df['INTER 1'] - t1)
#         return df
