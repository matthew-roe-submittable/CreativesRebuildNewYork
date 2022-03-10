import config
from lib.submittable import *
import logging

logger = logging.getLogger("logfile")


class InitialToInternal:

    def __init__(self):
        self.submittable = Submittable()
        self.project_id_1 = config.project_id_1
        self.project_id_2 = config.project_id_2

    def initial2internal(self):
        subsList = None
        # get list of submission from AEP project (new, in_progress)
        try:
            subsList = self.submittable.getListOfSubmissions(self.project_id_1, self.project_id_2)
            logger.info(f"subsList: {subsList}")
        except:
            logger.info("failed to get submission list for initial2Internal")

        for sub in subsList:
            subId = sub.getSubmissionId()
            logger.info(f"processing subId: {subId}")
            initialFormResponse     = []
            initialFormResponseData = []
            formResponses           = None

            try:
                logger.info(f"Starting sub id:{subId}")
                submission = self.submittable.getSubmission(subId)
                formResponses = submission.getFormResponses()
            except:
                print("failed to get form responses")

            for response in formResponses:
                formId = response.getFormId()
                print("form id", formId)
                # check that form ids match
                if formId == config.project_1_formId:
                    # pull the field data
                    initialFormResponseData = response.getFieldData()

            # for each submission clear the options list
            multi_select_options_1 = []
            multi_select_options_2 = []
            multi_select_options_3 = []
            multi_select_options_4 = []

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

            # loop through initial form response data
            for init_resp_Data in initialFormResponseData:
                fieldID = init_resp_Data.getFormFieldId()
                print("filed id:", fieldID)

                if fieldID == config.multi_select_id_1:
                    multi_select_options_1 = init_resp_Data.getOptions()
                    for option in multi_select_options_1:
                        if option == config.multi_options_ids_1[0]:
                            single_select_options_1.append(config.single_select_option_id_1)
                        elif option == config.multi_options_ids_1[1]:
                            single_select_options_2.append(config.single_select_option_id_2)
                        elif option == config.multi_options_ids_1[2]:
                            single_select_options_3.append(config.single_select_option_id_3)
                        elif option == config.multi_options_ids_1[3]:
                            single_select_options_4.append(config.single_select_option_id_4)
                        elif option == config.multi_options_ids_1[4]:
                            single_select_options_5.append(config.single_select_option_id_5)
                        elif option == config.multi_options_ids_1[5]:
                            single_select_options_6.append(config.single_select_option_id_6)
                        elif option == config.multi_options_ids_1[6]:
                            single_select_options_7.append(config.single_select_option_id_7)
                        elif option == config.multi_options_ids_1[7]:
                            single_select_options_8.append(config.single_select_option_id_8)
                        elif option == config.multi_options_ids_1[8]:
                            single_select_options_9.append(config.single_select_option_id_9)

                elif fieldID == config.multi_select_id_2:
                    multi_select_options_2 = init_resp_Data.getOptions()
                    for option in multi_select_options_1:
                        if option == config.multi_options_ids_2[0]:
                            single_select_options_10.append(config.single_select_option_id_10)
                        elif option == config.multi_options_ids_2[1]:
                            single_select_options_11.append(config.single_select_option_id_11)
                        elif option == config.multi_options_ids_2[2]:
                            single_select_options_12.append(config.single_select_option_id_12)
                        elif option == config.multi_options_ids_2[3]:
                            single_select_options_13.append(config.single_select_option_id_13)
                        elif option == config.multi_options_ids_2[4]:
                            single_select_options_14.append(config.single_select_option_id_14)
                        elif option == config.multi_options_ids_2[5]:
                            single_select_options_15.append(config.single_select_option_id_15)

                elif fieldID == config.multi_select_id_3:
                    multi_select_options_3 = init_resp_Data.getOptions()
                    for option in multi_select_options_3:
                        if option == config.multi_options_ids_3[0]:
                            single_select_options_16.append(config.single_select_option_id_16)
                        elif option == config.multi_options_ids_3[1]:
                            single_select_options_17.append(config.single_select_option_id_17)
                        elif option == config.multi_options_ids_3[2]:
                            single_select_options_18.append(config.single_select_option_id_18)
                        elif option == config.multi_options_ids_3[3]:
                            single_select_options_19.append(config.single_select_option_id_19)
                        elif option == config.multi_options_ids_3[4]:
                            single_select_options_20.append(config.single_select_option_id_20)

                elif fieldID == config.multi_select_id_4:
                    multi_select_options_4 = init_resp_Data.getOptions()
                    for option in multi_select_options_4:
                        if option == config.multi_options_ids_4[0]:
                            single_select_options_21.append(config.single_select_option_id_21)
                        elif option == config.multi_options_ids_4[1]:
                            single_select_options_22.append(config.single_select_option_id_22)
                        elif option == config.multi_options_ids_4[2]:
                            single_select_options_23.append(config.single_select_option_id_23)
                        elif option == config.multi_options_ids_4[3]:
                            single_select_options_24.append(config.single_select_option_id_24)
                        elif option == config.multi_options_ids_4[4]:
                            single_select_options_25.append(config.single_select_option_id_25)

            print("sub id:", subId)
            print("multi select options:", multi_select_options_1, multi_select_options_2, multi_select_options_3, multi_select_options_4)

            print("single select options:",  single_select_options_1,  single_select_options_2,  single_select_options_3,  single_select_options_4,
                  single_select_options_5,   single_select_options_6,  single_select_options_7,  single_select_options_8,  single_select_options_9,
                  single_select_options_10,  single_select_options_11, single_select_options_12, single_select_options_13, single_select_options_14,
                  single_select_options_15,  single_select_options_16, single_select_options_17, single_select_options_18, single_select_options_19,
                  single_select_options_20,  single_select_options_21, single_select_options_22, single_select_options_23, single_select_options_24,
                  single_select_options_25)

            primary_unique_id   = "123"
            collab_unique_id_1  = "321"

            self.submittable.submitInternalFormResponse(subId, primary_unique_id,
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
                                                        single_select_options_25, collab_unique_id_1)
