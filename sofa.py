# Initialize sofa column names
sofa = []
sofaLimit = 31

for day in range(0, sofaLimit):
    start = 'Data - Registro SOFA ' + str(day)
    end = 'Creatinina - Registro SOFA ' + str(day)
    sofa.append({'start': start, 'end': end})

sofaColumns = [
    'Data - Registro SOFA ',
    'Total - Registro SOFA ',
    'Glasgow - Registro SOFA ',
    'MAP - Registro SOFA ',
    'PaO2 - Registro SOFA ',
    'FiO2 - Registro SOFA ',
    'Ventilação Mecânica - Registro SOFA ',
    'Plaquetas - Registro SOFA ',
    'Bilirrubinas - Registro SOFA ',
    'Débito urinário - Registro SOFA ',
    'Creatinina - Registro SOFA '
]

def appendSofa(transferRow, parentRow, df, outputText):
    offset = lastFilledSofa(parentRow, df) + 1
    limit = lastFilledSofa(transferRow, df)
    increase = limit - 1
    # If there are at least one SOFA on transferRow to pass to parentRow
    if limit > 0:
        try:
            df.loc[parentRow, sofa[offset]['start']:sofa[offset + increase]['end']] = df.loc[transferRow, sofa[1]['start']:sofa[limit]['end']]
        except:
            # In case there wasn't enough SOFA columns, loop to increase until it's enough
            done = False
            while not done:
                with open(outputText, "a") as f:
                    f.write('Aumentando colunas de SOFA\n')
                df = increaseSOFA(df)
                done = True
                # Assume it was enough, try to use it, if it didn't work repeat loop to increase again
                try:
                    df.loc[parentRow, sofa[offset]['start']:sofa[offset + increase]['end']] = df.loc[transferRow, sofa[1]['start']:sofa[limit]['end']]
                except:
                    done = False
        print('Passando colunas: ' + str(1) + ' até ' + str(limit))
        print('Para colunas: ' + str(offset) + ' até ' + str(offset + increase))
    return df

def lastFilledSofa(row, df):
    for day in range(1, sofaLimit):
        if str(df.loc[row, sofa[day]['start']]) == 'N/H':
            return day - 1

def increaseSOFA(df):
    start = sofaLimit
    sofaLimit += 10
    emptyColumn = ['N/H']*len(df.index)
    for day in range(start, sofaLimit):
        start = 'Data - Registro SOFA ' + str(day)
        end = 'Creatinina - Registro SOFA ' + str(day)
        sofa.append({'start': start, 'end': end})
        for col in sofaColumns:
            df[col + day] = emptyColumn
    return df
