from lib.submittable import *
from lib.model import *
from datetime import datetime
import config
import logging

file_formatter    = logging.Formatter('%(asctime)s~%(levelname)s~%(message)s~module:%(module)s~function:%(module)s')
console_formatter = logging.Formatter('%(levelname)s -- %(message)s')

file_handler = logging.FileHandler("../logs/logfile.log")
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
        self.submittable  = Submittable(config.submittable_token)
        self.model        = Creative(config.mysql_conn)
        self.project_id_1 = "47b5697e-a7bb-4096-a708-b576cb218bc5"
        self.project_id_2 = "40a9c8f7-7254-48d1-aa08-bbb90c9984da"
        self.label_id_1   = "317974"
        self.label_id_2   = "317973"
        self.label_id_3   = "317972"


    #
    # update the creative's and/or submission model/table
    #
    def updateDatabase(self):
        return


    #
    # If submission is in the Accepted or Completed status, a ‘Awarded Duplicate’ label will be applied.
    # If submission is in the Withdrawn or Decline status, a ‘Not Awarded Duplicate’ label will be applied.
    # If submission is in the New or In Progress status, a ‘Pending Duplicate’ label will be applied.
    # submissionStatus	(string)
    # Enum: "new" "in_progress" "accepted" "declined" "withdrawn" "completed" "editable" "viewed" "received" "published"
    #
    def createLabel(self, stat, subId):
        submission_id = subId
        status        = stat
        if status == "accepted" or status == "completed":
            self.submittable.addLabel(submission_id, self.label_id_1)
            return True
        elif status == "withdrawn" or status == "declined":
            self.submittable.addLabel(submission_id, self.label_id_2)
            return True
        else:
            # status = "editable" "viewed" "received" "published" "new" "in_progress"
            self.submittable.addLabel(submission_id, self.label_id_3)
            return True


    #
    # Compare the UID value to the value in the CSV file
    # update the database ID verification status
    # update the Org. back end verification status by adding a label
    # ONLY verified submitters can receive payment
    #
    def uidDuplicateCheck(self):
        logger.info("start UID Duplicate check")

        # build up submission id list for project 2
        submission_list = self.submittable.getListOfSubmissions()
        unique_id_list_project_2 = []

        # loop through submissions from project 2 get UID
        for sub_item in submission_list:
            print("sub item:", sub_item)

            if sub_item.getProjectId() == self.project_id_2:
                submission_id  = sub_item.getSubmissionId()
                submission     = self.submittable.getSubmission(submission_id)
                submitter_id   = submission.getSubmitterId()
                form_responses = submission.getFormResponses()

                for response in form_responses:
                    for resp in response:
                        last_name      = resp.getLastName()
                        dob            = resp.getFirstName
                        zipcode        = resp.getFirstName

                # Set the unique id
                unique_id_project_2 = dob + last_name + zipcode
                unique_id_list_project_2.append(unique_id_project_2)


        # load all submitters in database
        creatives = self.model.all()
        for creative in creatives:
            for id in unique_id_list_project_2:
                if creative.unique_id == id:
                    status = None
                    if self.createLabel(status, creative.submission_id):
                        logger.info(f"created duplicate label status: {status} for submission: {creative.submission_id}")



    #
    # get all submissions
    # get submission id
    # get form id
    # get field values
    # save into database
    #
    def loadDatabase(self):
        logger.info(f"load the database")
        # build up submission id list for project 1
        submission_response = self.submittable.getListOfSubmissions()
        for sub_item in submission_response:
            print("sub item:", sub_item)

            model = Creative(config.mysql_conn)

            if sub_item.getProjectId() == self.project_id_2:
                print("project 1", self.project_id_2)
                model.submission_id  = sub_item.getSubmissionId()
                sub_response         = self.submittable.getSubmission(model.submission_id)
                model.submitter_id   = sub_response.getSubmitterId()
                form_responses       = sub_response.getFormResponses()

                # get each submission form responses
                for form_response in form_responses:
                    form_id    = form_response.getFormId()
                    responses  = sub_response.getFormResponse(form_id)
                    field_data = responses.getFieldData()

                    for data in field_data:
                        print("data in field_data", data)
                        field_id    = data.getFormFieldId()
                        field_value = responses.getFieldResponse(field_id)
                        field_id    = field_value.getFormFieldId()

                        model.form_response_id = form_response.getFormResponseId()

                        if field_id == "dca6592c-dd72-4996-b718-8c7773341e11":
                            model.last_name = data.getFieldValue("NAME")
                        if field_id == "969d426a-14bd-4e4e-9110-2c9e0bb69276":
                            date_string = data.getFieldValue("SHORT_ANSWER")
                            model.dob = date_string[0:10]
                        if field_id == "6a5f815a-3ef4-4a31-912b-3d9ad3bc2824":
                            model.zipcode = data.getFieldValue("ADDRESS")

                model.date_last_checked = datetime.now().strftime("%Y-%m-%d %H:%M:%SZ")
                model.unique_id = str(model.dob) + str(model.last_name) + str(model.zipcode)
                print("save")
                try:
                    model.save()
                except:
                    self.createLabel("in_progress", model.submission_id)
            else:
                # No Match continue to next submitter
                continue
    print("finished loading database")
