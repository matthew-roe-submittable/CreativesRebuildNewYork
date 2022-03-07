import mysql.connector

import data_struct

mysql_user  = "admin"
mysql_pass  = "adminadmin"
mysql_host  = "jesse-test.co76wjzk8jn7.us-east-2.rds.amazonaws.com"
mysql_db    = "test"

mysql_conn = mysql.connector.connect(user=mysql_user,
                                     password=mysql_pass,
                                     host=mysql_host,
                                     database=mysql_db)

# ------------------------------ LIVE ACCOUNT SETTINGS ------------------------------ #
# live account API key
submittable_token = "5379d0ca57f64c1f827f3d0a0b476554"

# Project: AEP
project_id_1                = "f5b5299e-149b-40fe-9764-f41fa3c57330"
# Initial form
project_1_formId            = "17b94926-61e9-4ec6-95be-df32c0176ea6"

# Initial Form Artist UID fields
project_1_artist_last_name  = "edfb62ed-9f31-49d6-bcf6-dce8ec0589b6"
project_1_artist_zipcode    = "254429d2-640b-4c8b-9839-73c3e5ba12a7"
project_1_artist_dob        = "a3c4efb3-c45b-4efc-bee5-6b5c94ed2592"

# Collaboratives Artist Reference
org_reference_form_id    = "8990f98a-7f90-49e8-819e-ef100781e11c"
artist_reference_form_id = "a5a47e3e-1aae-4eee-808f-d580aa38fb21"

# Initial Field ID of the reference form - can have up to 9 additional artists
reference_form_field_id_1    = "2f5df106-e782-422b-9c39-a3345788b715"
reference_form_field_id_2    = "da35f4fc-3219-4731-91ed-3e5a46ddc4ef"
reference_form_field_id_3    = "605e57c4-5488-4a75-a7ed-ad6399ee2085"
reference_form_field_id_4    = "eed9b6d8-119d-41e2-8763-6054b56a145c"
reference_form_field_id_5    = "99047e07-340b-4872-9f7e-3f9f08e29592"
reference_form_field_id_6    = "68900200-361f-416c-8fb4-4a5de1a92f89"
reference_form_field_id_7    = "53497706-6517-439c-83fd-430df1b8efac"
reference_form_field_id_8    = "6290ab16-2344-4fcd-b794-bedc3b576903"
reference_form_field_id_9    = "12b3eda5-25e6-45d8-bbee-4a8a37118ad9"

reference_form_name_id       = "2434c406-1ea5-48e0-935a-51e65f7c179b"
reference_form_dob_id        = "186190bc-113d-4490-a751-218314bdba29"
reference_form_zipcode_id    = "0e846040-cf76-4609-a107-be4b911ab18e"

# Project: GI
project_id_2                 = "a29ca1b8-2121-446e-aa93-e6739e77f09c"
project_2_formId             = "00df1db3-ae6c-446b-aaa0-7dea64388643"
project_2_name_field_id      = "582e9043-8977-447b-a569-cbc2e5df12ed"
project_2_dob_field_id       = "b5e07e17-8d0b-4705-9628-ba35de352804"
project_2_zipcode_field_id   = "d533967d-d72b-4266-a502-577b6ae6db81"

# internal form
internal_form_id            = "f2911a5d-1293-4f84-85b2-63ec0a1e6282"
# Primary Artist
internal_form_field_id_1    = "77667d07-9c56-461b-9e80-243b806a4882"
# Collaborators Artist
internal_form_field_id_2    = "1a97b9d8-a8ef-4270-b378-5c82a6d7b75c"
internal_form_field_id_3    = "f4d45c72-5f00-4358-bd8e-02d19710c442"
internal_form_field_id_4    = "bc6a7400-b138-499c-b6f8-fb4b5082e08c"
internal_form_field_id_5    = "9f37e441-cf00-458d-857a-a9bd22bc6b57"
internal_form_field_id_6    = "c13061e4-f3b9-4cee-96c8-981b3c6a4976"
internal_form_field_id_7    = "f386b80b-9842-4746-800e-86fa6d3d2dda"
internal_form_field_id_8    = "e6105f2a-3041-44a5-b0f2-42261a42436a"
internal_form_field_id_9    = "a402fa0e-e106-4630-aac8-9550b262db0b"
internal_form_field_id_10   = "9a02a624-26e2-4f8a-84fb-222f710b1079"

# label "Pending Duplicate"
label_id_1 = "320527"
# label "Not Awarded Duplicate"
label_id_2 = ""
# label "Pending Duplicate"
label_id_3 = ""

# multi select initial form IDs
first_multi_select_id  = "d04f1e3e-169e-4bd4-8d13-0f9a36007dc4"
second_multi_select_id = "028936dd-a753-4201-909c-38e4f6122c1a"
third_multi_select_id  = "94f117db-9536-4892-ab88-e8d4d60babe9"
fourth_multi_select_id = "cad583dc-a922-4746-8db5-1ad7559a5dbf"

