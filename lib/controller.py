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
        self.submittable  = Submittable()
        self.model        = Creative(config.mysql_conn)
        self.project_id_1 = config.project_id_1
        self.project_id_2 = config.project_id_2
        self.label_id_1   = config.label_id_1
        self.label_id_2   = config.label_id_2
        self.label_id_3   = config.label_id_3


    def createLabel(self, submission_id):
        self.submittable.addLabel(submission_id, self.label_id_1)


    def label_dups(self, submission_id, sub_id):
        print("label dups", submission_id, sub_id)
        # add dup label to original and new submission
        try:
            # add dup label to new sub
            self.createLabel(submission_id)
            logger.info(f"duplicate unique id project 1 submission: {submission_id} in the database already for submission {sub_id}")
        except ValueError:
            logger.info(f"failed to create duplicate label for submission id {submission_id}")
        try:
            # label original sub with dup label
            self.createLabel(sub_id)
            logger.info(f"duplicate unique id project 1 submission: {submission_id} in the database already for submission {sub_id}")
        except ValueError:
            logger.info(f"failed to create duplicate label for submission id {submission_id}")

    # UID - DOB-LASTNAME-ZIP
    def uid_chcek(self, uid_to_check):
        print("uid check run", uid_to_check, config.uid_data_struct)

        if uid_to_check is not None and config.uid_data_struct != []:
            for item in config.uid_data_struct:
                if item["primary_unique_id"]   == uid_to_check:
                    print(1)
                    return item["submission_id"]
                elif item["collab_unique_id_1"] == uid_to_check:
                    print(2)
                    return item["submission_id"]
                elif item["collab_unique_id_2"] == uid_to_check:
                    print(3)
                    return item["submission_id"]
                elif item["collab_unique_id_3"] == uid_to_check:
                    print(4)
                    return item["submission_id"]
                elif item["collab_unique_id_4"] == uid_to_check:
                    print(5)
                    return item["submission_id"]
                elif item["collab_unique_id_5"] == uid_to_check:
                    print(6)
                    return item["submission_id"]
                elif item["collab_unique_id_6"] == uid_to_check:
                    print(7)
                    return item["submission_id"]
                elif item["collab_unique_id_7"] == uid_to_check:
                    print(8)
                    return item["submission_id"]
                elif item["collab_unique_id_8"] == uid_to_check:
                    print(9)
                    return item["submission_id"]
                elif item["collab_unique_id_9"] == uid_to_check:
                    print(10)
                    return item["submission_id"]
        else:
            print("empty")
            return None


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
        # get all submission for project 1 & project 2 in "new" and "in_progress" states
        list_of_submissions = self.submittable.getListOfSubmissions()

        for sub_item in list_of_submissions:
            project_id    = sub_item.getProjectId()
            submission_id = sub_item.getSubmissionId()
            sub_response  = self.submittable.getSubmission(submission_id)
            # get submission form responses (initial)
            response_list = sub_response.getFormResponses()
            logger.info(f"response list length: {len(response_list)}")

            # load database from project 1 (AEP)
            if project_id == self.project_id_1:
                print("project 1 - Submission")
                ref_email = sub_response.getSubmitterEmail()
                print("ref email is", ref_email)

                # get list of reference form responses
                reference_responses = self.submittable.getReferenceResponses()

                # go through initial form response list
                for response in response_list:
                    # create local variables
                    primary_last_name  = None
                    primary_dob        = None
                    primary_zip        = None
                    primary_unique_id  = None

                    collab_last_name_1 = None
                    collab_dob_1       = None
                    collab_zip_1       = None
                    collab_unique_id_1 = None

                    collab_last_name_2 = None
                    collab_dob_2       = None
                    collab_zip_2       = None
                    collab_unique_id_2 = None

                    collab_last_name_3 = None
                    collab_dob_3       = None
                    collab_zip_3       = None
                    collab_unique_id_3 = None

                    collab_last_name_4 = None
                    collab_dob_4       = None
                    collab_zip_4       = None
                    collab_unique_id_4 = None

                    collab_last_name_5 = None
                    collab_dob_5       = None
                    collab_zip_5       = None
                    collab_unique_id_5 = None

                    collab_last_name_6 = None
                    collab_dob_6       = None
                    collab_zip_6       = None
                    collab_unique_id_6 = None

                    collab_last_name_7 = None
                    collab_dob_7       = None
                    collab_zip_7       = None
                    collab_unique_id_7 = None

                    collab_last_name_8 = None
                    collab_dob_8       = None
                    collab_zip_8       = None
                    collab_unique_id_8 = None

                    collab_last_name_9 = None
                    collab_dob_9       = None
                    collab_zip_9       = None
                    collab_unique_id_9 = None

                    id_list_check      = None

                    # Pull the initial forms response data
                    field_data = response.getFieldData()

                    # Get the primary artist UID fields
                    for data in field_data:
                        field_id = data.getFormFieldId()
                        logger.info(f"field_id {field_id}")

                        # Primary Artist UID | DOB-LastName-Zipcode
                        if field_id == config.project_1_artist_last_name:
                            primary_last_name = data.getFieldValue("SHORT_ANSWER")
                        elif field_id == config.project_1_artist_dob:
                            date_string = data.getFieldValue("DATE")
                            primary_dob = date_string[0:10]
                        elif field_id == config.project_1_artist_zipcode:
                            primary_zip = data.getFieldValue("SHORT_ANSWER")

                        # local variable used to pull latest reference response data
                        date_1 = None

                        # Reference from UIDs
                        if field_id == config.reference_form_field_id_1:
                            print("reference form id 1", field_id)
                            count = 0
                            for resp in reference_responses:
                                count = count + 1
                                print("resp 1", count)
                                print("response refEmail", resp.getRefEmail(), "ref_email", ref_email)
                                if field_id == config.reference_form_field_id_1 and ref_email == resp.getRefEmail():
                                    # TODO look into date complete and not created (?)
                                    if date_1 is None or date_1 < resp.getCreatedAt():
                                        date_1 = resp.getCreatedAt()
                                        ref_field_data = resp.getFieldData()
                                        for ref_data in ref_field_data:
                                            print("ref_data 1", ref_data)
                                            item_id = ref_data.getFormFieldId()
                                            if item_id == config.reference_form_name_id:
                                                collab_last_name_1 = ref_data.getFieldValue("SHORT_ANSWER")
                                            elif item_id == config.reference_form_dob_id:
                                                date_string = ref_data.getFieldValue("DATE")
                                                collab_dob_1 = date_string[0:10]
                                            elif item_id == config.reference_form_zipcode_id:
                                                collab_zip_1 = ref_data.getFieldValue("SHORT_ANSWER")
                                        collab_unique_id_1 = str(collab_dob_1) + str(collab_last_name_1) + str(collab_zip_1)
                                        collab_unique_id_1 = collab_unique_id_1.replace(" ", "")
                                        collab_unique_id_1 = collab_unique_id_1.replace("-", "")
                                        print("collab_unique_id_1", collab_unique_id_1)

                        if field_id == config.reference_form_field_id_2:
                            print("reference form id 2", field_id)
                            for resp in reference_responses:
                                print("resp 2")
                                if field_id == config.reference_form_field_id_2 and ref_email == resp.getRefEmail():
                                    if date_1 is None or date_1 < resp.getCreatedAt():
                                        date_1 = resp.getCreatedAt()
                                        ref_field_data = resp.getFieldData()
                                        for ref_data in ref_field_data:
                                            print("ref_data 2", ref_data)
                                            item_id = ref_data.getFormFieldId()
                                            if item_id == config.reference_form_name_id:
                                                collab_last_name_2 = ref_data.getFieldValue("SHORT_ANSWER")
                                            elif item_id == config.reference_form_dob_id:
                                                date_string = ref_data.getFieldValue("DATE")
                                                collab_dob_2 = date_string[0:10]
                                            elif item_id == config.reference_form_zipcode_id:
                                                collab_zip_2 = ref_data.getFieldValue("SHORT_ANSWER")
                                        collab_unique_id_2 = str(collab_dob_2) + str(collab_last_name_2) + str(collab_zip_2)
                                        collab_unique_id_2 = collab_unique_id_2.replace(" ", "")
                                        collab_unique_id_2 = collab_unique_id_2.replace("-", "")
                                        print("collab_unique_id_2", collab_unique_id_2)

                        if field_id == config.reference_form_field_id_3:
                            print("reference form id 3", field_id)
                            for resp in reference_responses:
                                print("resp 3")
                                if field_id == config.reference_form_field_id_3 and ref_email == resp.getRefEmail():
                                    if date_1 is None or date_1 < resp.getCreatedAt():
                                        date_1 = resp.getCreatedAt()
                                        ref_field_data = resp.getFieldData()
                                        for ref_data in ref_field_data:
                                            print("ref_data 3", ref_data)
                                            item_id = ref_data.getFormFieldId()
                                            if item_id == config.reference_form_name_id:
                                                collab_last_name_3 = ref_data.getFieldValue("SHORT_ANSWER")
                                            elif item_id == config.reference_form_dob_id:
                                                date_string = ref_data.getFieldValue("DATE")
                                                collab_dob_3 = date_string[0:10]
                                            elif item_id == config.reference_form_zipcode_id:
                                                collab_zip_3 = ref_data.getFieldValue("SHORT_ANSWER")
                                        collab_unique_id_3 = str(collab_dob_3) + str(collab_last_name_3) + str(collab_zip_3)
                                        collab_unique_id_3 = collab_unique_id_3.replace(" ", "")
                                        collab_unique_id_3 = collab_unique_id_3.replace("-", "")
                                        print("collab_unique_id_3", collab_unique_id_3)

                        if field_id == config.reference_form_field_id_4:
                            print("reference form id 4", field_id)
                            for resp in reference_responses:
                                if field_id == config.reference_form_field_id_4 and ref_email == resp.getRefEmail():
                                    if date_1 is None or date_1 < resp.getCreatedAt():
                                        date_1 = resp.getCreatedAt()
                                        ref_field_data = resp.getFieldData()
                                        for ref_data in ref_field_data:
                                            print("ref_data 4", ref_data)
                                            item_id = ref_data.getFormFieldId()
                                            if item_id == config.reference_form_name_id:
                                                collab_last_name_4 = ref_data.getFieldValue("SHORT_ANSWER")
                                            elif item_id == config.reference_form_dob_id:
                                                date_string = ref_data.getFieldValue("DATE")
                                                collab_dob_4 = date_string[0:10]
                                            elif item_id == config.reference_form_zipcode_id:
                                                collab_zip_4 = ref_data.getFieldValue("SHORT_ANSWER")
                                        collab_unique_id_4 = str(collab_dob_4) + str(collab_last_name_4) + str(collab_zip_4)
                                        collab_unique_id_4 = collab_unique_id_4.replace(" ", "")
                                        collab_unique_id_4 = collab_unique_id_4.replace("-", "")
                                        print("collab_unique_id_4", collab_unique_id_4)

                        if field_id == config.reference_form_field_id_5:
                            print("reference form id 5", field_id)
                            for resp in reference_responses:
                                if field_id == config.reference_form_field_id_5 and ref_email == resp.getRefEmail():
                                    if date_1 is None or date_1 < resp.getCreatedAt():
                                        date_1 = resp.getCreatedAt()
                                        ref_field_data = resp.getFieldData()
                                        for ref_data in ref_field_data:
                                            print("ref_data 5", ref_data)
                                            item_id = ref_data.getFormFieldId()
                                            if item_id == config.reference_form_name_id:
                                                collab_last_name_5 = ref_data.getFieldValue("SHORT_ANSWER")
                                            elif item_id == config.reference_form_dob_id:
                                                date_string = ref_data.getFieldValue("DATE")
                                                collab_dob_5 = date_string[0:10]
                                            elif item_id == config.reference_form_zipcode_id:
                                                collab_zip_5 = ref_data.getFieldValue("SHORT_ANSWER")
                                        collab_unique_id_5 = str(collab_dob_5) + str(collab_last_name_5) + str(collab_zip_5)
                                        collab_unique_id_5 = collab_unique_id_5.replace(" ", "")
                                        collab_unique_id_5 = collab_unique_id_5.replace("-", "")
                                        print("collab_unique_id_5", collab_unique_id_5)

                        if field_id == config.reference_form_field_id_6:
                            print("reference form id 6", field_id)
                            for resp in reference_responses:
                                if field_id == config.reference_form_field_id_6 and ref_email == resp.getRefEmail():
                                    if date_1 is None or date_1 < resp.getCreatedAt():
                                        date_1 = resp.getCreatedAt()
                                        ref_field_data = resp.getFieldData()
                                        for ref_data in ref_field_data:
                                            print("ref_data 6", ref_data)
                                            item_id = ref_data.getFormFieldId()
                                            if item_id == config.reference_form_name_id:
                                                collab_last_name_6 = ref_data.getFieldValue("SHORT_ANSWER")
                                            elif item_id == config.reference_form_dob_id:
                                                date_string = ref_data.getFieldValue("DATE")
                                                collab_dob_6 = date_string[0:10]
                                            elif item_id == config.reference_form_zipcode_id:
                                                collab_zip_6 = ref_data.getFieldValue("SHORT_ANSWER")

                                        collab_unique_id_6 = str(collab_dob_6) + str(collab_last_name_6) + str(collab_zip_6)
                                        collab_unique_id_6 = collab_unique_id_6.replace(" ", "")
                                        collab_unique_id_6 = collab_unique_id_6.replace("-", "")
                                        print("collab_unique_id_6", collab_unique_id_6)

                        if field_id == config.reference_form_field_id_7:
                            print("reference form id 7", field_id)
                            for resp in reference_responses:
                                if field_id == config.reference_form_field_id_7 and ref_email == resp.getRefEmail():
                                    if date_1 is None or date_1 < resp.getCreatedAt():
                                        date_1 = resp.getCreatedAt()
                                        ref_field_data = resp.getFieldData()
                                        for ref_data in ref_field_data:
                                            print("ref_data 7", ref_data)
                                            item_id = ref_data.getFormFieldId()
                                            if item_id == config.reference_form_name_id:
                                                collab_last_name_7 = ref_data.getFieldValue("SHORT_ANSWER")
                                            elif item_id == config.reference_form_dob_id:
                                                date_string = ref_data.getFieldValue("DATE")
                                                collab_dob_7 = date_string[0:10]
                                            elif item_id == config.reference_form_zipcode_id:
                                                collab_zip_7 = ref_data.getFieldValue("SHORT_ANSWER")
                                        collab_unique_id_7 = str(collab_dob_7) + str(collab_last_name_7) + str(collab_zip_7)
                                        collab_unique_id_7 = collab_unique_id_7.replace(" ", "")
                                        collab_unique_id_7 = collab_unique_id_7.replace("-", "")
                                        print("collab_unique_id_7", collab_unique_id_7)

                        if field_id == config.reference_form_field_id_8:
                            print("reference form id 8", field_id)
                            for resp in reference_responses:
                                if field_id == config.reference_form_field_id_5 and ref_email == resp.getRefEmail():
                                    if date_1 is None or date_1 < resp.getCreatedAt():
                                        date_1 = resp.getCreatedAt()
                                        ref_field_data = resp.getFieldData()
                                        for ref_data in ref_field_data:
                                            print("ref_data 8", ref_data)
                                            item_id = ref_data.getFormFieldId()
                                            if item_id == config.reference_form_name_id:
                                                collab_last_name_8 = ref_data.getFieldValue("SHORT_ANSWER")
                                            elif item_id == config.reference_form_dob_id:
                                                date_string = ref_data.getFieldValue("DATE")
                                                collab_dob_8 = date_string[0:10]
                                            elif item_id == config.reference_form_zipcode_id:
                                                collab_zip_8 = ref_data.getFieldValue("SHORT_ANSWER")
                                        collab_unique_id_8 = str(collab_dob_8) + str(collab_last_name_8) + str(collab_zip_8)
                                        collab_unique_id_8 = collab_unique_id_8.replace(" ", "")
                                        collab_unique_id_8 = collab_unique_id_8.replace("-", "")
                                        print("collab_unique_id_8", collab_unique_id_8)

                        if field_id == config.reference_form_field_id_9:
                            print("reference form id 9", field_id)
                            for resp in reference_responses:
                                if field_id == config.reference_form_field_id_9 and ref_email == resp.getRefEmail():
                                    if date_1 is None or date_1 < resp.getCreatedAt():
                                        date_1 = resp.getCreatedAt()
                                        ref_field_data = resp.getFieldData()
                                        for ref_data in ref_field_data:
                                            print("ref_data 9", ref_data)
                                            item_id = ref_data.getFormFieldId()
                                            if item_id == config.reference_form_name_id:
                                                collab_last_name_9 = ref_data.getFieldValue("SHORT_ANSWER")
                                            elif item_id == config.reference_form_dob_id:
                                                date_string = ref_data.getFieldValue("DATE")
                                                collab_dob_9 = date_string[0:10]
                                            elif item_id == config.reference_form_zipcode_id:
                                                collab_zip_9 = ref_data.getFieldValue("SHORT_ANSWER")
                                        collab_unique_id_9 = str(collab_dob_9) + str(collab_last_name_9) + str(collab_zip_9)
                                        collab_unique_id_9 = collab_unique_id_9.replace(" ", "")
                                        collab_unique_id_9 = collab_unique_id_9.replace("-", "")
                                        print("collab_unique_id_9", collab_unique_id_9)

                    # create the primary UID
                    # TODO maybe consider adding createdAt()/CompletedAt() date to UID or submission id
                    if primary_last_name is not None and primary_dob is not None and primary_zip is not None:
                        primary_unique_id = str(primary_dob) + str(primary_last_name) + str(primary_zip)
                        primary_unique_id = primary_unique_id.replace(" ", "")
                        primary_unique_id = primary_unique_id.replace("-", "")
                        logger.info(f"project 1 - primary_unique_id: {primary_unique_id}")

                    print("id list", id_list_check)

                    # check for duplicate collaborator ids internal to the submission
                    id_list_check = [primary_unique_id, collab_unique_id_1,
                                     collab_unique_id_2, collab_unique_id_3,
                                     collab_unique_id_4, collab_unique_id_5,
                                     collab_unique_id_6, collab_unique_id_7,
                                     collab_unique_id_8, collab_unique_id_9]

                    print("collaborator artist UID list", id_list_check)

                    # pull id out then loop through the list to check for dup
                    # check the uids in the form for dups
                    for elem in id_list_check:
                        if id_list_check.count(elem) > 1 and elem is not None:
                            logger.info(f"project 1 - INTERNAL FORM duplicate unique id project 1 {primary_unique_id} for submission {submission_id}")
                            try:
                                # add dup label to this submission (single form dup)
                                logger.info(f"project 1 - try to create label")
                                self.createLabel(submission_id)
                                break
                            except ValueError:
                                logger.info(f"project 1 - failed to create duplicate label for submission id {submission_id}")
                                break
                        else:
                            continue

                    if primary_last_name is not None and primary_dob is not None and primary_zip is not None:
                        try:
                            self.submittable.submitInternalFormResponse(submission_id, primary_unique_id, collab_unique_id_1,
                                                                        collab_unique_id_2, collab_unique_id_3, collab_unique_id_4,
                                                                        collab_unique_id_5, collab_unique_id_6, collab_unique_id_7,
                                                                        collab_unique_id_8, collab_unique_id_9)

                        except:
                            logger.info(f"project 1 - failed to create internal form for submission {submission_id}")

                        # check if uid already exist in list of dicts
                        uid_check_sub_id_1  = self.uid_chcek(primary_unique_id)
                        uid_check_sub_id_2  = self.uid_chcek(collab_unique_id_1)
                        uid_check_sub_id_3  = self.uid_chcek(collab_unique_id_2)
                        uid_check_sub_id_4  = self.uid_chcek(collab_unique_id_3)
                        uid_check_sub_id_5  = self.uid_chcek(collab_unique_id_4)
                        uid_check_sub_id_6  = self.uid_chcek(collab_unique_id_5)
                        uid_check_sub_id_7  = self.uid_chcek(collab_unique_id_6)
                        uid_check_sub_id_8  = self.uid_chcek(collab_unique_id_7)
                        uid_check_sub_id_9  = self.uid_chcek(collab_unique_id_8)
                        uid_check_sub_id_10 = self.uid_chcek(collab_unique_id_9)

                        if uid_check_sub_id_1 is not None:
                            print("project 1 - dup found")
                            self.label_dups(submission_id, uid_check_sub_id_1)
                        elif uid_check_sub_id_2 is not None:
                            print(f"project 1 - collab_unique_id_2 dup found")
                            self.label_dups(submission_id, uid_check_sub_id_2)
                        elif uid_check_sub_id_3 is not None:
                            print("project 1 - collab_unique_id_3 dup found")
                            self.label_dups(submission_id, uid_check_sub_id_3)
                        elif uid_check_sub_id_4 is not None:
                            print("project 1 - collab_unique_id_4 dup found")
                            self.label_dups(submission_id, uid_check_sub_id_4)
                        elif uid_check_sub_id_5 is not None:
                            print("project 1 - collab_unique_id_5 dup found")
                            self.label_dups(submission_id, uid_check_sub_id_5)
                        elif uid_check_sub_id_6 is not None:
                            print("project 1 - collab_unique_id_6 dup found")
                            self.label_dups(submission_id, uid_check_sub_id_6)
                        elif uid_check_sub_id_7 is not None:
                            print("project 1 - collab_unique_id_7 dup found")
                            self.label_dups(submission_id, uid_check_sub_id_7)
                        elif uid_check_sub_id_8 is not None:
                            print("project 1 - collab_unique_id_7 dup found")
                            self.label_dups(submission_id, uid_check_sub_id_8)
                        elif uid_check_sub_id_9 is not None:
                            print("project 1 - collab_unique_id_8 dup found")
                            self.label_dups(submission_id, uid_check_sub_id_9)
                        elif uid_check_sub_id_10 is not None:
                            print("project 1 - collab_unique_id_9 dup found")
                            self.label_dups(submission_id, uid_check_sub_id_10)

                        logger.info(f"project 1 - save to dict")
                        config.uid_data_struct.append({'submission_id':      submission_id,      'primary_unique_id':  primary_unique_id,
                                                       'collab_unique_id_1': collab_unique_id_1, 'collab_unique_id_2': collab_unique_id_2,
                                                       'collab_unique_id_3': collab_unique_id_3, 'collab_unique_id_4': collab_unique_id_4,
                                                       'collab_unique_id_5': collab_unique_id_5, 'collab_unique_id_6': collab_unique_id_6,
                                                       'collab_unique_id_7': collab_unique_id_7, 'collab_unique_id_8': collab_unique_id_8,
                                                       'collab_unique_id_9': collab_unique_id_9})


                        # go to next response
                        break
                    else:
                        logger.info(f"project 1 - collaborator UID field Null for submission {submission_id}")
                        # skip submission missing primary UID field(s)
                        continue

            # check project 2
            elif project_id == self.project_id_2:
                logger.info(f"project 2 - Submission")
                # Skip submission if not in "new" or "in_progress" state
                status = sub_response.getSubmissionStatus()
                if status != "new" and status != "in_progress":
                    logger.info(f"project 2 - skip sub in project 2 {status}  submission id: {submission_id}")
                    continue

                # get each submission form responses
                for form_response in response_list:
                    # create local variables
                    primary_last_name = None
                    primary_dob       = None
                    primary_zip       = None

                    form_id    = form_response.getFormId()
                    responses  = sub_response.getFormResponse(form_id)
                    field_data = responses.getFieldData()

                    for data in field_data:
                        logger.info(f"project 2 - data in field_data {data}")
                        field_id    = data.getFormFieldId()
                        field_value = responses.getFieldResponse(field_id)
                        field_id    = field_value.getFormFieldId()

                        # Primary Artist UID | DOB-LastName-Zipcode
                        if field_id == config.project_2_name_field_id:
                            primary_last_name = data.getFieldValue("SHORT_ANSWER")
                        if field_id == config.project_2_dob_field_id:
                            date_string = data.getFieldValue("DATE")
                            primary_dob = date_string[0:10]
                        if field_id == config.project_2_zipcode_field_id:
                            primary_zip = data.getFieldValue("SHORT_ANSWER")

                    # create the primary UID
                    primary_unique_id = str(primary_dob) + str(primary_last_name) + str(primary_zip)
                    primary_unique_id = primary_unique_id.replace(" ", "")
                    primary_unique_id = primary_unique_id.replace("-", "")

                    try:
                        if primary_last_name is not None and primary_dob is not None and primary_zip is not None:
                            # create internal entry using beta endpoint - Work In Progress
                            try:
                                self.submittable.submitInternalFormResponse(submission_id, primary_unique_id)
                            except:
                                logger.info(f"project 2 - failed to create/update internal form for submission {submission_id}")

                            # check if uid already exist in list of dicts
                            uid_check_sub_id_1 = self.uid_chcek(primary_unique_id)
                            if uid_check_sub_id_1 is not None:
                                print("project 2 - dup found")
                                self.label_dups(submission_id, uid_check_sub_id_1)

                            logger.info(f"project 2 - save to dict")
                            config.uid_data_struct.append({'submission_id': submission_id, 'primary_unique_id':  primary_unique_id,
                                                           'collab_unique_id_1': None,     'collab_unique_id_2': None,
                                                           'collab_unique_id_3': None,     'collab_unique_id_4': None,
                                                           'collab_unique_id_5': None,     'collab_unique_id_6': None,
                                                           'collab_unique_id_7': None,     'collab_unique_id_8': None,
                                                           'collab_unique_id_9': None})
                            break
                        else:
                            # skip submission missing UID field(s)
                            continue
                    except:
                        try:
                            list_of_submissions = self.submittable.getListOfSubmissions()
                            for sub in list_of_submissions:
                                sub_id = sub.getSubmissionId()
                                if submission_id == sub_id:
                                    # add dup label to new sub
                                    self.createLabel(submission_id)
                                    # label original sub with dup label
                                    self.createLabel(sub_id)
                                    logger.info(f"project 2 - duplicate unique id project 2 {primary_unique_id} submission: {submission_id} in the database already for submission {sub_id}")
                        except ValueError:
                            logger.info(f"project 2 - failed to create duplicate label for unique id {primary_unique_id}")

        logger.info(f"config struct {config.uid_data_struct}")
