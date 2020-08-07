import pandas as pd


def Function1():
    data = {'Name': ['Dave', 'Sue', 'John', 'Dave', 'Michael', 'Sue'],
            'QE': ['2019', '12', '14', '15', '16', '17']
            }
    df = pd.DataFrame(data, columns=['Name', 'QE'])
    print(df)

    Quarters = list(df['QE'].unique())
    print(Quarters)

    dfs = []
    for x in Quarters:
         df = df[df['QE'] == x]
         print(df)
    #     df = df['Name'].reset_index(drop=True)
    #     dfs.append(df)
    #
    # return df
    #

Function1()