import DBManager

class dlsAnalysis:
    # --- INSERT ---
    @staticmethod
    def addNewAnalysis(obj):
        query = (
            "INSERT INTO tblanalysis (AnalysisDate, PatientID, SymptomsID) "
            f"VALUES ('{obj.getAnalysisDate()}', {obj.getPatientID()}, {obj.getSymptomsID()});"
        )
        DBManager.QueryExecutor.processQuery(query)

    # --- UPDATE ---
    @staticmethod
    def updateAnalysis(obj):
        query = (
            "UPDATE tblanalysis SET "
            f"AnalysisDate = '{obj.getAnalysisDate()}', "
            f"PatientID = {obj.getPatientID()}, "
            f"SymptomsID = {obj.getSymptomsID()} "
            f"WHERE AnalysisID = {obj.getAnalysisID()};"
        )
        DBManager.QueryExecutor.processQuery(query)

    # --- DELETE ---
    @staticmethod
    def deleteAnalysis(obj):
        query = f"DELETE FROM tblanalysis WHERE AnalysisID = {obj.getAnalysisID()};"
        DBManager.QueryExecutor.processQuery(query)

    # --- SELECT ALL ---
    @staticmethod
    def getAllAnalysisInformation():
        query = """
        SELECT A.AnalysisID, A.AnalysisDate, A.PatientID, P.PatientName, A.SymptomsID, S.SymptomsName
        FROM tblanalysis A
        INNER JOIN tblpatient P ON A.PatientID = P.PatientID
        INNER JOIN tblsymptoms S ON A.SymptomsID = S.SymptomsID
        """
        return DBManager.QueryExecutor.getAllRows(query)

    # --- PATIENTS WITH SAME SYMPTOM ---
    @staticmethod
    def getPatientsBySymptom(sid):
        query = f"""
            SELECT DISTINCT P.PatientName 
            FROM tblanalysis A
            INNER JOIN tblpatient P ON A.PatientID = P.PatientID
            WHERE A.SymptomsID = {sid}
        """
        return DBManager.QueryExecutor.getSingleColumn(query)
