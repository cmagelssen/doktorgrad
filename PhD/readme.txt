I denne hovedfilen har vi tilgang til alle modulene vi trenger for å gjennomføre dataanalysen.

Jeg bruker følgende pakker for analysere dataen: Pandas, Seaborn, Matplotlib, Numpy. Ryddet data blir lagret i en SQLite3 database.

Modulen 'analysetrening' består av en klasse som heter 'Trening'. Denne innholder en rekke statiske metoder (@staticmethods) som rydder og analyserer dataen
 * loadData(): @staticmethod som leser inn .csv filen. Denne tar inn to nødvendige argumenter: path og fileName. F.eks. path = "/Users/cmagelssen/Desktop/DataAnalyse/data/pilot1/trening1/", filename = "PILOT1_SESSION2.csv". x = Trening.loadData(path, filename)
 * dnfCountandReplace(): @staticmethod som filtrer/select rader med DNF i FINISH-kolonnen. Metoden tar imot to argumenter: en dataframe og en LagreCsv som kan settes til True hvis man vil lagre en csv med alle DNF.
 * changeDataType():
 * renameCommentToCourse()
 * groupData()
 * findTwoFastestRunsbyGroup()
 * calculateSpeed
 * getDF

Modulen 'lageplot' inneholder klassen visualisering. Her er det foreløpig to metoder:
 * plotPrestasjon: lager et enkelt plot med loyper som X variabel og FINISH som Y variabel. COURSE er hue. Krever en dataframe som argument
 * plotInngangshastigetForLoyper: lager et enkelt plot for inngangshastighet for de ulike løypene per utøver. Tar X, Y og HUE og krever en DataFrame som et argument
