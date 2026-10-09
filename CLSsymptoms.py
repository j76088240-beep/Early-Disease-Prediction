import DLSsymptoms

class clsSymptoms:

    def __init__(self):
        self.__symptom_ID = None
        self.__symptom_name = None


    # -------- Setter Methods --------

    def setSymptomsID(self, symptom_ID):
        self.__symptom_ID = symptom_ID

    def setSymptomsName(self, symptom_name):
        self.__symptom_name = symptom_name


    # -------- Getter Methods --------

    def getSymptomsID(self):
        return self.__symptom_ID

    def getSymptomsName(self):
        return self.__symptom_name


    # -------- Display --------

    @staticmethod
    def showSymptoms(symptoms_obj):

        print("Symptoms ID   :", symptoms_obj.getSymptomsID())
        print("Symptoms Name :", symptoms_obj.getSymptomsName())


    # -------- CRUD --------

    @staticmethod
    def addNewSymptom(symptoms_obj):
        DLSsymptoms.dlsSymptoms.addNewSymptom(symptoms_obj)

    @staticmethod
    def updateSymptom(symptoms_obj):
        DLSsymptoms.dlsSymptoms.updateSymptom(symptoms_obj)

    @staticmethod
    def deleteSymptom(symptoms_obj):
        DLSsymptoms.dlsSymptoms.deleteSymptom(symptoms_obj)


    # -------- Other Methods --------

    @staticmethod
    def getRecordsCount():
        return DLSsymptoms.dlsSymptoms.getRecordsCount()


    # ComboBox ke liye (sirf names)
    @staticmethod
    def getAllSymptomsNames():
        return DLSsymptoms.dlsSymptoms.getAllSymptomsNames()


    @staticmethod
    def getIDFromName(symptomName):
        return DLSsymptoms.dlsSymptoms.getIDFromName(symptomName)


    @staticmethod
    def getNameFromID(symptomID):
        return DLSsymptoms.dlsSymptoms.getNameFromID(symptomID)


    @staticmethod
    def getAllSymptomInformation():
        return DLSsymptoms.dlsSymptoms.getAllSymptomInformation()
