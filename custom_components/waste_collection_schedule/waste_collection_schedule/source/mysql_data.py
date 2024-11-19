import datetime

import MySQLdb
from waste_collection_schedule import Collection


TITLE = "MySQL Source"
DESCRIPTION = "Source for MySQL waste collection."
URL = None
TEST_CASES = {"Example": {"days": 10}}


class Source:
    def __init__(self, host, database, user, password):
        self._host = host
        self._database = database
        self._user = user
        self._password = password

    def fetch(self):
        dbconnect = MySQLdb.connect(host=self._host, user=self._user, password=self._password, database=self._database)
        
        cursor = dbconnect.cursor()
        cursor.execute("SELECT waste_type, collection_date FROM waste_collection WHERE collection_date > DATE_SUB(CURRENT_DATE, INTERVAL 1 DAY)")
        
        resultList = cursor.fetchall()
        
        cursor.close()
        dbconnect.close()
        
        entries = []
        
        for row in resultList:
            entries.append(
                Collection(
                    t = row[0],
                    date = row[1]
                )
            )

        return entries
