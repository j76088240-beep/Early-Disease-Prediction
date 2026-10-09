import DBManager   

class dlsUser:

    @staticmethod
    def checkLogin(obj):

        query = f"""
        SELECT * FROM tbluser
        WHERE username = '{obj.getUsername()}'
        AND password = '{obj.getPassword()}'
        """

        result = DBManager.QueryExecutor.getAllRows(query)

        return True if result else False

