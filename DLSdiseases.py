import DBManager

class dlsDiseases:

    # -------- INSERT --------
    @staticmethod
    def addNewDisease(diseases_obj):

        query = (
            "INSERT INTO tbldiseases (DiseasesName) "
            f"VALUES ('{diseases_obj.getDiseasesName()}');"
        )

        DBManager.QueryExecutor.processQuery(query)

        print("Disease inserted successfully!")


    # -------- UPDATE --------
    @staticmethod
    def updateDisease(diseases_obj):

        query = (
            "UPDATE tbldiseases SET "
            f"DiseasesName = '{diseases_obj.getDiseasesName()}' "
            f"WHERE DiseasesID = {diseases_obj.getDiseasesID()};"
        )

        DBManager.QueryExecutor.processQuery(query)

        print("Disease updated successfully!")


    # -------- DELETE --------
    @staticmethod
    def deleteDisease(diseases_obj):

        query = (
            f"DELETE FROM tbldiseases WHERE DiseasesID = {diseases_obj.getDiseasesID()};"
        )

        DBManager.QueryExecutor.processQuery(query)

        print("Disease deleted successfully!")


    # -------- RECORD COUNT --------
    @staticmethod
    def getRecordsCount():

        query = "SELECT COUNT(*) FROM tbldiseases;"
        return DBManager.QueryExecutor.getSingleValue(query)


    # -------- FOR COMBOBOX (ONLY NAMES) --------
    @staticmethod
    def getAllDiseasesNames():

        query = "SELECT DiseasesName FROM tbldiseases;"
        return DBManager.QueryExecutor.getSingleColumn(query)


    # -------- GET ID FROM NAME --------
    @staticmethod
    def getIDFromName(diseaseName):

        query = f"SELECT DiseasesID FROM tbldiseases WHERE DiseasesName = '{diseaseName}';"
        return DBManager.QueryExecutor.getSingleValue(query)


    # -------- GET NAME FROM ID --------
    @staticmethod
    def getNameFromID(diseaseID):

        query = f"SELECT DiseasesName FROM tbldiseases WHERE DiseasesID = {diseaseID};"
        return DBManager.QueryExecutor.getSingleValue(query)


    # -------- TABLE DATA --------
    @staticmethod
    def getAllDiseaseInformation():

        query = "SELECT DiseasesID, DiseasesName FROM tbldiseases"
        return DBManager.QueryExecutor.getAllRows(query)
