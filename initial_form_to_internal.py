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
            initialFormResponse = []
            formResponses = None

            try:
                logger.info(f"Starting sub id:{subId}")
                submission = self.submittable.getSubmission(subId)
                formResponses = submission.getFormResponses()
            except:
                print("failed to get form responses")

            for response in formResponses:
                formId = response.getFormId()
                # check that form ids match
                if formId == config.project_1_formId:
                    # pull the field data
                    initialFormResponseData = formResponses.getFieldData()

            for init_resp_Data in initialFormResponseData:
                fieldID = init_resp_Data.getFormFieldId()

                if fieldID == config.first_multi_options_ids:
                    first_multi_select = init_resp_Data.getOptions()

                elif fieldID == config.second_multi_options_ids:
                    second_multi_select = init_resp_Data.getOptions()

                elif fieldID == config.third_multi_options_ids:
                    third_multi_select = init_resp_Data.getOptions()

                elif fieldID == config.third_multi_options_ids:
                    fourth_multi_select = init_resp_Data.getOptions()



            self.submittable.updateInternalFormResponse(subId, config.internalFormFieldData)

