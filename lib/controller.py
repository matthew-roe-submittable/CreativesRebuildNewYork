from lib.submittable import *
from lib.model import *
from datetime import datetime
import config
import logging
import sys

file_formatter = logging.Formatter('%(asctime)s~%(levelname)s~%(message)s~module:%(module)s~function:%(module)s')
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
        self.submittable = Submittable()
        self.model = Creative(config.mysql_conn)
        self.project_id_1 = config.project_id_1
        self.project_id_2 = config.project_id_2
        self.label_id_1 = config.label_id_1
        self.label_id_2 = config.label_id_2
        self.label_id_3 = config.label_id_3

    #
    # If submission is in the Accepted or Completed status, a ‘Awarded Duplicate’ label will be applied.
    # If submission is in the Withdrawn or Decline status, a ‘Not Awarded Duplicate’ label will be applied.
    # If submission is in the New or In Progress status, a ‘Pending Duplicate’ label will be applied.
    # submissionStatus	(string)
    # Enum: "new" "in_progress" "accepted" "declined" "withdrawn" "completed" "editable" "viewed" "received" "published"
    #
    def createLabel(self, stat, subId):
        submission_id = subId
        status = stat
        if status == "new" or status == "in_progress":
            self.submittable.addLabel(submission_id, self.label_id_1)
            return True
        else:
            return False

    #
    # get all submissions
    # get submission id
    # get form id
    # get field values
    # save into database
    #
    def loadArtistsToDatabase(self):
        logger.info(f"loading artists into database")

        # build up submission id list
        list_of_submissions = self.submittable.getListOfSubmissions()

        for sub_item in list_of_submissions:
            # Create model obj interface to database
            creatives_model = Creative(config.mysql_conn)

            # try to load model
            try:
                creatives_model.load_by_submission_id(sub_item.getSubmissionId())
                print("model id", creatives_model.id)
            except:
                print("new submission")

            # load database from project 1
            if sub_item.getProjectId() == self.project_id_1:
                print("project 1 - Submission")

                creatives_model.submission_id = sub_item.getSubmissionId()
                sub_response = self.submittable.getSubmission(creatives_model.submission_id)
                creatives_model.submitter_id = sub_response.getSubmitterId()
                # get submission form responses
                response_list = sub_response.getFormResponses()

                # Skip submission if not in "new" or "in_progress" state
                status = sub_response.getSubmissionStatus()
                if status != "new" and status != "in_progress":
                    print(f"project 1 - skip sub in project 1 {status}")
                    # go to next submission
                    continue

                print("project 1 - response list length:", len(response_list))

                # go through response list
                for response in response_list:

                    # create local variables
                    primary_last_name = None
                    primary_dob = None
                    primary_zip = None

                    collab_last_name_1 = None
                    collab_dob_1 = None
                    collab_zip_1 = None

                    collab_last_name_2 = None
                    collab_dob_2 = None
                    collab_zip_2 = None

                    collab_last_name_3 = None
                    collab_dob_3 = None
                    collab_zip_3 = None

                    collab_last_name_4 = None
                    collab_dob_4 = None
                    collab_zip_4 = None

                    collab_last_name_5 = None
                    collab_dob_5 = None
                    collab_zip_5 = None

                    collab_last_name_6 = None
                    collab_dob_6 = None
                    collab_zip_6 = None

                    collab_last_name_7 = None
                    collab_dob_7 = None
                    collab_zip_7 = None

                    collab_last_name_8 = None
                    collab_dob_8 = None
                    collab_zip_8 = None

                    collab_last_name_9 = None
                    collab_dob_9 = None
                    collab_zip_9 = None

                    dup_found = False
                    id_list_check = None

                    # Pull the forms response data
                    field_data = response.getFieldData()
                    # Get the primary artist UID fields
                    for data in field_data:
                        # print("project 1 - data in field_data", data)
                        field_id = data.getFormFieldId()
                        print("field_id", field_id)

                        # Primary Artist UID | DOB-LastName-Zipcode
                        if field_id == config.project_1_artist_last_name:
                            primary_last_name = data.getFieldValue("SHORT_ANSWER")
                        if field_id == config.project_1_artist_dob:
                            date_string = data.getFieldValue("DATE")
                            primary_dob = date_string[0:10]
                        if field_id == config.project_1_artist_zipcode:
                            primary_zip = data.getFieldValue("SHORT_ANSWER")

                        # Reference from UIDs
                        if field_id == config.reference_form_field_id_1:
                            print("reference form id 1", field_id)
                            # get reference form responses (collaborator artist form only)
                            reference_responses = self.submittable.getReferenceResponses()
                            print("response len", len(reference_responses))
                            count = 0
                            for resp in reference_responses:
                                count = count + 1
                                print("resp", count)
                                if field_id == resp.getFormFieldId():
                                    ref_field_data = resp.getFieldData()
                                    creatives_model.form_response_id = resp.getFormResponseId()
                                    for ref_data in ref_field_data:
                                        print("ref_data 1", ref_data)
                                        item_id = ref_data.getFormFieldId()
                                        if item_id == config.reference_form_name_id:
                                            collab_last_name_1 = ref_data.getFieldValue("SHORT_ANSWER")
                                        if item_id == config.reference_form_dob_id:
                                            date_string = ref_data.getFieldValue("DATE")
                                            collab_dob_1 = date_string[0:10]
                                        if item_id == config.reference_form_zipcode_id:
                                            collab_zip_1 = ref_data.getFieldValue("SHORT_ANSWER")
                                    creatives_model.collab_unique_id_1 = str(collab_dob_1) + str(
                                        collab_last_name_1) + str(collab_zip_1)
                                    creatives_model.collab_unique_id_1 = creatives_model.collab_unique_id_1.replace(" ",
                                                                                                                    "")
                                    print("creatives_model.collab_unique_id_1", creatives_model.collab_unique_id_1)

                        if field_id == config.reference_form_field_id_2:
                            print("reference form id 2", field_id)
                            reference_responses = self.submittable.getReferenceResponses()
                            for resp in reference_responses:
                                print("resp 2")
                                if field_id == config.reference_form_field_id_2:
                                    ref_field_data = resp.getFieldData()
                                    creatives_model.form_response_id = resp.getFormResponseId()
                                    for ref_data in ref_field_data:
                                        print("ref_data 2", ref_data)
                                        item_id = ref_data.getFormFieldId()
                                        if item_id == config.reference_form_name_id:
                                            collab_last_name_2 = ref_data.getFieldValue("SHORT_ANSWER")
                                        if item_id == config.reference_form_dob_id:
                                            date_string = ref_data.getFieldValue("DATE")
                                            collab_dob_2 = date_string[0:10]
                                        if item_id == config.reference_form_zipcode_id:
                                            collab_zip_2 = ref_data.getFieldValue("SHORT_ANSWER")
                                    creatives_model.collab_unique_id_2 = str(collab_dob_2) + str(
                                        collab_last_name_2) + str(collab_zip_2)
                                    creatives_model.collab_unique_id_2 = creatives_model.collab_unique_id_2.replace(" ",
                                                                                                                    "")
                                    print("creatives_model.collab_unique_id_2", creatives_model.collab_unique_id_2)

                        if field_id == config.reference_form_field_id_3:
                            print("reference form id 3", field_id)
                            reference_responses = self.submittable.getReferenceResponses()
                            for resp in reference_responses:
                                print("resp 3")
                                if field_id == config.reference_form_field_id_3:
                                    ref_field_data = resp.getFieldData()
                                    creatives_model.form_response_id = resp.getFormResponseId()
                                    for ref_data in ref_field_data:
                                        print("ref_data 3", ref_data)
                                        item_id = ref_data.getFormFieldId()
                                        if item_id == config.reference_form_name_id:
                                            collab_last_name_3 = ref_data.getFieldValue("SHORT_ANSWER")
                                        if item_id == config.reference_form_dob_id:
                                            date_string = ref_data.getFieldValue("DATE")
                                            collab_dob_3 = date_string[0:10]
                                        if item_id == config.reference_form_zipcode_id:
                                            collab_zip_3 = ref_data.getFieldValue("SHORT_ANSWER")
                                    creatives_model.collab_unique_id_3 = str(collab_dob_3) + str(
                                        collab_last_name_3) + str(collab_zip_3)
                                    creatives_model.collab_unique_id_3 = creatives_model.collab_unique_id_3.replace(" ",
                                                                                                                    "")
                                    print("creatives_model.collab_unique_id_3", creatives_model.collab_unique_id_3)

                        if field_id == config.reference_form_field_id_4:
                            # print("reference form id", field_id)
                            reference_responses = self.submittable.getReferenceResponses()
                            for resp in reference_responses:
                                if field_id == config.reference_form_field_id_4:
                                    ref_field_data = resp.getFieldData()
                                    creatives_model.form_response_id = resp.getFormResponseId()
                                    for ref_data in ref_field_data:
                                        # print("ref_data 4", ref_data)
                                        item_id = ref_data.getFormFieldId()
                                        if item_id == config.reference_form_name_id:
                                            collab_last_name_4 = ref_data.getFieldValue("SHORT_ANSWER")
                                        if item_id == config.reference_form_dob_id:
                                            date_string = ref_data.getFieldValue("DATE")
                                            collab_dob_4 = date_string[0:10]
                                        if item_id == config.reference_form_zipcode_id:
                                            collab_zip_4 = ref_data.getFieldValue("SHORT_ANSWER")
                                    creatives_model.collab_unique_id_4 = str(collab_dob_4) + str(
                                        collab_last_name_4) + str(collab_zip_4)
                                    creatives_model.collab_unique_id_4 = creatives_model.collab_unique_id_4.replace(" ",
                                                                                                                    "")
                                    print("creatives_model.collab_unique_id_4", creatives_model.collab_unique_id_4)

                        if field_id == config.reference_form_field_id_5:
                            # print("reference form id", field_id)
                            reference_responses = self.submittable.getReferenceResponses()
                            for resp in reference_responses:
                                if field_id == config.reference_form_field_id_5:
                                    ref_field_data = resp.getFieldData()
                                    creatives_model.form_response_id = resp.getFormResponseId()
                                    for ref_data in ref_field_data:
                                        # print("ref_data 5", ref_data)
                                        item_id = ref_data.getFormFieldId()
                                        if item_id == config.reference_form_name_id:
                                            collab_last_name_5 = ref_data.getFieldValue("SHORT_ANSWER")
                                        if item_id == config.reference_form_dob_id:
                                            date_string = ref_data.getFieldValue("DATE")
                                            collab_dob_5 = date_string[0:10]
                                        if item_id == config.reference_form_zipcode_id:
                                            collab_zip_5 = ref_data.getFieldValue("SHORT_ANSWER")
                                    creatives_model.collab_unique_id_5 = str(collab_dob_5) + str(
                                        collab_last_name_5) + str(collab_zip_5)
                                    creatives_model.collab_unique_id_5 = creatives_model.collab_unique_id_5.replace(" ",
                                                                                                                    "")
                                    print("creatives_model.collab_unique_id_5", creatives_model.collab_unique_id_5)

                        if field_id == config.reference_form_field_id_6:
                            # print("reference form id", field_id)
                            reference_responses = self.submittable.getReferenceResponses()
                            for resp in reference_responses:
                                if field_id == config.reference_form_field_id_6:
                                    ref_field_data = resp.getFieldData()
                                    creatives_model.form_response_id = resp.getFormResponseId()
                                    for ref_data in ref_field_data:
                                        # print("ref_data 6", ref_data)
                                        item_id = ref_data.getFormFieldId()
                                        if item_id == config.reference_form_name_id:
                                            collab_last_name_6 = ref_data.getFieldValue("SHORT_ANSWER")
                                        if item_id == config.reference_form_dob_id:
                                            date_string = ref_data.getFieldValue("DATE")
                                            collab_dob_6 = date_string[0:10]
                                        if item_id == config.reference_form_zipcode_id:
                                            collab_zip_6 = ref_data.getFieldValue("SHORT_ANSWER")
                                    creatives_model.collab_unique_id_6 = str(collab_dob_6) + str(
                                        collab_last_name_6) + str(collab_zip_6)
                                    creatives_model.collab_unique_id_6 = creatives_model.collab_unique_id_6.replace(" ",
                                                                                                                    "")
                                    print("creatives_model.collab_unique_id_6", creatives_model.collab_unique_id_6)

                        if field_id == config.reference_form_field_id_7:
                            # print("reference form id", field_id)
                            reference_responses = self.submittable.getReferenceResponses()
                            for resp in reference_responses:
                                if field_id == config.reference_form_field_id_7:
                                    ref_field_data = resp.getFieldData()
                                    creatives_model.form_response_id = resp.getFormResponseId()
                                    for ref_data in ref_field_data:
                                        # print("ref_data 7", ref_data)
                                        item_id = ref_data.getFormFieldId()
                                        if item_id == config.reference_form_name_id:
                                            collab_last_name_7 = ref_data.getFieldValue("SHORT_ANSWER")
                                        if item_id == config.reference_form_dob_id:
                                            date_string = ref_data.getFieldValue("DATE")
                                            collab_dob_7 = date_string[0:10]
                                        if item_id == config.reference_form_zipcode_id:
                                            collab_zip_7 = ref_data.getFieldValue("SHORT_ANSWER")
                                    creatives_model.collab_unique_id_7 = str(collab_dob_7) + str(
                                        collab_last_name_7) + str(collab_zip_7)
                                    creatives_model.collab_unique_id_7 = creatives_model.collab_unique_id_7.replace(" ",
                                                                                                                    "")
                                    print("creatives_model.collab_unique_id_7", creatives_model.collab_unique_id_7)

                        if field_id == config.reference_form_field_id_8:
                            # print("reference form id", field_id)
                            reference_responses = self.submittable.getReferenceResponses()
                            for resp in reference_responses:
                                if field_id == config.reference_form_field_id_8:
                                    ref_field_data = resp.getFieldData()
                                    creatives_model.form_response_id = resp.getFormResponseId()
                                    for ref_data in ref_field_data:
                                        # print("ref_data 8", ref_data)
                                        item_id = ref_data.getFormFieldId()
                                        if item_id == config.reference_form_name_id:
                                            collab_last_name_8 = ref_data.getFieldValue("SHORT_ANSWER")
                                        if item_id == config.reference_form_dob_id:
                                            date_string = ref_data.getFieldValue("DATE")
                                            collab_dob_8 = date_string[0:10]
                                        if item_id == config.reference_form_zipcode_id:
                                            collab_zip_8 = ref_data.getFieldValue("SHORT_ANSWER")
                                    creatives_model.collab_unique_id_8 = str(collab_dob_8) + str(
                                        collab_last_name_8) + str(collab_zip_8)
                                    creatives_model.collab_unique_id_8 = creatives_model.collab_unique_id_8.replace(" ",
                                                                                                                    "")
                                    print("creatives_model.collab_unique_id_8", creatives_model.collab_unique_id_8)

                        if field_id == config.reference_form_field_id_9:
                            # print("reference form id", field_id)
                            reference_responses = self.submittable.getReferenceResponses()
                            for resp in reference_responses:
                                if field_id == config.reference_form_field_id_9:
                                    ref_field_data = resp.getFieldData()
                                    creatives_model.form_response_id = resp.getFormResponseId()
                                    for ref_data in ref_field_data:
                                        # print("ref_data 9", ref_data)
                                        item_id = ref_data.getFormFieldId()
                                        if item_id == config.reference_form_name_id:
                                            collab_last_name_9 = ref_data.getFieldValue("SHORT_ANSWER")
                                        if item_id == config.reference_form_dob_id:
                                            date_string = ref_data.getFieldValue("DATE")
                                            collab_dob_9 = date_string[0:10]
                                        if item_id == config.reference_form_zipcode_id:
                                            collab_zip_9 = ref_data.getFieldValue("SHORT_ANSWER")
                                    creatives_model.collab_unique_id_9 = str(collab_dob_9) + str(
                                        collab_last_name_9) + str(collab_zip_9)
                                    creatives_model.collab_unique_id_9 = creatives_model.collab_unique_id_9.replace(" ",
                                                                                                                    "")
                                    print("creatives_model.collab_unique_id_9", creatives_model.collab_unique_id_9)

                    # create the primary UID
                    creatives_model.date_last_checked = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    creatives_model.primary_unique_id = str(primary_dob) + str(primary_last_name) + str(primary_zip)
                    creatives_model.primary_unique_id = creatives_model.primary_unique_id.replace(" ", "")
                    print("creatives_model primary_unique_id", creatives_model.primary_unique_id,
                          creatives_model.submission_id)

                    # check for duplicate collaborator ids
                    id_list_check = [creatives_model.primary_unique_id, creatives_model.collab_unique_id_1,
                                     creatives_model.collab_unique_id_2, creatives_model.collab_unique_id_3,
                                     creatives_model.collab_unique_id_4, creatives_model.collab_unique_id_5,
                                     creatives_model.collab_unique_id_6, creatives_model.collab_unique_id_7,
                                     creatives_model.collab_unique_id_8, creatives_model.collab_unique_id_9]

                    print("collaborator artist UID list", id_list_check)

                    # pull id out then loop through the list to check for dup
                    for elem in id_list_check:
                        if id_list_check.count(elem) > 1 and elem is not None:
                            dup_found = True
                            logger.info(f"project 1 - INTERNAL FORM duplicate unique id project 1 {creatives_model.primary_unique_id} "
                                        f"for submission {creatives_model.submission_id}")
                            try:
                                # add dup label to this submission (single form dup)
                                self.createLabel(sub_response.getSubmissionStatus(), creatives_model.submission_id)
                                break
                            except ValueError:
                                logger.info(f"project 1 - failed to create duplicate label for submission id {creatives_model.submission_id} - top try")
                        else:
                            continue

                    # save to database only if all UID fields have been pulled from form
                    try:
                        if primary_last_name is not None and primary_dob is not None and primary_zip is not None and not dup_found:
                            print("project 1 - creatives_model.primary_unique_id", creatives_model.primary_unique_id)
                            try:
                                creatives_model.entry_id = self.submittable.submitInternalFormResponse(creatives_model.submission_id,
                                                                                                       creatives_model.primary_unique_id,
                                                                                                       creatives_model.collab_unique_id_1,
                                                                                                       creatives_model.collab_unique_id_2,
                                                                                                       creatives_model.collab_unique_id_3,
                                                                                                       creatives_model.collab_unique_id_4,
                                                                                                       creatives_model.collab_unique_id_5,
                                                                                                       creatives_model.collab_unique_id_6,
                                                                                                       creatives_model.collab_unique_id_7,
                                                                                                       creatives_model.collab_unique_id_8,
                                                                                                       creatives_model.collab_unique_id_9)
                                logger.info("project 1 - successfully to create internal form")
                            except:
                                try:
                                    self.submittable.updateInternalFormResponse(creatives_model.entry_id,
                                                                                creatives_model.primary_unique_id,
                                                                                creatives_model.collab_unique_id_1,
                                                                                creatives_model.collab_unique_id_2,
                                                                                creatives_model.collab_unique_id_3,
                                                                                creatives_model.collab_unique_id_4,
                                                                                creatives_model.collab_unique_id_5,
                                                                                creatives_model.collab_unique_id_6,
                                                                                creatives_model.collab_unique_id_7,
                                                                                creatives_model.collab_unique_id_8,
                                                                                creatives_model.collab_unique_id_9)
                                except:
                                    logger.info(
                                        f"project 1 - failed to create/update internal form for submission {creatives_model.submission_id}")
                            print("project 1 - save to db")
                            creatives_model.save()
                            # go to next response
                            break
                        else:
                            logger.info(
                                f"project 1 - collaborator UID field Null for submission {creatives_model.submission_id}")
                            # move to next response
                            continue
                    except:
                        # add dup label to original and new submission
                        try:
                            list_of_submissions = self.submittable.getListOfSubmissions()
                            for sub in list_of_submissions:
                                sub_id = sub.getSubmissionId()
                                if creatives_model.submission_id == sub_id:
                                    # add dup label to new sub
                                    self.createLabel(sub_response.getSubmissionStatus(), creatives_model.submission_id)
                                    # label original sub with dup label
                                    self.createLabel(sub_response.getSubmissionStatus(), sub_id)
                                    logger.info(
                                        f"project 1 - duplicate unique id project 1 {creatives_model.primary_unique_id} submission: {creatives_model.submission_id} "
                                        f"in the database already for submission {sub_id}")
                        except ValueError:
                            logger.info(
                                f"project 1 - failed to create duplicate label for submission id {creatives_model.submission_id} - bottom try")

            # load database from project 2
            elif sub_item.getProjectId() == self.project_id_2:
                print("project 2 - Submission")
                creatives_model.submission_id = sub_item.getSubmissionId()
                sub_response = self.submittable.getSubmission(creatives_model.submission_id)
                creatives_model.submitter_id = sub_response.getSubmitterId()
                response_list = sub_response.getFormResponses()

                # Skip submission if not in "new" or "in_progress" state
                status = sub_response.getSubmissionStatus()
                if status != "new" and status != "in_progress":
                    print(f"project 2 - skip sub in project 2 {status} submission {creatives_model.submission_id}")
                    continue

                print("project 2 - response list length:", len(response_list))

                # get each submission form responses
                for form_response in response_list:
                    # create local variables
                    primary_last_name = None
                    primary_dob = None
                    primary_zip = None

                    form_id = form_response.getFormId()
                    responses = sub_response.getFormResponse(form_id)
                    field_data = responses.getFieldData()

                    for data in field_data:
                        print("project 2 - data in field_data", data)
                        field_id = data.getFormFieldId()
                        field_value = responses.getFieldResponse(field_id)
                        field_id = field_value.getFormFieldId()

                        creatives_model.form_response_id = form_response.getFormResponseId()

                        if field_id == config.project_2_name_field_id:
                            primary_last_name = data.getFieldValue("SHORT_ANSWER")
                        if field_id == config.project_2_dob_field_id:
                            date_string = data.getFieldValue("DATE")
                            primary_dob = date_string[0:10]
                        if field_id == config.project_2_zipcode_field_id:
                            primary_zip = data.getFieldValue("SHORT_ANSWER")

                    creatives_model.date_last_checked = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    creatives_model.primary_unique_id = str(primary_dob) + str(primary_last_name) + str(primary_zip)
                    creatives_model.primary_unique_id = creatives_model.primary_unique_id.replace(" ", "")

                    try:
                        if primary_last_name is not None and primary_dob is not None and primary_zip is not None:
                            # create internal entry using beta endpoint - Work In Progress
                            try:
                                creatives_model.entry_id = self.submittable.submitInternalFormResponse(
                                    creatives_model.submission_id, creatives_model.primary_unique_id)
                            except:
                                print("project 2 - failed to create internal form, try to update")
                                try:
                                    self.submittable.updateInternalFormResponse(creatives_model.entry_id,
                                                                                creatives_model.primary_unique_id)
                                except:
                                    print("project 2 - failed to create/update internal form")
                                    logger.info(
                                        f"project 2 - failed to create/update internal form for submission {creatives_model.submission_id}")
                            print("project 2 - save to db")
                            creatives_model.save()
                            break
                        else:
                            # skip submission missing UID field(s)
                            continue
                    except:
                        try:
                            list_of_submissions = self.submittable.getListOfSubmissions()
                            for sub in list_of_submissions:
                                sub_id = sub.getSubmissionId()
                                if creatives_model.submission_id == sub_id:
                                    # add dup label to new sub
                                    self.createLabel(sub_response.getSubmissionStatus(), creatives_model.submission_id)
                                    # label original sub with dup label
                                    self.createLabel(sub_response.getSubmissionStatus(), sub_id)
                                    logger.info(
                                        f"project 2 - duplicate unique id project 2 {creatives_model.primary_unique_id} submission: {creatives_model.submission_id} "
                                        f"in the database already for submission {sub_id}")
                        except ValueError:
                            logger.info(
                                f"project 2 - failed to create duplicate label for unique id {creatives_model.primary_unique_id}")

    print("finished loading database")
