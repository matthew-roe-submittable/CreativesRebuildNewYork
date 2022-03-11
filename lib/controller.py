import data_struct
from lib.submittable import *
from datetime import datetime
import config
import logging
import sys

file_formatter = logging.Formatter('%(asctime)s~%(levelname)s~%(message)s~module:%(module)s~function:%(module)s')
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
        self.submittable  = Submittable()
        self.project_id_1 = config.project_id_1
        self.project_id_2 = config.project_id_2
        self.label_id_1   = config.label_id_1
        self.label_id_2   = config.label_id_2
        self.label_id_3   = config.label_id_3


    def addLabel(self, submission_id, label_id):
        self.submittable.addLabel(submission_id, label_id)

    def createNewLabel(self, sub_id):
        try:
            label_id = self.submittable.createNewLabel(sub_id)
            return label_id
        except:
            return None

    def label_dups(self, submission_id, sub_id):
        logger.info(f"label dups new: {submission_id} old: {sub_id}")
        label_id = None
        # add dup label to original and new submission
        try:
            # add dup label to new sub
            self.addLabel(submission_id, self.label_id_1)
            # print(f"duplicate submission: {submission_id} with submission {sub_id}")
        except ValueError:
            print(f"failed to add duplicate label for submission id {submission_id}")

        try:
            # label submission id of original sub to new submission with dup label
            label_id = self.submittable.createNewLabel(sub_id)
            # print(f"duplicate UID new submission: {submission_id} with old submission: {sub_id}")
        except ValueError:
            label_id_list = self.submittable.getLabelIds()
            for id in label_id_list:
                if str(id.getName()) == str(sub_id):
                    label_id = id.getLabelId()
            print(f"failed to create new submission id duplicate label for submission id {submission_id}")

        if label_id is not None:
            try:
                # label submission id of original sub to new submission with dup label
                self.addLabel(submission_id, label_id)
                # print(f"duplicate UID submission: {submission_id} with submission {sub_id}")
            except ValueError:
                print(f"failed to create new submission id duplicate label for submission id {submission_id}")

    # UID - DOB-LASTNAME-ZIP
    def uid_chcek(self, uid_to_check):
        # logger.info(f"uid check run {uid_to_check}, list: {config.uid_data_struct}")

        if uid_to_check is not None and config.uid_data_struct != []:
            for item in config.uid_data_struct:
                if item["primary_unique_id"]   == uid_to_check:
                    return item["submission_id"]
                elif item["collab_unique_id_1"] == uid_to_check:
                    return item["submission_id"]
                elif item["collab_unique_id_2"] == uid_to_check:
                    return item["submission_id"]
                elif item["collab_unique_id_3"] == uid_to_check:
                    return item["submission_id"]
                elif item["collab_unique_id_4"] == uid_to_check:
                    return item["submission_id"]
                elif item["collab_unique_id_5"] == uid_to_check:
                    return item["submission_id"]
                elif item["collab_unique_id_6"] == uid_to_check:
                    return item["submission_id"]
                elif item["collab_unique_id_7"] == uid_to_check:
                    return item["submission_id"]
                elif item["collab_unique_id_8"] == uid_to_check:
                    return item["submission_id"]
                elif item["collab_unique_id_9"] == uid_to_check:
                    return item["submission_id"]
        else:
            return None


    #
    # get all submissions
    # get submission id
    # get form id
    # get field values
    # save into database
    #
    def checkForDupUID(self):
        # print(f"checking artists")

        # build up submission id list
        # get all submission for project 1 & project 2 in "new" and "in_progress" states
        list_of_submissions =  self.submittable.getListOfSubmissions(self.project_id_1, self.project_id_2)
        # list_of_submissions =  [23171861, 23171241, 23217200]

        # get list of reference form responses
        reference_responses = self.submittable.getReferenceResponses()

        for sub_item in list_of_submissions:
            submission_id = sub_item.getSubmissionId()
            project_id    = sub_item.getProjectId()

            '''
            # only used for re-runs 
            # data struct is a list of dicts
            # loop through pull out sub id and check if match skip
            skip = None
            for item in data_struct.data_struct:
                if submission_id == item["submission_id"]:
                    skip = True
            if skip and skip is not None:
                # skip sub its already processed
                print("top skip")
                continue
            '''

            sub_response  = self.submittable.getSubmission(submission_id)
            # project_id = sub_response.getProjectId()
            # get submission form responses (initial)
            response_list = sub_response.getFormResponses()
            # print(f"response list length: {len(response_list)}")

            # for each submission clear the options list
            multi_select_options_1 = []
            multi_select_options_2 = []
            multi_select_options_3 = []
            multi_select_options_4 = []

            single_select_options_1 = []
            single_select_options_2 = []
            single_select_options_3 = []
            single_select_options_4 = []
            single_select_options_5 = []
            single_select_options_6 = []
            single_select_options_7 = []
            single_select_options_8 = []
            single_select_options_9 = []
            single_select_options_10 = []
            single_select_options_11 = []
            single_select_options_12 = []
            single_select_options_13 = []
            single_select_options_14 = []
            single_select_options_15 = []
            single_select_options_16 = []
            single_select_options_17 = []
            single_select_options_18 = []
            single_select_options_19 = []
            single_select_options_20 = []
            single_select_options_21 = []
            single_select_options_22 = []
            single_select_options_23 = []
            single_select_options_24 = []
            single_select_options_25 = []

            # load database from project 1 (AEP)
            if project_id == self.project_id_1:
                print("project 1 - Submission")
                ref_email = sub_response.getSubmitterEmail()
                # print(f"ref email is: {ref_email}")

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

                    # Pull the initial forms response data
                    field_data = response.getFieldData()

                    # Get the primary artist UID fields
                    for data in field_data:
                        field_id = data.getFormFieldId()
                        # print(f"field_id: {field_id}")

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
                            for resp in reference_responses:
                                # logger.info(f"ref response refEmail 1: {resp.getRefEmail()}, ref_email: {ref_email}")
                                if resp.getFormFieldId() == config.reference_form_field_id_1 and ref_email == resp.getRefEmail():
                                    if date_1 is None or date_1 < resp.getCreatedAt():
                                        date_1 = resp.getCreatedAt()
                                        ref_field_data = resp.getFieldData()
                                        for ref_data in ref_field_data:
                                            # logger.info(f"ref form data 1: {ref_data}")
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
                                        logger.info(f"collab_unique_id_1: {collab_unique_id_1}")

                        elif field_id == config.reference_form_field_id_2:
                            for resp in reference_responses:
                                # logger.info(f"ref response refEmail 2: {resp.getRefEmail()}, ref_email: {ref_email}")
                                if resp.getFormFieldId() == config.reference_form_field_id_2 and ref_email == resp.getRefEmail():
                                    if date_1 is None or date_1 < resp.getCreatedAt():
                                        date_1 = resp.getCreatedAt()
                                        ref_field_data = resp.getFieldData()
                                        for ref_data in ref_field_data:
                                            # logger.info(f"ref form data 2: {ref_data}")
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
                                        logger.info(f"collab_unique_id_2: {collab_unique_id_2}")

                        elif field_id == config.reference_form_field_id_3:
                            for resp in reference_responses:
                                # logger.info(f"ref response refEmail 3: {resp.getRefEmail()}, ref_email: {ref_email}")
                                if resp.getFormFieldId() == config.reference_form_field_id_3 and ref_email == resp.getRefEmail():
                                    if date_1 is None or date_1 < resp.getCreatedAt():
                                        date_1 = resp.getCreatedAt()
                                        ref_field_data = resp.getFieldData()
                                        for ref_data in ref_field_data:
                                            # logger.info(f"ref form data 3: {ref_data}")
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
                                        logger.info(f"collab_unique_id_3: {collab_unique_id_3}")

                        elif field_id == config.reference_form_field_id_4:
                            for resp in reference_responses:
                                # logger.info(f"ref response refEmail 4: {resp.getRefEmail()}, ref_email: {ref_email}")
                                if resp.getFormFieldId() == config.reference_form_field_id_4 and ref_email == resp.getRefEmail():
                                    if date_1 is None or date_1 < resp.getCreatedAt():
                                        date_1 = resp.getCreatedAt()
                                        ref_field_data = resp.getFieldData()
                                        for ref_data in ref_field_data:
                                            # logger.info(f"ref form data 4: {ref_data}")
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
                                        logger.info(f"collab_unique_id_4: {collab_unique_id_4}")

                        elif field_id == config.reference_form_field_id_5:
                            for resp in reference_responses:
                                # logger.info(f"ref response refEmail 5: {resp.getRefEmail()}, ref_email: {ref_email}")
                                if resp.getFormFieldId() == config.reference_form_field_id_5 and ref_email == resp.getRefEmail():
                                    if date_1 is None or date_1 < resp.getCreatedAt():
                                        date_1 = resp.getCreatedAt()
                                        ref_field_data = resp.getFieldData()
                                        for ref_data in ref_field_data:
                                            # logger.info(f"ref form data 5: {ref_data}")
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
                                        logger.info("collab_unique_id_5: {collab_unique_id_5}")

                        elif field_id == config.reference_form_field_id_6:
                            for resp in reference_responses:
                                # logger.info(f"ref response refEmail 6: {resp.getRefEmail()}, ref_email: {ref_email}")
                                if resp.getFormFieldId() == config.reference_form_field_id_6 and ref_email == resp.getRefEmail():
                                    if date_1 is None or date_1 < resp.getCreatedAt():
                                        date_1 = resp.getCreatedAt()
                                        ref_field_data = resp.getFieldData()
                                        for ref_data in ref_field_data:
                                            # logger.info(f"ref form data 6: {ref_data}")
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
                                        logger.info(f"collab_unique_id_6: {collab_unique_id_6}")

                        elif field_id == config.reference_form_field_id_7:
                            for resp in reference_responses:
                                # logger.info(f"ref response refEmail 7: {resp.getRefEmail()}, ref_email: {ref_email}")
                                if resp.getFormFieldId() == config.reference_form_field_id_7 and ref_email == resp.getRefEmail():
                                    if date_1 is None or date_1 < resp.getCreatedAt():
                                        date_1 = resp.getCreatedAt()
                                        ref_field_data = resp.getFieldData()
                                        for ref_data in ref_field_data:
                                            # logger.info(f"ref form data 7: {ref_data}")
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
                                        logger.info(f"collab_unique_id_7: {collab_unique_id_7}")

                        elif field_id == config.reference_form_field_id_8:
                            for resp in reference_responses:
                                # logger.info(f"ref response refEmail 8: {resp.getRefEmail()}, ref_email: {ref_email}")
                                if resp.getFormFieldId() == config.reference_form_field_id_8 and ref_email == resp.getRefEmail():
                                    if date_1 is None or date_1 < resp.getCreatedAt():
                                        date_1 = resp.getCreatedAt()
                                        ref_field_data = resp.getFieldData()
                                        for ref_data in ref_field_data:
                                            # logger.info(f"ref form data 8: {ref_data}")
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
                                        logger.info(f"collab_unique_id_8: {collab_unique_id_8}")

                        elif field_id == config.reference_form_field_id_9:
                            for resp in reference_responses:
                                # logger.info(f"ref response refEmail 9: {resp.getRefEmail()}, ref_email: {ref_email}")
                                if resp.getFormFieldId() == config.reference_form_field_id_9 and ref_email == resp.getRefEmail():
                                    if date_1 is None or date_1 < resp.getCreatedAt():
                                        date_1 = resp.getCreatedAt()
                                        ref_field_data = resp.getFieldData()
                                        for ref_data in ref_field_data:
                                            # logger.info(f"ref form data 9: {ref_data}")
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
                                        logger.info(f"collab_unique_id_9: {collab_unique_id_9}")

                        # map multi-select fields to internal form single select fields
                        elif field_id == config.project_1_multi_select_id_1:
                            multi_select_options_1 = data.getOptions()
                            for option in multi_select_options_1:
                                if option == config.project_1_multi_options_ids_1[0]:
                                    single_select_options_1.append(config.single_select_option_id_1)
                                elif option == config.project_1_multi_options_ids_1[1]:
                                    single_select_options_2.append(config.single_select_option_id_2)
                                elif option == config.project_1_multi_options_ids_1[2]:
                                    single_select_options_3.append(config.single_select_option_id_3)
                                elif option == config.project_1_multi_options_ids_1[3]:
                                    single_select_options_4.append(config.single_select_option_id_4)
                                elif option == config.project_1_multi_options_ids_1[4]:
                                    single_select_options_5.append(config.single_select_option_id_5)
                                elif option == config.project_1_multi_options_ids_1[5]:
                                    single_select_options_6.append(config.single_select_option_id_6)
                                elif option == config.project_1_multi_options_ids_1[6]:
                                    single_select_options_7.append(config.single_select_option_id_7)
                                elif option == config.project_1_multi_options_ids_1[7]:
                                    single_select_options_8.append(config.single_select_option_id_8)
                                elif option == config.project_1_multi_options_ids_1[8]:
                                    single_select_options_9.append(config.single_select_option_id_9)

                        elif field_id == config.project_1_multi_select_id_2:
                            multi_select_options_2 = data.getOptions()
                            for option in multi_select_options_2:
                                if option == config.project_1_multi_options_ids_2[0]:
                                    single_select_options_10.append(config.single_select_option_id_10)
                                elif option == config.project_1_multi_options_ids_2[1]:
                                    single_select_options_11.append(config.single_select_option_id_11)
                                elif option == config.project_1_multi_options_ids_2[2]:
                                    single_select_options_12.append(config.single_select_option_id_12)
                                elif option == config.project_1_multi_options_ids_2[3]:
                                    single_select_options_13.append(config.single_select_option_id_13)
                                elif option == config.project_1_multi_options_ids_2[4]:
                                    single_select_options_14.append(config.single_select_option_id_14)
                                elif option == config.project_1_multi_options_ids_2[5]:
                                    single_select_options_15.append(config.single_select_option_id_15)

                        elif field_id == config.project_1_multi_select_id_3:
                            multi_select_options_3 = data.getOptions()
                            for option in multi_select_options_3:
                                if option == config.project_1_multi_options_ids_3[0]:
                                    single_select_options_16.append(config.single_select_option_id_16)
                                elif option == config.project_1_multi_options_ids_3[1]:
                                    single_select_options_17.append(config.single_select_option_id_17)
                                elif option == config.project_1_multi_options_ids_3[2]:
                                    single_select_options_18.append(config.single_select_option_id_18)
                                elif option == config.project_1_multi_options_ids_3[3]:
                                    single_select_options_19.append(config.single_select_option_id_19)
                                elif option == config.project_1_multi_options_ids_3[4]:
                                    single_select_options_20.append(config.single_select_option_id_20)

                    # create the primary UID
                    if primary_last_name is not None and primary_dob is not None and primary_zip is not None:
                        primary_unique_id = str(primary_dob) + str(primary_last_name) + str(primary_zip)
                        primary_unique_id = primary_unique_id.replace(" ", "")
                        primary_unique_id = primary_unique_id.replace("-", "")
                        logger.info(f"project 1 - primary_unique_id: {primary_unique_id}")

                    # check for duplicate collaborator ids internal to the submission
                    id_list_check = [primary_unique_id, collab_unique_id_1,
                                     collab_unique_id_2, collab_unique_id_3,
                                     collab_unique_id_4, collab_unique_id_5,
                                     collab_unique_id_6, collab_unique_id_7,
                                     collab_unique_id_8, collab_unique_id_9]

                    # logger.info(f"id list: {id_list_check}")

                    # pull id out then loop through the list to check for dup
                    # check the uids in the form for dups
                    for elem in id_list_check:
                        if id_list_check.count(elem) > 1 and elem is not None:
                            logger.info(f"project 1 - INTERNAL FORM duplicate unique id project 1 {primary_unique_id} for submission {submission_id}")
                            try:
                                # add dup label to this submission (single form dup)
                                # logger.info(f"project 1 - try to create label")
                                self.label_dups(submission_id, submission_id)
                                break
                            except ValueError:
                                # logger.info(f"project 1 - failed to create duplicate label for submission id {submission_id}")
                                break
                        else:
                            continue

                    if primary_last_name is not None and primary_dob is not None and primary_zip is not None:
                        try:
                            self.submittable.submitInternalFormResponse(submission_id,            primary_unique_id,
                                                                        single_select_options_1,  single_select_options_2,
                                                                        single_select_options_3,  single_select_options_4,
                                                                        single_select_options_5,  single_select_options_6,
                                                                        single_select_options_7,  single_select_options_8,
                                                                        single_select_options_9,  single_select_options_10,
                                                                        single_select_options_11, single_select_options_12,
                                                                        single_select_options_13, single_select_options_14,
                                                                        single_select_options_15, single_select_options_16,
                                                                        single_select_options_17, single_select_options_18,
                                                                        single_select_options_19, single_select_options_20,
                                                                        single_select_options_21, single_select_options_22,
                                                                        single_select_options_23, single_select_options_24,
                                                                        single_select_options_25, collab_unique_id_1,
                                                                        collab_unique_id_2,       collab_unique_id_3,
                                                                        collab_unique_id_4,       collab_unique_id_5,
                                                                        collab_unique_id_6,       collab_unique_id_7,
                                                                        collab_unique_id_8,       collab_unique_id_9)

                        except:
                            logger.info(f"project 1 - failed to create internal form for submission {submission_id}")

                        # check if UID already exist in list of dicts
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
                            # print("project 1 - dup found")
                            self.label_dups(submission_id, uid_check_sub_id_1)
                        elif uid_check_sub_id_2 is not None:
                            # print((f"project 1 - collab_unique_id_2 dup found")
                            self.label_dups(submission_id, uid_check_sub_id_2)
                        elif uid_check_sub_id_3 is not None:
                            # print(("project 1 - collab_unique_id_3 dup found")
                            self.label_dups(submission_id, uid_check_sub_id_3)
                        elif uid_check_sub_id_4 is not None:
                            # print(("project 1 - collab_unique_id_4 dup found")
                            self.label_dups(submission_id, uid_check_sub_id_4)
                        elif uid_check_sub_id_5 is not None:
                            # print(("project 1 - collab_unique_id_5 dup found")
                            self.label_dups(submission_id, uid_check_sub_id_5)
                        elif uid_check_sub_id_6 is not None:
                            # print(("project 1 - collab_unique_id_6 dup found")
                            self.label_dups(submission_id, uid_check_sub_id_6)
                        elif uid_check_sub_id_7 is not None:
                            # print(("project 1 - collab_unique_id_7 dup found")
                            self.label_dups(submission_id, uid_check_sub_id_7)
                        elif uid_check_sub_id_8 is not None:
                            # print(("project 1 - collab_unique_id_7 dup found")
                            self.label_dups(submission_id, uid_check_sub_id_8)
                        elif uid_check_sub_id_9 is not None:
                            # print(("project 1 - collab_unique_id_8 dup found")
                            self.label_dups(submission_id, uid_check_sub_id_9)
                        elif uid_check_sub_id_10 is not None:
                            # print(("project 1 - collab_unique_id_9 dup found")
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
                        # logger.info(f"project 2 - data in field_data {data}")
                        field_id    = data.getFormFieldId()
                        field_value = responses.getFieldResponse(field_id)
                        field_id    = field_value.getFormFieldId()

                        # Primary Artist UID | DOB-LastName-Zipcode
                        if field_id == config.project_2_name_field_id:
                            primary_last_name = data.getFieldValue("SHORT_ANSWER")
                        elif field_id == config.project_2_dob_field_id:
                            date_string = data.getFieldValue("DATE")
                            primary_dob = date_string[0:10]
                        elif field_id == config.project_2_zipcode_field_id:
                            primary_zip = data.getFieldValue("SHORT_ANSWER")

                        # map multi-select fields to internal form single select fields
                        elif field_id == config.project_2_multi_select_id_1:
                            multi_select_options_1 = data.getOptions()
                            for option in multi_select_options_1:
                                if option == config.project_2_multi_options_ids_1[0]:
                                    single_select_options_1.append(config.single_select_option_id_1)
                                elif option == config.project_2_multi_options_ids_1[1]:
                                    single_select_options_2.append(config.single_select_option_id_2)
                                elif option == config.project_2_multi_options_ids_1[2]:
                                    single_select_options_3.append(config.single_select_option_id_3)
                                elif option == config.project_2_multi_options_ids_1[3]:
                                    single_select_options_4.append(config.single_select_option_id_4)
                                elif option == config.project_2_multi_options_ids_1[4]:
                                    single_select_options_5.append(config.single_select_option_id_5)
                                elif option == config.project_2_multi_options_ids_1[5]:
                                    single_select_options_6.append(config.single_select_option_id_6)
                                elif option == config.project_2_multi_options_ids_1[6]:
                                    single_select_options_7.append(config.single_select_option_id_7)
                                elif option == config.project_2_multi_options_ids_1[7]:
                                    single_select_options_8.append(config.single_select_option_id_8)
                                elif option == config.project_2_multi_options_ids_1[8]:
                                    single_select_options_9.append(config.single_select_option_id_9)

                        elif field_id == config.project_2_multi_select_id_2:
                            multi_select_options_2 = data.getOptions()
                            for option in multi_select_options_2:
                                if option == config.project_2_multi_options_ids_2[0]:
                                    single_select_options_10.append(config.single_select_option_id_10)
                                elif option == config.project_2_multi_options_ids_2[1]:
                                    single_select_options_11.append(config.single_select_option_id_11)
                                elif option == config.project_2_multi_options_ids_2[2]:
                                    single_select_options_12.append(config.single_select_option_id_12)
                                elif option == config.project_2_multi_options_ids_2[3]:
                                    single_select_options_13.append(config.single_select_option_id_13)
                                elif option == config.project_2_multi_options_ids_2[4]:
                                    single_select_options_14.append(config.single_select_option_id_14)
                                elif option == config.project_2_multi_options_ids_2[5]:
                                    single_select_options_15.append(config.single_select_option_id_15)

                        elif field_id == config.project_2_multi_select_id_3:
                            multi_select_options_3 = data.getOptions()
                            for option in multi_select_options_3:
                                if option == config.project_2_multi_options_ids_3[0]:
                                    single_select_options_16.append(config.single_select_option_id_16)
                                elif option == config.project_2_multi_options_ids_3[1]:
                                    single_select_options_17.append(config.single_select_option_id_17)
                                elif option == config.project_2_multi_options_ids_3[2]:
                                    single_select_options_18.append(config.single_select_option_id_18)
                                elif option == config.project_2_multi_options_ids_3[3]:
                                    single_select_options_19.append(config.single_select_option_id_19)
                                elif option == config.project_2_multi_options_ids_3[4]:
                                    single_select_options_20.append(config.single_select_option_id_20)

                        # GI project only
                        elif field_id == config.project_2_multi_select_id_4:
                            multi_select_options_4 = data.getOptions()
                            for option in multi_select_options_4:
                                if option == config.project_2_multi_options_ids_4[0]:
                                    single_select_options_21.append(config.single_select_option_id_21)
                                elif option == config.project_2_multi_options_ids_4[1]:
                                    single_select_options_22.append(config.single_select_option_id_22)
                                elif option == config.project_2_multi_options_ids_4[2]:
                                    single_select_options_23.append(config.single_select_option_id_23)
                                elif option == config.project_2_multi_options_ids_4[3]:
                                    single_select_options_24.append(config.single_select_option_id_24)
                                elif option == config.project_2_multi_options_ids_4[4]:
                                    single_select_options_25.append(config.single_select_option_id_25)


                    # create the primary UID
                    primary_unique_id = str(primary_dob) + str(primary_last_name) + str(primary_zip)
                    primary_unique_id = primary_unique_id.replace(" ", "")
                    primary_unique_id = primary_unique_id.replace("-", "")
                    logger.info(f"project 2 - primary_unique_id: {primary_unique_id}")

                    try:
                        if primary_last_name is not None and primary_dob is not None and primary_zip is not None:
                            # create internal entry using beta endpoint - Work In Progress
                            try:
                                self.submittable.submitInternalFormResponse(submission_id,            primary_unique_id,
                                                                            single_select_options_1,  single_select_options_2,
                                                                            single_select_options_3,  single_select_options_4,
                                                                            single_select_options_5,  single_select_options_6,
                                                                            single_select_options_7,  single_select_options_8,
                                                                            single_select_options_9,  single_select_options_10,
                                                                            single_select_options_11, single_select_options_12,
                                                                            single_select_options_13, single_select_options_14,
                                                                            single_select_options_15, single_select_options_16,
                                                                            single_select_options_17, single_select_options_18,
                                                                            single_select_options_19, single_select_options_20,
                                                                            single_select_options_21, single_select_options_22,
                                                                            single_select_options_23, single_select_options_24,
                                                                            single_select_options_25)
                            except:
                                logger.info(f"project 2 - failed to create/update internal form for submission {submission_id}")

                            # check if uid already exist in list of dicts
                            uid_check_sub_id_1 = self.uid_chcek(primary_unique_id)
                            if uid_check_sub_id_1 is not None:
                                logger.info(f"project 2 - dup found")
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
                        # log the failure
                        logger.info(f"project 2 - failed to check unique id: {primary_unique_id} submission: {submission_id}")

        # log the completed list of UIDs
        logger.info(f"config struct {config.uid_data_struct}")
