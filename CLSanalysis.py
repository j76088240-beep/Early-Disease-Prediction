import DLSanalysis

class clsAnalysis:
    def __init__(self):
        self.__AnalysisID = 0
        self.__AnalysisDate = ""
        self.__PatientID = 0
        self.__SymptomsID = 0

    def setAnalysisID(self, val): self.__AnalysisID = val
    def setAnalysisDate(self, val): self.__AnalysisDate = val
    def setPatientID(self, val): self.__PatientID = val
    def setSymptomsID(self, val): self.__SymptomsID = val

    def getAnalysisID(self): return self.__AnalysisID
    def getAnalysisDate(self): return self.__AnalysisDate
    def getPatientID(self): return self.__PatientID
    def getSymptomsID(self): return self.__SymptomsID

    @staticmethod
    def addNewAnalysis(obj): DLSanalysis.dlsAnalysis.addNewAnalysis(obj)
    @staticmethod
    def updateAnalysis(obj): DLSanalysis.dlsAnalysis.updateAnalysis(obj)
    @staticmethod
    def deleteAnalysis(obj): DLSanalysis.dlsAnalysis.deleteAnalysis(obj)
    @staticmethod
    def getAllAnalysisInformation(): return DLSanalysis.dlsAnalysis.getAllAnalysisInformation()
    @staticmethod
    def getPatientsBySymptom(sid): return DLSanalysis.dlsAnalysis.getPatientsBySymptom(sid)
