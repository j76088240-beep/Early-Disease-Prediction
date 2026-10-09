import DBManager

class dlsParameters:

    @staticmethod
    def addNewParameter(obj):
        query = "insert into tblparameters(DiseasesID,SymptomsID) values({},{})".format(
            obj.getDiseaseID(),
            obj.getSymptomID()
        )
        DBManager.QueryExecutor.processQuery(query)

    @staticmethod
    def getAllParameterInformation():
        query = "SELECT ParameterID, SymptomsID, DiseasesID FROM tblparameters"
        return DBManager.QueryExecutor.getAllRows(query)

    @staticmethod
    def getAllParameterInformationExtracted(mDiseaseID=None):
        if mDiseaseID is None or mDiseaseID == 0:
            query = """
            SELECT P.ParameterID, P.SymptomsID, S.SymptomsName, P.DiseasesID, D.DiseasesName
            FROM tblparameters P
            INNER JOIN tblsymptoms S ON P.SymptomsID = S.SymptomsID 
            INNER JOIN tbldiseases D ON P.DiseasesID = D.DiseasesID
            """
        else:
            query = f"""
            SELECT P.ParameterID, P.SymptomsID, S.SymptomsName, P.DiseasesID, D.DiseasesName
            FROM tblparameters P
            INNER JOIN tblsymptoms S ON P.SymptomsID = S.SymptomsID 
            INNER JOIN tbldiseases D ON P.DiseasesID = D.DiseasesID
            WHERE P.DiseasesID = {mDiseaseID}
            """
        return DBManager.QueryExecutor.getAllRows(query)

    # ✅ Symptom wise diseases (TOP TABLE)
    @staticmethod
    def getDiseasesBySymptom(sid):
        query = f"""
        SELECT D.DiseasesName 
        FROM tblparameters P
        INNER JOIN tbldiseases D ON P.DiseasesID = D.DiseasesID
        WHERE P.SymptomsID = {sid}
        """
        return DBManager.QueryExecutor.getSingleColumn(query)

    # 🔥 FINAL SMART LOGIC (ONLY MAX MATCH DISEASES)
    @staticmethod
    def getDiseasesByPatientHistory(pid):
        query = f"""
        SELECT D.DiseasesName, COUNT(*) as match_count
        FROM tblanalysis A
        INNER JOIN tblparameters P ON A.SymptomsID = P.SymptomsID
        INNER JOIN tbldiseases D ON P.DiseasesID = D.DiseasesID
        WHERE A.PatientID = {pid}
        GROUP BY D.DiseasesName
        HAVING COUNT(*) = (
            SELECT MAX(cnt) FROM (
                SELECT COUNT(*) as cnt
                FROM tblanalysis A2
                INNER JOIN tblparameters P2 ON A2.SymptomsID = P2.SymptomsID
                WHERE A2.PatientID = {pid}
                GROUP BY P2.DiseasesID
            ) as temp
        )
        """
        return DBManager.QueryExecutor.getAllRows(query)

    @staticmethod
    def deleteParameter(pid):
        query = f"delete from tblparameters where ParameterID={pid}"
        DBManager.QueryExecutor.processQuery(query)

    @staticmethod
    def updateParameter(obj):
        query = f"""
        update tblparameters 
        set DiseasesID={obj.getDiseaseID()}, SymptomsID={obj.getSymptomID()}
        where ParameterID={obj.getParameterID()}
        """
        DBManager.QueryExecutor.processQuery(query)
