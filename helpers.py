from patient import Patient

def getHospitalByUti(uti):
    return uti.split()[0]

def getPatientByRow(row, df):
    return Patient(
        df.loc[row, 'UTI'], # UTI
        df.loc[row,'Paciente'], # Name
        df.loc[row,'Data/horário internamento'], # Admission Date
        df.loc[row,'Registro'], # Register
        df.loc[row,'Prontuário'], # medical Record
        df.loc[row,'Data alta'] # Discharge Date
    )

def comparePatients(previousPatient, currentPatient):
    samePatient = (
        # If it is the same patient
        previousPatient.hospital == currentPatient.hospital and
        previousPatient.name == currentPatient.name and
        previousPatient.register == currentPatient.register and
        previousPatient.medicalRecord == currentPatient.medicalRecord and
        # If it is a transfer
        previousPatient.dischargeDate == currentPatient.admissionDate
    )

    # Confirmar se o registro e prontuário sempre são iguais no reinternamento

# Planilha com 5 pacientes
# 
# todos com o mesmo nome e mesmo registro
# 
# 3 linhas (01/05/2017 marcelino 1 05/05/2017 -> 05/05/2017 marcelino 2 10/05/2017 -> 10/05/2017 marcelino 3 15/05/2017)
# 1 linha (03/05/2017 santa casa 07/05/2017)
# 1 linha (12/05/2017 cajuru 17/05/2017)