'Initial test file'

import pandas as pd

df = pd.read_excel('data/n_fot2022-01-12.xls')

# Clean the data
df.dropna(inplace=True)         # Remove None and NaN
df = df.set_index('Unnamed: 0') # Set date and time to index
df.columns = df.loc['Tid']      # Set correct labels on columns
df = df[1:]                     # Remove first row
df.columns.name = 'MWh'         # Remove ugly label on columns
df.index.name = 'Tid'           # Remove ugly "Unknown: 0"

# Make total consumption from negative to positive
df['Total förbrukning'] = df['Total förbrukning'] * -1

print(df)