# multi select option IDs
first_multi_options_ids  = ["6a782b6b-fa61-433e-9a8b-cf0a1f88ade1",
                            "14757995-2ce5-4902-9de6-70da31cc78d0",
                            "b4a7a3e7-a15b-4cd8-b781-3b70be1f95b5",
                            "a3092d24-5493-443a-9950-d4c860dacea9",
                            "9dcea11d-1829-4ba6-b27c-9224ca856236",
                            "7eed346b-2900-424c-901a-cd1797b66cb6"]

second_multi_options_ids = ["4330a73a-1ae9-4fa7-8e97-99b66d23ac92"]
third_multi_options_ids  = ["b00c64b9-5291-4f78-a1ae-10a498e5d566"]
fourth_multi_options_ids = ["89cf1db1-08ff-4496-84e8-75ba3fbedbbf"]

# single select internal form IDs
first_single_select_id  = ""
second_single_select_id = ""
third_single_select_id  = ""
fourth_single_select_id = ""

'''
# ------------------------------ DEMO ACCOUNT SETTINGS ------------------------------ #
# demo account
# submittable_token           = "700b04eccae244679785a0e8f13c786e"
# Demo Account
# Project: AEP demo project
project_id_1                = "1903ba4a-2cd2-4b55-9caa-b2ec58237955"
project_1_formId            = "f2ee04a8-8238-401d-863f-8783305b9897"
project_1_artist_last_name  = "9097486a-79ad-4b50-935d-8008f12b6cf1"
project_1_artist_dob        = "7cb13021-332e-4278-a98b-4a69ca96ec45"
project_1_artist_zipcode    = "2d27064a-a57a-4f2e-847e-dee5f5876a43"
# Reference form to hold up to 9 UID per submission
artist_collab_reference_form = "ad9a40c6-4152-4d21-a16c-9a885b1f2a41"
# Form field id of the reference form in the internal form
org_reference_form_field_id = "6d3bf23a-df28-4eca-b1fe-ff8504cd6a4a"
# collaborative artist 2-10
reference_form_field_id_1   = "7a96a260-af5f-4c43-b28c-b53ecf0f0080"
reference_form_field_id_2   = "b2aa5c71-e99a-4067-a3ea-2d70b442a286"
reference_form_field_id_3   = "9fe11e07-2caf-4e46-8634-f982c8e02dc2"
reference_form_field_id_4   = "d1905211-47ea-4095-9e7d-78c08337d5bc"
reference_form_field_id_5   = "aeba1ce6-ae4f-4095-9679-c366185b3f97"
reference_form_field_id_6   = "eb5ed7be-9954-400a-b891-4ad48fa98fc3"
reference_form_field_id_7   = "97ccc2c5-050e-4959-b2e5-add05ed27366"
reference_form_field_id_8   = "438071ae-e69d-4604-adc6-669d221fe844"
reference_form_field_id_9   = "bb7d5454-d7c5-4e40-9699-900d4eca770c"
# ref form fields
reference_form_name_id      = "0182623d-9114-4304-95ed-b2f9abd0ee6b"
reference_form_dob_id       = "a6c73923-316c-4e50-8b5a-379bc9225111"
reference_form_zipcode_id   = "a0936d07-ecc6-4031-ba5a-fc7da24f0526"
# Project: GI demo project
project_id_2                 = "cc425384-5ee6-4063-8642-3155383a6bd1"
project_2_formId             = "167be692-282c-46c4-baa7-0e8645fdfd89"
project_2_name_field_id      = "83f4d296-5aaf-428d-be76-905b240be153"
project_2_dob_field_id       = "3af16b68-d0a8-4dff-9bdb-dbb6bcae5b70"
project_2_zipcode_field_id   = "b18620bf-ba42-4293-879a-e27286a376df"
# internal form to hold up to 10 UID per submission
internal_form_id             = "d051aa12-614b-4f30-a9eb-db9f934a317a"
# 10 UID fields
internal_form_field_id_1     = "b8f1e240-3b57-4c05-8acb-566c79ac5d95"
internal_form_field_id_2     = "3357efb7-9412-42f0-9109-ddb3b1decff7"
internal_form_field_id_3     = "7743d945-b7bd-40c1-bcff-85669fce886f"
internal_form_field_id_4     = "d339ff5b-f35c-4e1c-8cc3-8868a5fc99d6"
internal_form_field_id_5     = "29dbacf9-01f0-4213-92bc-b4ea018bcae5"
internal_form_field_id_6     = "a66b68f9-448c-4e8a-8521-5c824aea10e1"
internal_form_field_id_7     = "59a845ff-83ab-4ffd-a204-d8247335bb73"
internal_form_field_id_8     = "bf13719d-85da-4acc-83dd-fd16cb196ee5"
internal_form_field_id_9     = "05bc0950-98c1-4822-bcd8-dc35e3fd4ca9"
internal_form_field_id_10    = "f7f704be-5ea5-4a68-8f0b-9e4cb5bdd0ab"
# label "Awarded Duplicate"
label_id_1 = "317972"
# label "Not Awarded Duplicate"
label_id_2 = "317973"
# label "Pending Duplicate"
label_id_3 = "317972"
'''
# Data structure to replace Database
# volatile memory used and thrown away
# list of dicts
uid_data_struct = data_struct.data_struct

