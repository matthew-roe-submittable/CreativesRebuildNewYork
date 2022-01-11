#
# Shareholder Database wrapper
#
import mysql.connector

import logging

logger = logging.getLogger("logfile")


class Submitter:

    def __init__(self, conn, id=None):
        self.conn               = conn
        self.id                 = None
        self.unique_id          = None
        self.submission_id      = None
        self.form_response_id   = None
        self.last_name          = None
        self.first_name         = None
        self.date_verified      = None
        self.verified           = None
        if id:
            self.load(id)

    def load_by_submission_id(self, submission_id):
        cur = self.conn.cursor()
        sql = """select id, unique_id, submission_id, form_response_id, first_name, last_name, 
                    date_verified, verified from shareholder where submission_id=%s""" % submission_id

        cur.execute(sql)
        res = cur.fetchall()

        # ID specified does not exist in the database
        if len(res) != 1:
            raise LookupError

        row                     = res[0]
        self.id                 = row[0]
        self.unique_id          = row[1]
        self.submission_id      = row[2]
        self.form_response_id   = row[3]
        self.first_name         = row[4]
        self.last_name          = row[5]
        self.date_verified      = row[6]
        self.verified           = row[7]
        return self

    def load_by_shareholder_id(self, unique_id):
        cur = self.conn.cursor()
        sql = """select id, unique_id, submission_id, form_response_id, first_name, last_name,
                    date_verified, verified from shareholder where unique_id='%s'""" % unique_id
        cur.execute(sql)
        res = cur.fetchall()

        # ID specified does not exist in the database
        if len(res) != 1:
            raise LookupError

        row                     = res[0]
        self.id                 = row[0]
        self.unique_id          = row[1]
        self.submission_id      = row[2]
        self.form_response_id   = row[3]
        self.first_name         = row[4]
        self.last_name          = row[5]
        self.date_verified      = row[6]
        self.verified           = row[7]
        return self

    def load(self, id):
        self.id = id
        cur = self.conn.cursor()
        sql = """select unique_id, submission_id, form_response_id, first_name, last_name, 
                    date_verified, verified from shareholder where id=%s""" % id

        cur.execute(sql)
        res = cur.fetchall()

        # ID specified does not exist in the database
        if len(res) != 1:
            raise LookupError

        row                     = res[0]
        self.id                 = row[0]
        self.unique_id          = row[1]
        self.submission_id      = row[2]
        self.form_response_id   = row[3]
        self.first_name         = row[4]
        self.last_name          = row[5]
        self.date_verified      = row[6]
        self.verified           = row[7]
        return self

    def save(self):
        sql = """update shareholder set unique_id=%s, submission_id=%s, form_response_id=%s, first_name=%s, 
                    last_name=%s, date_verified=%s, verified=%s where id=%s"""
        params = (self.unique_id, self.submission_id, self.form_response_id, self.first_name,
                  self.last_name, self.self.date_verified, self.verified, self.id)

        if self.new():
            sql = """insert into shareholder (unique_id, submission_id, form_response_id, first_name, 
                        last_name, date_verified, verified)
                        values (%s, %s, %s, %s, %s, %s, %s, %s)"""
            params = (self.unique_id, self.submission_id, self.form_response_id, self.first_name,
                      self.last_name, self.self.date_verified, self.verified)

        try:
            cur = self.conn.cursor()
            cur.execute(sql, params)
            self.conn.commit()
        except:
            raise mysql.connector.IntegrityError

        if self.new():
            self.id = cur.lastrowid

    def new(self):
        return self.id is None

    @staticmethod
    def all(conn):
        submitters = []
        sql = """select id, unique_id, submission_id, form_response_id, first_name, last_name, 
                    date_verified, verified  from shareholder"""
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            submitter                     = Submitter(conn)
            submitter.id                  = row[0]
            submitter.unique_id           = row[1]
            submitter.submission_id       = row[2]
            submitter.form_response_id    = row[3]
            submitter.first_name          = row[4]
            submitter.last_name           = row[5]
            submitter.date_verified       = row[7]
            submitter.verified            = row[8]
            submitters.append(submitter)
        return submitters
