from patient import Patient
import helpers as handle
from datetime import datetime
import pandas as pd

# Create dataframe and column list
# df = pd.read_csv('/mnt/d/Users/Cepeti1/Downloads/export.tsv', sep='\t', infer_datetime_format=True)
df = pd.read_excel('/mnt/d/Users/Cepeti1/Downloads/export.xlsx', sheet_name='Planilha1', engine="openpyxl")

toDelete = [False]*len(df.index)

dup = df[].duplicated()

# df.sort_values(by=['Paciente', 'Registro', 'Data/horário internamento'], inplace=True, ascending=[True, True, True])

# df.sort_values(by=['Paciente', 'Registro', 'Data/horário internamento'], ascending=[True, True, True], ignore_index=True)

# df.head(15000).to_excel("output.xlsx", sheet_name="Sheet_1", index=False)

df['Data/horário internamento'] = pd.to_datetime(df['Data/horário internamento'], format="%d/%m/%Y %H:%M:%S", errors='coerce')
df['Data alta'] = pd.to_datetime(df['Data alta'], format="%d/%m/%Y %H:%M", errors='coerce')

df.dropna(how='all')

df = df.sort_values(by=['Paciente', 'Registro', 'Data/horário internamento'], ascending=[True, True, True], ignore_index=True)

print(datetime.now().strftime('%T'))
print('Terminou de ordenar')

max = len(df.index)
stop = -1
step = 10000
loops = 1
start = 0
while start < max:
    start = stop + 1
    stop = 10000 * loops
    df.loc[start:stop].to_excel("ordered" + str(loops) + ".xlsx", sheet_name="Sheet_1", index=False)
    loops = loops + 1

print(datetime.now().strftime('%T'))
print('Terminou de exportar')
previousPatient = Patient(0, df)
for row in df.index.values[1:].tolist(): # removes first patient so it doesn't start without a previous patient
    if toDelete == True:
        currentPatient = Patient(row, df)
        comparison = comparePatients(previous, current)
        if comparison == -1:
            toDelete[row] = True
        if comparison == 1:
            # This patient has at least one namesake
            FirstLineData = previousPatient
            # for each line of this patient, in this hospital, if any transfer is found, copy the data
            lineOfTreatment = FirstLineData
            samePatient = true
            while samePatient
            # toAppend = current
            # Loop de transferência aka while comparePatients(FirstLineData, toAppend) == 1
                # appendSofa(toAppend.row, firstLineData.row, toDelete) # marks to delete toAppend's row on array toDelete
            # CopyDischarge(toAppend.row - 1, firstLineData.row)

    # previousPatient = currentPatient
