from patient import Patient

# Initialize sofa column names
sofa = []

for day in range(0,32):
    start = 'Data - Registro SOFA ' + str(day)
    end = 'Creatinina - Registro SOFA ' + str(day)
    sofa.append({'start': start, 'end': end})

def getPatientByRow(row, df):
    return Patient(
        df.loc[row, 'Hospital'], # Hospital
        df.loc[row, 'UTI'], # UTI
        df.loc[row, 'Paciente'], # Name
        df.loc[row, 'Data internamento'], # Admission Date
        df.loc[row, 'Registro'], # Register
        df.loc[row, 'Prontuário'], # medical Record
        df.loc[row, 'Data alta'], # Discharge Date
        row
    )

def getParent(row, cameFrom):
    parent = cameFrom[row]
    if parent == False:
        return row
    return getParent(cameFrom[row], cameFrom)

def appendSofa(transferRow, parentRow, df):
    offset = lastFilledSofa(parentRow, df) + 1
    limit = lastFilledSofa(transferRow, df)
    increase = limit - 1
    if limit != 0:
        print('Passando colunas: ' + str(1) + ' até ' + str(limit))
        print('Para colunas: ' + str(offset) + ' até ' + str(offset + increase))
        df.loc[parentRow, sofa[offset]['start']:sofa[offset + increase]['end']] = df.loc[transferRow, sofa[1]['start']:sofa[limit]['end']]
    return df

def lastFilledSofa(row, df):
    for day in range(1,32):
        if str(df.loc[row, sofa[day]['start']]) == 'N/H':
            return day - 1