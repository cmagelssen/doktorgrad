import seaborn as sns
import matplotlib.pyplot as plt

class Visualisering:
    @staticmethod
    def plotPrestasjon(plot):
        sns.set(style="darkgrid")
        ax = sns.catplot(x="COURSE", y="FINISH", hue="COURSE", col="BIB#", data=plot, s=9, palette="Set2")
        ax.set(xlabel='COURSES', ylabel='FINISH (sec)')
        plt.show()

    @staticmethod
    def plotInngangshastigetForLoyper(plot):
        sns.set(style="darkgrid")
        ax = sns.relplot(x="ENTRANCESPEED", y="FINISH", hue="COURSE", col="BIB#", data=plot, s=80, palette="Set2")
        ax.set(xlabel='ENTRANCE SPEED (m/sek)', ylabel='FINISH (sec)')
        plt.show()

