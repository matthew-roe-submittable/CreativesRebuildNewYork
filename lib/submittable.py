import datetime
import threading
import requests
import json
from ratelimit import limits, sleep_and_retry
import logging
import config

logger = logging.getLogger("logfile")


#
# Class for Accessing Submittable API
#
class Submittable:

    def __init__(self):
        self.api_key  = config.submittable_token
        self.baseURL  = "https://svcs.submittable.com/v3"


    @sleep_and_retry
    @limits(calls=10, period=0.25)
    def getLabelIds(self):
        endpoint = f'{self.baseURL}/labels/list'
        headers = {'Content-type': 'application/json'}
        response = requests.post(endpoint, auth=("", self.api_key), headers=headers)
        if response.status_code != 201:
            print("get label ids failed")
        else:
            print("get label ids successful")
        return response.json()

    @sleep_and_retry
    @limits(calls=10, period=0.25)
    def deleteLabel(self, submissionId, labelId):
        endpoint = f'{self.baseURL}/submissions/{submissionId}/labels/{labelId}'
        headers  = {'Content-type': 'application/json'}
        response = requests.delete(endpoint, auth=("", self.api_key), headers=headers)
        if response.status_code != 204:
            print(f"delete label failed {response.status_code}. Response payload: {response.content}")
            raise ValueError(f"delete label failed {response.status_code}. Response payload: {response.content}")
        else:
            print("delete label successful")
        return response


    @sleep_and_retry
    @limits(calls=10, period=0.25)
    def addLabel(self, submissionId, labelId):
        endpoint = f'{self.baseURL}/submissions/{submissionId}/labels/{labelId}'
        headers  = {'Content-type': 'application/json'}
        response = requests.put(endpoint, auth=("", self.api_key), headers=headers)
        if response.status_code != 204:
            print(f"add label failed {response.status_code}. Response payload: {response.content}")
            raise ValueError(f"add label failed {response.status_code}. Response payload: {response.content}")
        return response

    @sleep_and_retry
    @limits(calls=10, period=0.25)
    def getEntry(self, entry_id):
        endpoint = f"https://submittable-api.submittable.com/beta/entries/{entry_id}"
        headers  = {'Content-type': 'application/json'}
        response = requests.get(endpoint, auth=(":", self.api_key), headers=headers)
        print(response.status_code)
        if response.status_code != 201:
            print("get entry failed")
        else:
            print("get entry successful")
        return SubmittableBetaResponseEntry(response.json())


    @sleep_and_retry
    @limits(calls=10, period=0.25)
    def getInitialFormRequestId(self, subId):
        endpoint = f'{self.baseURL}/requests'
        headers = {'Content-type': 'application/json'}
        payload = {"formType": "initial",
                   "submissionId": subId}
        payload = json.dumps(payload)
        response = requests.post(endpoint, auth=(":", self.api_key), headers=headers, data=payload)
        if response.status_code != 201:
            print("initial from request id failed")
        else:
            print("initial form request id successful")
        return SubmittableFormRequestId(response.json())

    def submitInternalFormResponse(self, submission_id, primary_unique_id, collab_unique_id_1=None, collab_unique_id_2=None,
                                   collab_unique_id_3=None, collab_unique_id_4=None, collab_unique_id_5=None, collab_unique_id_6=None,
                                   collab_unique_id_7=None, collab_unique_id_8=None, collab_unique_id_9=None):
        endpoint = f'https://submittable-api.submittable.com/beta/entries/internal'
        headers = {'Content-type': 'application/json'}
        payload = {"submissionId": submission_id,
                   "fieldData": [
                       {
                           "fieldType":   "short_answer",
                           "formFieldId": config.internal_form_field_id_1,
                           "value":       primary_unique_id
                       },
                       {
                           "fieldType": "short_answer",
                           "formFieldId": config.internal_form_field_id_2,
                           "value": collab_unique_id_1
                       },
                       {
                           "fieldType": "short_answer",
                           "formFieldId": config.internal_form_field_id_3,
                           "value": collab_unique_id_2
                       },
                       {
                           "fieldType": "short_answer",
                           "formFieldId": config.internal_form_field_id_4,
                           "value": collab_unique_id_3
                       },
                       {
                           "fieldType":   "short_answer",
                           "formFieldId": config.internal_form_field_id_5,
                           "value": collab_unique_id_4
                       },
                       {
                           "fieldType": "short_answer",
                           "formFieldId": config.internal_form_field_id_6,
                           "value": collab_unique_id_5
                       },
                       {
                           "fieldType": "short_answer",
                           "formFieldId": config.internal_form_field_id_7,
                           "value": collab_unique_id_6
                       },
                       {
                           "fieldType": "short_answer",
                           "formFieldId": config.internal_form_field_id_8,
                           "value": collab_unique_id_7
                       },
                       {
                           "fieldType": "short_answer",
                           "formFieldId": config.internal_form_field_id_9,
                           "value": collab_unique_id_8
                       },
                       {
                           "fieldType": "short_answer",
                           "formFieldId": config.internal_form_field_id_10,
                           "value": collab_unique_id_9
                       }

                   ]
                   }
        payload  = json.dumps(payload)
        response = requests.post(endpoint, auth=("", self.api_key), headers=headers, data=payload)
        print("response:", response)
        if response.status_code != 201:
            print(f"submit internal form response failed {response.status_code}. Response payload: {response.content}. \nRequest payload: {str(payload)}")
            raise ValueError(f"submit internal from response failed {response.status_code}. Response payload: {response.content}. \nRequest payload: {str(payload)}")
        else:
            print("submit internal form response successful")
        return response.json()["entryId"]


    @sleep_and_retry
    @limits(calls=10, period=0.25)
    def updateInternalFormResponse(self, request_id, form_field_id, primary_unique_id, collab_unique_id_1=None, collab_unique_id_2=None,
        collab_unique_id_3=None, collab_unique_id_4=None, collab_unique_id_5=None, collab_unique_id_6=None,
        collab_unique_id_7=None, collab_unique_id_8=None, collab_unique_id_9=None):
        endpoint = f'https://submittable-api.submittable.com/beta/entries/{request_id}'
        headers = {'Content-type': 'application/json'}
        payload = {"formType": "internal",
                   "fieldData": [
                        {
                            "fieldType": "short_answer",
                            "formFieldId": config.internal_form_field_id_1,
                            "value": primary_unique_id
                        },
                        {
                            "fieldType": "short_answer",
                            "formFieldId": config.internal_form_field_id_2,
                            "value": collab_unique_id_1
                        },
                        {
                            "fieldType": "short_answer",
                            "formFieldId": config.internal_form_field_id_3,
                            "value": collab_unique_id_2
                        },
                        {
                            "fieldType": "short_answer",
                            "formFieldId": config.internal_form_field_id_4,
                            "value": collab_unique_id_3
                        },
                        {
                            "fieldType": "short_answer",
                            "formFieldId": config.internal_form_field_id_5,
                            "value": collab_unique_id_4
                        },
                        {
                            "fieldType": "short_answer",
                            "formFieldId": config.internal_form_field_id_6,
                            "value": collab_unique_id_5
                        },
                        {
                            "fieldType": "short_answer",
                            "formFieldId": config.internal_form_field_id_7,
                            "value": collab_unique_id_6
                        },
                        {
                            "fieldType": "short_answer",
                            "formFieldId": config.internal_form_field_id_8,
                            "value": collab_unique_id_7
                        },
                        {
                            "fieldType": "short_answer",
                            "formFieldId": config.internal_form_field_id_9,
                            "value": collab_unique_id_8
                        },
                        {
                            "fieldType": "short_answer",
                            "formFieldId": config.internal_form_field_id_10,
                            "value": collab_unique_id_9
                        }
                    ]
                }
        payload  = json.dumps(payload)
        response = requests.put(endpoint, auth=("", self.api_key), headers=headers, data=payload)
        # print(response.json())
        if response.status_code != 200:
            print(f"update initial form failed {response.status_code}. Response payload: {response.content}., \nRequest payload: {str(payload)}")
            raise ValueError(f"update initial form failed {response.status_code}. Response payload: {response.content}. \nRequest payload: {str(payload)}")
        else:
            print("update initial form successful")
        return response.json()

    # get an individual submission
    @sleep_and_retry
    @limits(calls=10, period=0.25)
    def getSubmission(self, submission_id):
        endpoint       = f'{self.baseURL}/submissions/{submission_id}'
        headers        = {'Content-type': 'application/json'}
        response       = requests.get(endpoint, auth=("", self.api_key), headers=headers)
        # print("get sub", response.json())
        if response.status_code != 200:
            print(f"get submission failed {response.status_code}. Response payload: {response.content}")
            raise ValueError(f"get submission failed {response.status_code}. Response payload: {response.content}")
        else:
            print("get submission successful")
        return SubmittableSubmission(response.json())

    # get an individual submission
    @sleep_and_retry
    @limits(calls=10, period=0.25)
    def getSubmissionBeta(self, submission_id):
        endpoint       = f'https://submittable-api.submittable.com/beta/submissions/{submission_id}'
        headers        = {'Content-type': 'application/json'}
        response       = requests.get(endpoint, auth=("", self.api_key), headers=headers)
        # print(response.json())
        if response.status_code != 200:
            print(f"get submission failed {response.status_code}. Response payload: {response.content}")
            raise ValueError(f"get submission failed {response.status_code}. Response payload: {response.content}")
        return SubmittableBetaSubmission(response.json())


    # get an list of submissions
    @sleep_and_retry
    @limits(calls=10, period=0.25)
    def getListOfSubmissions(self):
        submissions = []
        total_pages = 10
        for page in range(0, total_pages):
            if page == total_pages:
                break
            nextPage = page + 1
            endpoint = f'{self.baseURL}/submissions?page={nextPage}&pageSize=50'
            headers  = {'Content-type': 'application/json'}
            response = requests.get(endpoint, auth=("", self.api_key), headers=headers)
            if response.status_code != 200:
                raise ValueError(f"get submissions list failed {response.status_code}. Response payload: {response.content}")
            json_response    = response.json()
            total_pages      = response.json()["totalPages"]
            submissions_list = json_response["items"]
            for item in submissions_list:
                submissions.append(SubmittableSubmissionList(item))
        return submissions

    @sleep_and_retry
    @limits(calls=10, period=0.25)
    def getReferenceResponses(self):
        ref_responses = []
        total_pages   = 10
        for page in range(0, total_pages):
            if page == total_pages:
                break
            nextPage = page + 1
            endpoint = f'{self.baseURL}/responses/forms/{config.artist_collab_reference_form}?page={nextPage}&pageSize=50'
            headers = {'Content-type': 'application/json'}
            response = requests.get(endpoint, auth=("", self.api_key), headers=headers)
            print("ref form resp", response.json())
            if response.status_code != 200:
                raise ValueError(f"get reference responses list failed {response.status_code}. Response payload: {response.content}")
            json_response     = response.json()
            ref_response_list = json_response["items"]
            print(ref_response_list)
            total_pages       = response.json()["totalPages"]
            for item in ref_response_list:
                ref_responses.append(SubmittableResponseList(item))
        return ref_responses