# dict structure
"""
{
 'submission_id':      None,
 'primary_unique_id':  None,
 'collab_unique_id_1': None,
 'collab_unique_id_2': None,
 'collab_unique_id_3': None,
 'collab_unique_id_4': None,
 'collab_unique_id_5': None,
 'collab_unique_id_6': None,
 'collab_unique_id_7': None,
 'collab_unique_id_8': None,
 'collab_unique_id_9': None
 }
"""

# Initial forms multi-response questions mapped to single response
mappedInitial2Internal = [
  ["", "", ""],
  ["", "", ""],
  ["", "", ""],
  ["", "", ""],
  ["", "", ""],
  ["", "", ""],
  ["", "", ""],
  ["", "", ""],
  ["", "", ""],
  ["", "", ""],
  ["", "", ""],
  ["", "", ""],
  ["", "", ""],
]

internalFormFieldsFullOptions = [
    {
      "options": [
        {
          "formOptionId": "9000dc7a-3d39-437a-8d89-ea5268c9a9e2",
          "label": "Albermarle",
          "value":  False
        }
      ],
      "formFieldId": "b5c9662a-6aff-4af4-86bd-1995a533d080",
      "fieldType": "single_response",
      "label": "Does your organization serve Albermarle County?"
    },
    {
      "options": [
        {
          "formOptionId": "d8b3806f-b249-4423-bd43-1db0af06b715",
          "label": "Caroline",
          "value":  False
        }
      ],
      "formFieldId": "ebde95a1-b9b5-4f46-a2f3-20973f0980dc",
      "fieldType": "single_response",
      "label": "Does your organization serve Caroline County?"
    },
    {
      "options": [
        {
          "formOptionId": "2676c65c-8a0a-4641-aff3-2a1c274e3a07",
          "label": "Clarke",
          "value":  False
        }
      ],
      "formFieldId": "cb492d25-a5cc-46ca-9db2-4fcc1c06b843",
      "fieldType": "single_response",
      "label": "Does your organization serve Clarke County?"
    },
    {
      "options": [
        {
          "formOptionId": "c63f54c3-a220-44e5-8c7f-4bf9a4b8a11f",
          "label": "Culpepper",
          "value":  False
        }
      ],
      "formFieldId": "37407da6-009c-4e32-9276-7a45d2c2fd6d",
      "fieldType": "single_response",
      "label": "Does your organization serve Culpepper County?"
    },
    {
      "options": [
        {
          "formOptionId": "17094996-d804-42cb-b12a-be812f0e40f5",
          "label": "Essex",
          "value":  False
        }
      ],
      "formFieldId": "082ab98f-3d9a-4aa0-a802-92c5dbf7d7c2",
      "fieldType": "single_response",
      "label": "Does your organization serve Essex County?"
    },
    {
      "formFieldId": "e4d5480c-ac00-45b2-882a-131fd7400fac",
      "fieldType": "divider"
    },
    {
      "options": [
        {
          "formOptionId": "23da4a2f-e6de-4d64-9e6e-7f65ce534dd4",
          "label": "Albermarle",
          "value":  False
        }
      ],
      "formFieldId": "12223d40-5c0e-4abd-98de-671ae99f8056",
      "fieldType": "single_response",
      "label": "Does your event serve Albermarle County?"
    },
    {
      "options": [
        {
          "formOptionId": "a2ed3587-c5bc-4e51-a87e-a3b8132f9665",
          "label": "Caroline",
          "value":  False
        }
      ],
      "formFieldId": "502e4357-0ed0-42da-a641-a5942f2686ac",
      "fieldType": "single_response",
      "label": "Does your event serve Caroline County?"
    },
    {
      "options": [
        {
          "formOptionId": "66f19dce-b0bf-4a0b-9541-bc2bd1d3bb62",
          "label": "Clarke",
          "value":  False
        }
      ],
      "formFieldId": "fd5542bb-ec80-4464-b2f9-74c8f6976ec3",
      "fieldType": "single_response",
      "label": "Does your event serve Clarke County?"
    },
    {
      "options": [
        {
          "formOptionId": "d4abbf1a-4664-450f-af69-bb750269a6ba",
          "label": "Culpepper",
          "value":  False
        }
      ],
      "formFieldId": "7750aa04-1272-41ea-ba99-75c9e32318d2",
      "fieldType": "single_response",
      "label": "Does your event serve Culpepper County?"
    },
    {
      "options": [
        {
          "formOptionId": "14a35923-e506-4de6-b412-a1491093de00",
          "label": "Essex",
          "value":  False
        }
      ],
      "formFieldId": "71c76521-b41b-4490-a98b-c3d7090a70a5",
      "fieldType": "single_response",
      "label": "Does your event serve Essex County?"
    },
    {
      "formFieldId": "8bfee109-6ba8-4270-a24e-eeada0138190",
      "fieldType": "divider"
    },
    {
      "options": [
        {
          "formOptionId": "cec33d9a-f45f-40e4-8005-29b380c88d63",
          "label": "Donation",
          "value":  False
        }
      ],
      "formFieldId": "bac214a7-df66-4521-8209-2f498307efe3",
      "fieldType": "single_response",
      "label": "Are you requesting a donation?"
    },
    {
      "options": [
        {
          "formOptionId": "7b42e32c-80ad-4609-9bae-d2d290af6387",
          "label": "Sponsorship",
          "value":  False
        }
      ],
      "formFieldId": "4ea48418-d487-4272-8e20-f04c721859d7",
      "fieldType": "single_response",
      "label": "Are you requesting a sponsorship?"
    },
    {
      "options": [
        {
          "formOptionId": "0320847a-ef57-4a46-b781-f3443e733345",
          "label": "Event Participation",
          "value":  False
        }
      ],
      "formFieldId": "54a5205c-e035-43e6-88e6-31b1510964ff",
      "fieldType": "single_response",
      "label": "Are you requesting event participation?"
    }
  ]

