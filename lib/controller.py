import data_struct
from lib.submittable import *
import config
import logging


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
        self.label_id_1   = config.dup_label_id



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
        print(f"checking artists")

        # build up submission id list
        # get all submission for project 1 & project 2 in "new" and "in_progress" states
        # list_of_submissions = self.submittable.getListOfSubmissions()
        list_of_submissions = [23232315, 23231955, 23231915, 23231871, 23231790, 23231747, 23231718, 23231708, 23231687, 23231587, 23231570, 23231567, 23231523]

        # get list of reference form responses
        # reference_responses = self.submittable.getReferenceResponses()

        for sub_item in list_of_submissions:
            submission_id = sub_item
            # submission_id = sub_item.getSubmissionId()
            # project_id    = sub_item.getProjectId()

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

            print("get submission")
            sub_response  = self.submittable.getSubmission(submission_id)
            project_id = sub_response.getProjectId()

            # check for Migrated label - skip submission if label is present
            check_labels  = sub_response.getLabels()
            set_break     = False
            for label in check_labels:
                if config.migrated_label == str(label.getLabelId()):
                    set_break = True
            if set_break:
                # skip submission
                continue


            # get submission form responses (initial)
            response_list = sub_response.getFormResponses()
            # print(f"response list length: {len(response_list)}")

            # for each submission clear the options list
            multi_select_options_1 = []
            multi_select_options_2 = []
            multi_select_options_3 = []
            multi_select_options_4 = []
            multi_select_options_5 = []
            multi_select_options_6 = []
            multi_select_options_7 = []
            multi_select_options_8 = []
            multi_select_options_9 = []
            multi_select_options_10 = []
            multi_select_options_11 = []
            multi_select_options_12 = []
            multi_select_options_13 = []
            multi_select_options_14 = []
            multi_select_options_15 = []
            multi_select_options_16 = []
            multi_select_options_17 = []
            multi_select_options_18 = []
            multi_select_options_19 = []
            multi_select_options_20 = []
            multi_select_options_21 = []
            multi_select_options_22 = []
            multi_select_options_23 = []
            multi_select_options_24 = []
            multi_select_options_25 = []
            multi_select_options_26 = []
            multi_select_options_27 = []
            multi_select_options_28 = []
            multi_select_options_29 = []
            multi_select_options_30 = []
            multi_select_options_31 = []
            multi_select_options_32 = []
            multi_select_options_33 = []

            single_select_options_1  = []
            single_select_options_2  = []
            single_select_options_3  = []
            single_select_options_4  = []
            single_select_options_5  = []
            single_select_options_6  = []
            single_select_options_7  = []
            single_select_options_8  = []
            single_select_options_9  = []
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

            single_select_options_26 = []
            single_select_options_27 = []
            single_select_options_28 = []
            single_select_options_29 = []
            single_select_options_30 = []
            single_select_options_31 = []
            single_select_options_32 = []
            single_select_options_33 = []
            single_select_options_34 = []
            single_select_options_35 = []
            single_select_options_36 = []
            single_select_options_37 = []
            single_select_options_38 = []
            single_select_options_39 = []
            single_select_options_40 = []
            single_select_options_41 = []
            single_select_options_42 = []
            single_select_options_43 = []
            single_select_options_44 = []
            single_select_options_45 = []
            single_select_options_46 = []
            single_select_options_47 = []
            single_select_options_48 = []
            single_select_options_49 = []
            single_select_options_50 = []

            single_select_options_51 = []
            single_select_options_52 = []
            single_select_options_53 = []
            single_select_options_54 = []
            single_select_options_55 = []
            single_select_options_56 = []
            single_select_options_57 = []
            single_select_options_58 = []
            single_select_options_59 = []
            single_select_options_60 = []
            single_select_options_61 = []
            single_select_options_62 = []
            single_select_options_63 = []
            single_select_options_64 = []
            single_select_options_65 = []
            single_select_options_66 = []
            single_select_options_67 = []
            single_select_options_68 = []
            single_select_options_69 = []
            single_select_options_70 = []
            single_select_options_71 = []
            single_select_options_72 = []
            single_select_options_73 = []
            single_select_options_74 = []
            single_select_options_75 = []

            single_select_options_76 = []
            single_select_options_77 = []
            single_select_options_78 = []
            single_select_options_79 = []
            single_select_options_80 = []
            single_select_options_81 = []
            single_select_options_82 = []
            single_select_options_83 = []
            single_select_options_84 = []
            single_select_options_85 = []
            single_select_options_86 = []
            single_select_options_87 = []
            single_select_options_88 = []
            single_select_options_89 = []
            single_select_options_90 = []
            single_select_options_91 = []
            single_select_options_92 = []
            single_select_options_93 = []
            single_select_options_94 = []
            single_select_options_95 = []
            single_select_options_96 = []
            single_select_options_97 = []
            single_select_options_98 = []
            single_select_options_99 = []
            single_select_options_100 = []

            single_select_options_101 = []
            single_select_options_102 = []
            single_select_options_103 = []
            single_select_options_104 = []
            single_select_options_105 = []
            single_select_options_106 = []
            single_select_options_107 = []
            single_select_options_108 = []
            single_select_options_109 = []
            single_select_options_110 = []
            single_select_options_111 = []
            single_select_options_112 = []
            single_select_options_113 = []
            single_select_options_114 = []
            single_select_options_115 = []
            single_select_options_116 = []
            single_select_options_117 = []
            single_select_options_118 = []
            single_select_options_119 = []
            single_select_options_120 = []
            single_select_options_121 = []
            single_select_options_122 = []
            single_select_options_123 = []
            single_select_options_124 = []
            single_select_options_125 = []

            single_select_options_126 = []
            single_select_options_127 = []
            single_select_options_128 = []
            single_select_options_129 = []
            single_select_options_130 = []
            single_select_options_131 = []
            single_select_options_132 = []
            single_select_options_133 = []
            single_select_options_134 = []
            single_select_options_135 = []
            single_select_options_136 = []
            single_select_options_137 = []
            single_select_options_138 = []
            single_select_options_139 = []
            single_select_options_140 = []
            single_select_options_141 = []
            single_select_options_142 = []
            single_select_options_143 = []
            single_select_options_144 = []
            single_select_options_145 = []
            single_select_options_146 = []
            single_select_options_147 = []
            single_select_options_148 = []
            single_select_options_149 = []
            single_select_options_150 = []

            single_select_options_151 = []
            single_select_options_152 = []
            single_select_options_153 = []
            single_select_options_154 = []
            single_select_options_155 = []
            single_select_options_156 = []
            single_select_options_157 = []
            single_select_options_158 = []
            single_select_options_159 = []
            single_select_options_160 = []
            single_select_options_161 = []
            single_select_options_162 = []
            single_select_options_163 = []
            single_select_options_164 = []
            single_select_options_165 = []
            single_select_options_166 = []
            single_select_options_167 = []
            single_select_options_168 = []
            single_select_options_169 = []
            single_select_options_170 = []
            single_select_options_171 = []
            single_select_options_172 = []
            single_select_options_173 = []
            single_select_options_174 = []
            single_select_options_175 = []

            single_select_options_176 = []
            single_select_options_177 = []
            single_select_options_178 = []
            single_select_options_179 = []
            single_select_options_180 = []
            single_select_options_181 = []
            single_select_options_182 = []
            single_select_options_183 = []
            single_select_options_184 = []
            single_select_options_185 = []
            single_select_options_186 = []
            single_select_options_187 = []
            single_select_options_188 = []
            single_select_options_189 = []
            single_select_options_190 = []
            single_select_options_191 = []
            single_select_options_192 = []
            single_select_options_193 = []
            single_select_options_194 = []
            single_select_options_195 = []
            single_select_options_196 = []
            single_select_options_197 = []
            single_select_options_198 = []
            single_select_options_199 = []
            single_select_options_200 = []


            single_select_options_201 = []
            single_select_options_202 = []
            single_select_options_203 = []
            single_select_options_204 = []
            single_select_options_205 = []
            single_select_options_206 = []
            single_select_options_207 = []
            single_select_options_208 = []
            single_select_options_209 = []
            single_select_options_210 = []
            single_select_options_211 = []
            single_select_options_212 = []
            single_select_options_213 = []
            single_select_options_214 = []
            single_select_options_215 = []
            single_select_options_216 = []
            single_select_options_217 = []
            single_select_options_218 = []
            single_select_options_219 = []
            single_select_options_220 = []
            single_select_options_221 = []
            single_select_options_222 = []
            single_select_options_223 = []
            single_select_options_224 = []
            single_select_options_225 = []

            single_select_options_226 = []
            single_select_options_227 = []
            single_select_options_228 = []
            single_select_options_229 = []
            single_select_options_230 = []
            single_select_options_231 = []
            single_select_options_232 = []
            single_select_options_233 = []
            single_select_options_234 = []
            single_select_options_235 = []
            single_select_options_236 = []
            single_select_options_237 = []
            single_select_options_238 = []
            single_select_options_239 = []
            single_select_options_240 = []
            single_select_options_241 = []
            single_select_options_242 = []
            single_select_options_243 = []
            single_select_options_244 = []
            single_select_options_245 = []
            single_select_options_246 = []
            single_select_options_247 = []
            single_select_options_248 = []
            single_select_options_249 = []
            single_select_options_250 = []

            # load database from project 1 (AEP)
            if project_id == self.project_id_1:
                logger.info(f"project 1 - Submission {submission_id}")
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
                        #
                        # ineligible multi-selects
                        elif field_id == config.ineligible_survey_multi_select_id_1:
                            multi_select_options_1 = data.getOptions()
                            for option in multi_select_options_1:
                                if option == config.ineligible_survey_multi_options_ids_1[0]:
                                    single_select_options_1.append(config.ineligible_single_select_option_id_1)
                                elif option == config.ineligible_survey_multi_options_ids_1[1]:
                                    single_select_options_2.append(config.ineligible_single_select_option_id_2)
                                elif option == config.ineligible_survey_multi_options_ids_1[2]:
                                    single_select_options_3.append(config.ineligible_single_select_option_id_3)
                                elif option == config.ineligible_survey_multi_options_ids_1[3]:
                                    single_select_options_4.append(config.ineligible_single_select_option_id_4)
                                elif option == config.ineligible_survey_multi_options_ids_1[4]:
                                    single_select_options_5.append(config.ineligible_single_select_option_id_5)
                                elif option == config.ineligible_survey_multi_options_ids_1[5]:
                                    single_select_options_6.append(config.ineligible_single_select_option_id_6)

                        elif field_id == config.ineligible_survey_multi_select_id_2:
                            multi_select_options_2 = data.getOptions()
                            for option in multi_select_options_2:
                                if option == config.ineligible_survey_multi_options_ids_2[0]:
                                    single_select_options_7.append(config.ineligible_single_select_option_id_7)
                                elif option == config.ineligible_survey_multi_options_ids_2[1]:
                                    single_select_options_8.append(config.ineligible_single_select_option_id_8)
                                elif option == config.ineligible_survey_multi_options_ids_2[2]:
                                    single_select_options_9.append(config.ineligible_single_select_option_id_9)
                                elif option == config.ineligible_survey_multi_options_ids_2[3]:
                                    single_select_options_10.append(config.ineligible_single_select_option_id_10)
                                elif option == config.ineligible_survey_multi_options_ids_2[4]:
                                    single_select_options_11.append(config.ineligible_single_select_option_id_11)
                                elif option == config.ineligible_survey_multi_options_ids_2[5]:
                                    single_select_options_12.append(config.ineligible_single_select_option_id_12)
                                elif option == config.ineligible_survey_multi_options_ids_2[6]:
                                    single_select_options_13.append(config.ineligible_single_select_option_id_13)

                        elif field_id == config.ineligible_survey_multi_select_id_3:
                            multi_select_options_3 = data.getOptions()
                            for option in multi_select_options_3:
                                if option == config.ineligible_survey_multi_options_ids_3[0]:
                                    single_select_options_14.append(config.ineligible_single_select_option_id_14)
                                elif option == config.ineligible_survey_multi_options_ids_3[1]:
                                    single_select_options_15.append(config.ineligible_single_select_option_id_15)
                                elif option == config.ineligible_survey_multi_options_ids_3[2]:
                                    single_select_options_16.append(config.ineligible_single_select_option_id_16)
                                elif option == config.ineligible_survey_multi_options_ids_3[3]:
                                    single_select_options_17.append(config.ineligible_single_select_option_id_17)
                                elif option == config.ineligible_survey_multi_options_ids_3[4]:
                                    single_select_options_18.append(config.ineligible_single_select_option_id_18)

                        elif field_id == config.ineligible_survey_multi_select_id_4:
                            multi_select_options_4 = data.getOptions()
                            for option in multi_select_options_4:
                                if option == config.ineligible_survey_multi_options_ids_4[0]:
                                    single_select_options_19.append(config.ineligible_single_select_option_id_19)
                                elif option == config.ineligible_survey_multi_options_ids_4[1]:
                                    single_select_options_20.append(config.ineligible_single_select_option_id_20)
                                elif option == config.ineligible_survey_multi_options_ids_4[2]:
                                    single_select_options_21.append(config.ineligible_single_select_option_id_21)
                                elif option == config.ineligible_survey_multi_options_ids_4[3]:
                                    single_select_options_22.append(config.ineligible_single_select_option_id_22)
                                elif option == config.ineligible_survey_multi_options_ids_4[4]:
                                    single_select_options_23.append(config.ineligible_single_select_option_id_23)
                                elif option == config.ineligible_survey_multi_options_ids_4[5]:
                                    single_select_options_24.append(config.ineligible_single_select_option_id_24)
                                elif option == config.ineligible_survey_multi_options_ids_4[6]:
                                    single_select_options_25.append(config.ineligible_single_select_option_id_25)
                                elif option == config.ineligible_survey_multi_options_ids_4[7]:
                                    single_select_options_26.append(config.ineligible_single_select_option_id_26)
                                elif option == config.ineligible_survey_multi_options_ids_4[8]:
                                    single_select_options_27.append(config.ineligible_single_select_option_id_27)
                                elif option == config.ineligible_survey_multi_options_ids_4[9]:
                                    single_select_options_28.append(config.ineligible_single_select_option_id_28)

                        elif field_id == config.ineligible_survey_multi_select_id_5:
                            multi_select_options_5 = data.getOptions()
                            for option in multi_select_options_5:
                                if option == config.ineligible_survey_multi_options_ids_5[0]:
                                    single_select_options_29.append(config.ineligible_single_select_option_id_29)
                                elif option == config.ineligible_survey_multi_options_ids_5[1]:
                                    single_select_options_30.append(config.ineligible_single_select_option_id_30)
                                elif option == config.ineligible_survey_multi_options_ids_5[2]:
                                    single_select_options_31.append(config.ineligible_single_select_option_id_31)
                                elif option == config.ineligible_survey_multi_options_ids_5[3]:
                                    single_select_options_32.append(config.ineligible_single_select_option_id_32)
                                elif option == config.ineligible_survey_multi_options_ids_5[4]:
                                    single_select_options_33.append(config.ineligible_single_select_option_id_33)
                                elif option == config.ineligible_survey_multi_options_ids_5[5]:
                                    single_select_options_34.append(config.ineligible_single_select_option_id_34)

                        elif field_id == config.ineligible_survey_multi_select_id_6:
                            multi_select_options_6 = data.getOptions()
                            for option in multi_select_options_6:
                                if option == config.ineligible_survey_multi_options_ids_6[0]:
                                    single_select_options_35.append(config.ineligible_single_select_option_id_35)
                                elif option == config.ineligible_survey_multi_options_ids_6[1]:
                                    single_select_options_36.append(config.ineligible_single_select_option_id_36)
                                elif option == config.ineligible_survey_multi_options_ids_6[2]:
                                    single_select_options_37.append(config.ineligible_single_select_option_id_37)
                                elif option == config.ineligible_survey_multi_options_ids_6[3]:
                                    single_select_options_38.append(config.ineligible_single_select_option_id_38)
                                elif option == config.ineligible_survey_multi_options_ids_6[4]:
                                    single_select_options_39.append(config.ineligible_single_select_option_id_39)
                                elif option == config.ineligible_survey_multi_options_ids_6[5]:
                                    single_select_options_40.append(config.ineligible_single_select_option_id_40)
                                elif option == config.ineligible_survey_multi_options_ids_6[6]:
                                    single_select_options_41.append(config.ineligible_single_select_option_id_41)
                                elif option == config.ineligible_survey_multi_options_ids_6[7]:
                                    single_select_options_42.append(config.ineligible_single_select_option_id_42)
                                elif option == config.ineligible_survey_multi_options_ids_6[8]:
                                    single_select_options_43.append(config.ineligible_single_select_option_id_43)

                        elif field_id == config.ineligible_survey_multi_select_id_7:
                            multi_select_options_7 = data.getOptions()
                            for option in multi_select_options_7:
                                if option == config.ineligible_survey_multi_options_ids_7[0]:
                                    single_select_options_44.append(config.ineligible_single_select_option_id_44)
                                elif option == config.ineligible_survey_multi_options_ids_7[1]:
                                    single_select_options_45.append(config.ineligible_single_select_option_id_45)
                                elif option == config.ineligible_survey_multi_options_ids_7[2]:
                                    single_select_options_46.append(config.ineligible_single_select_option_id_46)
                                elif option == config.ineligible_survey_multi_options_ids_7[3]:
                                    single_select_options_47.append(config.ineligible_single_select_option_id_47)
                                elif option == config.ineligible_survey_multi_options_ids_7[4]:
                                    single_select_options_48.append(config.ineligible_single_select_option_id_48)
                                elif option == config.ineligible_survey_multi_options_ids_7[5]:
                                    single_select_options_49.append(config.ineligible_single_select_option_id_49)
                                elif option == config.ineligible_survey_multi_options_ids_7[6]:
                                    single_select_options_50.append(config.ineligible_single_select_option_id_50)
                                elif option == config.ineligible_survey_multi_options_ids_7[7]:
                                    single_select_options_51.append(config.ineligible_single_select_option_id_51)
                                elif option == config.ineligible_survey_multi_options_ids_7[8]:
                                    single_select_options_52.append(config.ineligible_single_select_option_id_52)
                                elif option == config.ineligible_survey_multi_options_ids_7[9]:
                                    single_select_options_53.append(config.ineligible_single_select_option_id_53)
                                elif option == config.ineligible_survey_multi_options_ids_7[10]:
                                    single_select_options_54.append(config.ineligible_single_select_option_id_54)
                                elif option == config.ineligible_survey_multi_options_ids_7[11]:
                                    single_select_options_55.append(config.ineligible_single_select_option_id_55)
                                elif option == config.ineligible_survey_multi_options_ids_7[12]:
                                    single_select_options_56.append(config.ineligible_single_select_option_id_56)
                                elif option == config.ineligible_survey_multi_options_ids_7[13]:
                                    single_select_options_57.append(config.ineligible_single_select_option_id_57)

                        elif field_id == config.ineligible_survey_multi_select_id_8:
                            multi_select_options_8 = data.getOptions()
                            for option in multi_select_options_8:
                                if option == config.ineligible_survey_multi_options_ids_8[0]:
                                    single_select_options_58.append(config.ineligible_single_select_option_id_58)
                                elif option == config.ineligible_survey_multi_options_ids_8[1]:
                                    single_select_options_59.append(config.ineligible_single_select_option_id_59)
                                elif option == config.ineligible_survey_multi_options_ids_8[2]:
                                    single_select_options_60.append(config.ineligible_single_select_option_id_60)
                                elif option == config.ineligible_survey_multi_options_ids_8[3]:
                                    single_select_options_61.append(config.ineligible_single_select_option_id_61)
                                elif option == config.ineligible_survey_multi_options_ids_8[4]:
                                    single_select_options_62.append(config.ineligible_single_select_option_id_62)
                                elif option == config.ineligible_survey_multi_options_ids_8[5]:
                                    single_select_options_63.append(config.ineligible_single_select_option_id_63)
                                elif option == config.ineligible_survey_multi_options_ids_8[6]:
                                    single_select_options_64.append(config.ineligible_single_select_option_id_64)
                                elif option == config.ineligible_survey_multi_options_ids_8[7]:
                                    single_select_options_65.append(config.ineligible_single_select_option_id_65)
                                elif option == config.ineligible_survey_multi_options_ids_8[8]:
                                    single_select_options_66.append(config.ineligible_single_select_option_id_66)
                                elif option == config.ineligible_survey_multi_options_ids_8[9]:
                                    single_select_options_67.append(config.ineligible_single_select_option_id_67)
                                elif option == config.ineligible_survey_multi_options_ids_8[10]:
                                    single_select_options_68.append(config.ineligible_single_select_option_id_68)
                                elif option == config.ineligible_survey_multi_options_ids_8[11]:
                                    single_select_options_69.append(config.ineligible_single_select_option_id_69)
                                elif option == config.ineligible_survey_multi_options_ids_8[12]:
                                    single_select_options_70.append(config.ineligible_single_select_option_id_70)

                        elif field_id == config.ineligible_survey_multi_select_id_9:
                            multi_select_options_9 = data.getOptions()
                            for option in multi_select_options_9:
                                if option == config.ineligible_survey_multi_options_ids_9[0]:
                                    single_select_options_71.append(config.ineligible_single_select_option_id_71)
                                elif option == config.ineligible_survey_multi_options_ids_9[1]:
                                    single_select_options_72.append(config.ineligible_single_select_option_id_72)
                                elif option == config.ineligible_survey_multi_options_ids_9[2]:
                                    single_select_options_73.append(config.ineligible_single_select_option_id_73)
                                elif option == config.ineligible_survey_multi_options_ids_9[3]:
                                    single_select_options_74.append(config.ineligible_single_select_option_id_74)
                                elif option == config.ineligible_survey_multi_options_ids_9[4]:
                                    single_select_options_75.append(config.ineligible_single_select_option_id_75)
                                elif option == config.ineligible_survey_multi_options_ids_9[5]:
                                    single_select_options_76.append(config.ineligible_single_select_option_id_76)
                                elif option == config.ineligible_survey_multi_options_ids_9[6]:
                                    single_select_options_77.append(config.ineligible_single_select_option_id_77)
                                elif option == config.ineligible_survey_multi_options_ids_9[7]:
                                    single_select_options_78.append(config.ineligible_single_select_option_id_78)
                                elif option == config.ineligible_survey_multi_options_ids_9[8]:
                                    single_select_options_79.append(config.ineligible_single_select_option_id_79)

                        elif field_id == config.ineligible_survey_multi_select_id_10:
                            multi_select_options_10 = data.getOptions()
                            for option in multi_select_options_10:
                                if option == config.ineligible_survey_multi_options_ids_10[0]:
                                    single_select_options_80.append(config.ineligible_single_select_option_id_80)
                                elif option == config.ineligible_survey_multi_options_ids_10[1]:
                                    single_select_options_81.append(config.ineligible_single_select_option_id_81)
                                elif option == config.ineligible_survey_multi_options_ids_10[2]:
                                    single_select_options_82.append(config.ineligible_single_select_option_id_82)
                                elif option == config.ineligible_survey_multi_options_ids_10[3]:
                                    single_select_options_83.append(config.ineligible_single_select_option_id_83)
                                elif option == config.ineligible_survey_multi_options_ids_10[4]:
                                    single_select_options_84.append(config.ineligible_single_select_option_id_84)
                                elif option == config.ineligible_survey_multi_options_ids_10[5]:
                                    single_select_options_85.append(config.ineligible_single_select_option_id_85)

                        elif field_id == config.ineligible_survey_multi_select_id_11:
                            multi_select_options_11 = data.getOptions()
                            for option in multi_select_options_11:
                                if option == config.ineligible_survey_multi_options_ids_11[0]:
                                    single_select_options_86.append(config.ineligible_single_select_option_id_86)
                                elif option == config.ineligible_survey_multi_options_ids_11[1]:
                                    single_select_options_87.append(config.ineligible_single_select_option_id_87)
                                elif option == config.ineligible_survey_multi_options_ids_11[2]:
                                    single_select_options_88.append(config.ineligible_single_select_option_id_88)
                                elif option == config.ineligible_survey_multi_options_ids_11[3]:
                                    single_select_options_89.append(config.ineligible_single_select_option_id_89)
                                elif option == config.ineligible_survey_multi_options_ids_11[4]:
                                    single_select_options_90.append(config.ineligible_single_select_option_id_90)

                        # AEP multi-select
                        elif field_id == config.aep_multi_select_id_1:
                            multi_select_options_12 = data.getOptions()
                            for option in multi_select_options_12:
                                if option   == config.aep_multi_options_ids_1[0]:
                                    single_select_options_91.append(config.aep_single_select_option_id_1)
                                elif option == config.aep_multi_options_ids_1[1]:
                                    single_select_options_92.append(config.aep_single_select_option_id_2)
                                elif option == config.aep_multi_options_ids_1[2]:
                                    single_select_options_93.append(config.aep_single_select_option_id_3)
                                elif option == config.aep_multi_options_ids_1[3]:
                                    single_select_options_94.append(config.aep_single_select_option_id_4)
                                elif option == config.aep_multi_options_ids_1[4]:
                                    single_select_options_95.append(config.aep_single_select_option_id_5)
                                elif option == config.aep_multi_options_ids_1[5]:
                                    single_select_options_96.append(config.aep_single_select_option_id_6)
                                elif option == config.aep_multi_options_ids_1[6]:
                                    single_select_options_97.append(config.aep_single_select_option_id_7)
                                elif option == config.aep_multi_options_ids_1[7]:
                                    single_select_options_98.append(config.aep_single_select_option_id_8)
                                elif option == config.aep_multi_options_ids_1[8]:
                                    single_select_options_99.append(config.aep_single_select_option_id_9)

                        elif field_id == config.aep_multi_select_id_2:
                            multi_select_options_13 = data.getOptions()
                            for option in multi_select_options_13:
                                if option   == config.aep_multi_options_ids_2[0]:
                                    single_select_options_100.append(config.aep_single_select_option_id_10)
                                elif option == config.aep_multi_options_ids_2[1]:
                                    single_select_options_101.append(config.aep_single_select_option_id_11)
                                elif option == config.aep_multi_options_ids_2[2]:
                                    single_select_options_102.append(config.aep_single_select_option_id_12)
                                elif option == config.aep_multi_options_ids_2[3]:
                                    single_select_options_103.append(config.aep_single_select_option_id_13)
                                elif option == config.aep_multi_options_ids_2[4]:
                                    single_select_options_104.append(config.aep_single_select_option_id_14)
                                elif option == config.aep_multi_options_ids_2[5]:
                                    single_select_options_105.append(config.aep_single_select_option_id_15)

                        elif field_id == config.aep_multi_select_id_3:
                            multi_select_options_14 = data.getOptions()
                            for option in multi_select_options_14:
                                if option   == config.aep_multi_options_ids_3[0]:
                                    single_select_options_106.append(config.aep_single_select_option_id_16)
                                elif option == config.aep_multi_options_ids_3[1]:
                                    single_select_options_107.append(config.aep_single_select_option_id_17)
                                elif option == config.aep_multi_options_ids_3[2]:
                                    single_select_options_108.append(config.aep_single_select_option_id_18)
                                elif option == config.aep_multi_options_ids_3[3]:
                                    single_select_options_109.append(config.aep_single_select_option_id_19)
                                elif option == config.aep_multi_options_ids_3[4]:
                                    single_select_options_110.append(config.aep_single_select_option_id_20)

                        elif field_id == config.aep_multi_select_id_4:
                            multi_select_options_15 = data.getOptions()
                            for option in multi_select_options_15:
                                if option   == config.aep_multi_options_ids_4[0]:
                                    single_select_options_111.append(config.aep_single_select_option_id_21)
                                elif option == config.aep_multi_options_ids_4[1]:
                                    single_select_options_112.append(config.aep_single_select_option_id_22)
                                elif option == config.aep_multi_options_ids_4[2]:
                                    single_select_options_113.append(config.aep_single_select_option_id_23)
                                elif option == config.aep_multi_options_ids_4[3]:
                                    single_select_options_114.append(config.aep_single_select_option_id_24)
                                elif option == config.aep_multi_options_ids_4[4]:
                                    single_select_options_115.append(config.aep_single_select_option_id_25)

                        elif field_id == config.aep_multi_select_id_5:
                            multi_select_options_16 = data.getOptions()
                            for option in multi_select_options_16:
                                if option   == config.aep_multi_options_ids_5[0]:
                                    single_select_options_116.append(config.aep_single_select_option_id_26)
                                elif option == config.aep_multi_options_ids_5[1]:
                                    single_select_options_117.append(config.aep_single_select_option_id_27)
                                elif option == config.aep_multi_options_ids_5[2]:
                                    single_select_options_118.append(config.aep_single_select_option_id_28)
                                elif option == config.aep_multi_options_ids_5[3]:
                                    single_select_options_119.append(config.aep_single_select_option_id_29)
                                elif option == config.aep_multi_options_ids_5[4]:
                                    single_select_options_120.append(config.aep_single_select_option_id_30)
                                elif option == config.aep_multi_options_ids_5[5]:
                                    single_select_options_121.append(config.aep_single_select_option_id_31)

                        elif field_id == config.aep_multi_select_id_6:
                            multi_select_options_17 = data.getOptions()
                            for option in multi_select_options_17:
                                if option   == config.aep_multi_options_ids_6[0]:
                                    single_select_options_122.append(config.aep_single_select_option_id_32)
                                elif option == config.aep_multi_options_ids_6[1]:
                                    single_select_options_123.append(config.aep_single_select_option_id_33)
                                elif option == config.aep_multi_options_ids_6[2]:
                                    single_select_options_124.append(config.aep_single_select_option_id_34)
                                elif option == config.aep_multi_options_ids_6[3]:
                                    single_select_options_125.append(config.aep_single_select_option_id_35)

                        elif field_id == config.aep_multi_select_id_7:
                            multi_select_options_18 = data.getOptions()
                            for option in multi_select_options_18:
                                if option   == config.aep_multi_options_ids_7[0]:
                                    single_select_options_126.append(config.aep_single_select_option_id_36)
                                elif option == config.aep_multi_options_ids_7[1]:
                                    single_select_options_127.append(config.aep_single_select_option_id_37)
                                elif option == config.aep_multi_options_ids_7[2]:
                                    single_select_options_128.append(config.aep_single_select_option_id_38)
                                elif option == config.aep_multi_options_ids_7[3]:
                                    single_select_options_129.append(config.aep_single_select_option_id_39)
                                elif option == config.aep_multi_options_ids_7[4]:
                                    single_select_options_130.append(config.aep_single_select_option_id_40)
                                elif option == config.aep_multi_options_ids_7[5]:
                                    single_select_options_131.append(config.aep_single_select_option_id_41)
                                elif option == config.aep_multi_options_ids_7[6]:
                                    single_select_options_132.append(config.aep_single_select_option_id_42)
                                elif option == config.aep_multi_options_ids_7[7]:
                                    single_select_options_133.append(config.aep_single_select_option_id_43)

                        elif field_id == config.aep_multi_select_id_8:
                            multi_select_options_19 = data.getOptions()
                            for option in multi_select_options_19:
                                if option   == config.aep_multi_options_ids_8[0]:
                                    single_select_options_134.append(config.aep_single_select_option_id_44)
                                elif option == config.aep_multi_options_ids_8[1]:
                                    single_select_options_135.append(config.aep_single_select_option_id_45)
                                elif option == config.aep_multi_options_ids_8[2]:
                                    single_select_options_136.append(config.aep_single_select_option_id_46)
                                elif option == config.aep_multi_options_ids_8[3]:
                                    single_select_options_137.append(config.aep_single_select_option_id_47)

                        elif field_id == config.aep_multi_select_id_9:
                            multi_select_options_20 = data.getOptions()
                            for option in multi_select_options_20:
                                if option   == config.aep_multi_options_ids_9[0]:
                                    single_select_options_138.append(config.aep_single_select_option_id_48)
                                elif option == config.aep_multi_options_ids_9[1]:
                                    single_select_options_139.append(config.aep_single_select_option_id_49)
                                elif option == config.aep_multi_options_ids_9[2]:
                                    single_select_options_140.append(config.aep_single_select_option_id_50)
                                elif option == config.aep_multi_options_ids_9[3]:
                                    single_select_options_141.append(config.aep_single_select_option_id_51)

                        # GI multi-select
                        elif field_id == config.gi_multi_select_id_1:
                            multi_select_options_21 = data.getOptions()
                            for option in multi_select_options_21:
                                if option   == config.gi_multi_options_ids_1[0]:
                                    single_select_options_142.append(config.gi_single_select_option_id_1)
                                elif option == config.gi_multi_options_ids_1[1]:
                                    single_select_options_143.append(config.gi_single_select_option_id_2)
                                elif option == config.gi_multi_options_ids_1[2]:
                                    single_select_options_144.append(config.gi_single_select_option_id_3)
                                elif option == config.gi_multi_options_ids_1[3]:
                                    single_select_options_145.append(config.gi_single_select_option_id_4)
                                elif option == config.gi_multi_options_ids_1[4]:
                                    single_select_options_146.append(config.gi_single_select_option_id_5)
                                elif option == config.gi_multi_options_ids_1[5]:
                                    single_select_options_147.append(config.gi_single_select_option_id_6)
                                elif option == config.gi_multi_options_ids_1[6]:
                                    single_select_options_148.append(config.gi_single_select_option_id_7)
                                elif option == config.gi_multi_options_ids_1[7]:
                                    single_select_options_149.append(config.gi_single_select_option_id_8)
                                elif option == config.gi_multi_options_ids_1[8]:
                                    single_select_options_150.append(config.gi_single_select_option_id_9)

                        elif field_id == config.gi_multi_select_id_2:
                            multi_select_options_22 = data.getOptions()
                            for option in multi_select_options_22:
                                if option   == config.gi_multi_options_ids_2[0]:
                                    single_select_options_151.append(config.gi_single_select_option_id_10)
                                elif option == config.gi_multi_options_ids_2[1]:
                                    single_select_options_152.append(config.gi_single_select_option_id_11)
                                elif option == config.gi_multi_options_ids_2[2]:
                                    single_select_options_153.append(config.gi_single_select_option_id_12)
                                elif option == config.gi_multi_options_ids_2[3]:
                                    single_select_options_154.append(config.gi_single_select_option_id_13)
                                elif option == config.gi_multi_options_ids_2[4]:
                                    single_select_options_155.append(config.gi_single_select_option_id_14)
                                elif option == config.gi_multi_options_ids_2[5]:
                                    single_select_options_156.append(config.gi_single_select_option_id_15)

                        elif field_id == config.gi_multi_select_id_3:
                            multi_select_options_23 = data.getOptions()
                            for option in multi_select_options_23:
                                if option   == config.gi_multi_options_ids_3[0]:
                                    single_select_options_157.append(config.gi_single_select_option_id_16)
                                elif option == config.gi_multi_options_ids_3[1]:
                                    single_select_options_158.append(config.gi_single_select_option_id_17)
                                elif option == config.gi_multi_options_ids_3[2]:
                                    single_select_options_159.append(config.gi_single_select_option_id_18)
                                elif option == config.gi_multi_options_ids_3[3]:
                                    single_select_options_160.append(config.gi_single_select_option_id_19)
                                elif option == config.gi_multi_options_ids_3[4]:
                                    single_select_options_161.append(config.gi_single_select_option_id_20)

                        elif field_id == config.gi_multi_select_id_4:
                            multi_select_options_24 = data.getOptions()
                            for option in multi_select_options_24:
                                if option   == config.gi_multi_options_ids_4[0]:
                                    single_select_options_162.append(config.gi_single_select_option_id_21)
                                elif option == config.gi_multi_options_ids_4[1]:
                                    single_select_options_163.append(config.gi_single_select_option_id_22)
                                elif option == config.gi_multi_options_ids_4[2]:
                                    single_select_options_164.append(config.gi_single_select_option_id_23)
                                elif option == config.gi_multi_options_ids_4[3]:
                                    single_select_options_165.append(config.gi_single_select_option_id_24)
                                elif option == config.gi_multi_options_ids_4[4]:
                                    single_select_options_166.append(config.gi_single_select_option_id_25)

                        elif field_id == config.gi_multi_select_id_5:
                            multi_select_options_25 = data.getOptions()
                            for option in multi_select_options_25:
                                if option   == config.gi_multi_options_ids_5[0]:
                                    single_select_options_167.append(config.gi_single_select_option_id_26)
                                elif option == config.gi_multi_options_ids_5[1]:
                                    single_select_options_168.append(config.gi_single_select_option_id_27)
                                elif option == config.gi_multi_options_ids_5[2]:
                                    single_select_options_169.append(config.gi_single_select_option_id_28)
                                elif option == config.gi_multi_options_ids_5[3]:
                                    single_select_options_170.append(config.gi_single_select_option_id_29)
                                elif option == config.gi_multi_options_ids_5[4]:
                                    single_select_options_171.append(config.gi_single_select_option_id_30)
                                elif option == config.gi_multi_options_ids_5[5]:
                                    single_select_options_172.append(config.gi_single_select_option_id_31)

                        elif field_id == config.gi_multi_select_id_6:
                            multi_select_options_26 = data.getOptions()
                            for option in multi_select_options_26:
                                if option   == config.gi_multi_options_ids_6[0]:
                                    single_select_options_173.append(config.gi_single_select_option_id_32)
                                elif option == config.gi_multi_options_ids_6[1]:
                                    single_select_options_174.append(config.gi_single_select_option_id_33)
                                elif option == config.gi_multi_options_ids_6[2]:
                                    single_select_options_175.append(config.gi_single_select_option_id_34)
                                elif option == config.gi_multi_options_ids_6[3]:
                                    single_select_options_176.append(config.gi_single_select_option_id_35)
                                elif option == config.gi_multi_options_ids_6[4]:
                                    single_select_options_177.append(config.gi_single_select_option_id_36)
                                elif option == config.gi_multi_options_ids_6[5]:
                                    single_select_options_178.append(config.gi_single_select_option_id_37)
                                elif option == config.gi_multi_options_ids_6[6]:
                                    single_select_options_179.append(config.gi_single_select_option_id_38)
                                elif option == config.gi_multi_options_ids_6[7]:
                                    single_select_options_180.append(config.gi_single_select_option_id_39)
                                elif option == config.gi_multi_options_ids_6[8]:
                                    single_select_options_181.append(config.gi_single_select_option_id_40)
                                elif option == config.gi_multi_options_ids_6[9]:
                                    single_select_options_182.append(config.gi_single_select_option_id_41)
                                elif option == config.gi_multi_options_ids_6[10]:
                                    single_select_options_183.append(config.gi_single_select_option_id_42)
                                elif option == config.gi_multi_options_ids_6[11]:
                                    single_select_options_184.append(config.gi_single_select_option_id_43)
                                elif option == config.gi_multi_options_ids_6[12]:
                                    single_select_options_185.append(config.gi_single_select_option_id_44)
                                elif option == config.gi_multi_options_ids_6[13]:
                                    single_select_options_186.append(config.gi_single_select_option_id_45)

                        # App survey multi-select
                        elif field_id == config.app_survey_multi_select_id_1:
                            multi_select_options_27 = data.getOptions()
                            for option in multi_select_options_27:
                                if option   == config.app_survey_multi_options_ids_1[0]:
                                    single_select_options_187.append(config.app_single_select_option_id_1)
                                elif option == config.app_survey_multi_options_ids_1[1]:
                                    single_select_options_188.append(config.app_single_select_option_id_2)
                                elif option == config.app_survey_multi_options_ids_1[2]:
                                    single_select_options_189.append(config.app_single_select_option_id_3)
                                elif option == config.app_survey_multi_options_ids_1[3]:
                                    single_select_options_190.append(config.app_single_select_option_id_4)
                                elif option == config.app_survey_multi_options_ids_1[4]:
                                    single_select_options_191.append(config.app_single_select_option_id_5)
                                elif option == config.app_survey_multi_options_ids_1[5]:
                                    single_select_options_192.append(config.app_single_select_option_id_6)
                                elif option == config.app_survey_multi_options_ids_1[6]:
                                    single_select_options_193.append(config.app_single_select_option_id_7)

                        elif field_id == config.app_survey_multi_select_id_2:
                            multi_select_options_28 = data.getOptions()
                            for option in multi_select_options_28:
                                if option   == config.app_survey_multi_options_ids_2[0]:
                                    single_select_options_194.append(config.app_single_select_option_id_8)
                                elif option == config.app_survey_multi_options_ids_2[1]:
                                    single_select_options_195.append(config.app_single_select_option_id_9)
                                elif option == config.app_survey_multi_options_ids_2[2]:
                                    single_select_options_196.append(config.app_single_select_option_id_10)
                                elif option == config.app_survey_multi_options_ids_2[3]:
                                    single_select_options_197.append(config.app_single_select_option_id_11)
                                elif option == config.app_survey_multi_options_ids_2[4]:
                                    single_select_options_198.append(config.app_single_select_option_id_12)

                        elif field_id == config.app_survey_multi_select_id_3:
                            multi_select_options_29 = data.getOptions()
                            for option in multi_select_options_29:
                                if option   == config.app_survey_multi_options_ids_3[0]:
                                    single_select_options_199.append(config.app_single_select_option_id_13)
                                elif option == config.app_survey_multi_options_ids_3[1]:
                                    single_select_options_200.append(config.app_single_select_option_id_14)
                                elif option == config.app_survey_multi_options_ids_3[2]:
                                    single_select_options_201.append(config.app_single_select_option_id_15)
                                elif option == config.app_survey_multi_options_ids_3[3]:
                                    single_select_options_202.append(config.app_single_select_option_id_16)
                                elif option == config.app_survey_multi_options_ids_3[4]:
                                    single_select_options_203.append(config.app_single_select_option_id_17)
                                elif option == config.app_survey_multi_options_ids_3[5]:
                                    single_select_options_204.append(config.app_single_select_option_id_18)
                                elif option == config.app_survey_multi_options_ids_3[6]:
                                    single_select_options_205.append(config.app_single_select_option_id_19)
                                elif option == config.app_survey_multi_options_ids_3[7]:
                                    single_select_options_206.append(config.app_single_select_option_id_20)
                                elif option == config.app_survey_multi_options_ids_3[8]:
                                    single_select_options_207.append(config.app_single_select_option_id_21)
                                elif option == config.app_survey_multi_options_ids_3[9]:
                                    single_select_options_208.append(config.app_single_select_option_id_22)

                        elif field_id == config.app_survey_multi_select_id_4:
                            multi_select_options_30 = data.getOptions()
                            for option in multi_select_options_30:
                                if option   == config.app_survey_multi_options_ids_4[0]:
                                    single_select_options_209.append(config.app_single_select_option_id_23)
                                elif option == config.app_survey_multi_options_ids_4[1]:
                                    single_select_options_210.append(config.app_single_select_option_id_24)
                                elif option == config.app_survey_multi_options_ids_4[2]:
                                    single_select_options_211.append(config.app_single_select_option_id_25)
                                elif option == config.app_survey_multi_options_ids_4[3]:
                                    single_select_options_212.append(config.app_single_select_option_id_26)
                                elif option == config.app_survey_multi_options_ids_4[4]:
                                    single_select_options_213.append(config.app_single_select_option_id_27)
                                elif option == config.app_survey_multi_options_ids_4[5]:
                                    single_select_options_214.append(config.app_single_select_option_id_28)

                        elif field_id == config.app_survey_multi_select_id_5:
                            multi_select_options_31 = data.getOptions()
                            for option in multi_select_options_31:
                                if option   == config.app_survey_multi_options_ids_3[0]:
                                    single_select_options_215.append(config.app_single_select_option_id_29)
                                elif option == config.app_survey_multi_options_ids_3[1]:
                                    single_select_options_216.append(config.app_single_select_option_id_30)
                                elif option == config.app_survey_multi_options_ids_3[2]:
                                    single_select_options_217.append(config.app_single_select_option_id_31)
                                elif option == config.app_survey_multi_options_ids_3[3]:
                                    single_select_options_218.append(config.app_single_select_option_id_32)
                                elif option == config.app_survey_multi_options_ids_3[4]:
                                    single_select_options_219.append(config.app_single_select_option_id_33)
                                elif option == config.app_survey_multi_options_ids_3[5]:
                                    single_select_options_220.append(config.app_single_select_option_id_34)
                                elif option == config.app_survey_multi_options_ids_3[6]:
                                    single_select_options_221.append(config.app_single_select_option_id_35)
                                elif option == config.app_survey_multi_options_ids_3[7]:
                                    single_select_options_222.append(config.app_single_select_option_id_36)
                                elif option == config.app_survey_multi_options_ids_3[8]:
                                    single_select_options_223.append(config.app_single_select_option_id_37)

                        elif field_id == config.app_survey_multi_select_id_6:
                            multi_select_options_32 = data.getOptions()
                            for option in multi_select_options_32:
                                if option   == config.app_survey_multi_options_ids_6[0]:
                                    single_select_options_224.append(config.app_single_select_option_id_38)
                                elif option == config.app_survey_multi_options_ids_6[1]:
                                    single_select_options_225.append(config.app_single_select_option_id_39)
                                elif option == config.app_survey_multi_options_ids_6[2]:
                                    single_select_options_226.append(config.app_single_select_option_id_40)
                                elif option == config.app_survey_multi_options_ids_6[3]:
                                    single_select_options_227.append(config.app_single_select_option_id_41)
                                elif option == config.app_survey_multi_options_ids_6[4]:
                                    single_select_options_228.append(config.app_single_select_option_id_42)
                                elif option == config.app_survey_multi_options_ids_6[5]:
                                    single_select_options_229.append(config.app_single_select_option_id_43)
                                elif option == config.app_survey_multi_options_ids_6[6]:
                                    single_select_options_230.append(config.app_single_select_option_id_44)
                                elif option == config.app_survey_multi_options_ids_6[7]:
                                    single_select_options_231.append(config.app_single_select_option_id_45)
                                elif option == config.app_survey_multi_options_ids_6[8]:
                                    single_select_options_232.append(config.app_single_select_option_id_46)
                                elif option == config.app_survey_multi_options_ids_6[9]:
                                    single_select_options_233.append(config.app_single_select_option_id_47)
                                elif option == config.app_survey_multi_options_ids_6[10]:
                                    single_select_options_234.append(config.app_single_select_option_id_48)
                                elif option == config.app_survey_multi_options_ids_6[11]:
                                    single_select_options_235.append(config.app_single_select_option_id_49)
                                elif option == config.app_survey_multi_options_ids_6[12]:
                                    single_select_options_236.append(config.app_single_select_option_id_50)
                                elif option == config.app_survey_multi_options_ids_6[13]:
                                    single_select_options_237.append(config.app_single_select_option_id_51)

                        elif field_id == config.app_survey_multi_select_id_7:
                            multi_select_options_33 = data.getOptions()
                            for option in multi_select_options_33:
                                if option   == config.app_survey_multi_options_ids_7[0]:
                                    single_select_options_238.append(config.app_single_select_option_id_52)
                                elif option == config.app_survey_multi_options_ids_7[1]:
                                    single_select_options_239.append(config.app_single_select_option_id_53)
                                elif option == config.app_survey_multi_options_ids_7[2]:
                                    single_select_options_240.append(config.app_single_select_option_id_54)
                                elif option == config.app_survey_multi_options_ids_7[3]:
                                    single_select_options_241.append(config.app_single_select_option_id_55)
                                elif option == config.app_survey_multi_options_ids_7[4]:
                                    single_select_options_242.append(config.app_single_select_option_id_56)
                                elif option == config.app_survey_multi_options_ids_7[5]:
                                    single_select_options_243.append(config.app_single_select_option_id_57)
                                elif option == config.app_survey_multi_options_ids_7[6]:
                                    single_select_options_244.append(config.app_single_select_option_id_58)
                                elif option == config.app_survey_multi_options_ids_7[7]:
                                    single_select_options_245.append(config.app_single_select_option_id_59)
                                elif option == config.app_survey_multi_options_ids_7[8]:
                                    single_select_options_246.append(config.app_single_select_option_id_60)
                                elif option == config.app_survey_multi_options_ids_7[9]:
                                    single_select_options_247.append(config.app_single_select_option_id_61)
                                elif option == config.app_survey_multi_options_ids_7[10]:
                                    single_select_options_248.append(config.app_single_select_option_id_62)
                                elif option == config.app_survey_multi_options_ids_7[11]:
                                    single_select_options_249.append(config.app_single_select_option_id_63)
                                elif option == config.app_survey_multi_options_ids_7[12]:
                                    single_select_options_250.append(config.app_single_select_option_id_64)

                    if primary_last_name is not None and primary_dob is not None and primary_zip is not None:
                        # create the primary UID
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
                            logger.info(f"project 1 - INTERNAL FORM duplicate unique id project 1 for submission {submission_id}")
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
                            self.submittable.submitInternalFormResponse(submission_id,
                                                                        primary_unique_id,
                                                                        single_select_options_1,
                                                                        single_select_options_2,
                                                                        single_select_options_3,
                                                                        single_select_options_4,
                                                                        single_select_options_5,
                                                                        single_select_options_6,
                                                                        single_select_options_7,
                                                                        single_select_options_8,
                                                                        single_select_options_9,
                                                                        single_select_options_10,
                                                                        single_select_options_11,
                                                                        single_select_options_12,
                                                                        single_select_options_13,
                                                                        single_select_options_14,
                                                                        single_select_options_15,
                                                                        single_select_options_16,
                                                                        single_select_options_17,
                                                                        single_select_options_18,
                                                                        single_select_options_19,
                                                                        single_select_options_20,
                                                                        single_select_options_21,
                                                                        single_select_options_22,
                                                                        single_select_options_23,
                                                                        single_select_options_24,
                                                                        single_select_options_25,
                                                                        single_select_options_26,
                                                                        single_select_options_27,
                                                                        single_select_options_28,
                                                                        single_select_options_29,
                                                                        single_select_options_30,
                                                                        single_select_options_31,
                                                                        single_select_options_32,
                                                                        single_select_options_33,
                                                                        single_select_options_34,
                                                                        single_select_options_35,
                                                                        single_select_options_36,
                                                                        single_select_options_37,
                                                                        single_select_options_38,
                                                                        single_select_options_39,
                                                                        single_select_options_40,
                                                                        single_select_options_41,
                                                                        single_select_options_42,
                                                                        single_select_options_43,
                                                                        single_select_options_44,
                                                                        single_select_options_45,
                                                                        single_select_options_46,
                                                                        single_select_options_47,
                                                                        single_select_options_48,
                                                                        single_select_options_49,
                                                                        single_select_options_50,
                                                                        single_select_options_51,
                                                                        single_select_options_52,
                                                                        single_select_options_53,
                                                                        single_select_options_54,
                                                                        single_select_options_55,
                                                                        single_select_options_56,
                                                                        single_select_options_57,
                                                                        single_select_options_58,
                                                                        single_select_options_59,
                                                                        single_select_options_60,
                                                                        single_select_options_61,
                                                                        single_select_options_62,
                                                                        single_select_options_63,
                                                                        single_select_options_64,
                                                                        single_select_options_65,
                                                                        single_select_options_66,
                                                                        single_select_options_67,
                                                                        single_select_options_68,
                                                                        single_select_options_69,
                                                                        single_select_options_70,
                                                                        single_select_options_71,
                                                                        single_select_options_72,
                                                                        single_select_options_73,
                                                                        single_select_options_74,
                                                                        single_select_options_75,
                                                                        single_select_options_76,
                                                                        single_select_options_77,
                                                                        single_select_options_78,
                                                                        single_select_options_79,
                                                                        single_select_options_80,
                                                                        single_select_options_81,
                                                                        single_select_options_82,
                                                                        single_select_options_83,
                                                                        single_select_options_84,
                                                                        single_select_options_85,
                                                                        single_select_options_86,
                                                                        single_select_options_87,
                                                                        single_select_options_88,
                                                                        single_select_options_89,
                                                                        single_select_options_90,
                                                                        single_select_options_91,
                                                                        single_select_options_92,
                                                                        single_select_options_93,
                                                                        single_select_options_94,
                                                                        single_select_options_95,
                                                                        single_select_options_96,
                                                                        single_select_options_97,
                                                                        single_select_options_98,
                                                                        single_select_options_99,
                                                                        single_select_options_100,
                                                                        single_select_options_101,
                                                                        single_select_options_102,
                                                                        single_select_options_103,
                                                                        single_select_options_104,
                                                                        single_select_options_105,
                                                                        single_select_options_106,
                                                                        single_select_options_107,
                                                                        single_select_options_108,
                                                                        single_select_options_109,
                                                                        single_select_options_110,
                                                                        single_select_options_111,
                                                                        single_select_options_112,
                                                                        single_select_options_113,
                                                                        single_select_options_114,
                                                                        single_select_options_115,
                                                                        single_select_options_116,
                                                                        single_select_options_117,
                                                                        single_select_options_118,
                                                                        single_select_options_119,
                                                                        single_select_options_120,
                                                                        single_select_options_121,
                                                                        single_select_options_122,
                                                                        single_select_options_123,
                                                                        single_select_options_124,
                                                                        single_select_options_125,
                                                                        single_select_options_126,
                                                                        single_select_options_127,
                                                                        single_select_options_128,
                                                                        single_select_options_129,
                                                                        single_select_options_130,
                                                                        single_select_options_131,
                                                                        single_select_options_132,
                                                                        single_select_options_133,
                                                                        single_select_options_134,
                                                                        single_select_options_135,
                                                                        single_select_options_136,
                                                                        single_select_options_137,
                                                                        single_select_options_138,
                                                                        single_select_options_139,
                                                                        single_select_options_140,
                                                                        single_select_options_141,
                                                                        single_select_options_142,
                                                                        single_select_options_143,
                                                                        single_select_options_144,
                                                                        single_select_options_145,
                                                                        single_select_options_146,
                                                                        single_select_options_147,
                                                                        single_select_options_148,
                                                                        single_select_options_149,
                                                                        single_select_options_150,
                                                                        single_select_options_151,
                                                                        single_select_options_152,
                                                                        single_select_options_153,
                                                                        single_select_options_154,
                                                                        single_select_options_155,
                                                                        single_select_options_156,
                                                                        single_select_options_157,
                                                                        single_select_options_158,
                                                                        single_select_options_159,
                                                                        single_select_options_160,
                                                                        single_select_options_161,
                                                                        single_select_options_162,
                                                                        single_select_options_163,
                                                                        single_select_options_164,
                                                                        single_select_options_165,
                                                                        single_select_options_166,
                                                                        single_select_options_167,
                                                                        single_select_options_168,
                                                                        single_select_options_169,
                                                                        single_select_options_170,
                                                                        single_select_options_171,
                                                                        single_select_options_172,
                                                                        single_select_options_173,
                                                                        single_select_options_174,
                                                                        single_select_options_175,
                                                                        single_select_options_176,
                                                                        single_select_options_177,
                                                                        single_select_options_178,
                                                                        single_select_options_179,
                                                                        single_select_options_180,
                                                                        single_select_options_181,
                                                                        single_select_options_182,
                                                                        single_select_options_183,
                                                                        single_select_options_184,
                                                                        single_select_options_185,
                                                                        single_select_options_186,
                                                                        single_select_options_187,
                                                                        single_select_options_188,
                                                                        single_select_options_189,
                                                                        single_select_options_190,
                                                                        single_select_options_191,
                                                                        single_select_options_192,
                                                                        single_select_options_193,
                                                                        single_select_options_194,
                                                                        single_select_options_195,
                                                                        single_select_options_196,
                                                                        single_select_options_197,
                                                                        single_select_options_198,
                                                                        single_select_options_199,
                                                                        single_select_options_200,
                                                                        single_select_options_201,
                                                                        single_select_options_202,
                                                                        single_select_options_203,
                                                                        single_select_options_204,
                                                                        single_select_options_205,
                                                                        single_select_options_206,
                                                                        single_select_options_207,
                                                                        single_select_options_208,
                                                                        single_select_options_209,
                                                                        single_select_options_210,
                                                                        single_select_options_211,
                                                                        single_select_options_212,
                                                                        single_select_options_213,
                                                                        single_select_options_214,
                                                                        single_select_options_215,
                                                                        single_select_options_216,
                                                                        single_select_options_217,
                                                                        single_select_options_218,
                                                                        single_select_options_219,
                                                                        single_select_options_220,
                                                                        single_select_options_221,
                                                                        single_select_options_222,
                                                                        single_select_options_223,
                                                                        single_select_options_224,
                                                                        single_select_options_225,
                                                                        single_select_options_226,
                                                                        single_select_options_227,
                                                                        single_select_options_228,
                                                                        single_select_options_229,
                                                                        single_select_options_230,
                                                                        single_select_options_231,
                                                                        single_select_options_232,
                                                                        single_select_options_233,
                                                                        single_select_options_234,
                                                                        single_select_options_235,
                                                                        single_select_options_236,
                                                                        single_select_options_237,
                                                                        single_select_options_238,
                                                                        single_select_options_239,
                                                                        single_select_options_240,
                                                                        single_select_options_241,
                                                                        single_select_options_242,
                                                                        single_select_options_243,
                                                                        single_select_options_244,
                                                                        single_select_options_245,
                                                                        single_select_options_246,
                                                                        single_select_options_247,
                                                                        single_select_options_248,
                                                                        single_select_options_249,
                                                                        single_select_options_250,
                                                                        collab_unique_id_1,
                                                                        collab_unique_id_2,
                                                                        collab_unique_id_3,
                                                                        collab_unique_id_4,
                                                                        collab_unique_id_5,
                                                                        collab_unique_id_6,
                                                                        collab_unique_id_7,
                                                                        collab_unique_id_8,
                                                                        collab_unique_id_9)

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
                            logger.info(f"project 1 - dup found  sub id: {submission_id}")
                            self.label_dups(submission_id, uid_check_sub_id_1)
                        elif uid_check_sub_id_2 is not None:
                            logger.info(f"project 1 - collab_unique_id_2 dup found sub id: {submission_id}")
                            self.label_dups(submission_id, uid_check_sub_id_2)
                        elif uid_check_sub_id_3 is not None:
                            logger.info(f"project 1 - collab_unique_id_3 dup found sub id: {submission_id}")
                            self.label_dups(submission_id, uid_check_sub_id_3)
                        elif uid_check_sub_id_4 is not None:
                            logger.info(f"project 1 - collab_unique_id_4 dup found sub id: {submission_id}")
                            self.label_dups(submission_id, uid_check_sub_id_4)
                        elif uid_check_sub_id_5 is not None:
                            logger.info(f"project 1 - collab_unique_id_5 dup found sub id: {submission_id}")
                            self.label_dups(submission_id, uid_check_sub_id_5)
                        elif uid_check_sub_id_6 is not None:
                            logger.info(f"project 1 - collab_unique_id_6 dup found sub id: {submission_id}")
                            self.label_dups(submission_id, uid_check_sub_id_6)
                        elif uid_check_sub_id_7 is not None:
                            logger.info(f"project 1 - collab_unique_id_7 dup found sub id: {submission_id}")
                            self.label_dups(submission_id, uid_check_sub_id_7)
                        elif uid_check_sub_id_8 is not None:
                            logger.info(f"project 1 - collab_unique_id_7 dup found sub id: {submission_id}")
                            self.label_dups(submission_id, uid_check_sub_id_8)
                        elif uid_check_sub_id_9 is not None:
                            logger.info(f"project 1 - collab_unique_id_8 dup found sub id: {submission_id}")
                            self.label_dups(submission_id, uid_check_sub_id_9)
                        elif uid_check_sub_id_10 is not None:
                            logger.info(f"project 1 - collab_unique_id_9 dup found sub id: {submission_id}")
                            self.label_dups(submission_id, uid_check_sub_id_10)

                        logger.info(f"project 1 - save to dict {primary_unique_id} sub id {submission_id}")
                        config.uid_data_struct.append({'submission_id':      submission_id,      'primary_unique_id':  primary_unique_id,
                                                       'collab_unique_id_1': collab_unique_id_1, 'collab_unique_id_2': collab_unique_id_2,
                                                       'collab_unique_id_3': collab_unique_id_3, 'collab_unique_id_4': collab_unique_id_4,
                                                       'collab_unique_id_5': collab_unique_id_5, 'collab_unique_id_6': collab_unique_id_6,
                                                       'collab_unique_id_7': collab_unique_id_7, 'collab_unique_id_8': collab_unique_id_8,
                                                       'collab_unique_id_9': collab_unique_id_9})


                        # go to next response
                        break
                    else:
                        logger.info(f"project 1 - primary UID field Null: {primary_unique_id} for submission: {submission_id}")
                        # skip submission missing primary UID field(s)
                        continue

            # check project 2
            elif project_id == self.project_id_2:
                logger.info(f"project 2 - Submission {submission_id}")
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
                        #
                        # ineligible multi-selects
                        elif field_id == config.ineligible_survey_multi_select_id_1:
                            multi_select_options_1 = data.getOptions()
                            for option in multi_select_options_1:
                                if option == config.ineligible_survey_multi_options_ids_1[0]:
                                    single_select_options_1.append(config.ineligible_single_select_option_id_1)
                                elif option == config.ineligible_survey_multi_options_ids_1[1]:
                                    single_select_options_2.append(config.ineligible_single_select_option_id_2)
                                elif option == config.ineligible_survey_multi_options_ids_1[2]:
                                    single_select_options_3.append(config.ineligible_single_select_option_id_3)
                                elif option == config.ineligible_survey_multi_options_ids_1[3]:
                                    single_select_options_4.append(config.ineligible_single_select_option_id_4)
                                elif option == config.ineligible_survey_multi_options_ids_1[4]:
                                    single_select_options_5.append(config.ineligible_single_select_option_id_5)
                                elif option == config.ineligible_survey_multi_options_ids_1[5]:
                                    single_select_options_6.append(config.ineligible_single_select_option_id_6)

                        elif field_id == config.ineligible_survey_multi_select_id_2:
                            multi_select_options_2 = data.getOptions()
                            for option in multi_select_options_2:
                                if option == config.ineligible_survey_multi_options_ids_2[0]:
                                    single_select_options_7.append(config.ineligible_single_select_option_id_7)
                                elif option == config.ineligible_survey_multi_options_ids_2[1]:
                                    single_select_options_8.append(config.ineligible_single_select_option_id_8)
                                elif option == config.ineligible_survey_multi_options_ids_2[2]:
                                    single_select_options_9.append(config.ineligible_single_select_option_id_9)
                                elif option == config.ineligible_survey_multi_options_ids_2[3]:
                                    single_select_options_10.append(config.ineligible_single_select_option_id_10)
                                elif option == config.ineligible_survey_multi_options_ids_2[4]:
                                    single_select_options_11.append(config.ineligible_single_select_option_id_11)
                                elif option == config.ineligible_survey_multi_options_ids_2[5]:
                                    single_select_options_12.append(config.ineligible_single_select_option_id_12)
                                elif option == config.ineligible_survey_multi_options_ids_2[6]:
                                    single_select_options_13.append(config.ineligible_single_select_option_id_13)

                        elif field_id == config.ineligible_survey_multi_select_id_3:
                            multi_select_options_3 = data.getOptions()
                            for option in multi_select_options_3:
                                if option == config.ineligible_survey_multi_options_ids_3[0]:
                                    single_select_options_14.append(config.ineligible_single_select_option_id_14)
                                elif option == config.ineligible_survey_multi_options_ids_3[1]:
                                    single_select_options_15.append(config.ineligible_single_select_option_id_15)
                                elif option == config.ineligible_survey_multi_options_ids_3[2]:
                                    single_select_options_16.append(config.ineligible_single_select_option_id_16)
                                elif option == config.ineligible_survey_multi_options_ids_3[3]:
                                    single_select_options_17.append(config.ineligible_single_select_option_id_17)
                                elif option == config.ineligible_survey_multi_options_ids_3[4]:
                                    single_select_options_18.append(config.ineligible_single_select_option_id_18)

                        elif field_id == config.ineligible_survey_multi_select_id_4:
                            multi_select_options_4 = data.getOptions()
                            for option in multi_select_options_4:
                                if option == config.ineligible_survey_multi_options_ids_4[0]:
                                    single_select_options_19.append(config.ineligible_single_select_option_id_19)
                                elif option == config.ineligible_survey_multi_options_ids_4[1]:
                                    single_select_options_20.append(config.ineligible_single_select_option_id_20)
                                elif option == config.ineligible_survey_multi_options_ids_4[2]:
                                    single_select_options_21.append(config.ineligible_single_select_option_id_21)
                                elif option == config.ineligible_survey_multi_options_ids_4[3]:
                                    single_select_options_22.append(config.ineligible_single_select_option_id_22)
                                elif option == config.ineligible_survey_multi_options_ids_4[4]:
                                    single_select_options_23.append(config.ineligible_single_select_option_id_23)
                                elif option == config.ineligible_survey_multi_options_ids_4[5]:
                                    single_select_options_24.append(config.ineligible_single_select_option_id_24)
                                elif option == config.ineligible_survey_multi_options_ids_4[6]:
                                    single_select_options_25.append(config.ineligible_single_select_option_id_25)
                                elif option == config.ineligible_survey_multi_options_ids_4[7]:
                                    single_select_options_26.append(config.ineligible_single_select_option_id_26)
                                elif option == config.ineligible_survey_multi_options_ids_4[8]:
                                    single_select_options_27.append(config.ineligible_single_select_option_id_27)
                                elif option == config.ineligible_survey_multi_options_ids_4[9]:
                                    single_select_options_28.append(config.ineligible_single_select_option_id_28)

                        elif field_id == config.ineligible_survey_multi_select_id_5:
                            multi_select_options_5 = data.getOptions()
                            for option in multi_select_options_5:
                                if option == config.ineligible_survey_multi_options_ids_5[0]:
                                    single_select_options_29.append(config.ineligible_single_select_option_id_29)
                                elif option == config.ineligible_survey_multi_options_ids_5[1]:
                                    single_select_options_30.append(config.ineligible_single_select_option_id_30)
                                elif option == config.ineligible_survey_multi_options_ids_5[2]:
                                    single_select_options_31.append(config.ineligible_single_select_option_id_31)
                                elif option == config.ineligible_survey_multi_options_ids_5[3]:
                                    single_select_options_32.append(config.ineligible_single_select_option_id_32)
                                elif option == config.ineligible_survey_multi_options_ids_5[4]:
                                    single_select_options_33.append(config.ineligible_single_select_option_id_33)
                                elif option == config.ineligible_survey_multi_options_ids_5[5]:
                                    single_select_options_34.append(config.ineligible_single_select_option_id_34)

                        elif field_id == config.ineligible_survey_multi_select_id_6:
                            multi_select_options_6 = data.getOptions()
                            for option in multi_select_options_6:
                                if option == config.ineligible_survey_multi_options_ids_6[0]:
                                    single_select_options_35.append(config.ineligible_single_select_option_id_35)
                                elif option == config.ineligible_survey_multi_options_ids_6[1]:
                                    single_select_options_36.append(config.ineligible_single_select_option_id_36)
                                elif option == config.ineligible_survey_multi_options_ids_6[2]:
                                    single_select_options_37.append(config.ineligible_single_select_option_id_37)
                                elif option == config.ineligible_survey_multi_options_ids_6[3]:
                                    single_select_options_38.append(config.ineligible_single_select_option_id_38)
                                elif option == config.ineligible_survey_multi_options_ids_6[4]:
                                    single_select_options_39.append(config.ineligible_single_select_option_id_39)
                                elif option == config.ineligible_survey_multi_options_ids_6[5]:
                                    single_select_options_40.append(config.ineligible_single_select_option_id_40)
                                elif option == config.ineligible_survey_multi_options_ids_6[6]:
                                    single_select_options_41.append(config.ineligible_single_select_option_id_41)
                                elif option == config.ineligible_survey_multi_options_ids_6[7]:
                                    single_select_options_42.append(config.ineligible_single_select_option_id_42)
                                elif option == config.ineligible_survey_multi_options_ids_6[8]:
                                    single_select_options_43.append(config.ineligible_single_select_option_id_43)

                        elif field_id == config.ineligible_survey_multi_select_id_7:
                            multi_select_options_7 = data.getOptions()
                            for option in multi_select_options_7:
                                if option == config.ineligible_survey_multi_options_ids_7[0]:
                                    single_select_options_44.append(config.ineligible_single_select_option_id_44)
                                elif option == config.ineligible_survey_multi_options_ids_7[1]:
                                    single_select_options_45.append(config.ineligible_single_select_option_id_45)
                                elif option == config.ineligible_survey_multi_options_ids_7[2]:
                                    single_select_options_46.append(config.ineligible_single_select_option_id_46)
                                elif option == config.ineligible_survey_multi_options_ids_7[3]:
                                    single_select_options_47.append(config.ineligible_single_select_option_id_47)
                                elif option == config.ineligible_survey_multi_options_ids_7[4]:
                                    single_select_options_48.append(config.ineligible_single_select_option_id_48)
                                elif option == config.ineligible_survey_multi_options_ids_7[5]:
                                    single_select_options_49.append(config.ineligible_single_select_option_id_49)
                                elif option == config.ineligible_survey_multi_options_ids_7[6]:
                                    single_select_options_50.append(config.ineligible_single_select_option_id_50)
                                elif option == config.ineligible_survey_multi_options_ids_7[7]:
                                    single_select_options_51.append(config.ineligible_single_select_option_id_51)
                                elif option == config.ineligible_survey_multi_options_ids_7[8]:
                                    single_select_options_52.append(config.ineligible_single_select_option_id_52)
                                elif option == config.ineligible_survey_multi_options_ids_7[9]:
                                    single_select_options_53.append(config.ineligible_single_select_option_id_53)
                                elif option == config.ineligible_survey_multi_options_ids_7[10]:
                                    single_select_options_54.append(config.ineligible_single_select_option_id_54)
                                elif option == config.ineligible_survey_multi_options_ids_7[11]:
                                    single_select_options_55.append(config.ineligible_single_select_option_id_55)
                                elif option == config.ineligible_survey_multi_options_ids_7[12]:
                                    single_select_options_56.append(config.ineligible_single_select_option_id_56)
                                elif option == config.ineligible_survey_multi_options_ids_7[13]:
                                    single_select_options_57.append(config.ineligible_single_select_option_id_57)

                        elif field_id == config.ineligible_survey_multi_select_id_8:
                            multi_select_options_8 = data.getOptions()
                            for option in multi_select_options_8:
                                if option == config.ineligible_survey_multi_options_ids_8[0]:
                                    single_select_options_58.append(config.ineligible_single_select_option_id_58)
                                elif option == config.ineligible_survey_multi_options_ids_8[1]:
                                    single_select_options_59.append(config.ineligible_single_select_option_id_59)
                                elif option == config.ineligible_survey_multi_options_ids_8[2]:
                                    single_select_options_60.append(config.ineligible_single_select_option_id_60)
                                elif option == config.ineligible_survey_multi_options_ids_8[3]:
                                    single_select_options_61.append(config.ineligible_single_select_option_id_61)
                                elif option == config.ineligible_survey_multi_options_ids_8[4]:
                                    single_select_options_62.append(config.ineligible_single_select_option_id_62)
                                elif option == config.ineligible_survey_multi_options_ids_8[5]:
                                    single_select_options_63.append(config.ineligible_single_select_option_id_63)
                                elif option == config.ineligible_survey_multi_options_ids_8[6]:
                                    single_select_options_64.append(config.ineligible_single_select_option_id_64)
                                elif option == config.ineligible_survey_multi_options_ids_8[7]:
                                    single_select_options_65.append(config.ineligible_single_select_option_id_65)
                                elif option == config.ineligible_survey_multi_options_ids_8[8]:
                                    single_select_options_66.append(config.ineligible_single_select_option_id_66)
                                elif option == config.ineligible_survey_multi_options_ids_8[9]:
                                    single_select_options_67.append(config.ineligible_single_select_option_id_67)
                                elif option == config.ineligible_survey_multi_options_ids_8[10]:
                                    single_select_options_68.append(config.ineligible_single_select_option_id_68)
                                elif option == config.ineligible_survey_multi_options_ids_8[11]:
                                    single_select_options_69.append(config.ineligible_single_select_option_id_69)
                                elif option == config.ineligible_survey_multi_options_ids_8[12]:
                                    single_select_options_70.append(config.ineligible_single_select_option_id_70)

                        elif field_id == config.ineligible_survey_multi_select_id_9:
                            multi_select_options_9 = data.getOptions()
                            for option in multi_select_options_9:
                                if option == config.ineligible_survey_multi_options_ids_9[0]:
                                    single_select_options_71.append(config.ineligible_single_select_option_id_71)
                                elif option == config.ineligible_survey_multi_options_ids_9[1]:
                                    single_select_options_72.append(config.ineligible_single_select_option_id_72)
                                elif option == config.ineligible_survey_multi_options_ids_9[2]:
                                    single_select_options_73.append(config.ineligible_single_select_option_id_73)
                                elif option == config.ineligible_survey_multi_options_ids_9[3]:
                                    single_select_options_74.append(config.ineligible_single_select_option_id_74)
                                elif option == config.ineligible_survey_multi_options_ids_9[4]:
                                    single_select_options_75.append(config.ineligible_single_select_option_id_75)
                                elif option == config.ineligible_survey_multi_options_ids_9[5]:
                                    single_select_options_76.append(config.ineligible_single_select_option_id_76)
                                elif option == config.ineligible_survey_multi_options_ids_9[6]:
                                    single_select_options_77.append(config.ineligible_single_select_option_id_77)
                                elif option == config.ineligible_survey_multi_options_ids_9[7]:
                                    single_select_options_78.append(config.ineligible_single_select_option_id_78)
                                elif option == config.ineligible_survey_multi_options_ids_9[8]:
                                    single_select_options_79.append(config.ineligible_single_select_option_id_79)

                        elif field_id == config.ineligible_survey_multi_select_id_10:
                            multi_select_options_10 = data.getOptions()
                            for option in multi_select_options_10:
                                if option == config.ineligible_survey_multi_options_ids_10[0]:
                                    single_select_options_80.append(config.ineligible_single_select_option_id_80)
                                elif option == config.ineligible_survey_multi_options_ids_10[1]:
                                    single_select_options_81.append(config.ineligible_single_select_option_id_81)
                                elif option == config.ineligible_survey_multi_options_ids_10[2]:
                                    single_select_options_82.append(config.ineligible_single_select_option_id_82)
                                elif option == config.ineligible_survey_multi_options_ids_10[3]:
                                    single_select_options_83.append(config.ineligible_single_select_option_id_83)
                                elif option == config.ineligible_survey_multi_options_ids_10[4]:
                                    single_select_options_84.append(config.ineligible_single_select_option_id_84)
                                elif option == config.ineligible_survey_multi_options_ids_10[5]:
                                    single_select_options_85.append(config.ineligible_single_select_option_id_85)

                        elif field_id == config.ineligible_survey_multi_select_id_11:
                            multi_select_options_11 = data.getOptions()
                            for option in multi_select_options_11:
                                if option == config.ineligible_survey_multi_options_ids_11[0]:
                                    single_select_options_86.append(config.ineligible_single_select_option_id_86)
                                elif option == config.ineligible_survey_multi_options_ids_11[1]:
                                    single_select_options_87.append(config.ineligible_single_select_option_id_87)
                                elif option == config.ineligible_survey_multi_options_ids_11[2]:
                                    single_select_options_88.append(config.ineligible_single_select_option_id_88)
                                elif option == config.ineligible_survey_multi_options_ids_11[3]:
                                    single_select_options_89.append(config.ineligible_single_select_option_id_89)
                                elif option == config.ineligible_survey_multi_options_ids_11[4]:
                                    single_select_options_90.append(config.ineligible_single_select_option_id_90)

                        # AEP multi-select
                        elif field_id == config.aep_multi_select_id_1:
                            multi_select_options_12 = data.getOptions()
                            for option in multi_select_options_12:
                                if option == config.aep_multi_options_ids_1[0]:
                                    single_select_options_91.append(config.aep_single_select_option_id_1)
                                elif option == config.aep_multi_options_ids_1[1]:
                                    single_select_options_92.append(config.aep_single_select_option_id_2)
                                elif option == config.aep_multi_options_ids_1[2]:
                                    single_select_options_93.append(config.aep_single_select_option_id_3)
                                elif option == config.aep_multi_options_ids_1[3]:
                                    single_select_options_94.append(config.aep_single_select_option_id_4)
                                elif option == config.aep_multi_options_ids_1[4]:
                                    single_select_options_95.append(config.aep_single_select_option_id_5)
                                elif option == config.aep_multi_options_ids_1[5]:
                                    single_select_options_96.append(config.aep_single_select_option_id_6)
                                elif option == config.aep_multi_options_ids_1[6]:
                                    single_select_options_97.append(config.aep_single_select_option_id_7)
                                elif option == config.aep_multi_options_ids_1[7]:
                                    single_select_options_98.append(config.aep_single_select_option_id_8)
                                elif option == config.aep_multi_options_ids_1[8]:
                                    single_select_options_99.append(config.aep_single_select_option_id_9)

                        elif field_id == config.aep_multi_select_id_2:
                            multi_select_options_13 = data.getOptions()
                            for option in multi_select_options_13:
                                if option == config.aep_multi_options_ids_2[0]:
                                    single_select_options_100.append(config.aep_single_select_option_id_10)
                                elif option == config.aep_multi_options_ids_2[1]:
                                    single_select_options_101.append(config.aep_single_select_option_id_11)
                                elif option == config.aep_multi_options_ids_2[2]:
                                    single_select_options_102.append(config.aep_single_select_option_id_12)
                                elif option == config.aep_multi_options_ids_2[3]:
                                    single_select_options_103.append(config.aep_single_select_option_id_13)
                                elif option == config.aep_multi_options_ids_2[4]:
                                    single_select_options_104.append(config.aep_single_select_option_id_14)
                                elif option == config.aep_multi_options_ids_2[5]:
                                    single_select_options_105.append(config.aep_single_select_option_id_15)

                        elif field_id == config.aep_multi_select_id_3:
                            multi_select_options_14 = data.getOptions()
                            for option in multi_select_options_14:
                                if option == config.aep_multi_options_ids_3[0]:
                                    single_select_options_106.append(config.aep_single_select_option_id_16)
                                elif option == config.aep_multi_options_ids_3[1]:
                                    single_select_options_107.append(config.aep_single_select_option_id_17)
                                elif option == config.aep_multi_options_ids_3[2]:
                                    single_select_options_108.append(config.aep_single_select_option_id_18)
                                elif option == config.aep_multi_options_ids_3[3]:
                                    single_select_options_109.append(config.aep_single_select_option_id_19)
                                elif option == config.aep_multi_options_ids_3[4]:
                                    single_select_options_110.append(config.aep_single_select_option_id_20)

                        elif field_id == config.aep_multi_select_id_4:
                            multi_select_options_15 = data.getOptions()
                            for option in multi_select_options_15:
                                if option == config.aep_multi_options_ids_4[0]:
                                    single_select_options_111.append(config.aep_single_select_option_id_21)
                                elif option == config.aep_multi_options_ids_4[1]:
                                    single_select_options_112.append(config.aep_single_select_option_id_22)
                                elif option == config.aep_multi_options_ids_4[2]:
                                    single_select_options_113.append(config.aep_single_select_option_id_23)
                                elif option == config.aep_multi_options_ids_4[3]:
                                    single_select_options_114.append(config.aep_single_select_option_id_24)
                                elif option == config.aep_multi_options_ids_4[4]:
                                    single_select_options_115.append(config.aep_single_select_option_id_25)

                        elif field_id == config.aep_multi_select_id_5:
                            multi_select_options_16 = data.getOptions()
                            for option in multi_select_options_16:
                                if option == config.aep_multi_options_ids_5[0]:
                                    single_select_options_116.append(config.aep_single_select_option_id_26)
                                elif option == config.aep_multi_options_ids_5[1]:
                                    single_select_options_117.append(config.aep_single_select_option_id_27)
                                elif option == config.aep_multi_options_ids_5[2]:
                                    single_select_options_118.append(config.aep_single_select_option_id_28)
                                elif option == config.aep_multi_options_ids_5[3]:
                                    single_select_options_119.append(config.aep_single_select_option_id_29)
                                elif option == config.aep_multi_options_ids_5[4]:
                                    single_select_options_120.append(config.aep_single_select_option_id_30)
                                elif option == config.aep_multi_options_ids_5[5]:
                                    single_select_options_121.append(config.aep_single_select_option_id_31)

                        elif field_id == config.aep_multi_select_id_6:
                            multi_select_options_17 = data.getOptions()
                            for option in multi_select_options_17:
                                if option == config.aep_multi_options_ids_6[0]:
                                    single_select_options_122.append(config.aep_single_select_option_id_32)
                                elif option == config.aep_multi_options_ids_6[1]:
                                    single_select_options_123.append(config.aep_single_select_option_id_33)
                                elif option == config.aep_multi_options_ids_6[2]:
                                    single_select_options_124.append(config.aep_single_select_option_id_34)
                                elif option == config.aep_multi_options_ids_6[3]:
                                    single_select_options_125.append(config.aep_single_select_option_id_35)

                        elif field_id == config.aep_multi_select_id_7:
                            multi_select_options_18 = data.getOptions()
                            for option in multi_select_options_18:
                                if option == config.aep_multi_options_ids_7[0]:
                                    single_select_options_126.append(config.aep_single_select_option_id_36)
                                elif option == config.aep_multi_options_ids_7[1]:
                                    single_select_options_127.append(config.aep_single_select_option_id_37)
                                elif option == config.aep_multi_options_ids_7[2]:
                                    single_select_options_128.append(config.aep_single_select_option_id_38)
                                elif option == config.aep_multi_options_ids_7[3]:
                                    single_select_options_129.append(config.aep_single_select_option_id_39)
                                elif option == config.aep_multi_options_ids_7[4]:
                                    single_select_options_130.append(config.aep_single_select_option_id_40)
                                elif option == config.aep_multi_options_ids_7[5]:
                                    single_select_options_131.append(config.aep_single_select_option_id_41)
                                elif option == config.aep_multi_options_ids_7[6]:
                                    single_select_options_132.append(config.aep_single_select_option_id_42)
                                elif option == config.aep_multi_options_ids_7[7]:
                                    single_select_options_133.append(config.aep_single_select_option_id_43)

                        elif field_id == config.aep_multi_select_id_8:
                            multi_select_options_19 = data.getOptions()
                            for option in multi_select_options_19:
                                if option == config.aep_multi_options_ids_8[0]:
                                    single_select_options_134.append(config.aep_single_select_option_id_44)
                                elif option == config.aep_multi_options_ids_8[1]:
                                    single_select_options_135.append(config.aep_single_select_option_id_45)
                                elif option == config.aep_multi_options_ids_8[2]:
                                    single_select_options_136.append(config.aep_single_select_option_id_46)
                                elif option == config.aep_multi_options_ids_8[3]:
                                    single_select_options_137.append(config.aep_single_select_option_id_47)

                        elif field_id == config.aep_multi_select_id_9:
                            multi_select_options_20 = data.getOptions()
                            for option in multi_select_options_20:
                                if option == config.aep_multi_options_ids_9[0]:
                                    single_select_options_138.append(config.aep_single_select_option_id_48)
                                elif option == config.aep_multi_options_ids_9[1]:
                                    single_select_options_139.append(config.aep_single_select_option_id_49)
                                elif option == config.aep_multi_options_ids_9[2]:
                                    single_select_options_140.append(config.aep_single_select_option_id_50)
                                elif option == config.aep_multi_options_ids_9[3]:
                                    single_select_options_141.append(config.aep_single_select_option_id_51)

                        # GI multi-select
                        elif field_id == config.gi_multi_select_id_1:
                            multi_select_options_21 = data.getOptions()
                            for option in multi_select_options_21:
                                if option == config.gi_multi_options_ids_1[0]:
                                    single_select_options_142.append(config.gi_single_select_option_id_1)
                                elif option == config.gi_multi_options_ids_1[1]:
                                    single_select_options_143.append(config.gi_single_select_option_id_2)
                                elif option == config.gi_multi_options_ids_1[2]:
                                    single_select_options_144.append(config.gi_single_select_option_id_3)
                                elif option == config.gi_multi_options_ids_1[3]:
                                    single_select_options_145.append(config.gi_single_select_option_id_4)
                                elif option == config.gi_multi_options_ids_1[4]:
                                    single_select_options_146.append(config.gi_single_select_option_id_5)
                                elif option == config.gi_multi_options_ids_1[5]:
                                    single_select_options_147.append(config.gi_single_select_option_id_6)
                                elif option == config.gi_multi_options_ids_1[6]:
                                    single_select_options_148.append(config.gi_single_select_option_id_7)
                                elif option == config.gi_multi_options_ids_1[7]:
                                    single_select_options_149.append(config.gi_single_select_option_id_8)
                                elif option == config.gi_multi_options_ids_1[8]:
                                    single_select_options_150.append(config.gi_single_select_option_id_9)

                        elif field_id == config.gi_multi_select_id_2:
                            multi_select_options_22 = data.getOptions()
                            for option in multi_select_options_22:
                                if option == config.gi_multi_options_ids_2[0]:
                                    single_select_options_151.append(config.gi_single_select_option_id_10)
                                elif option == config.gi_multi_options_ids_2[1]:
                                    single_select_options_152.append(config.gi_single_select_option_id_11)
                                elif option == config.gi_multi_options_ids_2[2]:
                                    single_select_options_153.append(config.gi_single_select_option_id_12)
                                elif option == config.gi_multi_options_ids_2[3]:
                                    single_select_options_154.append(config.gi_single_select_option_id_13)
                                elif option == config.gi_multi_options_ids_2[4]:
                                    single_select_options_155.append(config.gi_single_select_option_id_14)
                                elif option == config.gi_multi_options_ids_2[5]:
                                    single_select_options_156.append(config.gi_single_select_option_id_15)

                        elif field_id == config.gi_multi_select_id_3:
                            multi_select_options_23 = data.getOptions()
                            for option in multi_select_options_23:
                                if option == config.gi_multi_options_ids_3[0]:
                                    single_select_options_157.append(config.gi_single_select_option_id_16)
                                elif option == config.gi_multi_options_ids_3[1]:
                                    single_select_options_158.append(config.gi_single_select_option_id_17)
                                elif option == config.gi_multi_options_ids_3[2]:
                                    single_select_options_159.append(config.gi_single_select_option_id_18)
                                elif option == config.gi_multi_options_ids_3[3]:
                                    single_select_options_160.append(config.gi_single_select_option_id_19)
                                elif option == config.gi_multi_options_ids_3[4]:
                                    single_select_options_161.append(config.gi_single_select_option_id_20)

                        elif field_id == config.gi_multi_select_id_4:
                            multi_select_options_24 = data.getOptions()
                            for option in multi_select_options_24:
                                if option == config.gi_multi_options_ids_4[0]:
                                    single_select_options_162.append(config.gi_single_select_option_id_21)
                                elif option == config.gi_multi_options_ids_4[1]:
                                    single_select_options_163.append(config.gi_single_select_option_id_22)
                                elif option == config.gi_multi_options_ids_4[2]:
                                    single_select_options_164.append(config.gi_single_select_option_id_23)
                                elif option == config.gi_multi_options_ids_4[3]:
                                    single_select_options_165.append(config.gi_single_select_option_id_24)
                                elif option == config.gi_multi_options_ids_4[4]:
                                    single_select_options_166.append(config.gi_single_select_option_id_25)

                        elif field_id == config.gi_multi_select_id_5:
                            multi_select_options_25 = data.getOptions()
                            for option in multi_select_options_25:
                                if option == config.gi_multi_options_ids_5[0]:
                                    single_select_options_167.append(config.gi_single_select_option_id_26)
                                elif option == config.gi_multi_options_ids_5[1]:
                                    single_select_options_168.append(config.gi_single_select_option_id_27)
                                elif option == config.gi_multi_options_ids_5[2]:
                                    single_select_options_169.append(config.gi_single_select_option_id_28)
                                elif option == config.gi_multi_options_ids_5[3]:
                                    single_select_options_170.append(config.gi_single_select_option_id_29)
                                elif option == config.gi_multi_options_ids_5[4]:
                                    single_select_options_171.append(config.gi_single_select_option_id_30)
                                elif option == config.gi_multi_options_ids_5[5]:
                                    single_select_options_172.append(config.gi_single_select_option_id_31)

                        elif field_id == config.gi_multi_select_id_6:
                            multi_select_options_26 = data.getOptions()
                            for option in multi_select_options_26:
                                if option == config.gi_multi_options_ids_6[0]:
                                    single_select_options_173.append(config.gi_single_select_option_id_32)
                                elif option == config.gi_multi_options_ids_6[1]:
                                    single_select_options_174.append(config.gi_single_select_option_id_33)
                                elif option == config.gi_multi_options_ids_6[2]:
                                    single_select_options_175.append(config.gi_single_select_option_id_34)
                                elif option == config.gi_multi_options_ids_6[3]:
                                    single_select_options_176.append(config.gi_single_select_option_id_35)
                                elif option == config.gi_multi_options_ids_6[4]:
                                    single_select_options_177.append(config.gi_single_select_option_id_36)
                                elif option == config.gi_multi_options_ids_6[5]:
                                    single_select_options_178.append(config.gi_single_select_option_id_37)
                                elif option == config.gi_multi_options_ids_6[6]:
                                    single_select_options_179.append(config.gi_single_select_option_id_38)
                                elif option == config.gi_multi_options_ids_6[7]:
                                    single_select_options_180.append(config.gi_single_select_option_id_39)
                                elif option == config.gi_multi_options_ids_6[8]:
                                    single_select_options_181.append(config.gi_single_select_option_id_40)
                                elif option == config.gi_multi_options_ids_6[9]:
                                    single_select_options_182.append(config.gi_single_select_option_id_41)
                                elif option == config.gi_multi_options_ids_6[10]:
                                    single_select_options_183.append(config.gi_single_select_option_id_42)
                                elif option == config.gi_multi_options_ids_6[11]:
                                    single_select_options_184.append(config.gi_single_select_option_id_43)
                                elif option == config.gi_multi_options_ids_6[12]:
                                    single_select_options_185.append(config.gi_single_select_option_id_44)
                                elif option == config.gi_multi_options_ids_6[13]:
                                    single_select_options_186.append(config.gi_single_select_option_id_45)

                        # App survey multi-select
                        elif field_id == config.app_survey_multi_select_id_1:
                            multi_select_options_27 = data.getOptions()
                            for option in multi_select_options_27:
                                if option == config.app_survey_multi_options_ids_1[0]:
                                    single_select_options_187.append(config.app_single_select_option_id_1)
                                elif option == config.app_survey_multi_options_ids_1[1]:
                                    single_select_options_188.append(config.app_single_select_option_id_2)
                                elif option == config.app_survey_multi_options_ids_1[2]:
                                    single_select_options_189.append(config.app_single_select_option_id_3)
                                elif option == config.app_survey_multi_options_ids_1[3]:
                                    single_select_options_190.append(config.app_single_select_option_id_4)
                                elif option == config.app_survey_multi_options_ids_1[4]:
                                    single_select_options_191.append(config.app_single_select_option_id_5)
                                elif option == config.app_survey_multi_options_ids_1[5]:
                                    single_select_options_192.append(config.app_single_select_option_id_6)
                                elif option == config.app_survey_multi_options_ids_1[6]:
                                    single_select_options_193.append(config.app_single_select_option_id_7)

                        elif field_id == config.app_survey_multi_select_id_2:
                            multi_select_options_28 = data.getOptions()
                            for option in multi_select_options_28:
                                if option == config.app_survey_multi_options_ids_2[0]:
                                    single_select_options_194.append(config.app_single_select_option_id_8)
                                elif option == config.app_survey_multi_options_ids_2[1]:
                                    single_select_options_195.append(config.app_single_select_option_id_9)
                                elif option == config.app_survey_multi_options_ids_2[2]:
                                    single_select_options_196.append(config.app_single_select_option_id_10)
                                elif option == config.app_survey_multi_options_ids_2[3]:
                                    single_select_options_197.append(config.app_single_select_option_id_11)
                                elif option == config.app_survey_multi_options_ids_2[4]:
                                    single_select_options_198.append(config.app_single_select_option_id_12)

                        elif field_id == config.app_survey_multi_select_id_3:
                            multi_select_options_29 = data.getOptions()
                            for option in multi_select_options_29:
                                if option == config.app_survey_multi_options_ids_3[0]:
                                    single_select_options_199.append(config.app_single_select_option_id_13)
                                elif option == config.app_survey_multi_options_ids_3[1]:
                                    single_select_options_200.append(config.app_single_select_option_id_14)
                                elif option == config.app_survey_multi_options_ids_3[2]:
                                    single_select_options_201.append(config.app_single_select_option_id_15)
                                elif option == config.app_survey_multi_options_ids_3[3]:
                                    single_select_options_202.append(config.app_single_select_option_id_16)
                                elif option == config.app_survey_multi_options_ids_3[4]:
                                    single_select_options_203.append(config.app_single_select_option_id_17)
                                elif option == config.app_survey_multi_options_ids_3[5]:
                                    single_select_options_204.append(config.app_single_select_option_id_18)
                                elif option == config.app_survey_multi_options_ids_3[6]:
                                    single_select_options_205.append(config.app_single_select_option_id_19)
                                elif option == config.app_survey_multi_options_ids_3[7]:
                                    single_select_options_206.append(config.app_single_select_option_id_20)
                                elif option == config.app_survey_multi_options_ids_3[8]:
                                    single_select_options_207.append(config.app_single_select_option_id_21)
                                elif option == config.app_survey_multi_options_ids_3[9]:
                                    single_select_options_208.append(config.app_single_select_option_id_22)

                        elif field_id == config.app_survey_multi_select_id_4:
                            multi_select_options_30 = data.getOptions()
                            for option in multi_select_options_30:
                                if option == config.app_survey_multi_options_ids_4[0]:
                                    single_select_options_209.append(config.app_single_select_option_id_23)
                                elif option == config.app_survey_multi_options_ids_4[1]:
                                    single_select_options_210.append(config.app_single_select_option_id_24)
                                elif option == config.app_survey_multi_options_ids_4[2]:
                                    single_select_options_211.append(config.app_single_select_option_id_25)
                                elif option == config.app_survey_multi_options_ids_4[3]:
                                    single_select_options_212.append(config.app_single_select_option_id_26)
                                elif option == config.app_survey_multi_options_ids_4[4]:
                                    single_select_options_213.append(config.app_single_select_option_id_27)
                                elif option == config.app_survey_multi_options_ids_4[5]:
                                    single_select_options_214.append(config.app_single_select_option_id_28)

                        elif field_id == config.app_survey_multi_select_id_5:
                            multi_select_options_31 = data.getOptions()
                            for option in multi_select_options_31:
                                if option == config.app_survey_multi_options_ids_3[0]:
                                    single_select_options_215.append(config.app_single_select_option_id_29)
                                elif option == config.app_survey_multi_options_ids_3[1]:
                                    single_select_options_216.append(config.app_single_select_option_id_30)
                                elif option == config.app_survey_multi_options_ids_3[2]:
                                    single_select_options_217.append(config.app_single_select_option_id_31)
                                elif option == config.app_survey_multi_options_ids_3[3]:
                                    single_select_options_218.append(config.app_single_select_option_id_32)
                                elif option == config.app_survey_multi_options_ids_3[4]:
                                    single_select_options_219.append(config.app_single_select_option_id_33)
                                elif option == config.app_survey_multi_options_ids_3[5]:
                                    single_select_options_220.append(config.app_single_select_option_id_34)
                                elif option == config.app_survey_multi_options_ids_3[6]:
                                    single_select_options_221.append(config.app_single_select_option_id_35)
                                elif option == config.app_survey_multi_options_ids_3[7]:
                                    single_select_options_222.append(config.app_single_select_option_id_36)
                                elif option == config.app_survey_multi_options_ids_3[8]:
                                    single_select_options_223.append(config.app_single_select_option_id_37)

                        elif field_id == config.app_survey_multi_select_id_6:
                            multi_select_options_32 = data.getOptions()
                            for option in multi_select_options_32:
                                if option == config.app_survey_multi_options_ids_6[0]:
                                    single_select_options_224.append(config.app_single_select_option_id_38)
                                elif option == config.app_survey_multi_options_ids_6[1]:
                                    single_select_options_225.append(config.app_single_select_option_id_39)
                                elif option == config.app_survey_multi_options_ids_6[2]:
                                    single_select_options_226.append(config.app_single_select_option_id_40)
                                elif option == config.app_survey_multi_options_ids_6[3]:
                                    single_select_options_227.append(config.app_single_select_option_id_41)
                                elif option == config.app_survey_multi_options_ids_6[4]:
                                    single_select_options_228.append(config.app_single_select_option_id_42)
                                elif option == config.app_survey_multi_options_ids_6[5]:
                                    single_select_options_229.append(config.app_single_select_option_id_43)
                                elif option == config.app_survey_multi_options_ids_6[6]:
                                    single_select_options_230.append(config.app_single_select_option_id_44)
                                elif option == config.app_survey_multi_options_ids_6[7]:
                                    single_select_options_231.append(config.app_single_select_option_id_45)
                                elif option == config.app_survey_multi_options_ids_6[8]:
                                    single_select_options_232.append(config.app_single_select_option_id_46)
                                elif option == config.app_survey_multi_options_ids_6[9]:
                                    single_select_options_233.append(config.app_single_select_option_id_47)
                                elif option == config.app_survey_multi_options_ids_6[10]:
                                    single_select_options_234.append(config.app_single_select_option_id_48)
                                elif option == config.app_survey_multi_options_ids_6[11]:
                                    single_select_options_235.append(config.app_single_select_option_id_49)
                                elif option == config.app_survey_multi_options_ids_6[12]:
                                    single_select_options_236.append(config.app_single_select_option_id_50)
                                elif option == config.app_survey_multi_options_ids_6[13]:
                                    single_select_options_237.append(config.app_single_select_option_id_51)

                        elif field_id == config.app_survey_multi_select_id_7:
                            multi_select_options_33 = data.getOptions()
                            for option in multi_select_options_33:
                                if option == config.app_survey_multi_options_ids_7[0]:
                                    single_select_options_238.append(config.app_single_select_option_id_52)
                                elif option == config.app_survey_multi_options_ids_7[1]:
                                    single_select_options_239.append(config.app_single_select_option_id_53)
                                elif option == config.app_survey_multi_options_ids_7[2]:
                                    single_select_options_240.append(config.app_single_select_option_id_54)
                                elif option == config.app_survey_multi_options_ids_7[3]:
                                    single_select_options_241.append(config.app_single_select_option_id_55)
                                elif option == config.app_survey_multi_options_ids_7[4]:
                                    single_select_options_242.append(config.app_single_select_option_id_56)
                                elif option == config.app_survey_multi_options_ids_7[5]:
                                    single_select_options_243.append(config.app_single_select_option_id_57)
                                elif option == config.app_survey_multi_options_ids_7[6]:
                                    single_select_options_244.append(config.app_single_select_option_id_58)
                                elif option == config.app_survey_multi_options_ids_7[7]:
                                    single_select_options_245.append(config.app_single_select_option_id_59)
                                elif option == config.app_survey_multi_options_ids_7[8]:
                                    single_select_options_246.append(config.app_single_select_option_id_60)
                                elif option == config.app_survey_multi_options_ids_7[9]:
                                    single_select_options_247.append(config.app_single_select_option_id_61)
                                elif option == config.app_survey_multi_options_ids_7[10]:
                                    single_select_options_248.append(config.app_single_select_option_id_62)
                                elif option == config.app_survey_multi_options_ids_7[11]:
                                    single_select_options_249.append(config.app_single_select_option_id_63)
                                elif option == config.app_survey_multi_options_ids_7[12]:
                                    single_select_options_250.append(config.app_single_select_option_id_64)

                    if primary_last_name is not None and primary_dob is not None and primary_zip is not None:
                        # create the primary UID
                        primary_unique_id = str(primary_dob) + str(primary_last_name) + str(primary_zip)
                        primary_unique_id = primary_unique_id.replace(" ", "")
                        primary_unique_id = primary_unique_id.replace("-", "")
                        logger.info(f"project 2 - primary_unique_id: {primary_unique_id}")

                    try:
                        if primary_last_name is not None and primary_dob is not None and primary_zip is not None:
                            # create internal entry using beta endpoint - Work In Progress
                            try:
                                self.submittable.submitInternalFormResponse(submission_id,
                                                                            primary_unique_id,
                                                                            single_select_options_1,
                                                                            single_select_options_2,
                                                                            single_select_options_3,
                                                                            single_select_options_4,
                                                                            single_select_options_5,
                                                                            single_select_options_6,
                                                                            single_select_options_7,
                                                                            single_select_options_8,
                                                                            single_select_options_9,
                                                                            single_select_options_10,
                                                                            single_select_options_11,
                                                                            single_select_options_12,
                                                                            single_select_options_13,
                                                                            single_select_options_14,
                                                                            single_select_options_15,
                                                                            single_select_options_16,
                                                                            single_select_options_17,
                                                                            single_select_options_18,
                                                                            single_select_options_19,
                                                                            single_select_options_20,
                                                                            single_select_options_21,
                                                                            single_select_options_22,
                                                                            single_select_options_23,
                                                                            single_select_options_24,
                                                                            single_select_options_25,
                                                                            single_select_options_26,
                                                                            single_select_options_27,
                                                                            single_select_options_28,
                                                                            single_select_options_29,
                                                                            single_select_options_30,
                                                                            single_select_options_31,
                                                                            single_select_options_32,
                                                                            single_select_options_33,
                                                                            single_select_options_34,
                                                                            single_select_options_35,
                                                                            single_select_options_36,
                                                                            single_select_options_37,
                                                                            single_select_options_38,
                                                                            single_select_options_39,
                                                                            single_select_options_40,
                                                                            single_select_options_41,
                                                                            single_select_options_42,
                                                                            single_select_options_43,
                                                                            single_select_options_44,
                                                                            single_select_options_45,
                                                                            single_select_options_46,
                                                                            single_select_options_47,
                                                                            single_select_options_48,
                                                                            single_select_options_49,
                                                                            single_select_options_50,
                                                                            single_select_options_51,
                                                                            single_select_options_52,
                                                                            single_select_options_53,
                                                                            single_select_options_54,
                                                                            single_select_options_55,
                                                                            single_select_options_56,
                                                                            single_select_options_57,
                                                                            single_select_options_58,
                                                                            single_select_options_59,
                                                                            single_select_options_60,
                                                                            single_select_options_61,
                                                                            single_select_options_62,
                                                                            single_select_options_63,
                                                                            single_select_options_64,
                                                                            single_select_options_65,
                                                                            single_select_options_66,
                                                                            single_select_options_67,
                                                                            single_select_options_68,
                                                                            single_select_options_69,
                                                                            single_select_options_70,
                                                                            single_select_options_71,
                                                                            single_select_options_72,
                                                                            single_select_options_73,
                                                                            single_select_options_74,
                                                                            single_select_options_75,
                                                                            single_select_options_76,
                                                                            single_select_options_77,
                                                                            single_select_options_78,
                                                                            single_select_options_79,
                                                                            single_select_options_80,
                                                                            single_select_options_81,
                                                                            single_select_options_82,
                                                                            single_select_options_83,
                                                                            single_select_options_84,
                                                                            single_select_options_85,
                                                                            single_select_options_86,
                                                                            single_select_options_87,
                                                                            single_select_options_88,
                                                                            single_select_options_89,
                                                                            single_select_options_90,
                                                                            single_select_options_91,
                                                                            single_select_options_92,
                                                                            single_select_options_93,
                                                                            single_select_options_94,
                                                                            single_select_options_95,
                                                                            single_select_options_96,
                                                                            single_select_options_97,
                                                                            single_select_options_98,
                                                                            single_select_options_99,
                                                                            single_select_options_100,
                                                                            single_select_options_101,
                                                                            single_select_options_102,
                                                                            single_select_options_103,
                                                                            single_select_options_104,
                                                                            single_select_options_105,
                                                                            single_select_options_106,
                                                                            single_select_options_107,
                                                                            single_select_options_108,
                                                                            single_select_options_109,
                                                                            single_select_options_110,
                                                                            single_select_options_111,
                                                                            single_select_options_112,
                                                                            single_select_options_113,
                                                                            single_select_options_114,
                                                                            single_select_options_115,
                                                                            single_select_options_116,
                                                                            single_select_options_117,
                                                                            single_select_options_118,
                                                                            single_select_options_119,
                                                                            single_select_options_120,
                                                                            single_select_options_121,
                                                                            single_select_options_122,
                                                                            single_select_options_123,
                                                                            single_select_options_124,
                                                                            single_select_options_125,
                                                                            single_select_options_126,
                                                                            single_select_options_127,
                                                                            single_select_options_128,
                                                                            single_select_options_129,
                                                                            single_select_options_130,
                                                                            single_select_options_131,
                                                                            single_select_options_132,
                                                                            single_select_options_133,
                                                                            single_select_options_134,
                                                                            single_select_options_135,
                                                                            single_select_options_136,
                                                                            single_select_options_137,
                                                                            single_select_options_138,
                                                                            single_select_options_139,
                                                                            single_select_options_140,
                                                                            single_select_options_141,
                                                                            single_select_options_142,
                                                                            single_select_options_143,
                                                                            single_select_options_144,
                                                                            single_select_options_145,
                                                                            single_select_options_146,
                                                                            single_select_options_147,
                                                                            single_select_options_148,
                                                                            single_select_options_149,
                                                                            single_select_options_150,
                                                                            single_select_options_151,
                                                                            single_select_options_152,
                                                                            single_select_options_153,
                                                                            single_select_options_154,
                                                                            single_select_options_155,
                                                                            single_select_options_156,
                                                                            single_select_options_157,
                                                                            single_select_options_158,
                                                                            single_select_options_159,
                                                                            single_select_options_160,
                                                                            single_select_options_161,
                                                                            single_select_options_162,
                                                                            single_select_options_163,
                                                                            single_select_options_164,
                                                                            single_select_options_165,
                                                                            single_select_options_166,
                                                                            single_select_options_167,
                                                                            single_select_options_168,
                                                                            single_select_options_169,
                                                                            single_select_options_170,
                                                                            single_select_options_171,
                                                                            single_select_options_172,
                                                                            single_select_options_173,
                                                                            single_select_options_174,
                                                                            single_select_options_175,
                                                                            single_select_options_176,
                                                                            single_select_options_177,
                                                                            single_select_options_178,
                                                                            single_select_options_179,
                                                                            single_select_options_180,
                                                                            single_select_options_181,
                                                                            single_select_options_182,
                                                                            single_select_options_183,
                                                                            single_select_options_184,
                                                                            single_select_options_185,
                                                                            single_select_options_186,
                                                                            single_select_options_187,
                                                                            single_select_options_188,
                                                                            single_select_options_189,
                                                                            single_select_options_190,
                                                                            single_select_options_191,
                                                                            single_select_options_192,
                                                                            single_select_options_193,
                                                                            single_select_options_194,
                                                                            single_select_options_195,
                                                                            single_select_options_196,
                                                                            single_select_options_197,
                                                                            single_select_options_198,
                                                                            single_select_options_199,
                                                                            single_select_options_200,
                                                                            single_select_options_201,
                                                                            single_select_options_202,
                                                                            single_select_options_203,
                                                                            single_select_options_204,
                                                                            single_select_options_205,
                                                                            single_select_options_206,
                                                                            single_select_options_207,
                                                                            single_select_options_208,
                                                                            single_select_options_209,
                                                                            single_select_options_210,
                                                                            single_select_options_211,
                                                                            single_select_options_212,
                                                                            single_select_options_213,
                                                                            single_select_options_214,
                                                                            single_select_options_215,
                                                                            single_select_options_216,
                                                                            single_select_options_217,
                                                                            single_select_options_218,
                                                                            single_select_options_219,
                                                                            single_select_options_220,
                                                                            single_select_options_221,
                                                                            single_select_options_222,
                                                                            single_select_options_223,
                                                                            single_select_options_224,
                                                                            single_select_options_225,
                                                                            single_select_options_226,
                                                                            single_select_options_227,
                                                                            single_select_options_228,
                                                                            single_select_options_229,
                                                                            single_select_options_230,
                                                                            single_select_options_231,
                                                                            single_select_options_232,
                                                                            single_select_options_233,
                                                                            single_select_options_234,
                                                                            single_select_options_235,
                                                                            single_select_options_236,
                                                                            single_select_options_237,
                                                                            single_select_options_238,
                                                                            single_select_options_239,
                                                                            single_select_options_240,
                                                                            single_select_options_241,
                                                                            single_select_options_242,
                                                                            single_select_options_243,
                                                                            single_select_options_244,
                                                                            single_select_options_245,
                                                                            single_select_options_246,
                                                                            single_select_options_247,
                                                                            single_select_options_248,
                                                                            single_select_options_249,
                                                                            single_select_options_250)
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
                            logger.info(f"project 2 - primary UID field Null: {primary_unique_id} for submission: {submission_id}")
                            continue
                    except:
                        # log the failure
                        logger.info(f"project 2 - failed to check unique id for submission: {submission_id}")

        # log the completed list of UIDs
        logger.info(f"config struct {config.uid_data_struct}")