class SubmittableResponseList:
    def __init__(self, payload):
        self.payload = payload

    def getFormFieldId(self):
        return self.payload["fieldId"]

    def getFormResponseId(self):
        return self.payload["formResponseId"]

    def getFormType(self):
        return self.payload["formType"]

    def getFormId(self):
        return self.payload["formId"]

    def getCreatedAt(self):
        return self.payload["createdAt"]

    def getRefEmail(self):
        return self.payload["refereeEmail"]

    def getFieldData(self):
        field_data = []
        for data in self.payload['fieldData']:
            field_data.append(SubmittableFieldData(data))
        return field_data


#
# json Response wrapper classes
#
class SubmittableFormRequestId:
    def __init__(self, payload):
        self.payload = payload

    def getRequestId(self):
        return self.payload["requestId"]


class SubmittableBetaResponseEntry:
    def __init__(self, payload):
        self.payload = payload

    def getEntry(self):
        # print("getEntry", self.payload)
        return self.payload["entry"]

    def getFieldData(self):
        entry = self.getEntry()
        field_data = []
        for data in entry['fieldData']:
            field_data.append(SubmittableFieldData(data))
        return field_data

    def getFormResponseId(self):
        payload = self.payload["entry"]
        # print(payload)
        return payload["formResponseId"]


