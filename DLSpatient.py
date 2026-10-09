import DBManager

class dlsPatient:

    # -------- INSERT --------
    @staticmethod
    def addNewPatient(obj):

        query = (
            "INSERT INTO tblpatient "
            "(PatientName, ContactNo, Age, Height, Weight, BloodGroup, EmailID, City, Address) "
            f"VALUES ('{obj.getPatientName()}', '{obj.getContactNo()}', {obj.getAge()}, "
            f"{obj.getHeight()}, {obj.getWeight()}, '{obj.getBloodGroup()}', "
            f"'{obj.getEmailID()}', '{obj.getCity()}', '{obj.getAddress()}');"
        )

        DBManager.QueryExecutor.processQuery(query)

        print("Patient inserted successfully!")


    # -------- UPDATE --------
    @staticmethod
    def updatePatient(obj):

        query = (
            "UPDATE tblpatient SET "
            f"PatientName = '{obj.getPatientName()}', "
            f"ContactNo = '{obj.getContactNo()}', "
            f"Age = {obj.getAge()}, "
            f"Height = {obj.getHeight()}, "
            f"Weight = {obj.getWeight()}, "
            f"BloodGroup = '{obj.getBloodGroup()}', "
            f"EmailID = '{obj.getEmailID()}', "
            f"City = '{obj.getCity()}', "
            f"Address = '{obj.getAddress()}' "
            f"WHERE PatientID = {obj.getPatientID()};"
        )

        DBManager.QueryExecutor.processQuery(query)

        print("Patient updated successfully!")


    # -------- DELETE --------
    @staticmethod
    def deletePatient(obj):

        query = (
            f"DELETE FROM tblpatient WHERE PatientID = {obj.getPatientID()};"
        )

        DBManager.QueryExecutor.processQuery(query)

        print("Patient deleted successfully!")


    # -------- RECORD COUNT --------
    @staticmethod
    def getRecordsCount():

        query = "SELECT COUNT(*) FROM tblpatient;"
        return DBManager.QueryExecutor.getSingleValue(query)


    # -------- FOR COMBOBOX (ONLY NAMES) --------
    @staticmethod
    def getAllPatientNames():

        query = "SELECT PatientName FROM tblpatient;"
        return DBManager.QueryExecutor.getSingleColumn(query)


    # -------- GET ID FROM NAME --------
    @staticmethod
    def getIDFromName(patientName):

        query = f"SELECT PatientID FROM tblpatient WHERE PatientName = '{patientName}';"
        return DBManager.QueryExecutor.getSingleValue(query)


    # -------- GET NAME FROM ID --------
    @staticmethod
    def getNameFromID(patientID):

        query = f"SELECT PatientName FROM tblpatient WHERE PatientID = {patientID};"
        return DBManager.QueryExecutor.getSingleValue(query)


    # -------- TABLE DATA --------
    @staticmethod
    def getAllPatientInformation():

        query = (
            "SELECT PatientID, PatientName, ContactNo, Age, Height, Weight, "
            "BloodGroup, EmailID, City, Address FROM tblpatient"
        )

        return DBManager.QueryExecutor.getAllRows(query)


    # -------- GET FULL RECORD BY ID --------
    @staticmethod
    def getPatientByID(patientID):

        query = (
            f"SELECT * FROM tblpatient WHERE PatientID = {patientID};"
        )

        return DBManager.QueryExecutor.getAllRows(query)