internalFormFieldData = [
    {
      "options": [],
      "formFieldId": "b5c9662a-6aff-4af4-86bd-1995a533d080",
      "fieldType": "single_response",
      "label": "Does your organization serve Albermarle County?"
    },
    {
      "options": [],
      "formFieldId": "ebde95a1-b9b5-4f46-a2f3-20973f0980dc",
      "fieldType": "single_response",
      "label": "Does your organization serve Caroline County?"
    },
    {
      "options": [],
      "formFieldId": "cb492d25-a5cc-46ca-9db2-4fcc1c06b843",
      "fieldType": "single_response",
      "label": "Does your organization serve Clarke County?"
    },
    {
      "options": [],
      "formFieldId": "37407da6-009c-4e32-9276-7a45d2c2fd6d",
      "fieldType": "single_response",
      "label": "Does your organization serve Culpepper County?"
    },
    {
      "options": [],
      "formFieldId": "082ab98f-3d9a-4aa0-a802-92c5dbf7d7c2",
      "fieldType": "single_response",
      "label": "Does your organization serve Essex County?"
    },
    {
      "formFieldId": "e4d5480c-ac00-45b2-882a-131fd7400fac",
      "fieldType": "divider"
    },
    {
      "options": [],
      "formFieldId": "12223d40-5c0e-4abd-98de-671ae99f8056",
      "fieldType": "single_response",
      "label": "Does your event serve Albermarle County?"
    },
    {
      "options": [],
      "formFieldId": "502e4357-0ed0-42da-a641-a5942f2686ac",
      "fieldType": "single_response",
      "label": "Does your event serve Caroline County?"
    },
    {
      "options": [],
      "formFieldId": "fd5542bb-ec80-4464-b2f9-74c8f6976ec3",
      "fieldType": "single_response",
      "label": "Does your event serve Clarke County?"
    },
    {
      "options": [],
      "formFieldId": "7750aa04-1272-41ea-ba99-75c9e32318d2",
      "fieldType": "single_response",
      "label": "Does your event serve Culpepper County?"
    },
    {
      "options": [],
      "formFieldId": "71c76521-b41b-4490-a98b-c3d7090a70a5",
      "fieldType": "single_response",
      "label": "Does your event serve Essex County?"
    },
    {
      "formFieldId": "8bfee109-6ba8-4270-a24e-eeada0138190",
      "fieldType": "divider"
    },
    {
      "options": [],
      "formFieldId": "bac214a7-df66-4521-8209-2f498307efe3",
      "fieldType": "single_response",
      "label": "Are you requesting a donation?"
    },
    {
      "options": [],
      "formFieldId": "4ea48418-d487-4272-8e20-f04c721859d7",
      "fieldType": "single_response",
      "label": "Are you requesting a sponsorship?"
    },
    {
      "options": [],
      "formFieldId": "54a5205c-e035-43e6-88e6-31b1510964ff",
      "fieldType": "single_response",
      "label": "Are you requesting event participation?"
    }
  ]