class SubmittableBetaFieldData:

    def __init__(self, payload):
        self.payload = payload

    def getFormFieldId(self):
        return self.payload["formFieldId"]

    def getFieldType(self):
        return self.payload["fieldType"]


class SubmittableForm:
    def __init__(self, payload):
        self.payload = payload

    def getFormType(self):
        return self.payload["formType"]

    def getPrice(self):
        return self.payload["price"]

    def getPaymentDescription(self):
        return self.payload["paymentDescription"]

    def getEnablePayment(self):
        return self.payload["enablePayment"]

    def getCurrencyCode(self):
        return self.payload["currencyCode"]

    def getFormId(self):
        return self.payload["formId"]

    def getName(self):
        return self.payload["name"]

    def getFields(self):
        fields = []
        for field in self.payload["fields"]:
            fields.append(SubmittableFormField(field))
        return fields

    def getBranches(self):
        branches = []
        for branch in self.payload["branches"]:
            branches.append(SubmittableFormBranch(branch))
        return branches

    def getCreatedBy(self):
        return self.payload["createdBy"]

    def getCreatedAt(self):
        return self.payload["createdAt"]


class SubmittableFormBranch:

    def __init__(self, payload):
        self.payload = payload

    def formBranchId(self):
        return self.payload["formBranchId"]

    def getLabel(self):
        return self.payload["label"]

    def getColor(self):
        return self.payload["color"]


