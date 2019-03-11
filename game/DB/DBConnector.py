import mysql.connector
from game.ConfigDB import ConfigDB as db


class DBConnector:
    # TODO make this singleton
    def __init__(self):
        self.mydb = None

    def connect(self):
        self.mydb = mysql.connector.connect(
            host=db.host, port=db.port, database=db.database,
            user=db.user,
            passwd=db.passwd
        )

    def close(self):
        if self.mydb.is_connected():
            self.mydb.close()

    def get_high_scores(self):
        self.connect()
        mycursor = self.mydb.cursor()
        mycursor.execute("select * from " + db.table_name)
        high_scores = []
        for x in mycursor:
            high_scores.append(x)

        return high_scores
