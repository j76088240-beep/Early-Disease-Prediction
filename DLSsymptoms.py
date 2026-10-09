import DBManager

class dlsSymptoms:


    # -------- INSERT --------
    @staticmethod
    def addNewSymptom(symptoms_obj):

        query = (
            "INSERT INTO tblsymptoms (SymptomsName) "
            f"VALUES ('{symptoms_obj.getSymptomsName()}');"
        )

        DBManager.QueryExecutor.processQuery(query)

        print("Symptoms inserted successfully!")


    # -------- UPDATE --------
    @staticmethod
    def updateSymptom(symptoms_obj):

        query = (
            "UPDATE tblsymptoms SET "
            f"SymptomsName = '{symptoms_obj.getSymptomsName()}' "
            f"WHERE SymptomsID = {symptoms_obj.getSymptomsID()};"
        )

        DBManager.QueryExecutor.processQuery(query)

        print("Symptom updated successfully!")


    # -------- DELETE --------
    @staticmethod
    def deleteSymptom(symptoms_obj):

        query = (
            f"DELETE FROM tblsymptoms WHERE SymptomsID = {symptoms_obj.getSymptomsID()};"
        )

        DBManager.QueryExecutor.processQuery(query)

        print("Symptom deleted successfully!")


    # -------- RECORD COUNT --------
    @staticmethod
    def getRecordsCount():

        query = "SELECT COUNT(*) FROM tblsymptoms;"
        return DBManager.QueryExecutor.getSingleValue(query)


    # -------- COMBOBOX NAMES --------
    @staticmethod
    def getAllSymptomsNames():

        query = "SELECT SymptomsName FROM tblsymptoms;"
        return DBManager.QueryExecutor.getSingleColumn(query)


    # -------- GET ID FROM NAME --------
    @staticmethod
    def getIDFromName(symptomName):

        query = f"SELECT SymptomsID FROM tblsymptoms WHERE SymptomsName = '{symptomName}';"
        return DBManager.QueryExecutor.getSingleValue(query)


    # -------- GET NAME FROM ID --------
    @staticmethod
    def getNameFromID(symptomID):

        query = f"SELECT SymptomsName FROM tblsymptoms WHERE SymptomsID = {symptomID};"
        return DBManager.QueryExecutor.getSingleValue(query)


    # -------- TABLE DATA --------
    @staticmethod
    def getAllSymptomInformation():

        query = "SELECT SymptomsID, SymptomsName FROM tblsymptoms"
        return DBManager.QueryExecutor.getAllRows(query)