class SubmittableFormField:

    def __init__(self, payload):
        self.payload = payload

    def getFormFieldId(self):
        return self.payload["formFieldId"]

    def getFieldType(self):
        return self.payload["fieldType"]

    def getLabel(self):
        return self.payload["label"]

    def getMinValue(self):
        return self.payload["minValue"]

    def getMaxValue(self):
        return self.payload["maxValue"]

    def getFormat(self):
        return self.payload["format"]

    def getCurrency(self):
        return self.payload["currency"]

    def getDefaultCountry(self):
        return self.payload["defaultCountry"]

    def requireValidUSAddress(self):
        return self.payload["requireValidUSAddress"]

    def getReferenceFormId(self):
        return self.payload["referenceFormId"]

    def getOrgMessage(self):
        return self.payload["orgMessage"]

    def getShowOrgMessage(self):
        return self.payload["showOrgMessage"]

    def getCountLimit(self):
        return self.payload["countLimit"]

    def getCountType(self):
        return self.payload["countType"]

    def allowRichTextEditing(self):
        return self.payload["allowRichTextEditing"]

    def getAdditionalInstructions(self):
        return self.payload["additionalInstructions"]

    def isRequired(self):
        return self.payload["isRequired"]

    def isInternal(self):
        return self.payload["isInternal"]

    def isEditable(self):
        return self.payload["isEditable"]

    def getAutoLabel(self):
        return self.payload["autoLabel"]

    def isCustomAutoLabel(self):
        return self.payload["isCustomAutoLabel"]

    def getCustomAutoLabel(self):
        return self.payload["customAutoLabel"]

    def isBlind(self):
        return self.payload["isBlind"]

    def inline(self):
        return self.payload["inline"]

    def enableBranching(self):
        return self.payload["enableBranching"]

    def enablePayment(self):
        return self.payload["enablePayment"]

    def getPrice(self):
        return self.payload["price"]

    def getBranchId(self):
        return self.payload["branchId"]

    def getOptions(self):
        options = []
        for option in self.payload["options"]:
            options.append(SubmittableFormOption(option))
        return options

    def getFileTypes(self):
        return self.payload["fileTypes"]

    def getFileLimit(self):
        return self.payload["fileLimit"]

    def getMetadata(self):
        metadata = []
        for data in self.payload['metadata']:
            metadata.append(SubmittableMetadata(data))
        return metadata

    def getTableId(self):
        return self.payload["tableId"]

    def getTableIsReadonly(self):
        return self.payload["tableIsReadonly"]

    def getTableFileName(self):
        return self.payload["tableFileName"]

    def getTextBlock(self):
        return self.payload["textBlock"]

    def computeTableUrl(self):
        return self.payload["computeTableUrl"]

    def getDuplicateTableTemplateUrl(self):
        return self.payload["duplicateTableTemplateUrl"]

    def getCreateFileUrl(self):
        return self.payload["createFileUrl"]

    def getCreateLargeFileUrl(self):
        return self.payload["createLargeFileUrl"]

    def getShareFeedback(self):
        return self.payload["shareFeedback"]

    def getEligibleSubsections(self):
        return self.payload["eligibleSubsections"]

    def isEligibleValue(self):
        return self.payload["isEligibleValue"]

    def getSpecialValidation(self):
        return self.payload["specialValidation"]

    def hasRoutingNumber(self):
        return self.payload["hasRoutingNumber"]

    def hasAccountNumber(self):
        return self.payload["hasAccountNumber"]


