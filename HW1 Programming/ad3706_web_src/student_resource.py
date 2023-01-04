import pymysql

class Student:

    def __init__(self):
        # You may have to put code here.
        pass

    def get_by_id(self, ID):
        # Connect to DB.
        conn = pymysql.connect(host="localhost", user="root", password="dbuserdbuser")
        # Form SQL
        sql = ''' select * from db_book.student where ID = %s '''
        pattern_1 = ID
        # Run query
        cur = conn.cursor()
        res = cur.execute(
            sql, args=(pattern_1)
        )
        res = cur.fetchall()
        # return result
        return str(res)
