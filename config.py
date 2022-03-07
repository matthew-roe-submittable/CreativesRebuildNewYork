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
'''
# live account API key
# submittable_token = "5379d0ca57f64c1f827f3d0a0b476554"

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

# TODO - update for production 
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
first_single_select_id  = "0df8cde3-7b60-456d-9a8d-9bcf94de39d8"
second_single_select_id = "9bb8c05d-e110-45eb-af5c-9254f3d276a7"
third_single_select_id  = "fab97e78-8d3c-4d99-9e32-caded4ec3780"
fourth_single_select_id = "fedc23b7-0c77-4b9b-b983-6fd0618c845f"

# single select option IDs
first_single_select_option_ids  = ["69b10947-53d8-44fd-9cc3-985dbabdac08", "d810d10b-d2ed-4568-ae80-2f42d2c4d4c7", "bfdc8d99-978c-4ab2-a530-b2456bc7734b"]
second_single_select_option_ids = ["b1920b24-90e5-44ee-a943-6a64f591f394", "5e81cf6c-d039-4658-8e66-0f6af06dc354", "22a989cb-76e8-4d22-8f7f-067f5fdfa842"]
third_single_select_option_ids  = ["a30a5f94-f5eb-452b-8f36-70e0be188af3", "6aeb62f7-0481-4f10-80b0-bbc12b4937ab", "be4a565b-47d2-479c-9677-4eaa6486149d"]
fourth_single_select_option_ids = ["01c9c092-531f-4fa8-ac1a-2b0f39c3ffae", "e2c5deb6-b98d-4e42-872b-a6c05048c34d", "6dcea3ce-a1f9-44c7-9d24-6b9300f3a7ed"]
'''

# ------------------------------ DEMO ACCOUNT SETTINGS ------------------------------ #
# demo account
submittable_token           = "700b04eccae244679785a0e8f13c786e"
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

# multi select initial form IDs
multi_select_id_1  = "7eb3e60a-46d4-4af4-a7d3-da3e16bb9668"
multi_select_id_2  = "d4b5d654-b49a-4bbc-83bb-108b5ce3720f"
multi_select_id_3  = "3e7b727d-3673-4188-9e9f-8c8fd63acea2"
multi_select_id_5  = "74b3f2a8-e875-4822-bccc-fe3a75f32dd0"

# multi select option IDs
multi_options_ids_1  = ["f095a8a8-a5cf-45cd-b19e-889e0b35893b", "768db764-ff17-492e-8c24-8876b81a9ba0"]
multi_options_ids_2  = ["12100b3c-e0a7-4c41-90b6-12c84852087f", "6b52484a-5c65-45ca-8b3d-32d86bbf63dc",
                        "fad906d2-13cf-459b-b1fb-6329a724c13e", "1edc7f65-f9a7-4771-a5e5-8029f648e615"]
multi_options_ids_3  = ["6b2afce6-69bd-412d-bdff-32e76c9751d4"]
multi_options_ids_4  = ["b0180bf4-fc17-4d4c-ad19-abc106e020b2", "bcf235b1-b3ba-4323-8b0e-d37c0819b889"]

# single select internal form IDs
single_select_id_1  = "0df8cde3-7b60-456d-9a8d-9bcf94de39d8"
single_select_id_2 = "9bb8c05d-e110-45eb-af5c-9254f3d276a7"
single_select_id_3  = "fab97e78-8d3c-4d99-9e32-caded4ec3780"
single_select_id_4 = "fedc23b7-0c77-4b9b-b983-6fd0618c845f"

# single select option IDs
first_single_select_option_ids  = ["69b10947-53d8-44fd-9cc3-985dbabdac08", "d810d10b-d2ed-4568-ae80-2f42d2c4d4c7", "bfdc8d99-978c-4ab2-a530-b2456bc7734b"]
second_single_select_option_ids = ["b1920b24-90e5-44ee-a943-6a64f591f394", "5e81cf6c-d039-4658-8e66-0f6af06dc354", "22a989cb-76e8-4d22-8f7f-067f5fdfa842"]
third_single_select_option_ids  = ["a30a5f94-f5eb-452b-8f36-70e0be188af3", "6aeb62f7-0481-4f10-80b0-bbc12b4937ab", "be4a565b-47d2-479c-9677-4eaa6486149d"]
fourth_single_select_option_ids = ["01c9c092-531f-4fa8-ac1a-2b0f39c3ffae", "e2c5deb6-b98d-4e42-872b-a6c05048c34d", "6dcea3ce-a1f9-44c7-9d24-6b9300f3a7ed"]

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