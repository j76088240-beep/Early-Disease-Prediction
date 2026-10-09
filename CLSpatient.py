import DLSpatient

class clsPatient:

    def __init__(self):
        self.__PatientID = None
        self.__PatientName = None
        self.__ContactNo = None
        self.__Age = None
        self.__Height = None
        self.__Weight = None
        self.__BloodGroup = None
        self.__EmailID = None
        self.__City = None
        self.__Address = None


    # -------- Setter Methods --------

    def setPatientID(self, value):
        self.__PatientID = value

    def setPatientName(self, value):
        self.__PatientName = value

    def setContactNo(self, value):
        self.__ContactNo = value

    def setAge(self, value):
        self.__Age = value

    def setHeight(self, value):
        self.__Height = value

    def setWeight(self, value):
        self.__Weight = value

    def setBloodGroup(self, value):
        self.__BloodGroup = value

    def setEmailID(self, value):
        self.__EmailID = value

    def setCity(self, value):
        self.__City = value

    def setAddress(self, value):
        self.__Address = value


    # -------- Getter Methods --------

    def getPatientID(self):
        return self.__PatientID

    def getPatientName(self):
        return self.__PatientName

    def getContactNo(self):
        return self.__ContactNo

    def getAge(self):
        return self.__Age

    def getHeight(self):
        return self.__Height

    def getWeight(self):
        return self.__Weight

    def getBloodGroup(self):
        return self.__BloodGroup

    def getEmailID(self):
        return self.__EmailID

    def getCity(self):
        return self.__City

    def getAddress(self):
        return self.__Address


    # -------- Show Method --------

    @staticmethod
    def showPatient(obj):
        print("Patient ID   :", obj.getPatientID())
        print("Name         :", obj.getPatientName())
        print("Contact No   :", obj.getContactNo())
        print("Age          :", obj.getAge())
        print("Height       :", obj.getHeight())
        print("Weight       :", obj.getWeight())
        print("Blood Group  :", obj.getBloodGroup())
        print("Email        :", obj.getEmailID())
        print("City         :", obj.getCity())
        print("Address      :", obj.getAddress())


    # -------- CRUD Operations --------

    @staticmethod
    def addNewPatient(obj):
        DLSpatient.dlsPatient.addNewPatient(obj)

    @staticmethod
    def updatePatient(obj):
        DLSpatient.dlsPatient.updatePatient(obj)

    @staticmethod
    def deletePatient(obj):
        DLSpatient.dlsPatient.deletePatient(obj)


    # -------- Other Functions --------

    @staticmethod
    def getRecordsCount():
        return DLSpatient.dlsPatient.getRecordsCount()


    @staticmethod
    def getAllPatients():
        return DLSpatient.dlsPatient.getAllPatients()


    @staticmethod
    def getPatientByID(patientID):
        return DLSpatient.dlsPatient.getPatientByID(patientID)
    @staticmethod
    def getAllPatientInformation():
        return DLSpatient.dlsPatient.getAllPatientInformation()