class SubmittableFormOption:

    def __init__(self, payload):
        self.payload = payload

    def getFormOptionId(self):
        return self.payload["formOptionId"]

    def getLabel(self):
        return self.payload["label"]

    def getBranchId(self):
        return self.payload["branchId"]

    def getScore(self):
        return self.payload["score"]

    def getCustomAutoLabel(self):
        return self.payload["customAutoLabel"]

    def getPrice(self):
        return self.payload["price"]

    def isEligible(self):
        return self.payload["isEligible"]


class SubmittableTransaction:
    status_awarded    = "awarded"
    status_paid       = "paid"
    status_processing = "processing"

    def __init__(self, payload):
        self.payload = payload

    def getTransactionId(self):
        return self.payload["transactionId"]

    def getAmount(self):
        return self.payload["amount"]

    def getFundId(self):
        return self.payload["fundId"]

    def getStatus(self):
        return self.payload["status"]

    def getSubmissionId(self):
        return self.payload["submissionId"]

    def getCreatedAt(self):
        return self.payload["createdAt"]

    def getDescription(self):
        return self.payload["description"]

    def getAwardTransactionId(self):
        return self.payload["awardTransactionId"]


class SubmittableSubmissionList:

    def __init__(self, payload):
        self.payload = payload

    def getSubmissionId(self):
        return self.payload["submissionId"]

    def getProjectId(self):
        return self.payload["projectId"]

    def getSubmitterId(self):
        return self.payload["submitterId"]

    def getSumbissionIdList(self):
        submission_list = []
        for item in self.payload:
            submission_list.append(item['submissionId'])
        return submission_list

    def getSubmitterIdList(self):
        submitter_list = []
        items = self.payload['items']
        for item in items:
            submitter_list.append(item['submitterId'])
        return submitter_list

    def getLabelsIdList(self):
        labels = self.payload['labels']
        return labels


class SubmittableBetaSubmission:
    def __init__(self, payload):
        self.payload = payload

    def getFormType(self):
        return self.payload["formType"]

    def getSubmissionId(self):
        return self.payload["submissionId"]

    def getProjectId(self):
        return self.payload["projectId"]

    def getSubmitterId(self):
        return self.payload["submitterId"]

    def getFirstName(self):
        return self.payload["submitterFirstName"]

    def getLastName(self):
        return self.payload["submitterLastName"]

    def getEmail(self):
        return self.payload["submitterEmail"]

    def getSubmissionStatus(self):
        return self.payload["submissionStatus"]

    def getFormEntries(self):
        form_responses = []
        for response in self.payload["formEntries"]:
            form_responses.append(SubmittableBetaFormEntry(response))
        return form_responses


