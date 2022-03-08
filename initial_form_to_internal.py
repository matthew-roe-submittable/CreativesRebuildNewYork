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

            # loop through initial form response data
            for init_resp_Data in initialFormResponseData:
                fieldID = init_resp_Data.getFormFieldId()
                print("filed id:", fieldID)

                if fieldID == config.multi_select_id_1:
                    multi_select_options_1 = init_resp_Data.getOptions()

                elif fieldID == config.multi_select_id_2:
                    multi_select_options_2 = init_resp_Data.getOptions()

                elif fieldID == config.multi_select_id_3:
                    multi_select_options_3 = init_resp_Data.getOptions()

                elif fieldID == config.multi_select_id_4:
                    multi_select_options_4 = init_resp_Data.getOptions()


            print(multi_select_options_1, multi_select_options_2, multi_select_options_3, multi_select_options_4)

            primary_unique_id   = "123"
            collab_unique_id_1  = "321"
            single_select_1     = True
            single_select_2     = True
            single_select_3     = True
            single_select_4     = True



            self.submittable.submitInternalFormResponse(subId, primary_unique_id, single_select_1, single_select_2, single_select_3, single_select_4, collab_unique_id_1)

            # self.submittable.updateInternalFormResponse(subId, config.internalFormFieldData)

