from lib.submittable import *
from lib.model import *
from datetime import datetime
import config
import logging
import sys

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
        self.submittable  = Submittable()
        self.model        = Creative(config.mysql_conn)
        self.project_id_1 = config.project_id_1
        self.project_id_2 = config.project_id_2
        self.label_id_1   = config.label_id_1
        self.label_id_2   = config.label_id_2
        self.label_id_3   = config.label_id_3


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
        if status == "new" or status == "in_progress":
            self.submittable.addLabel(submission_id, self.label_id_1)
            return True
        else:
            return False


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
        # build up submission id list
        submission_response = self.submittable.getListOfSubmissions()

        for sub_item in submission_response:
            # print("sub item:", sub_item)

            # Create model obj interface to database
            creatives_model = Creative(config.mysql_conn)

            # load database from project 1
            if sub_item.getProjectId() == self.project_id_1:
                print("project 1")
                creatives_model.submission_id  = sub_item.getSubmissionId()
                sub_response                   = self.submittable.getSubmission(creatives_model.submission_id)
                creatives_model.submitter_id   = sub_response.getSubmitterId()
                response_list                  = sub_response.getFormResponses()

                # Skip submission if not in "new" or "in_progress" state
                status = sub_response.getSubmissionStatus()
                if status != "new" and status != "in_progress":
                    print(f"skip sub in project 1 {status}")
                    # go to next submission
                    continue

                # get each submission form responses
                for response in response_list:
                    print("response:", response)
                    # if config == response.getFormId() and config.reference_form_id_2 != response.getFormId():
                    # model.form_response_id  = response.getFormResponseId()
                    field_data = response.getFieldData()
                    form_type = response.getFormType()
                    print("form_type", form_type)

                    # Get the primary artist UID fields
                    for data in field_data:
                        print("project 1 - data in field_data", data)
                        field_id = data.getFormFieldId()
                        # create collaborators model
                        collaborator_model = Collaborators(config.mysql_conn)
                        # Primary Artist UID | DOB-LastName-Zipcode
                        if field_id == config.project_1_artist_last_name:
                            creatives_model.primary_last_name = data.getFieldValue("SHORT_ANSWER")
                            print("creatives_model.primary_last_name", creatives_model.primary_last_name)
                        if field_id == config.project_1_artist_dob:
                            date_string = data.getFieldValue("DATE")
                            creatives_model.primary_dob = date_string[0:10]
                            print("creatives_model.primary_dob", creatives_model.primary_dob)
                        if field_id == config.project_1_artist_zipcode:
                            creatives_model.primary_zipcode = data.getFieldValue("SHORT_ANSWER")
                            print("creatives_model.primary_zipcod", creatives_model.primary_zipcode)
                        # Reference from UIDs
                        if field_id == config.reference_form_field_id_1:
                            print("reference form id", field_id)
                            ref_responses = self.submittable.getReferenceResponses()
                            for resp in ref_responses:
                                ref_field_data = resp.getFieldData()
                                collaborator_model.form_response_id = resp.getFormResponseId()
                                for ref_data in ref_field_data:
                                    print("ref_data 1", ref_data)
                                    item_id = ref_data.getFormFieldId()
                                    if item_id == config.reference_form_name_id:
                                        collaborator_model.primary_last_name = ref_data.getFieldValue("SHORT_ANSWER")
                                    if item_id == config.reference_form_dob_id:
                                        date_string = ref_data.getFieldValue("DATE")
                                        collaborator_model.primary_dob = date_string[0:10]
                                    if item_id == config.reference_form_zipcode_id:
                                        collaborator_model.primary_zipcode = ref_data.getFieldValue("SHORT_ANSWER")
                        if field_id == config.reference_form_field_id_2:
                            print("reference form id", field_id)
                            ref_responses = self.submittable.getReferenceResponses()
                            for resp in ref_responses:
                                ref_field_data         = resp.getFieldData()
                                collaborator_model.form_response_id = resp.getFormResponseId()
                                for ref_data in ref_field_data:
                                    print("ref_data 2", ref_data)
                                    item_id = ref_data.getFormFieldId()
                                    if item_id == config.reference_form_name_id:
                                        collaborator_model.primary_last_name = ref_data.getFieldValue("SHORT_ANSWER")
                                    if item_id == config.reference_form_dob_id:
                                        date_string = ref_data.getFieldValue("DATE")
                                        collaborator_model.primary_dob = date_string[0:10]
                                    if item_id == config.reference_form_zipcode_id:
                                        collaborator_model.primary_zipcode = ref_data.getFieldValue("SHORT_ANSWER")
                        if field_id == config.reference_form_field_id_3:
                            print("reference form id", field_id)
                            ref_responses = self.submittable.getReferenceResponses()
                            for resp in ref_responses:
                                ref_field_data         = resp.getFieldData()
                                collaborator_model.form_response_id = resp.getFormResponseId()
                                for ref_data in ref_field_data:
                                    print("ref_data 3", ref_data)
                                    item_id = ref_data.getFormFieldId()
                                    if item_id == config.reference_form_name_id:
                                        collaborator_model.primary_last_name = ref_data.getFieldValue("SHORT_ANSWER")
                                    if item_id == config.reference_form_dob_id:
                                        date_string = ref_data.getFieldValue("DATE")
                                        collaborator_model.primary_dob = date_string[0:10]
                                    if item_id == config.reference_form_zipcode_id:
                                        collaborator_model.primary_zipcode = ref_data.getFieldValue("SHORT_ANSWER")
                        if field_id == config.reference_form_field_id_4:
                            print("reference form id", field_id)
                            ref_responses = self.submittable.getReferenceResponses()
                            for resp in ref_responses:
                                ref_field_data         = resp.getFieldData()
                                collaborator_model.form_response_id = resp.getFormResponseId()
                                for ref_data in ref_field_data:
                                    print("ref_data 4", ref_data)
                                    item_id = ref_data.getFormFieldId()
                                    if item_id == config.reference_form_name_id:
                                        collaborator_model.primary_last_name = ref_data.getFieldValue("SHORT_ANSWER")
                                    if item_id == config.reference_form_dob_id:
                                        date_string = ref_data.getFieldValue("DATE")
                                        collaborator_model.primary_dob = date_string[0:10]
                                    if item_id == config.reference_form_zipcode_id:
                                        collaborator_model.primary_zipcode = ref_data.getFieldValue("SHORT_ANSWER")
                        if field_id == config.reference_form_field_id_5:
                            print("reference form id", field_id)
                            ref_responses = self.submittable.getReferenceResponses()
                            for resp in ref_responses:
                                ref_field_data         = resp.getFieldData()
                                collaborator_model.form_response_id = resp.getFormResponseId()
                                for ref_data in ref_field_data:
                                    print("ref_data 5", ref_data)
                                    item_id = ref_data.getFormFieldId()
                                    if item_id == config.reference_form_name_id:
                                        collaborator_model.primary_last_name = ref_data.getFieldValue("SHORT_ANSWER")
                                    if item_id == config.reference_form_dob_id:
                                        date_string = ref_data.getFieldValue("DATE")
                                        collaborator_model.primary_dob = date_string[0:10]
                                    if item_id == config.reference_form_zipcode_id:
                                        collaborator_model.primary_zipcode = ref_data.getFieldValue("SHORT_ANSWER")
                        if field_id == config.reference_form_field_id_6:
                            print("reference form id", field_id)
                            ref_responses = self.submittable.getReferenceResponses()
                            for resp in ref_responses:
                                ref_field_data         = resp.getFieldData()
                                collaborator_model.form_response_id = resp.getFormResponseId()
                                for ref_data in ref_field_data:
                                    print("ref_data 6", ref_data)
                                    item_id = ref_data.getFormFieldId()
                                    if item_id == config.reference_form_name_id:
                                        collaborator_model.primary_last_name = ref_data.getFieldValue("SHORT_ANSWER")
                                    if item_id == config.reference_form_dob_id:
                                        date_string = ref_data.getFieldValue("DATE")
                                        collaborator_model.primary_dob = date_string[0:10]
                                    if item_id == config.reference_form_zipcode_id:
                                        collaborator_model.primary_zipcode = ref_data.getFieldValue("SHORT_ANSWER")
                        if field_id == config.reference_form_field_id_7:
                            print("reference form id", field_id)
                            ref_responses = self.submittable.getReferenceResponses()
                            for resp in ref_responses:
                                ref_field_data         = resp.getFieldData()
                                collaborator_model.form_response_id = resp.getFormResponseId()
                                for ref_data in ref_field_data:
                                    print("ref_data 7", ref_data)
                                    item_id = ref_data.getFormFieldId()
                                    if item_id == config.reference_form_name_id:
                                        collaborator_model.primary_last_name = ref_data.getFieldValue("SHORT_ANSWER")
                                    if item_id == config.reference_form_dob_id:
                                        date_string = ref_data.getFieldValue("DATE")
                                        collaborator_model.primary_dob = date_string[0:10]
                                    if item_id == config.reference_form_zipcode_id:
                                        collaborator_model.primary_zipcode = ref_data.getFieldValue("SHORT_ANSWER")
                        if field_id == config.reference_form_field_id_8:
                            print("reference form id", field_id)
                            ref_responses = self.submittable.getReferenceResponses()
                            for resp in ref_responses:
                                ref_field_data         = resp.getFieldData()
                                collaborator_model.form_response_id = resp.getFormResponseId()
                                for ref_data in ref_field_data:
                                    print("ref_data 8", ref_data)
                                    item_id = ref_data.getFormFieldId()
                                    if item_id == config.reference_form_name_id:
                                        collaborator_model.primary_last_name = ref_data.getFieldValue("SHORT_ANSWER")
                                    if item_id == config.reference_form_dob_id:
                                        date_string = ref_data.getFieldValue("DATE")
                                        collaborator_model.primary_dob = date_string[0:10]
                                    if item_id == config.reference_form_zipcode_id:
                                        collaborator_model.primary_zipcode = ref_data.getFieldValue("SHORT_ANSWER")
                        if field_id == config.reference_form_field_id_9:
                            print("reference form id", field_id)
                            ref_responses = self.submittable.getReferenceResponses()
                            for resp in ref_responses:
                                ref_field_data         = resp.getFieldData()
                                collaborator_model.form_response_id = resp.getFormResponseId()
                                for ref_data in ref_field_data:
                                    print("ref_data 9", ref_data)
                                    item_id = ref_data.getFormFieldId()
                                    if item_id == config.reference_form_name_id:
                                        collaborator_model.primary_last_name = ref_data.getFieldValue("SHORT_ANSWER")
                                    if item_id == config.reference_form_dob_id:
                                        date_string = ref_data.getFieldValue("DATE")
                                        collaborator_model.primary_dob = date_string[0:10]
                                    if item_id == config.reference_form_zipcode_id:
                                        collaborator_model.primary_zipcode = ref_data.getFieldValue("SHORT_ANSWER")

                        collaborator_model.submission_id = creatives_model.submission_id
                        print("collab dob:" + str(collaborator_model.collab_dob) + " collab lastname:" + str(collaborator_model.collab_last_name) + " collab zip:" + str(collaborator_model.collab_zipcode))
                        collaborator_model.collab_unique_id = str(collaborator_model.collab_dob) + str(collaborator_model.collab_last_name) + str(collaborator_model.collab_zipcode)

                        try:
                            if collaborator_model.collab_last_name is not None and collaborator_model.collab_dob is not None and collaborator_model.collab_zipcode is not None:
                                print("save to collab table")
                                collaborator_model.save()
                            else:
                                logger.info(f"collaborator UID field Null for submission {creatives_model.submission_id}")
                                # move to next response
                                continue
                        except:
                            try:
                                self.createLabel(sub_response.getSubmissionStatus(), creatives_model.submission_id)
                                logger.info( f"duplicate unique id {collaborator_model.collab_unique_id} in the database already for submission {collaborator_model.submission_id}")
                            except ValueError:
                                logger.info(f"failed to create duplicate label for unique id {collaborator_model.collab_unique_id}")

                creatives_model.date_last_checked = datetime.now().strftime("%Y-%m-%d %H:%M:%SZ")
                print("project 1 UID -", str(creatives_model.primary_dob) + str(creatives_model.primary_last_name) + str(creatives_model.primary_zipcode))

                creatives_model.primary_unique_id = str(creatives_model.primary_dob) + str(creatives_model.primary_last_name) + str(creatives_model.primary_zipcode)
                print("project 1 UID -", creatives_model.primary_unique_id)

                try:
                    print("primary:", creatives_model.primary_last_name, creatives_model.primary_dob, creatives_model.primary_zipcode)
                    if creatives_model.primary_last_name is not None and creatives_model.primary_dob is not None and creatives_model.primary_zipcode is not None:
                        print("project 1 - save db")
                        creatives_model.save()
                        # create internal entry using beta endpoint - Work In Progress
                        creatives_model.entry_id = self.submittable.submitInternalFormResponse(creatives_model.submission_id, creatives_model.unique_id)
                        # self.submittable.updateInternalFormResponse(entry_id, config.internal_form_field_id_1, model.unique_id)
                    else:
                        logger.info(f"primary UID field Null for submission {creatives_model.submission_id}")
                        # skip submission missing UID field(s)
                        continue
                except:
                    try:
                        self.createLabel(sub_response.getSubmissionStatus(), creatives_model.submission_id)
                        logger.info(f"duplicate unique id {creatives_model.unique_id} in the database already for submission {creatives_model.submission_id}")
                    except ValueError:
                        logger.info(f"failed to create duplicate label for unique id {creatives_model.unique_id}")

            # load database from project 2
            elif sub_item.getProjectId() == self.project_id_2:
                print("project 2")
                creatives_model.submission_id = sub_item.getSubmissionId()
                sub_response                  = self.submittable.getSubmission(creatives_model.submission_id)
                creatives_model.submitter_id  = sub_response.getSubmitterId()
                form_responses                = sub_response.getFormResponses()

                # Skip submission if not in "new" or "in_progress" state
                status = sub_response.getSubmissionStatus()
                if status != "new" and status != "in_progress":
                    print(f"skip sub in project 2 {status}")
                    continue

                # get each submission form responses
                for form_response in form_responses:
                    form_id    = form_response.getFormId()
                    responses  = sub_response.getFormResponse(form_id)
                    field_data = responses.getFieldData()

                    for data in field_data:
                        print("project 2 - data in field_data", data)
                        field_id    = data.getFormFieldId()
                        field_value = responses.getFieldResponse(field_id)
                        field_id    = field_value.getFormFieldId()

                        creatives_model.form_response_id = form_response.getFormResponseId()

                        if field_id == config.project_2_name_field_id:
                            creatives_model.primary_last_name = data.getFieldValue("SHORT_ANSWER")
                        if field_id == config.project_2_dob_field_id:
                            date_string = data.getFieldValue("DATE")
                            creatives_model.primary_dob = date_string[0:10]
                        if field_id == config.project_2_zipcode_field_id:
                            creatives_model.primary_zipcode = data.getFieldValue("SHORT_ANSWER")

                creatives_model.date_last_checked = datetime.now().strftime("%Y-%m-%d %H:%M:%SZ")
                print("project 2 UID -", str(creatives_model.primary_dob) + str(creatives_model.primary_last_name) + str(creatives_model.primary_zipcode))
                creatives_model.primary_unique_id = str(creatives_model.primary_dob) + str(creatives_model.primary_last_name) + str(creatives_model.primary_zipcode)
                print("project 2 UID -", creatives_model.primary_unique_id)
                try:
                    if creatives_model.primary_last_name is not None and creatives_model.primary_dob is not None and creatives_model.primary_zipcode is not None:
                        print("project 2 - save db")
                        creatives_model.save()
                        # create internal entry using beta endpoint - Work In Progress
                        creatives_model.entry_id = self.submittable.submitInternalFormResponse(creatives_model.submission_id, creatives_model.primary_unique_id)
                        # self.submittable.updateInternalFormResponse(entry_id, config.internal_form_field_id_1, model.unique_id)
                    else:
                        # skip submission missing UID field(s)
                        continue
                except:
                    try:
                        self.createLabel(sub_response.getSubmissionStatus(), creatives_model.submission_id)
                        logger.info(f"duplicate unique id {creatives_model.primary_unique_id} in the database already for submission {creatives_model.submission_id}")
                    except ValueError:
                        logger.info(f"failed to create duplicate label for unique id {creatives_model.primary_unique_id}")
    print("finished loading database")
