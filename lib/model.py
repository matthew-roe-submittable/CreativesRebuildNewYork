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
        self.primary_last_name  = None
        self.primary_zipcode    = None
        self.primary_dob        = None
        self.date_last_checked  = None

        if id:
            self.load(id)

    def load_by_submission_id(self, submission_id):
        cur = self.conn.cursor()
        sql = """select id, primary_unique_id, submission_id, submitter_id, form_response_id, entry_id, primary_last_name, 
        primary_zipcode, primary_dob, date_last_checked from creatives where submission_id=%s""" % submission_id

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
        self.primary_last_name  = row[6]
        self.primary_zipcode    = row[7]
        self.primary_dob        = row[8]
        self.date_last_checked  = row[9]
        return self

    def load_by_primary_unique_id(self, primary_unique_id):
        cur = self.conn.cursor()
        sql = """select id, primary_unique_id, submission_id, submitter_id, form_response_id, entry_id, primary_last_name, 
        primary_zipcode, primary_dob, date_last_checked from creatives where primary_unique_id='%s'""" % primary_unique_id

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
        self.primary_last_name  = row[6]
        self.primary_zipcode    = row[7]
        self.primary_dob        = row[8]
        self.date_last_checked  = row[9]
        return self

    def load(self, id):
        self.id = id
        cur = self.conn.cursor()
        sql = """select primary_unique_id, submission_id, submitter_id, form_response_id, entry_id, primary_last_name, 
        primary_zipcode, primary_dob, date_last_checked from creatives where id=%s""" % id

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
        self.primary_last_name  = row[6]
        self.primary_zipcode    = row[7]
        self.primary_dob        = row[8]
        self.date_last_checked  = row[9]
        return self

    def save(self):

        if self.new():
            sql = """insert into creatives (primary_unique_id, submission_id, submitter_id, form_response_id, entry_id,
            primary_last_name, primary_zipcode, primary_dob, date_last_checked)
                        values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            params = (self.primary_unique_id, self.submission_id, self.submitter_id, self.form_response_id, self.entry_id,
                      self.primary_last_name, self.primary_zipcode, self.primary_dob, self.date_last_checked)
        else:
            sql = """update creatives set primary_unique_id=%s, submission_id=%s, submitter_id=%, form_response_id=%s, entry_id=%s,
            primary_last_name=%s, primary_zipcode=%s, primary_dob=%s, date_last_checkeds=%s
                                where id=%s"""
            params = (self.primary_unique_id, self.submission_id, self.submitter_id, self.form_response_id, self.entry_id,
                      self.primary_last_name, self.primary_zipcode, self.primary_dob, self.date_last_checked, self.id)
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
        sql = """select id, primary_unique_id, submission_id, submitter_id, form_response_id, entry_id, primary_last_name, 
        primary_zipcode, primary_dob, date_last_checked from creatives"""
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            submitter                     = Creative(conn)
            submitter.id                  = row[0]
            submitter.primary_unique_id           = row[1]
            submitter.submission_id       = row[2]
            submitter.submitter_id        = row[3]
            submitter.form_response_id    = row[4]
            submitter.entry_id            = row[5]
            submitter.primary_last_name   = row[6]
            submitter.primary_zipcode     = row[7]
            submitter.primary_dob         = row[8]
            submitter.date_last_checked   = row[9]
            submitters.append(submitter)
        return submitters



class Collaborators:

    def __init__(self, conn, id=None):
        self.conn               = conn
        self.id                 = None
        self.collab_unique_id   = None
        self.submission_id      = None
        self.form_response_id   = None
        self.collab_last_name   = None
        self.collab_zipcode     = None
        self.collab_dob         = None
        self.form_id            = None

        if id:
            self.load(id)

    def load(self, id):
        self.id = id
        cur = self.conn.cursor()
        sql = """select collab_unique_id, submission_id, form_response_id, collab_last_name, collab_zipcode, collab_dob, 
            form_id from collaborators where id=%s""" % id

        cur.execute(sql)
        res = cur.fetchall()

        # ID specified does not exist in the database
        if len(res) != 1:
            raise LookupError

        row                     = res[0]
        self.id                 = row[0]
        self.collab_unique_id   = row[1]
        self.submission_id      = row[2]
        self.form_response_id   = row[3]
        self.collab_last_name   = row[4]
        self.collab_zipcode     = row[5]
        self.collab_dob         = row[6]
        self.form_id            = row[7]
        return self

    def save(self):
        if self.new():
            sql = """insert into collaborators (collab_unique_id, submission_id, form_response_id, collab_last_name,
                collab_zipcode, collab_dob, form_id)
                        values (%s, %s, %s, %s, %s, %s, %s)"""
            params = (self.collab_unique_id, self.submission_id, self.form_response_id, self.collab_last_name,
                      self.collab_zipcode, self.collab_dob, self.form_id)
        else:
            sql = """update collaborators set collab_unique_id=%s, submission_id=%s, form_response_id=%s, collab_last_name=%s,
                collab_zipcode=%s, collab_dob=%s, form_id=%s
                                where id=%s"""
            params = (self.collab_unique_id, self.submission_id, self.form_response_id, self.collab_last_name,
                      self.collab_zipcode, self.collab_dob, self.form_id, self.id)

        try:
            cur = self.conn.cursor()
            cur.execute(sql, params)
            self.conn.commit()
        except:
            print("error collab save")
            raise mysql.connector.IntegrityError

        if self.new():
            self.id = cur.lastrowid

    def new(self):
        return self.id is None

    @staticmethod
    def all(conn):
        collaborators_list = []
        sql = """select id, collab_unique_id, submission_id, form_response_id, collab_last_name, collab_zipcode, 
            collab_dob, form_id from collaborators"""

        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        for row in rows:
            collaborators                   = Collaborators(conn)
            collaborators.id                = row[0]
            collaborators.collab_unique_id  = row[1]
            collaborators.submission_id     = row[2]
            collaborators.form_response_id  = row[3]
            collaborators.collab_last_name  = row[4]
            collaborators.collab_zipcode    = row[5]
            collaborators.collab_dob        = row[6]
            collaborators.form_id           = row[7]
            collaborators_list.append(collaborators)

        return collaborators_list
