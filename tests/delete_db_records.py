import config


print("create connect to db")
conn = config.mysql_conn


class db_interface():
    @staticmethod
    def deleteCreativesTableData():
        cur = conn.cursor()
        sql = """delete from creatives where id>0"""
        cur.execute(sql)
        conn.commit()
        print(cur.rowcount, "record(s) deleted")


db_interface.deleteCreativesTableData()
