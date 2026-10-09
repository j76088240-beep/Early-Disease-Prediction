import DLSUser

class clsUser:

    def __init__(self):
        self.__username = ""
        self.__password = ""

    def setUsername(self, username):
        self.__username = username

    def setPassword(self, password):
        self.__password = password

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    @staticmethod
    def checkLogin(obj):
        return DLSUser.dlsUser.checkLogin(obj)
