import datetime
import threading
import time

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
        self.api_key = config.submittable_token
        self.baseURL = "https://svcs.submittable.com/v3"
        self.event = threading.Event()

    @sleep_and_retry
    @limits(calls=10, period=1)
    def getLabelIds(self):
        # self.event.wait(0.1)
        page_size = 50
        label_ids = []
        total_pages = 1
        endpoint = f'{self.baseURL}/labels?pageSize={page_size}'
        headers = {'Content-type': 'application/json'}
        response = requests.get(endpoint, auth=("", self.api_key), headers=headers)
        if response.status_code != 200:
            logger.info(
                f"get reference responses list failed {response.status_code}. Response payload: {response.content}")
        else:
            total_pages = response.json()["totalPages"]
            # print("total pages:", total_pages)
        for page in range(0, total_pages):
            time.sleep(0.1)
            if page == total_pages:
                break
            nextPage = page + 1
            endpoint = f'{self.baseURL}/labels?page={nextPage}&pageSize={page_size}'
            response = requests.get(endpoint, auth=("", self.api_key), headers=headers)
            if response.status_code != 200:
                logger.info(f"get label ids failed {response.status_code}. Response payload: {response.content}")
            response_list = response.json()["items"]
            for item in response_list:
                label_ids.append(SubmittableLabel(item))
        return label_ids

    @sleep_and_retry
    @limits(calls=10, period=1)
    def deleteLabel(self, submissionId, labelId):
        self.event.wait(0.1)
        endpoint = f'{self.baseURL}/submissions/{submissionId}/labels/{labelId}'
        headers = {'Content-type': 'application/json'}
        response = requests.delete(endpoint, auth=("", self.api_key), headers=headers)
        if response.status_code != 204:
            logger.info(f"delete label failed {response.status_code}. Response payload: {response.content}")
            raise ValueError(f"delete label failed {response.status_code}. Response payload: {response.content}")
        return response

    @sleep_and_retry
    @limits(calls=10, period=1)
    def addLabel(self, submissionId, labelId):
        # self.event.wait(0.2)
        time.sleep(0.1)
        endpoint = f'{self.baseURL}/submissions/{submissionId}/labels/{labelId}'
        headers = {'Content-type': 'application/json'}
        response = requests.put(endpoint, auth=("", self.api_key), headers=headers)
        if response.status_code != 204:
            logger.info(f"add label failed {response.status_code}. Response payload: {response.content}")
            raise ValueError(f"add label failed {response.status_code}. Response payload: {response.content}")
        return response

    def createNewLabel(self, submission_id):
        # self.event.wait(0.1)
        endpoint = f'{self.baseURL}/labels'
        headers = {'Content-type': 'application/json'}
        payload = {'name': submission_id}
        payload = json.dumps(payload)
        response = requests.post(endpoint, auth=("", self.api_key), headers=headers, data=payload)
        if response.status_code != 201:
            logger.info(f"create new label failed {response.status_code}. Response payload: {response.content}")
            raise ValueError(f"create new label failed {response.status_code}. Response payload: {response.content}")
        return response.json()['labelId']

    @sleep_and_retry
    @limits(calls=10, period=1)
    def getEntry(self, entry_id):
        # self.event.wait(0.1)
        endpoint = f"https://submittable-api.submittable.com/beta/entries/{entry_id}"
        headers = {'Content-type': 'application/json'}
        response = requests.get(endpoint, auth=(":", self.api_key), headers=headers)
        # print(response.status_code)
        if response.status_code != 201:
            logger.info("get entry failed")
        return SubmittableBetaResponseEntry(response.json())

    @sleep_and_retry
    @limits(calls=10, period=1)
    def getInitialFormRequestId(self, subId):
        # self.event.wait(0.1)
        endpoint = f'{self.baseURL}/requests'
        headers = {'Content-type': 'application/json'}
        payload = {"formType": "initial",
                   "submissionId": subId}
        payload = json.dumps(payload)
        response = requests.post(endpoint, auth=(":", self.api_key), headers=headers, data=payload)
        if response.status_code != 201:
            logger.info("initial from request id failed")
        return SubmittableFormRequestId(response.json())

    def submitInternalFormResponse(self, submission_id, primary_unique_id,
                                   single_select_options_1,   single_select_options_2,    single_select_options_3,    single_select_options_4,
                                   single_select_options_5,   single_select_options_6,    single_select_options_7,    single_select_options_8,
                                   single_select_options_9,   single_select_options_10,   single_select_options_11,   single_select_options_12,
                                   single_select_options_13,  single_select_options_14,   single_select_options_15,   single_select_options_16,
                                   single_select_options_17,  single_select_options_18,   single_select_options_19,   single_select_options_20,
                                   single_select_options_21,  single_select_options_22,   single_select_options_23,   single_select_options_24,
                                   single_select_options_25,  single_select_options_26,   single_select_options_27,   single_select_options_28,
                                   single_select_options_29,  single_select_options_30,   single_select_options_31,   single_select_options_32,
                                   single_select_options_33,  single_select_options_34,   single_select_options_35,   single_select_options_36,
                                   single_select_options_37,  single_select_options_38,   single_select_options_39,   single_select_options_40,
                                   single_select_options_41,  single_select_options_42,   single_select_options_43,   single_select_options_44,
                                   single_select_options_45,  single_select_options_46,   single_select_options_47,   single_select_options_48,
                                   single_select_options_49,  single_select_options_50,   single_select_options_51,   single_select_options_52,
                                   single_select_options_53,  single_select_options_54,   single_select_options_55,   single_select_options_56,
                                   single_select_options_57,  single_select_options_58,   single_select_options_59,   single_select_options_60,
                                   single_select_options_61,  single_select_options_62,   single_select_options_63,   single_select_options_64,
                                   single_select_options_65,  single_select_options_66,   single_select_options_67,   single_select_options_68,
                                   single_select_options_69,  single_select_options_70,   single_select_options_71,   single_select_options_72,
                                   single_select_options_73,  single_select_options_74,   single_select_options_75,   single_select_options_76,
                                   single_select_options_77,  single_select_options_78,   single_select_options_79,   single_select_options_80,
                                   single_select_options_81,  single_select_options_82,   single_select_options_83,   single_select_options_84,
                                   single_select_options_85,  single_select_options_86,   single_select_options_87,   single_select_options_88,
                                   single_select_options_89,  single_select_options_90,   single_select_options_91,   single_select_options_92,
                                   single_select_options_93,  single_select_options_94,   single_select_options_95,   single_select_options_96,
                                   single_select_options_97,  single_select_options_98,   single_select_options_99,   single_select_options_100,
                                   single_select_options_101, single_select_options_102, single_select_options_103,   single_select_options_104,
                                   single_select_options_105, single_select_options_106, single_select_options_107,   single_select_options_108,
                                   single_select_options_109, single_select_options_110, single_select_options_111,   single_select_options_112,
                                   single_select_options_113, single_select_options_114, single_select_options_115,   single_select_options_116,
                                   single_select_options_117, single_select_options_118, single_select_options_119,   single_select_options_120,
                                   single_select_options_121, single_select_options_122, single_select_options_123,   single_select_options_124,
                                   single_select_options_125, single_select_options_126, single_select_options_127,   single_select_options_128,
                                   single_select_options_129, single_select_options_130, single_select_options_131,   single_select_options_132,
                                   single_select_options_133, single_select_options_134, single_select_options_135,   single_select_options_136,
                                   single_select_options_137, single_select_options_138, single_select_options_139,   single_select_options_140,
                                   single_select_options_141, single_select_options_142, single_select_options_143,   single_select_options_144,
                                   single_select_options_145, single_select_options_146, single_select_options_147,   single_select_options_148,
                                   single_select_options_149, single_select_options_150, single_select_options_151,   single_select_options_152,
                                   single_select_options_153, single_select_options_154, single_select_options_155,   single_select_options_156,
                                   single_select_options_157, single_select_options_158, single_select_options_159,   single_select_options_160,
                                   single_select_options_161, single_select_options_162, single_select_options_163,   single_select_options_164,
                                   single_select_options_165, single_select_options_166, single_select_options_167,   single_select_options_168,
                                   single_select_options_169, single_select_options_170, single_select_options_171,   single_select_options_172,
                                   single_select_options_173, single_select_options_174, single_select_options_175,   single_select_options_176,
                                   single_select_options_177, single_select_options_178, single_select_options_179,   single_select_options_180,
                                   single_select_options_181, single_select_options_182, single_select_options_183,   single_select_options_184,
                                   single_select_options_185, single_select_options_186, single_select_options_187,   single_select_options_188,
                                   single_select_options_189, single_select_options_190, single_select_options_191,   single_select_options_192,
                                   single_select_options_193, single_select_options_194, single_select_options_195,   single_select_options_196,
                                   single_select_options_197, single_select_options_198, single_select_options_199,   single_select_options_200,
                                   single_select_options_201, single_select_options_202, single_select_options_203,   single_select_options_204,
                                   single_select_options_205, single_select_options_206, single_select_options_207,   single_select_options_208,
                                   single_select_options_209, single_select_options_210, single_select_options_211,   single_select_options_212,
                                   single_select_options_213, single_select_options_214, single_select_options_215,   single_select_options_216,
                                   single_select_options_217, single_select_options_218, single_select_options_219,   single_select_options_220,
                                   single_select_options_221, single_select_options_222, single_select_options_223,   single_select_options_224,
                                   single_select_options_225, single_select_options_226, single_select_options_227,   single_select_options_228,
                                   single_select_options_229, single_select_options_230, single_select_options_231,   single_select_options_232,
                                   single_select_options_233, single_select_options_234, single_select_options_235,   single_select_options_236,
                                   single_select_options_237, single_select_options_238, single_select_options_239,   single_select_options_240,
                                   single_select_options_241, single_select_options_242, single_select_options_243,   single_select_options_244,
                                   single_select_options_245, single_select_options_246, single_select_options_247,   single_select_options_248,
                                   single_select_options_249, single_select_options_250, collab_unique_id_1=None,     collab_unique_id_2=None,
                                   collab_unique_id_3=None,   collab_unique_id_4=None,   collab_unique_id_5=None,     collab_unique_id_6=None,
                                   collab_unique_id_7=None,   collab_unique_id_8=None,   collab_unique_id_9=None):
        time.sleep(0.1)
        endpoint = f'https://submittable-api.submittable.com/beta/entries/internal'
        headers = {'Content-type': 'application/json'}
        payload = {"submissionId": submission_id,
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
                       },
                       {
                           "options": single_select_options_1,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_1
                       },
                       {
                           "options": single_select_options_2,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_2
                       },
                       {
                           "options": single_select_options_3,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_3
                       },
                       {
                           "options": single_select_options_4,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_4
                       },
                       {
                           "options": single_select_options_5,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_5
                       },
                       {
                           "options": single_select_options_6,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_6
                       },
                       {
                           "options": single_select_options_7,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_7
                       },
                       {
                           "options": single_select_options_8,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_8
                       },
                       {
                           "options": single_select_options_9,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_9
                       },
                       {
                           "options": single_select_options_10,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_10
                       },
                       {
                           "options": single_select_options_11,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_11
                       },
                       {
                           "options": single_select_options_12,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_12
                       },
                       {
                           "options": single_select_options_13,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_13
                       },
                       {
                           "options": single_select_options_14,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_14
                       },
                       {
                           "options": single_select_options_15,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_15
                       },
                       {
                           "options": single_select_options_16,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_16
                       },
                       {
                           "options": single_select_options_17,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_17
                       },
                       {
                           "options": single_select_options_18,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_18
                       },
                       {
                           "options": single_select_options_19,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_19
                       },
                       {
                           "options": single_select_options_20,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_20
                       },
                       {
                           "options": single_select_options_21,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_21
                       },
                       {
                           "options": single_select_options_22,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_22
                       },
                       {
                           "options": single_select_options_23,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_23
                       },
                       {
                           "options": single_select_options_24,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_24
                       },
                       {
                           "options": single_select_options_25,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_25
                       },
                       {
                           "options": single_select_options_26,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_26
                       },
                       {
                           "options": single_select_options_27,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_27
                       },
                       {
                           "options": single_select_options_28,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_28
                       },
                       {
                           "options": single_select_options_29,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_29
                       },
                       {
                           "options": single_select_options_30,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_30
                       },
                       {
                           "options": single_select_options_31,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_31
                       },
                       {
                           "options": single_select_options_32,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_32
                       },
                       {
                           "options": single_select_options_33,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_33
                       },
                       {
                           "options": single_select_options_34,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_34
                       },
                       {
                           "options": single_select_options_35,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_35
                       },
                       {
                           "options": single_select_options_36,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_36
                       },
                       {
                           "options": single_select_options_37,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_37
                       },
                       {
                           "options": single_select_options_38,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_38
                       },
                       {
                           "options": single_select_options_39,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_39
                       },
                       {
                           "options": single_select_options_40,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_40
                       },
                       {
                           "options": single_select_options_41,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_41
                       },
                       {
                           "options": single_select_options_42,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_42
                       },
                       {
                           "options": single_select_options_43,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_43
                       },
                       {
                           "options": single_select_options_44,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_44
                       },
                       {
                           "options": single_select_options_45,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_45
                       },
                       {
                           "options": single_select_options_46,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_46
                       },
                       {
                           "options": single_select_options_47,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_47
                       },
                       {
                           "options": single_select_options_48,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_48
                       },
                       {
                           "options": single_select_options_49,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_49
                       },
                       {
                           "options": single_select_options_50,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_50
                       },
                       {
                           "options": single_select_options_51,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_51
                       },
                       {
                           "options": single_select_options_52,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_52
                       },
                       {
                           "options": single_select_options_53,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_53
                       },
                       {
                           "options": single_select_options_54,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_54
                       },
                       {
                           "options": single_select_options_55,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_55
                       },
                       {
                           "options": single_select_options_56,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_56
                       },
                       {
                           "options": single_select_options_57,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_57
                       },
                       {
                           "options": single_select_options_58,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_58
                       },
                       {
                           "options": single_select_options_59,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_59
                       },
                       {
                           "options": single_select_options_60,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_60
                       },
                       {
                           "options": single_select_options_61,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_61
                       },
                       {
                           "options": single_select_options_62,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_62
                       },
                       {
                           "options": single_select_options_63,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_63
                       },
                       {
                           "options": single_select_options_64,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_64
                       },
                       {
                           "options": single_select_options_65,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_65
                       },
                       {
                           "options": single_select_options_66,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_66
                       },
                       {
                           "options": single_select_options_67,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_67
                       },
                       {
                           "options": single_select_options_68,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_68
                       },
                       {
                           "options": single_select_options_69,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_69
                       },
                       {
                           "options": single_select_options_70,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_70
                       },
                       {
                           "options": single_select_options_71,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_71
                       },
                       {
                           "options": single_select_options_72,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_72
                       },
                       {
                           "options": single_select_options_73,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_73
                       },
                       {
                           "options": single_select_options_74,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_74
                       },
                       {
                           "options": single_select_options_75,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_75
                       },
                       {
                           "options": single_select_options_76,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_76
                       },
                       {
                           "options": single_select_options_77,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_77
                       },
                       {
                           "options": single_select_options_78,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_78
                       },
                       {
                           "options": single_select_options_79,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_79
                       },
                       {
                           "options": single_select_options_80,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_80
                       },
                       {
                           "options": single_select_options_81,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_81
                       },
                       {
                           "options": single_select_options_82,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_82
                       },
                       {
                           "options": single_select_options_83,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_83
                       },
                       {
                           "options": single_select_options_84,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_84
                       },
                       {
                           "options": single_select_options_85,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_85
                       },
                       {
                           "options": single_select_options_86,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_86
                       },
                       {
                           "options": single_select_options_87,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_87
                       },
                       {
                           "options": single_select_options_88,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_88
                       },
                       {
                           "options": single_select_options_89,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_89
                       },
                       {
                           "options": single_select_options_90,
                           "fieldType": "single_response",
                           "formFieldId": config.ineligible_single_select_id_90
                       },
                       {
                           "options": single_select_options_91,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_1
                       },
                       {
                           "options": single_select_options_92,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_2
                       },
                       {
                           "options": single_select_options_93,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_3
                       },
                       {
                           "options": single_select_options_94,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_4
                       },
                       {
                           "options": single_select_options_95,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_5
                       },
                       {
                           "options": single_select_options_96,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_6
                       },
                       {
                           "options": single_select_options_97,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_7
                       },
                       {
                           "options": single_select_options_98,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_8
                       },
                       {
                           "options": single_select_options_99,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_9
                       },
                       {
                           "options": single_select_options_100,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_10
                       },
                       {
                           "options": single_select_options_101,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_11
                       },
                       {
                           "options": single_select_options_102,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_12
                       },
                       {
                           "options": single_select_options_103,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_13
                       },
                       {
                           "options": single_select_options_104,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_14
                       },
                       {
                           "options": single_select_options_105,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_15
                       },
                       {
                           "options": single_select_options_106,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_16
                       },
                       {
                           "options": single_select_options_107,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_17
                       },
                       {
                           "options": single_select_options_108,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_18
                       },
                       {
                           "options": single_select_options_109,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_19
                       },
                       {
                           "options": single_select_options_110,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_20
                       },
                       {
                           "options": single_select_options_111,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_21
                       },
                       {
                           "options": single_select_options_112,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_22
                       },
                       {
                           "options": single_select_options_113,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_23
                       },
                       {
                           "options": single_select_options_114,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_24
                       },
                       {
                           "options": single_select_options_115,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_25
                       },
                       {
                           "options": single_select_options_116,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_26
                       },
                       {
                           "options": single_select_options_117,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_27
                       },
                       {
                           "options": single_select_options_118,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_28
                       },
                       {
                           "options": single_select_options_119,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_29
                       },
                       {
                           "options": single_select_options_120,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_30
                       },
                       {
                           "options": single_select_options_121,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_31
                       },
                       {
                           "options": single_select_options_122,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_32
                       },
                       {
                           "options": single_select_options_123,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_33
                       },
                       {
                           "options": single_select_options_124,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_34
                       },
                       {
                           "options": single_select_options_125,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_35
                       },
                       {
                           "options": single_select_options_126,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_36
                       },
                       {
                           "options": single_select_options_127,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_37
                       },
                       {
                           "options": single_select_options_128,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_38
                       },
                       {
                           "options": single_select_options_129,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_39
                       },
                       {
                           "options": single_select_options_130,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_40
                       },
                       {
                           "options": single_select_options_131,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_41
                       },
                       {
                           "options": single_select_options_132,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_42
                       },
                       {
                           "options": single_select_options_133,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_43
                       },
                       {
                           "options": single_select_options_134,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_44
                       },
                       {
                           "options": single_select_options_135,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_45
                       },
                       {
                           "options": single_select_options_136,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_46
                       },
                       {
                           "options": single_select_options_137,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_47
                       },
                       {
                           "options": single_select_options_138,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_48
                       },
                       {
                           "options": single_select_options_139,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_49
                       },
                       {
                           "options": single_select_options_140,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_50
                       },
                       {
                           "options": single_select_options_141,
                           "fieldType": "single_response",
                           "formFieldId": config.aep_single_select_id_51
                       },
                       {
                           "options": single_select_options_142,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_1
                       },
                       {
                           "options": single_select_options_143,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_2
                       },
                       {
                           "options": single_select_options_144,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_3
                       },
                       {
                           "options": single_select_options_145,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_4
                       },
                       {
                           "options": single_select_options_146,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_5
                       },
                       {
                           "options": single_select_options_147,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_6
                       },
                       {
                           "options": single_select_options_148,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_7
                       },
                       {
                           "options": single_select_options_149,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_8
                       },
                       {
                           "options": single_select_options_150,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_9
                       },
                       {
                           "options": single_select_options_151,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_10
                       },
                       {
                           "options": single_select_options_152,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_11
                       },
                       {
                           "options": single_select_options_153,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_12
                       },
                       {
                           "options": single_select_options_154,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_13
                       },
                       {
                           "options": single_select_options_155,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_14
                       },
                       {
                           "options": single_select_options_156,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_15
                       },
                       {
                           "options": single_select_options_157,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_16
                       },
                       {
                           "options": single_select_options_158,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_17
                       },
                       {
                           "options": single_select_options_159,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_18
                       },
                       {
                           "options": single_select_options_160,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_19
                       },
                       {
                           "options": single_select_options_161,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_20
                       },
                       {
                           "options": single_select_options_162,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_21
                       },
                       {
                           "options": single_select_options_163,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_22
                       },
                       {
                           "options": single_select_options_164,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_23
                       },
                       {
                           "options": single_select_options_165,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_24
                       },
                       {
                           "options": single_select_options_166,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_25
                       },
                       {
                           "options": single_select_options_167,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_26
                       },
                       {
                           "options": single_select_options_168,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_27
                       },
                       {
                           "options": single_select_options_169,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_28
                       },
                       {
                           "options": single_select_options_170,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_29
                       },
                       {
                           "options": single_select_options_171,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_30
                       },
                       {
                           "options": single_select_options_172,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_31
                       },
                       {
                           "options": single_select_options_173,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_32
                       },
                       {
                           "options": single_select_options_174,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_33
                       },
                       {
                           "options": single_select_options_175,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_34
                       },
                       {
                           "options": single_select_options_176,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_35
                       },
                       {
                           "options": single_select_options_177,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_36
                       },
                       {
                           "options": single_select_options_178,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_37
                       },
                       {
                           "options": single_select_options_179,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_38
                       },
                       {
                           "options": single_select_options_180,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_39
                       },
                       {
                           "options": single_select_options_181,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_40
                       },
                       {
                           "options": single_select_options_182,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_41
                       },
                       {
                           "options": single_select_options_183,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_42
                       },
                       {
                           "options": single_select_options_184,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_43
                       },
                       {
                           "options": single_select_options_185,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_44
                       },
                       {
                           "options": single_select_options_186,
                           "fieldType": "single_response",
                           "formFieldId": config.gi_single_select_id_45
                       },
                       {
                           "options": single_select_options_187,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_1
                       },
                       {
                           "options": single_select_options_188,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_2
                       },
                       {
                           "options": single_select_options_189,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_3
                       },
                       {
                           "options": single_select_options_190,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_4
                       },
                       {
                           "options": single_select_options_191,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_5
                       },
                       {
                           "options": single_select_options_192,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_6
                       },
                       {
                           "options": single_select_options_193,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_7
                       },
                       {
                           "options": single_select_options_194,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_8
                       },
                       {
                           "options": single_select_options_195,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_9
                       },
                       {
                           "options": single_select_options_196,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_10
                       },
                       {
                           "options": single_select_options_197,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_11
                       },
                       {
                           "options": single_select_options_198,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_12
                       },
                       {
                           "options": single_select_options_199,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_13
                       },
                       {
                           "options": single_select_options_200,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_14
                       },
                       {
                           "options": single_select_options_201,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_15
                       },
                       {
                           "options": single_select_options_202,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_16
                       },
                       {
                           "options": single_select_options_203,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_17
                       },
                       {
                           "options": single_select_options_204,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_18
                       },
                       {
                           "options": single_select_options_205,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_19
                       },
                       {
                           "options": single_select_options_206,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_20
                       },
                       {
                           "options": single_select_options_207,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_21
                       },
                       {
                           "options": single_select_options_208,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_22
                       },
                       {
                           "options": single_select_options_209,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_23
                       },
                       {
                           "options": single_select_options_210,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_24
                       },
                       {
                           "options": single_select_options_211,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_25
                       },
                       {
                           "options": single_select_options_212,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_26
                       },
                       {
                           "options": single_select_options_213,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_27
                       },
                       {
                           "options": single_select_options_214,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_28
                       },
                       {
                           "options": single_select_options_215,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_29
                       },
                       {
                           "options": single_select_options_216,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_30
                       },
                       {
                           "options": single_select_options_217,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_31
                       },
                       {
                           "options": single_select_options_218,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_32
                       },
                       {
                           "options": single_select_options_219,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_33
                       },
                       {
                           "options": single_select_options_220,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_34
                       },
                       {
                           "options": single_select_options_221,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_35
                       },
                       {
                           "options": single_select_options_222,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_36
                       },
                       {
                           "options": single_select_options_223,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_37
                       },
                       {
                           "options": single_select_options_224,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_38
                       },
                       {
                           "options": single_select_options_225,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_39
                       },
                       {
                           "options": single_select_options_226,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_40
                       },
                       {
                           "options": single_select_options_227,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_41
                       },
                       {
                           "options": single_select_options_228,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_42
                       },
                       {
                           "options": single_select_options_229,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_43
                       },
                       {
                           "options": single_select_options_230,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_44
                       },
                       {
                           "options": single_select_options_231,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_45
                       },
                       {
                           "options": single_select_options_232,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_46
                       },
                       {
                           "options": single_select_options_233,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_47
                       },
                       {
                           "options": single_select_options_234,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_48
                       },
                       {
                           "options": single_select_options_235,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_49
                       },
                       {
                           "options": single_select_options_236,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_50
                       },
                       {
                           "options": single_select_options_237,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_51
                       },
                       {
                           "options": single_select_options_238,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_52
                       },
                       {
                           "options": single_select_options_239,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_53
                       },
                       {
                           "options": single_select_options_240,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_54
                       },
                       {
                           "options": single_select_options_241,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_55
                       },
                       {
                           "options": single_select_options_242,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_56
                       },
                       {
                           "options": single_select_options_243,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_57
                       },
                       {
                           "options": single_select_options_244,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_58
                       },
                       {
                           "options": single_select_options_245,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_59
                       },
                       {
                           "options": single_select_options_246,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_60
                       },
                       {
                           "options": single_select_options_247,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_61
                       },
                       {
                           "options": single_select_options_248,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_62
                       },
                       {
                           "options": single_select_options_249,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_63
                       },
                       {
                           "options": single_select_options_250,
                           "fieldType": "single_response",
                           "formFieldId": config.app_single_select_id_64
                       }
                   ]
                   }
        payload = json.dumps(payload)
        response = requests.post(endpoint, auth=("", self.api_key), headers=headers, data=payload)
        print("response:", response)
        if response.status_code != 201:
            logger.info(
                f"submit internal form response failed {response.status_code}. Response payload: {response.content}. \nRequest payload: {str(payload)}")
            raise ValueError(
                f"submit internal from response failed {response.status_code}. Response payload: {response.content}. \nRequest payload: {str(payload)}")
        return response.json()["entryId"]

    # get an individual submission
    @sleep_and_retry
    @limits(calls=10, period=1)
    def getSubmission(self, submission_id):
        # self.event.wait(0.2)
        time.sleep(0.1)
        endpoint = f'{self.baseURL}/submissions/{submission_id}'
        headers = {'Content-type': 'application/json'}
        response = requests.get(endpoint, auth=("", self.api_key), headers=headers)
        # print("get sub", response.json())
        if response.status_code != 200:
            if response.status_code == 429:
                print("api rate limit hit wait 15 mins")
                # self.event.wait(900)
                time.sleep(900)
                # call to get submission again
                self.getSubmission(submission_id)
            else:
                logger.info(f"get submission failed {response.status_code}. Response payload: {response.content}")
                raise ValueError(f"get submission failed {response.status_code}. Response payload: {response.content}")
        return SubmittableSubmission(response.json())

    # get an individual submission
    @sleep_and_retry
    @limits(calls=10, period=1)
    def getSubmissionBeta(self, submission_id):
        # self.event.wait(0.1)
        endpoint = f'https://submittable-api.submittable.com/beta/submissions/{submission_id}'
        headers = {'Content-type': 'application/json'}
        response = requests.get(endpoint, auth=("", self.api_key), headers=headers)
        # print(response.json())
        if response.status_code != 200:
            logger.info(f"get submission failed {response.status_code}. Response payload: {response.content}")
            raise ValueError(f"get submission failed {response.status_code}. Response payload: {response.content}")
        return SubmittableBetaSubmission(response.json())

    # get an list of submissions
    @sleep_and_retry
    @limits(calls=10, period=1)
    def getListOfSubmissions(self):
        # self.event.wait(0.1)
        submissions = []
        page_size = 50
        total_pages = 1
        endpoint = f'{self.baseURL}/submissions?projects.include={config.project_id_1}&projects.include={config.project_id_2}&statuses.include=new&statuses.include=in_progress&pageSize={page_size}'
        headers = {'Content-type': 'application/json'}
        response = requests.get(endpoint, auth=("", self.api_key), headers=headers)
        if response.status_code != 200:
            raise ValueError(
                f"get submissions list failed {response.status_code}. Response payload: {response.content}")
        else:
            total_pages = response.json()["totalPages"]
            print("total pages:", total_pages)
        for page in range(0, total_pages):
            # self.event.wait(0.1)
            if page == total_pages:
                break
            nextPage = page + 1
            endpoint = f'{self.baseURL}/submissions?projects.include={config.project_id_1}&projects.include={config.project_id_2}&statuses.include=new&statuses.include=in_progress&page={nextPage}&pageSize={page_size}'
            headers = {'Content-type': 'application/json'}
            response = requests.get(endpoint, auth=("", self.api_key), headers=headers)
            if response.status_code != 200:
                logger.info(
                    f"get submissions list failed {response.status_code}. Response payload: {response.content}, skip item")
                # skip over do not add to list
                continue
            json_response = response.json()
            submissions_list = json_response["items"]
            # total_pages    = response.json()["totalPages"]
            print("page:", page)
            for item in submissions_list:
                submissions.append(SubmittableSubmissionList(item))
        return submissions

    @sleep_and_retry
    @limits(calls=10, period=1)
    def getReferenceResponses(self):
        ref_responses = []
        page_size = 1
        total_pages = 1
        endpoint = f'{self.baseURL}/responses/forms/{config.artist_reference_form_id}?page=300&pageSize={page_size}'
        headers = {'Content-type': 'application/json'}
        response = requests.get(endpoint, auth=("", self.api_key), headers=headers)
        if response.status_code != 200:
            logger.info(
                f"get reference responses list failed {response.status_code}. Response payload: {response.content}, skip item 1")
        else:
            total_pages = response.json()["totalPages"]
            print("get ref form total pages:", total_pages)
        for page in range(0, total_pages):
            # self.event.wait(0.1)
            if page == total_pages:
                break
            nextPage = page + 1
            endpoint = f'{self.baseURL}/responses/forms/{config.artist_reference_form_id}?page={nextPage}&pageSize={page_size}'
            headers = {'Content-type': 'application/json'}
            response = requests.get(endpoint, auth=("", self.api_key), headers=headers)
            # print("ref form resp", response.json())
            if response.status_code != 200:
                logger.info(
                    f"get reference responses list failed {response.status_code}. Response payload: {response.content}, skip item 2")
                # skip over go to next response
                continue
            json_response = response.json()
            ref_response_list = json_response["items"]
            # total_pages     = response.json()["totalPages"]
            print("page:", page)
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
        return self.payload["entry"]

    def getFieldData(self):
        entry = self.getEntry()
        field_data = []
        for data in entry['fieldData']:
            field_data.append(SubmittableFieldData(data))
        return field_data

    def getFormResponseId(self):
        payload = self.payload["entry"]
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
    status_awarded = "awarded"
    status_paid = "paid"
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
        return self.payload["formResponseId"]

    def getFormId(self):
        return self.payload["formId"]

    def getFieldData(self):
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
        return self.payload['refereeEmail']

    def getFormFieldId(self):
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
            value = self.getValue()
        # print("get field value", value)
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
