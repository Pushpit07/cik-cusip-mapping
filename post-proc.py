import sys

import pandas as pd

df = pd.read_csv(sys.argv[1], names=['f','cik','cusip']).dropna()

df['leng'] = df.cusip.map(len)

df = df[(df.leng==6) | (df.leng==8) | (df.leng==9)]

df['cusip'] = df.cusip

df.cik = pd.to_numeric(df.cik, downcast ='signed')

df = df[['cik','cusip']].drop_duplicates(
            ).to_csv('final_maps.csv',index=False)
