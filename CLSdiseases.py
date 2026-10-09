import DLSdiseases

class clsDiseases:

    def __init__(self):
        self.__disease_ID = None
        self.__diseases_name = None


    # -------- Setter Methods --------

    def setDiseasesID(self, disease_ID):
        self.__disease_ID = disease_ID

    def setDiseasesName(self, disease_name):
        self.__diseases_name = disease_name


    # -------- Getter Methods --------

    def getDiseasesID(self):
        return self.__disease_ID

    def getDiseasesName(self):
        return self.__diseases_name


    # -------- Show Method --------

    @staticmethod
    def showDiseases(diseases_obj):

        print("Diseases ID   :", diseases_obj.getDiseasesID())
        print("Diseases Name :", diseases_obj.getDiseasesName())


    # -------- CRUD Operations --------

    @staticmethod
    def addNewDiseases(diseases_obj):
        DLSdiseases.dlsDiseases.addNewDisease(diseases_obj)

    @staticmethod
    def updateDiseases(diseases_obj):
        DLSdiseases.dlsDiseases.updateDisease(diseases_obj)

    @staticmethod
    def deleteDiseases(diseases_obj):
        DLSdiseases.dlsDiseases.deleteDisease(diseases_obj)


    # -------- Other Functions --------

    @staticmethod
    def getRecordsCount():
        return DLSdiseases.dlsDiseases.getRecordsCount()


    # ComboBox ke liye (sirf names)
    @staticmethod
    def getAllDiseasesNames():
        return DLSdiseases.dlsDiseases.getAllDiseasesNames()


    @staticmethod
    def getIDFromName(diseaseName):
        return DLSdiseases.dlsDiseases.getIDFromName(diseaseName)


    @staticmethod
    def getNameFromID(diseaseID):
        return DLSdiseases.dlsDiseases.getNameFromID(diseaseID)


    @staticmethod
    def getAllDiseaseInformation():
        return DLSdiseases.dlsDiseases.getAllDiseaseInformation()
