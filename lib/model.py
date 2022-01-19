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
        self.unique_id          = None
        self.submission_id      = None
        self.submitter_id       = None
        self.form_response_id   = None
        self.first_name         = None
        self.last_name          = None
        self.address            = None
        self.zipcode            = None
        self.dob                = None
        self.last4SNN           = None
        self.phone              = None
        self.date_last_checked  = None

        if id:
            self.load(id)

    def load_by_submission_id(self, submission_id):
        cur = self.conn.cursor()
        sql = """select id, unique_id, submission_id, submitter_id, form_response_id, first_name, last_name, address,
        zipcode, dob, last4SNN, phone, date_last_checked from creatives where submission_id=%s""" % submission_id

        cur.execute(sql)
        res = cur.fetchall()

        # ID specified does not exist in the database
        if len(res) != 1:
            raise LookupError

        row                     = res[0]
        self.id                 = row[0]
        self.unique_id          = row[1]
        self.submission_id      = row[2]
        self.submitter_id       = row[3]
        self.form_response_id   = row[4]
        self.first_name         = row[5]
        self.last_name          = row[6]
        self.address            = row[7]
        self.zipcode            = row[8]
        self.dob                = row[9]
        self.last4SNN           = row[10]
        self.phone              = row[11]
        self.date_last_checked  = row[12]
        return self

    def load_by_unique_id(self, unique_id):
        cur = self.conn.cursor()
        sql = """select id, unique_id, submission_id, submitter_id, form_response_id, first_name, last_name, address,
        zipcode, dob, last4SNN, phone, date_last_checked from creatives where unique_id='%s'""" % unique_id

        cur.execute(sql)
        res = cur.fetchall()

        # ID specified does not exist in the database
        if len(res) != 1:
            raise LookupError

        row                     = res[0]
        self.id                 = row[0]
        self.unique_id          = row[1]
        self.submission_id      = row[2]
        self.submitter_id       = row[3]
        self.form_response_id   = row[4]
        self.first_name         = row[5]
        self.last_name          = row[6]
        self.address            = row[7]
        self.zipcode            = row[8]
        self.dob                = row[9]
        self.last4SNN           = row[10]
        self.phone              = row[11]
        self.date_last_checked  = row[12]
        return self

    def load(self, id):
        self.id = id
        cur = self.conn.cursor()
        sql = """select unique_id, submission_id, submitter_id, form_response_id, first_name, last_name, address,
        zipcode, dob, last4SNN, phone, date_last_checked from creatvies where id=%s""" % id

        cur.execute(sql)
        res = cur.fetchall()

        # ID specified does not exist in the database
        if len(res) != 1:
            raise LookupError

        row                     = res[0]
        self.id                 = row[0]
        self.unique_id          = row[1]
        self.submission_id      = row[2]
        self.submitter_id       = row[3]
        self.form_response_id   = row[4]
        self.first_name         = row[5]
        self.last_name          = row[6]
        self.address            = row[7]
        self.zipcode            = row[8]
        self.dob                = row[9]
        self.last4SNN           = row[10]
        self.phone              = row[11]
        self.date_last_checked  = row[12]
        return self

    def save(self):

        if self.new():
            sql = """insert into creatives (unique_id, submission_id, submitter_id, form_response_id, first_name,
            last_name, address, zipcode, dob, last4SNN, phone, date_last_checked)
                        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            params = (self.unique_id, self.submission_id, self.submitter_id, self.form_response_id, self.first_name,
                      self.last_name, self.address, self.zipcode, self.dob, self.last4SNN, self.phone, self.date_last_checked)
        else:
            sql = """update creatives set unique_id=%s, submission_id=%s, submitter_id=%, form_response_id=%s, first_name=%s,
            last_name=%s, address=%s, zipcode=%s, dob=%s, last4SNN=%s, phone=%s, date_last_checkeds=%s
                                where id=%s"""
            params = (self.unique_id, self.submission_id, self.submitter_id, self.form_response_id, self.first_name,
                      self.last_name, self.address, self.zipcode, self.dob, self.last4SNN, self.phone,
                      self.date_last_checked, self.id)

        print(sql)
        print(params)
        try:
            cur = self.conn.cursor()
            cur.execute(sql, params)
            self.conn.commit()
        except:
            print("error")
            # raise mysql.connector.IntegrityError

        if self.new():
            self.id = cur.lastrowid

    def new(self):
        return self.id is None

    @staticmethod
    def all(conn):
        submitters = []
        sql = """select id, unique_id, submission_id, submitter_id, form_response_id, first_name, last_name, address,
        zipcode, dob, last4SNN, phone, date_last_checked from creatives"""
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            submitter                     = Creative(conn)
            submitter.id                  = row[0]
            submitter.unique_id           = row[1]
            submitter.submission_id       = row[2]
            submitter.submitter_id        = row[3]
            submitter.form_response_id    = row[4]
            submitter.first_name          = row[5]
            submitter.last_name           = row[6]
            submitter.address             = row[7]
            submitter.zipcode             = row[8]
            submitter.dob                 = row[9]
            submitter.last4SNN            = row[10]
            submitter.phone               = row[11]
            submitter.date_last_checked   = row[12]
            submitters.append(submitter)
        return submitters
