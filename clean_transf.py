from patient import Patient
import helpers as handle
from datetime import datetime
import pandas as pd

# Create dataframe and column list
# df = pd.read_csv('/mnt/d/Users/Cepeti1/Downloads/export.tsv', sep='\t', infer_datetime_format=True)
# df = pd.read_excel('export.xlsx', sheet_name='Planilha1', engine="openpyxl")
df = pd.read_excel('final.xlsx', sheet_name='Página 1', engine="openpyxl")

print('Importação concluída')


# Tells if each row came from a transfer (False or row index)
orig = df

cameFrom = [False]*len(df.index)

# df.sort_values(by=['Paciente', 'Registro', 'Data/horário internamento'], inplace=True, ascending=[True, True, True])

# df.sort_values(by=['Paciente', 'Registro', 'Data/horário internamento'], ascending=[True, True, True], ignore_index=True)

# Make sure all cells are strings
df['Paciente'] = df['Paciente'].astype('str') 
df['Paciente'] = df['Paciente'].str.strip().str.upper() # Clean trailing and preceding spaces // makes all upper case
df['Destino alta'] = df['Destino alta'].astype('str')
df['Hospital'] = df['Hospital'].astype('str')
df['UTI'] = df['UTI'].astype('str')

df['Registro'] = df['Registro'].astype('Int64', errors='ignore').astype('str')
df['Prontuário'] = df['Prontuário'].astype('Int64', errors='ignore').astype('str')

df['Data internamento'] = pd.to_datetime(df['Data internamento'], format="%d/%m/%Y", errors='ignore')
df['Data alta'] = pd.to_datetime(df['Data alta'], format="%d/%m/%Y", errors='ignore')

df['Data internamento'] = df['Data internamento'].dt.date
df['Data alta'] = df['Data alta'].dt.date

# df.dropna(how='all')
df.drop_duplicates(subset=['Paciente', 'Hospital', 'Data internamento', 'Registro', 'Prontuário', 'Data alta', 'Data nascimento'], keep='first', inplace=True)

df.sort_values(by=['Paciente', 'Hospital', 'Registro', 'Data internamento'], ascending=[True, True, True, True], ignore_index=True, inplace=True)

print('Tratamento de caracteres, remoção de linhas duplicadas e ordenação concluídos')
print('------x------x------x------x------')
print('------x------x------x------x------')
print('------x------x------x------x------')

rowsWithTransfers = df.loc[df['Destino alta'] == 'Outra UTI'].index.tolist()
for row in rowsWithTransfers:
    transferPatient = handle.getPatientByRow(row, df)
    possibleTrasnferedRows = df.loc[(df['Hospital'] == transferPatient.hospital) & (df['Paciente'] == transferPatient.name) & (df['Registro'] == transferPatient.register)].drop(row)
    for index in possibleTrasnferedRows.index.tolist():
        possiblePatient = handle.getPatientByRow(index, df)
        # If is a transfer
        if transferPatient.dischargeDate == possiblePatient.admissionDate:
            cameFrom[possiblePatient.row] = transferPatient.row
            parentRow = handle.getParent(transferPatient.row, cameFrom)
            # Copy discharge data to parent
            print('Paciente ' + transferPatient.name + ' transferido de ' + transferPatient.uti + ' para ' + possiblePatient.uti + ' no dia ' + transferPatient.dischargeDate.strftime('%d/%m/%Y'))
            df.loc[parentRow, 'Tipo alta':'Resumo alta'] = df.loc[possiblePatient.row, 'Tipo alta':'Resumo alta']
            # df = handle.appendSofa(possiblePatient.row, parentRow, df)
            break

print('------x------x------x------x------')
print('------x------x------x------x------')
print('------x------x------x------x------')
print('Cópia de dados de alta de transferências concluída')

for index, parent in enumerate(cameFrom):
    if parent != False:
        df = df.drop(index)

print('Exclusão de linhas de transferências concluída')

df.to_excel("done.xlsx", sheet_name="Página 1", index=False)

print('Exportação concluída sem erros')

# ----------------
# Segmented export
# ----------------

# In case of failure to export all in one file

# Max step achieved on LaptopTI = 10.000 (failed on 30.000)

# Max step achieved on Blade2 = 30.000 (never failed)

# max = len(df.index)
# stop = -1
# step = 10000
# loops = 1
# start = 0
# while start < max:
#     start = stop + 1
#     stop = 10000 * loops
#     df.loc[start:stop].to_excel("ordered" + str(loops) + ".xlsx", sheet_name="Sheet_1", index=False)
#     loops = loops + 1
