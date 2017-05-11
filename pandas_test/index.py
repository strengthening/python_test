import pandas as pd

df_quote = pd.read_csv('quote.csv' ,index_col = ['DTE','TKR'] , usecols=['DTE','TKR','OPEN','LOW','CLOSE','PRECLSE'])
df_quote0508 = pd.read_csv('quote0508.csv' ,index_col = ['DTE','TKR'] , usecols=['DTE','TKR','OPEN','LOW','CLOSE','PRECLSE'])
df_all = pd.read_csv('all.csv' ,index_col = ['DTE','TKR'] , usecols = ['DTE','TKR','AMT'])

pdata = df_quote.to_panel()
pdata2 = df_quote.append(df_quote0508).to_panel()
pdata3 = pdata2.join( df_all.to_panel() , how = 'outer')

pdata3['RET'] = pdata3['CLOSE'].pct_change()

print pdata3['RET']