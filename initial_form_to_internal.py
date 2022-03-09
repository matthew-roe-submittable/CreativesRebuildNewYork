import config
from lib.submittable import *
import logging

logger = logging.getLogger("logfile")


class InitialToInternal:

    def __init__(self):
        self.submittable = Submittable()
        self.project_id_1 = config.project_id_1

    def initial2internal(self):
        subsList = None
        # get list of submission from AEP project (new, in_progress)
        try:
            subsList = self.submittable.getListOfSubmissions(self.project_id_1)
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

            single_select_options_1 = []
            single_select_options_2 = []
            single_select_options_3 = []
            single_select_options_4 = []

            # loop through initial form response data
            for init_resp_Data in initialFormResponseData:
                fieldID = init_resp_Data.getFormFieldId()
                print("filed id:", fieldID)

                if fieldID == config.multi_select_id_1:
                    multi_select_options_1 = init_resp_Data.getOptions()
                    for option in multi_select_options_1:
                        if option == config.multi_options_ids_1[0]:
                            single_select_options_1.append(config.single_select_option_ids_1[0])
                        elif option == config.multi_options_ids_1[1]:
                            single_select_options_1.append(config.single_select_option_ids_1[1])
                        elif option == config.multi_options_ids_1[2]:
                            single_select_options_1.append(config.single_select_option_ids_1[2])
                        elif option == config.multi_options_ids_1[3]:
                            single_select_options_1.append(config.single_select_option_ids_1[3])
                        elif option == config.multi_options_ids_1[4]:
                            single_select_options_1.append(config.single_select_option_ids_1[4])

                elif fieldID == config.multi_select_id_2:
                    multi_select_options_2 = init_resp_Data.getOptions()
                    for option in multi_select_options_1:
                        if option == config.multi_options_ids_2[0]:
                            single_select_options_2.append(config.single_select_option_ids_2[0])
                        elif option == config.multi_options_ids_2[1]:
                            single_select_options_2.append(config.single_select_option_ids_2[1])
                        elif option == config.multi_options_ids_2[2]:
                            single_select_options_2.append(config.single_select_option_ids_2[2])
                        elif option == config.multi_options_ids_2[3]:
                            single_select_options_2.append(config.single_select_option_ids_2[3])
                        elif option == config.multi_options_ids_2[4]:
                            single_select_options_2.append(config.single_select_option_ids_2[4])
                        elif option == config.multi_options_ids_2[5]:
                            single_select_options_2.append(config.single_select_option_ids_2[5])

                elif fieldID == config.multi_select_id_3:
                    multi_select_options_3 = init_resp_Data.getOptions()
                    for option in multi_select_options_3:
                        if option == config.multi_options_ids_3[0]:
                            single_select_options_3.append(config.single_select_option_ids_3[0])
                        if option == config.multi_options_ids_3[1]:
                            single_select_options_3.append(config.single_select_option_ids_3[1])
                        if option == config.multi_options_ids_3[2]:
                            single_select_options_3.append(config.single_select_option_ids_3[2])
                        if option == config.multi_options_ids_3[3]:
                            single_select_options_3.append(config.single_select_option_ids_3[3])
                        if option == config.multi_options_ids_3[4]:
                            single_select_options_3.append(config.single_select_option_ids_3[4])
                        if option == config.multi_options_ids_3[5]:
                            single_select_options_3.append(config.single_select_option_ids_3[5])
                        if option == config.multi_options_ids_3[6]:
                            single_select_options_3.append(config.single_select_option_ids_3[6])
                        if option == config.multi_options_ids_3[7]:
                            single_select_options_3.append(config.single_select_option_ids_3[7])
                        if option == config.multi_options_ids_3[8]:
                            single_select_options_3.append(config.single_select_option_ids_3[8])

                elif fieldID == config.multi_select_id_4:
                    multi_select_options_4 = init_resp_Data.getOptions()
                    for option in multi_select_options_4:
                        if option == config.multi_options_ids_4[0]:
                            single_select_options_4.append(config.single_select_option_ids_4[0])
                        if option == config.multi_options_ids_4[1]:
                            single_select_options_4.append(config.single_select_option_ids_4[1])
                        if option == config.multi_options_ids_4[2]:
                            single_select_options_4.append(config.single_select_option_ids_4[2])
                        if option == config.multi_options_ids_4[3]:
                            single_select_options_4.append(config.single_select_option_ids_4[3])
                        if option == config.multi_options_ids_4[4]:
                            single_select_options_4.append(config.single_select_option_ids_4[4])
                        if option == config.multi_options_ids_4[5]:
                            single_select_options_4.append(config.single_select_option_ids_4[5])


            print(multi_select_options_1, multi_select_options_2, multi_select_options_3, multi_select_options_4)

            print(single_select_options_1, single_select_options_2, single_select_options_3, single_select_options_4)

            primary_unique_id   = "123"
            collab_unique_id_1  = "321"



            self.submittable.submitInternalFormResponse(subId, primary_unique_id, single_select_options_1, single_select_options_2, single_select_options_3, single_select_options_4, collab_unique_id_1)

            # self.submittable.updateInternalFormResponse(subId, config.internalFormFieldData)

