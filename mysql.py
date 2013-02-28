import MySQLdb

class MySQL:
    def __init_(self, database):
        host = "127.0.0.1"
        username = "root"
        password = "root"
        self.conn = MySQLdb.connect (host = host, user = username, passwd = password, db = database)
        self.cursor = self.conn.cursor()
    
    def query(self, query):
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except:
            raise