class SubmittableSubmission:

    def __init__(self, payload):
        self.payload = payload

    def getSubmitterEmail(self):
        return self.payload["submitterEmail"]

    def getSubmissionId(self):
        return self.payload["submissionId"]

    def getProjectId(self):
        return self.payload["projectId"]

    def getSubmitterId(self):
        return self.payload["submitterId"]

    def getFirstName(self):
        return self.payload["submitterFirstName"]

    def getLastName(self):
        return self.payload["submitterLastName"]

    def getEmail(self):
        return self.payload["submitterEmail"]

    def getPhone(self):
        return self.payload["submitterPhone"]

    def getSubmissionStatus(self):
        return self.payload["submissionStatus"]

    def isArchivedBySubmitter(self):
        return self.payload["isArchivedBySubmitter"]

    def isArchivedByOrganization(self):
        return self.payload["isArchivedByOrganization"]

    def isPaid(self):
        return self.payload["isPaid"]

    def getLabels(self):
        labels = []
        for label in self.payload["labels"]:
            labels.append(SubmittableLabel(label))
        return labels

    def getReviewStageId(self):
        return self.payload["reviewStageId"]

    def getFormResponses(self):
        form_responses = []
        for response in self.payload["formResponses"]:
            form_responses.append(SubmittableFormResponse(response))
        return form_responses

    def getFormResponse(self, form_id):
        for response in self.getFormResponses():
            if response.getFormId() == form_id:
                return response
        return None


class SubmittableBetaFormEntry:

    def __init__(self, payload):
        self.payload = payload

    def getFormType(self):
        return self.payload["formType"]

    def getEntry(self):
        # print(self.payload)
        return SubmittableBetaEntry(self.payload["entry"])


class SubmittableBetaEntry:

    def __init__(self, payload):
        self.payload = payload

    def getProjectId(self):
        return self.payload["projectId"]

    def getSubmissionId(self):
        return self.payload["formId"]

    def getFormId(self):
        return self.payload["formId"]

    def getEntryId(self):
        return self.payload["entryId"]

    def getStatus(self):
        return self.payload["status"]


class SubmittableFormResponse:

    def __init__(self, payload):
        self.payload = payload

    def getFormType(self):
        return self.payload["formType"]

    def getSubmissionId(self):
        return self.payload["submissionId"]

    def getProjectId(self):
        return self.payload["projectId"]

    def getFormResponseId(self):
        print("getFormResponseId", self.payload)
        return self.payload["formResponseId"]

    def getFormId(self):
        return self.payload["formId"]

    def getFieldData(self):
        print("get field data payload", self.payload)
        # field_data = self.payload["fieldData"]
        field_data = []
        for data in self.payload['fieldData']:
            field_data.append(SubmittableFieldData(data))
        return field_data

    def getFieldResponse(self, field_id):
        for data in self.getFieldData():
            if data.getFormFieldId() == field_id:
                return data
        return None

    def getCreatedBy(self):
        return self.payload["createdBy"]

    def getCreatedAt(self):
        return self.payload["createdAt"]

    def isCompleted(self):
        return self.payload["isCompleted"]

    def getCompletedAt(self):
        return self.payload["completedAt"]

    def isDeleted(self):
        return self.payload["isDeleted"]

    def getDeletedAt(self):
        return self.payload["deletedAt"]


