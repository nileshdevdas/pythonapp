import mysql.connector;

class UserDAO:

    def __init__(self):
        pass;

    def __getConnection(self):
        connection = mysql.connector.connect(user="root", password="root", database="test", host="localhost", port="3306");
        return  connection;


    def save(self):
        try:
            print("Inside userdao....")
            connection = self.__getConnection();
            print(connection)
        except Exception as err:
            print(err);
        finally:
            pass

    def update(self, ):
        try:
            pass
        except:
            pass
        finally:
            pass

    def delete(self, ):
        try:
            pass
        except:
            pass
        finally:
            pass

    def find(self, ):
        try:
            pass
        except:
            pass
        finally:
            pass

