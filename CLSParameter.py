import DLSParameter

class clsParameters:

    def __init__(self):
        self.__ParameterID = 0
        self.__SymptomID = 0
        self.__DiseaseID = 0

    # -------- Setters & Getters --------
    def setParameterID(self, pid): self.__ParameterID = pid
    def setSymptomID(self, sid): self.__SymptomID = sid
    def setDiseaseID(self, did): self.__DiseaseID = did

    def getParameterID(self): return self.__ParameterID
    def getSymptomID(self): return self.__SymptomID
    def getDiseaseID(self): return self.__DiseaseID

    # -------- Static Methods (Business Logic to Data Layer) --------

    @staticmethod
    def addNewParameter(obj):
        DLSParameter.dlsParameters.addNewParameter(obj)

    @staticmethod
    def updateParameter(obj):
        DLSParameter.dlsParameters.updateParameter(obj)

    @staticmethod
    def deleteParameter(obj):
        # Database se delete karne ke liye Parameter ID pass ki jati hai
        DLSParameter.dlsParameters.deleteParameter(obj.getParameterID())

    @staticmethod
    def getAllParameterInformation():
        return DLSParameter.dlsParameters.getAllParameterInformation()

    @staticmethod
    def getAllParameterInformationExtracted(mDiseaseID=None):
        return DLSParameter.dlsParameters.getAllParameterInformationExtracted(mDiseaseID)

    # Prediction logic: Single Symptom ke basis par
    @staticmethod
    def getDiseasesBySymptom(sid):
        return DLSParameter.dlsParameters.getDiseasesBySymptom(sid)

    # 🔥 NAYA FUNCTION: Patient ki poori history (purane symptoms) ke basis par diagnosis
    @staticmethod
    def getDiseasesByPatientHistory(pid):
        """
        Ye function DLS layer se baat karke us patient ki history 
        ki saari predicted diseases ki list return karega.
        """
        return DLSParameter.dlsParameters.getDiseasesByPatientHistory(pid)