class SubmittableFieldData:
    field_type_title = "TITLE"
    field_type_name = "NAME"
    field_type_address = "ADDRESS"
    field_type_short_answer = "SHORT_ANSWER"
    field_type_long_answer = "LONG_ANSWER"
    field_type_single_checkbox = "SINGLE_CHECKBOX"
    field_type_multiple_response = "MULTIPLE_RESPONSE"
    field_type_single_response = "SINGLE_RESPONSE"
    field_type_file_upload = "FILE_UPLOAD"
    field_type_table = "TABLE"
    field_type_number = "NUMBER"
    field_type_date = "DATE"
    field_type_email = "EMAIL"
    field_type_website = "WEBSITE"
    field_type_phone = "PHONE"
    field_type_cover_letter = "COVER_LETTER"
    field_type_text_only = "TEXT_ONLY"
    field_type_reference_form = "REFERENCE_FORM"
    field_type_divider = "DIVIDER"
    field_type_single_rating = "SINGLE_RATING"
    field_type_multiple_rating = "MULTIPLE_RATING"
    field_type_dropdown_rating = "DROPDOWN_RATING"
    field_type_charity_check = "CHARITY_CHECK"
    field_type_eligibility_charity_check = "ELIGIBILITY_CHARITY_CHECK"
    field_type_eligibility_single_checkbox = "ELIGIBILITY_SINGLE_CHECKBOX"
    field_type_eligibility_single_response = "ELIGIBILITY_SINGLE_RESPONSE"
    field_type_eligibility_dropdown_list = "ELIGIBILITY_DROPDOWN_LIST"
    field_type_bank_details = "BANK_DETAILS"

    def __init__(self, payload):
        self.payload = payload

    # overrides toString method
    def __str__(self):
        return str(self.payload)

    def getFieldType(self):
        return self.payload["fieldType"]

    def getRefEmail(self):
        print(self.payload)
        return self.payload['refereeEmail']

    def getFormFieldId(self):
        # print("getFormFieldId", self.payload)
        return self.payload["formFieldId"]

    def getValue(self):
        return self.payload["value"]

    def getFirstName(self):
        return self.payload["firstName"]

    def getLastName(self):
        return self.payload["lastName"]

    def getAddress1(self):
        return self.payload["address1"]

    def getAddress2(self):
        return self.payload["address2"]

    def getCity(self):
        return self.payload["city"]

    def getRegion(self):
        return self.payload["region"]

    def getPostalCode(self):
        return self.payload["postalCode"]

    def getCountry(self):
        return self.payload["country"]

    def getOptions(self):
        return self.payload["options"]

    def getFiles(self):
        files = []
        for file in self.payload["files"]:
            files.append(SubmittableFile(file))
        return files

    def getTable(self):
        return SubmittableTable(self.payload['table'])

    def getRefereeEmail(self):
        return self.payload["refereeEmail"]

    def getReferenceePersonalMessage(self):
        return self.payload["personalMessage"]

    def getRoutingNumber(self):
        return self.payload["routingNumber"]

    def getAccountNumber(self):
        return self.payload["accountNumber"]

    def getCharityCheckEIN(self):
        return self.payload["ein"]

    def getCharityCheckStatusCode(self):
        return self.payload["statusCode"]

    def getCharityCheckOrganizationName(self):
        return self.payload["organizationName"]

    def getCharityCheckAddress(self):
        return self.payload["address"]

    def getCharityCheckAddress2(self):
        return self.payload["address2"]

    def getCharityCheckCity(self):
        return self.payload["city"]

    def getCharityCheckState(self):
        return self.payload["state"]

    def getCharityCheckZip(self):
        return self.payload["zip"]

    def getCharityCheckOfacStatus(self):
        return self.payload["ofacStatus"]

    def getCharityCheckPub78Verified(self):
        return self.payload["pub78Verified"]

    def getCharityCheckIrsBmfPub78Conflict(self):
        return self.payload["irsBmfPub78Conflict"]

    def getCharityCheckMostRecentPub78(self):
        return self.payload["mostRecentPub78"]

    def getCharityCheckMostRecentIrb(self):
        return self.payload["mostRecentIrb"]

    def getCharityCheckSubsectionDescription(self):
        return self.payload["address2"]

    def getCharityCheckDeductibilityStatus(self):
        return self.payload["subsectionDescription"]

    def getCharityCheckFoundation509AStatus(self):
        return self.payload["foundation509AStatus"]

    def getCharityCheckMostRecentBmf(self):
        return self.payload["mostRecentBmf"]

    def getCharityCheckRulingYear(self):
        return self.payload["rulingYear"]

    def getCharityCheckRulingMonth(self):
        return self.payload["rulingMonth"]

    def getFieldValue(self, response_field_type):
        print("get field value")
        if response_field_type == "NAME":
            value = self.getLastName()
        elif response_field_type == "PHONE":
            value = self.getValue()
        elif response_field_type == "EMAIL":
            value = self.getValue()
        elif response_field_type == "BANK_DETAILS":
            value = {self.getAccountNumber(), self.getRoutingNumber()}
        elif response_field_type == "ADDRESS":
            value = self.getPostalCode()
        elif response_field_type == "DATE":
            value = self.getValue()
        elif response_field_type == "SHORT_ANSWER":
            # print('short answer', self.payload)
            value = self.getValue()
        print(value)
        return value


