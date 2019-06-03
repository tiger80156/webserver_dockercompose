import pymysql
import os

MYSQLURL = os.environ["MYSQLURL"]
MYSQLPORT = os.environ["MYSQLPORT"]
MYSQLUSERNAME = os.environ["MYSQLUSERNAME"]
MYSQLURLPASSWORD = os.environ["MYSQLPASSWORD"]
MYSQLDATABASE = os.environ["MYSQLDATABASE"]


class MysqlInstance():
    def __init__(self, url, username, password, port, db):
        self.db = pymysql.connect(
            host=url, user=username, password=password, port=int(port), database=db)

    def NewUser(self, newusername, newpassword):
        with self.db.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `users` (`username`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, (newusername, newpassword))
            self.db.commit()


mysqlInstance = MysqlInstance(
    url=MYSQLURL, username=MYSQLUSERNAME, password=MYSQLURLPASSWORD, port=MYSQLPORT, db=MYSQLDATABASE)
