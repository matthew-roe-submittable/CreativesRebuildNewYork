#
# Creatives Database wrapper
#
import mysql.connector
import logging

logger = logging.getLogger("logfile")


class Creative:

    def __init__(self, conn, id=None):
        self.conn               = conn
        self.id                 = None
        self.primary_unique_id  = None
        self.submission_id      = None
        self.submitter_id       = None
        self.form_response_id   = None
        self.entry_id           = None
        self.collab_unique_id_1 = None
        self.collab_unique_id_2 = None
        self.collab_unique_id_3 = None
        self.collab_unique_id_4 = None
        self.collab_unique_id_5 = None
        self.collab_unique_id_6 = None
        self.collab_unique_id_7 = None
        self.collab_unique_id_8 = None
        self.collab_unique_id_9 = None
        self.date_last_checked  = None

        if id:
            self.load(id)

    def load_by_submission_id(self, submission_id):
        cur = self.conn.cursor()
        sql = """select id, primary_unique_id, submission_id, submitter_id, form_response_id, entry_id, collab_unique_id_1,
        collab_unique_id_2, collab_unique_id_3, collab_unique_id_4, collab_unique_id_5, collab_unique_id_6, collab_unique_id_7,
        collab_unique_id_8, collab_unique_id_9, date_last_checked from creatives where submission_id=%s""" % submission_id

        cur.execute(sql)
        res = cur.fetchall()

        # ID specified does not exist in the database
        if len(res) != 1:
            raise LookupError

        row                     = res[0]
        self.id                 = row[0]
        self.primary_unique_id  = row[1]
        self.submission_id      = row[2]
        self.submitter_id       = row[3]
        self.form_response_id   = row[4]
        self.entry_id           = row[5]
        self.collab_unique_id_1 = row[6]
        self.collab_unique_id_2 = row[7]
        self.collab_unique_id_3 = row[8]
        self.collab_unique_id_4 = row[9]
        self.collab_unique_id_5 = row[10]
        self.collab_unique_id_6 = row[11]
        self.collab_unique_id_7 = row[12]
        self.collab_unique_id_8 = row[13]
        self.collab_unique_id_9 = row[14]
        self.date_last_checked  = row[15]
        return self

    def load_by_primary_unique_id(self, unique_id):
        cur = self.conn.cursor()
        sql = """select id, primary_unique_id, submission_id, submitter_id, form_response_id, entry_id, collab_unique_id_1,
        collab_unique_id_2, collab_unique_id_3, collab_unique_id_4, collab_unique_id_5, collab_unique_id_6, collab_unique_id_7,
        collab_unique_id_8, collab_unique_id_9, date_last_checked from creatives where primary_unique_id='%s'""" % unique_id

        cur.execute(sql)
        res = cur.fetchall()

        # ID specified does not exist in the database
        if len(res) != 1:
            raise LookupError

        row                     = res[0]
        self.id                 = row[0]
        self.primary_unique_id  = row[1]
        self.submission_id      = row[2]
        self.submitter_id       = row[3]
        self.form_response_id   = row[4]
        self.entry_id           = row[5]
        self.collab_unique_id_1 = row[6]
        self.collab_unique_id_2 = row[7]
        self.collab_unique_id_3 = row[8]
        self.collab_unique_id_4 = row[9]
        self.collab_unique_id_5 = row[10]
        self.collab_unique_id_6 = row[11]
        self.collab_unique_id_7 = row[12]
        self.collab_unique_id_8 = row[13]
        self.collab_unique_id_9 = row[14]
        self.date_last_checked  = row[15]
        return self

    def load(self, id):
        self.id = id
        cur = self.conn.cursor()
        sql = """select id, primary_unique_id, submission_id, submitter_id, form_response_id, entry_id, collab_unique_id_1,
        collab_unique_id_2, collab_unique_id_3, collab_unique_id_4, collab_unique_id_5, collab_unique_id_6, collab_unique_id_7,
        collab_unique_id_8, collab_unique_id_9, date_last_checked from creatives where id=%s""" % id

        cur.execute(sql)
        res = cur.fetchall()

        # ID specified does not exist in the database
        if len(res) != 1:
            raise LookupError

        row                     = res[0]
        self.id                 = row[0]
        self.primary_unique_id  = row[1]
        self.submission_id      = row[2]
        self.submitter_id       = row[3]
        self.form_response_id   = row[4]
        self.entry_id           = row[5]
        self.collab_unique_id_1 = row[6]
        self.collab_unique_id_2 = row[7]
        self.collab_unique_id_3 = row[8]
        self.collab_unique_id_4 = row[9]
        self.collab_unique_id_5 = row[10]
        self.collab_unique_id_6 = row[11]
        self.collab_unique_id_7 = row[12]
        self.collab_unique_id_8 = row[13]
        self.collab_unique_id_9 = row[14]
        self.date_last_checked  = row[15]
        return self

    def save(self):

        if self.new():
            sql = """insert into creatives (primary_unique_id, submission_id, submitter_id, form_response_id, entry_id, collab_unique_id_1,
                        collab_unique_id_2, collab_unique_id_3, collab_unique_id_4, collab_unique_id_5, collab_unique_id_6, collab_unique_id_7,
                        collab_unique_id_8, collab_unique_id_9, date_last_checked)
                        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            params = (self.primary_unique_id, self.submission_id, self.submitter_id, self.form_response_id, self.entry_id,
                      self.collab_unique_id_1, self.collab_unique_id_2, self.collab_unique_id_3, self.collab_unique_id_4,
                      self.collab_unique_id_5, self.collab_unique_id_6, self.collab_unique_id_7, self.collab_unique_id_8,
                      self.collab_unique_id_9, self.date_last_checked)
        else:
            sql = """update creatives set primary_unique_id=%s, submission_id=%s, submitter_id=%s, form_response_id=%s, entry_id=%s,
            collab_unique_id_1=%s, collab_unique_id_2=%s, collab_unique_id_3=%s, collab_unique_id_4=%s, collab_unique_id_5=%s,
            collab_unique_id_6=%s, collab_unique_id_7=%s, collab_unique_id_8=%s, collab_unique_id_9=%s, date_last_checked=%s where id=%s"""

            params = (self.primary_unique_id, self.submission_id, self.submitter_id, self.form_response_id, self.entry_id,
                      self.collab_unique_id_1, self.collab_unique_id_2, self.collab_unique_id_3, self.collab_unique_id_4,
                      self.collab_unique_id_5, self.collab_unique_id_6, self.collab_unique_id_7, self.collab_unique_id_8,
                      self.collab_unique_id_9, self.date_last_checked, self.id)
        print(sql)
        print(params)
        try:
            cur = self.conn.cursor()
            cur.execute(sql, params)
            self.conn.commit()
            print("SAVED")

        except:
            print("error creatives save")
            raise mysql.connector.IntegrityError

        if self.new():
            self.id = cur.lastrowid

    def new(self):
        return self.id is None

    @staticmethod
    def all(conn):
        submitters = []
        sql = """select id, primary_unique_id, submission_id, submitter_id, form_response_id, entry_id, collab_unique_id_1,
        collab_unique_id_2, collab_unique_id_3, collab_unique_id_4, collab_unique_id_5, collab_unique_id_6, collab_unique_id_7,
        collab_unique_id_8, collab_unique_id_9, date_last_checked from creatives"""

        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            submitter                     = Creative(conn)
            submitter.id                  = row[0]
            submitter.primary_unique_id   = row[1]
            submitter.submission_id       = row[2]
            submitter.submitter_id        = row[3]
            submitter.form_response_id    = row[4]
            submitter.entry_id            = row[5]
            submitter.collab_unique_id_1  = row[6]
            submitter.collab_unique_id_2  = row[7]
            submitter.collab_unique_id_3  = row[8]
            submitter.collab_unique_id_4  = row[9]
            submitter.collab_unique_id_5  = row[10]
            submitter.collab_unique_id_6  = row[11]
            submitter.collab_unique_id_7  = row[12]
            submitter.collab_unique_id_8  = row[13]
            submitter.collab_unique_id_9  = row[14]
            submitter.primary_last_name   = row[15]
            submitter.primary_zipcode     = row[16]
            submitter.primary_dob         = row[17]
            submitter.date_last_checked   = row[18]
            submitters.append(submitter)
        return submitters
