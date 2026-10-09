import mysql.connector
class QueryExecutor:

    @staticmethod
    def processQuery(Query):
        # Display generated query
        print("Generated SQL Query:")
        #print(Query)

        try:
            # Establish connection
            connection = mysql.connector.connect(
                host="localhost",
                user="root",            # change if your username is different
                password="System",    # put your MySQL password here
                database="diseaseprediction"
            )

            if connection.is_connected():
                print("Successfully connected to MySQL database: predictiondatamap")

            # Create cursor
            cursor = connection.cursor()

            cursor.execute(Query)
            connection.commit()

        except mysql.connector.Error as e:
            print("Error while connecting to MySQL:", e)

        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection closed")

    @staticmethod
    def getSingleValue(Query):
        # Display generated query
        print("Generated SQL Query:")
        #print(Query)

        value =0

        try:
            # Establish connection
            connection = mysql.connector.connect(
                host="localhost",
                user="root",            # change if your username is different
                password="System",    # put your MySQL password here
                database="diseaseprediction"
            )

            if connection.is_connected():
                print("Successfully connected to MySQL database: predictiondatamap")

            # Create cursor
            cursor = connection.cursor()

            cursor.execute(Query)
            
            row = cursor.fetchone()
            if row is not None:
                value = row[0]
            else:
                value = None  # or some default, e.g., 0, empty tuple, etc.


        except mysql.connector.Error as e:
            print("Error while connecting to MySQL:", e)

        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection closed")

        return(value) 



    @staticmethod
    def getSingleColumn(Query):
        # Display generated query
        print("Generated SQL Query:")
        #print(Query)

        value = ()

        try:
            # Establish connection
            connection = mysql.connector.connect(
                host="localhost",
                user="root",            # change if your username is different
                password="System",    # put your MySQL password here
                database="diseaseprediction"
            )

            if connection.is_connected():
                print("Successfully connected to MySQL database: predictiondatamap")

            # Create cursor
            cursor = connection.cursor()
            cursor.execute(Query)
            rows = cursor.fetchall()  # fetch all rows
            #print("Purva",rows)
            value = [row[0] for row in rows]  # first column of each row

        except mysql.connector.Error as e:
            print("Error while connecting to MySQL:", e)

        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection closed")

        return value

    @staticmethod
    def getSingleRow(Query):
        # Display generated query
        print("Generated SQL Query:")
        #print(Query)

        value = ()

        try:
            # Establish connection
            connection = mysql.connector.connect(
                host="localhost",
                user="root",            # change if your username is different
                password="System",    # put your MySQL password here
                database="diseaseprediction"
            )

            if connection.is_connected():
                print("Successfully connected to MySQL database: predictiondatamap")

            # Create cursor
            cursor = connection.cursor()
            cursor.execute(Query)
            rows = cursor.fetchall()  # fetch all rows
            value = tuple(row for row in rows[0])  # first column of each row

        except mysql.connector.Error as e:
            print("Error while connecting to MySQL:", e)

        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection closed")

        return value


    @staticmethod
    def getAllRows(query):
        
        rows = []   # initialize first
        try:
            connection = mysql.connector.connect(
                    host="localhost",
                    user="root",            # change if your username is different
                    password="System",    # put your MySQL password here
                database="diseaseprediction"
                )
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

        return rows
