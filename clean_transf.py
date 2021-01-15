import pandas as pd

# Create dataframe and column list
df = pd.read_csv('export.tsv', sep='\t')

print(df)

new_header = df.iloc[0] #grab the first row for the header
df = df[1:] #take the data less the header row
df.columns = new_header #set the header row as the df header

print(df.columns)

# loc = df.loc[:,:] -- line_start:line_end,row_start:row_end
