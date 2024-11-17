import pandas as pd
import os
#%%
param = ['CO2Intensity', 'DiscountedInvestmentPerCitizen', 'LCOE']
path = 'results/221026/results'
for p in param:
    path_in = os.path.join(path, p+'.csv')
    df = pd.read_csv(path_in)
    df_10th = pd.DataFrame()
    df_10th = pd.concat([df_10th, df.iloc[:,-2:]])
    df_10th = pd.concat([df_10th, df.iloc[:,::10]], axis=1)
    path_out = os.path.join(path, p+'_10th.csv')
    df_10th.to_csv(path_out, index=False)