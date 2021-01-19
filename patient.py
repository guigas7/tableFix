class Patient:
    def __init__(self, uti, name, admissionDate, register, medicalRecord, dischargeDate, row):
        self.uti = uti
        self.hospital = uti.split()[0]
        self.name = name
        self.admissionDate = admissionDate.split()[0]
        self.register = register
        self.medicalRecord = medicalRecord
        self.dischargeDate = dischargeDate.split()[0]
        self.row = row