class SubmittableFile:

    def __init__(self, payload):
        self.payload = payload

    def getFileId(self):
        return self.payload["fileId"]

    def getFilename(self):
        return self.payload["fileName"]

    def getType(self):
        return self.payload["type"]

    def getDownloadUrl(self):
        return self.payload["getDownloadUrl"]

    def getThumbnailUrl(self):
        return self.payload["getThumbnailUrl"]

    def getConversionUrl(self):
        return self.payload["getConversionUrl"]

    def getBucket(self):
        return self.payload["bucket"]

    def getStorageKey(self):
        return self.payload["storageKey"]

    def getDuration(self):
        return self.payload["duration"]

    def getThumbnailInterval(self):
        return self.payload["thumbnailInterval"]

    def getConvertedBucketName(self):
        return self.payload["convertedBucketName"]

    def getConvertedStorageKey(self):
        return self.payload["convertedStorageKey"]

    def getFileSizeBytes(self):
        return self.payload["fileSizeBytes"]

    def getMetadata(self):
        metadata = []
        for data in self.payload["metadata"]:
            metadata.append(SubmittableMetadata(data))
        return metadata


class SubmittableMetadata:

    def __init__(self, payload):
        self.payload = payload

    def getFormMetadataId(self):
        return self.payload["formMetadataId"]

    def getValue(self):
        return self.payload["value"]


class SubmittableTable:

    def __init__(self, payload):
        self.payload = payload
        self.cells = None

    def getFileName(self):
        return self.payload["fileName"]

    def getDownloadUrl(self):
        return self.payload["getDownloadUrl"]

    def getConversionUrl(self):
        return self.payload["getConversionUrl"]

    def getCells(self):
        if self.cells:
            return self.cells

        self.cells = []
        for cell in self.payload["cells"]:
            self.cells.append(SubmittableTableCell(cell))

        return self.cells

    def getCell(self, row, col):
        for cell in self.getCells():
            if row == cell.getRow() and col == cell.getColumn():
                return cell
        return None


class SubmittableTableCell:

    def __init__(self, payload):
        self.payload = payload

    def getRow(self):
        return self.payload["r"]

    def getColumn(self):
        return self.payload["c"]

    def getValue(self):
        return self.payload["value"]


class SubmittableLabel:

    def __init__(self, payload):
        self.payload = payload

    def getLabelId(self):
        return self.payload["labelId"]

    def getName(self):
        return self.payload["name"]

    def getBackgroundColor(self):
        return self.payload["backgroundColor"]

    def getForegroundColor(self):
        return self.payload["foregroundColor"]


class SubmittablePaymentReceipt:

    def __init__(self, payload):
        self.payload = payload

    def getTotal(self):
        return self.payload["total"]

    def getPaymentLineItems(self):
        line_items = []
        for item in self.payload["paymentLines"]:
            line_items.append(SubmittablePaymentLine(item))
        return line_items


class SubmittablePaymentLine:

    def __init__(self, payload):
        self.payload = payload

    def isGrouping(self):
        return self.payload["isGrouping"]

    def getGroupings(self):
        return SubmittablePaymentLineGroup(self.payload["grouping"])

    def getLineItems(self):
        return SubmittablePaymentLineItem(self.payload["item"])


class SubmittablePaymentLineGroup:

    def __init__(self, payload):
        self.payload = payload

    def getDescription(self):
        return self.payload["description"]

    def getItems(self):
        items = []
        for item in self.payload["items"]:
            items.append(SubmittablePaymentLineItem(item))
        return items


class SubmittablePaymentLineItem:

    def __init__(self, payload):
        self.payload = payload

    def getDescription(self):
        return self.payload["description"]

    def getPrice(self):
        return self.payload["price"]

    def getPriceDisplay(self):
        return self.payload["priceDisplay"]

    def isSubmissionFee(self):
        return self.payload["isSubmissionFee"]