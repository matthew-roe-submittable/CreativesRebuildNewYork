import mysql.connector
from submittable import *
from model import *
import datetime
import config
import logging

file_formatter    = logging.Formatter('%(asctime)s~%(levelname)s~%(message)s~module:%(module)s~function:%(module)s')
console_formatter = logging.Formatter('%(levelname)s -- %(message)s')

file_handler = logging.FileHandler("logs/logfile.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(file_formatter)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(console_formatter)

logger = logging.getLogger("logfile")
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)


#
# Verify Unique Identifier
#


class CreativesRebuildController:

    def __init__(self):
        self.submittable = Submittable(config.submittable_token)
        self.model = self.model(config.mysql_conn)

    def checkUniqueIdentifier(self):
        return

    # update the submitters status in database
    def updateDatabase(self):
        return

    def updateSubmissionLabels(self, subId):
        # call submittable API - get submission
        # check the project id
        # call submittable API - add label "Verification Complete"
        # return true if submission label was added successfully
        return True

    # Compare the UID value to the value in the CSV file
    # update the database ID verification status
    # update the Org. back end verification status by adding a label
    # ONLY verified submitters can receive payment

    def idVerification(self, koniagfile):
        print("idVerification called")
        logger.info("start id verification")
        # load all submitters in database

    # get all submissions
    # get submission id
    # get form id
    # get field values
    # check for duplicate submitter id
    # save into database
    # repeat for all new submissions
    @staticmethod
    def loadDatabaseFromSubmittable():
        logger.info(f"load the database")
        # call to submittable API to get submitter_id, get list of submission ids
        submittable = Submittable(config.submittable_token)
        submission_response = submittable.getListOfSubmissions()
        submissions = []
        # build up submission id list
        for sub_item in submission_response:
            sub_id = sub_item.getSubmissionId()
            submissions.append(sub_id)

        # get form filed value for submitter id
        for sub in submissions:
            # create submitter object for submission
            submitter = Submitter(config.mysql_conn)

            # check the submission is in project
            try:
                sub_response = submittable.getSubmission(sub)
                form_responses = sub_response.getFormResponses()
                # CreativesRebuildNewYork
                if sub_response.getProjectId() != 'replace_with_project_id':
                    # continue to next submitter submission not in project
                    print("submission not in project skip to next submission")
                    continue
            except:
                print("failed")

            # check database for submission by submission id
            # load the submitter if the exist in database
            submitter.load_by_submission_id(sub)

            # print("get submission and from responses")
            sub_response = submittable.getSubmission(sub)
            if sub_response == "get submission failed":
                continue
            form_responses = sub_response.getFormResponses()

            # get each submission form responses
            for form_response in form_responses:
                form_id = form_response.getFormId()
                form_response_by_id = sub_response.getFormResponse(form_id)
                field_data = form_response_by_id.getFieldData()

                for data in field_data:
                    field_id = data.getFormFieldId()
                    field_value = form_response_by_id.getFieldResponse(field_id)
                    field_id = field_value.getFormFieldId()

                    # TODO update field ids
                    if field_id == "583e24e6-1fc5-420f-9447-9cf68d05ca7b":
                        submitter.descendent_name = field_value.getValue()

                    if field_id == "73dbdceb-fe26-494d-99db-e6c9affd0fae":
                        submitter.maiden_name = field_value.getValue()

                    if field_id == "4704c397-8e28-479b-957c-2c4dfc22b12b":
                        print("submitter_id field_value: %s" % str(field_value))
                        submitter.unique_id = field_value.getValue()

            # set the submitter information and save to database
            submitter.submission_id = sub
            # save the submitters to the database
            submitter.save()

        print("finished loading database")
