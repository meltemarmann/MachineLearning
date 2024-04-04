import pandas as pd

df = pd.read_csv('fineTune.csv')

df[0:400].to_csv('fineTune400.csv', index=False)