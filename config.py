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
dup_label_id = "320527"
# label "Migrated"
migrated_label = "325691"



# AEP multi select initial form field IDs
project_1_multi_select_id_1  = "028936dd-a753-4201-909c-38e4f6122c1a"  # Which of the following best describes you
project_1_multi_select_id_2  = "94f117db-9536-4892-ab88-e8d4d60babe9"  # What is your gender identity
project_1_multi_select_id_3  = "cad583dc-a922-4746-8db5-1ad7559a5dbf"  # Do you regularly provide care—either on your own or with someone else—to any of the following people

# multi select option IDs
project_1_multi_options_ids_1  = ["91ceece7-c757-45d1-8596-33c9b38c103d", "87a30d36-0550-49eb-84ce-2de922506cf7", "5cf12f61-ec64-415f-b2ae-9bc242e5efec",
                                  "a9142c59-79fc-4e6d-a3a1-7b97cb61bcca", "b20a0284-4ddf-4588-82c8-fbc5dfc8d9ed", "85cb5937-1cb2-499f-8ffa-8d3a06f7f33c",
                                  "4330a73a-1ae9-4fa7-8e97-99b66d23ac92", "708ccca7-571e-4a55-a68c-7a1689125287", "d5f06b5c-5257-4fb5-a739-60785fba2aa2"]

project_1_multi_options_ids_2  = ["b00c64b9-5291-4f78-a1ae-10a498e5d566", "7a380a61-c348-4193-9db8-030f5799ad98","16a007c4-20b6-4911-a8ff-852dad20d2bf",
                                  "8b9ca158-27a2-4e42-94f0-ddd47ac95ca5", "6276f882-1985-4fdb-8b1e-af0776ebf4bd", "ad7991d1-1f9c-4791-a90a-5c5014ab79a0"]

project_1_multi_options_ids_3  = ["637ec5f0-2eff-4831-92a4-5fe81261622d", "e2f20a0e-b0e2-4ecf-8626-7b21f36916fb", "95aec17a-4eda-4f86-b3e3-8e1e18851a90",
                                  "89cf1db1-08ff-4496-84e8-75ba3fbedbbf", "8c9f4e92-2430-417c-8071-168805ad984a"]

# GI multi select initial form field IDs
project_2_multi_select_id_1  = "758c4332-05cd-4bc4-aa8c-29608f25aa23"  # Which of the following best describes you
project_2_multi_select_id_2  = "4c251fd1-79f1-4f2e-9cf2-c2ba4a3e978b"  # What is your gender identity
project_2_multi_select_id_3  = "7958711d-5b0a-47b2-bb18-626c85aeb810"  # Do you regularly provide care—either on your own or with someone else—to any of the following people
# GI project only
project_2_multi_select_id_4  = "57229736-c2e0-4394-8741-4456e0aa4afc"  # Please check all that apply regarding your financial safety net

# multi select option IDs
project_2_multi_options_ids_1  = ["c0a1fa70-2901-4dba-9fd2-01c7e9411940", "d102efb5-5855-4fb6-a55e-cbdbbb590255", "0acea73a-cde1-44c6-8e91-ca2179461651",
                                  "bab9b368-671a-416d-b796-58d33ce2e6c4", "df7fbb0a-8b13-4ba9-be60-5548f9359a33", "718b9f71-3eab-475d-b621-ca720970a791",
                                  "a103d095-d51f-420e-a017-ab49a6cc0421", "49fff122-a902-482c-91d6-4178d8e73f87", "c09931d0-422d-4697-9833-73b98efdb444"]

project_2_multi_options_ids_2  = ["b4a52ba9-6961-48a0-9e40-84ec49847e72", "1c7a9ad7-f6ba-44f4-aa27-d4299dd698e9", "7314db42-ccfd-474b-aaea-e10be26d9529",
                                  "cc4611cd-e7ba-4df4-bcac-85f6f81f59d2", "4ea1d978-b361-4595-a758-f1bd0d251718", "7525a512-64fc-4a97-a282-ff50609704f9"]

project_2_multi_options_ids_3  = ["2e6dfc90-8106-4107-a910-552d4197a8c6", "702b6585-a1c8-4d99-8e16-d1d797c92d36", "ec6fb886-5ca3-47f6-908f-d4a5c7f00347",
                                  "c491e047-30f8-4e7c-8754-417e50e3f8aa", "f45bd78a-08fc-41c7-b5a8-8dab724d52b9"]

# GI project only
project_2_multi_options_ids_4  = ["ba27ef1b-2b26-4a14-bed4-e9ebc34b0248", "db505e3b-d0df-485e-9e80-851dac87821c", "ef9d1bf4-37c6-4c79-93bf-a154a4f17dc0",
                                  "13f70502-7549-4dc6-86f7-d04ca4b05134", "a0bd6179-bbb6-422d-8cb2-1ab8a1a1f8cd"]


# single select internal form IDs 1-25
#
# single select form field IDs for Multi-Select Question: "Which of the following best describes you"
single_select_id_1   = "90b7e584-a834-4bcd-948d-d0fcd90cdcdb"  # Arab or Middle Eastern
single_select_id_2   = "dbd9a5fc-f8ee-4486-a1d9-631952149f0e"  # Asian or Pacific Islander
single_select_id_3   = "b1bb0975-2256-442f-9f75-2fed4f8b1a17"  # Black or African American
single_select_id_4   = "ff294db0-b3e5-4394-a859-5dcdfb3cd2ee"  # Hispanic or Latinx
single_select_id_5   = "f642f43e-832f-4be9-9ebd-05f700b0ee36"  # Indigenous American, First Nation, or Alaska Native
single_select_id_6   = "936c0d42-01ca-4356-89f2-5504c6d6d6b8"  # Pacific Islander or Native Hawaiian
single_select_id_7   = "77002d8f-7d56-44f1-a3b6-262888449130"  # White
single_select_id_8   = "1e6826d3-ada0-4161-92cf-e8673cdc7fc6"  # Other (please describe)
single_select_id_9   = "13aa0a48-b6df-4d73-9996-f2ee48ef5eb8"  # I prefer not to answer


# single select option IDs for Multi-Select Question: "What is your gender identity"
single_select_id_10  = "ef768aeb-5ab9-4b11-bb22-42f03e569548"  # Man
single_select_id_11  = "5592c59e-c3fe-42dc-8214-92ce7a1c6ef2"  # Woman
single_select_id_12  = "78ecc6d2-8c6b-43ce-aaab-2cf769dfa89c"  # Non-binary
single_select_id_13  = "8f6ef29b-12be-41c6-82a5-565ce2ff1f23"  # Two-spirit
single_select_id_14  = "2ecfe0c1-9119-4874-a54e-4f71a9743e14"  # Other (please describe)
single_select_id_15  = "af0c3735-020b-4c2d-840a-ad6ed569a4b0"  # I prefer not to answer

# single select option IDs for Multi-Select Question: "Do you regularly provide care—either on your own or with someone else—to any of the following people"
single_select_id_16  = "9b378d16-a1bf-4276-9197-fd9b19d16ea2"  # Yes, a child or children
single_select_id_17  = "275673c7-fd28-4990-b9b1-c30e25643fb8"  # Yes, a spouse or partner who is elderly, ill, or disabled
single_select_id_18  = "9ecb2f4f-82d1-4e93-8647-2e30fec87f76"  # Yes, an adult/adults who is/are elderly, ill, or disabled
single_select_id_19  = "664cd79a-d2cc-4bf8-9f3f-60e7545c87b9"  # No
single_select_id_20  = "3ae3d3c6-49ef-4e47-b52b-7b8ea21eeaf6"  # I prefer not to answer

# single select option IDs for Multi-Select Question: "Please check all that apply regarding your financial safety net"
single_select_id_21  = "97e6fc50-6a45-4ce7-b1a3-26c2ee32d97b"  # I am unsure when I will make any income again
single_select_id_22  = "0e11b4b3-44ea-4c35-9256-51a331316800"  # I have no financial safety net (savings, assets, family resources)
single_select_id_23  = "d77551d6-2d1a-4908-af17-cca24508599a"  # I am vulnerable to a medical emergency
single_select_id_24  = "31124d16-8763-43ff-b77d-071e660a3a32"  # I have unmanageable debt (financial obligations not paid in full each month like credit cards, personal loans, payday loans or short-term debt, student loan debt, housing debt, automobile loan, other)
single_select_id_25  = "7728da4b-e57b-4085-98c4-3dbfc30dc127"  # None of the above

# single select option IDs for Multi-Select Question: "Which of the following best describes you"
single_select_option_id_1   = "f89526fa-2498-4855-900c-3db5415b5cdb"
single_select_option_id_2   = "9c790d51-c08c-4630-8de8-650fefdd7f73"
single_select_option_id_3   = "30bed219-d669-471d-beca-a09d1bf152fc"
single_select_option_id_4   = "1c2680ef-7222-47fe-93a4-127cfc3c2285"
single_select_option_id_5   = "7f9c0e65-2983-4e2a-b530-7c8f83135d1c"
single_select_option_id_6   = "7832c635-ae2b-407c-afd9-e7bb7230aed6"
single_select_option_id_7   = "9347685b-b39a-4045-9b5e-92b024755206"
single_select_option_id_8   = "1ff30422-f5bb-4dd1-bbfd-ee945c63f502"
single_select_option_id_9   = "e8fe5a2b-a445-43b8-9156-fb96fa902906"

# single select option IDs for Multi-Select Question: "What is your gender identity"
single_select_option_id_10  = "5cc64c48-ec92-475a-bfbf-dc09a7294e5f"
single_select_option_id_11  = "146aeb7f-506e-465c-92e0-115c9569d47f"
single_select_option_id_12  = "acb58eab-cb62-4a03-a547-c612cbebce04"
single_select_option_id_13  = "09a490a5-8adf-4fd1-a79e-8734f9af0b04"
single_select_option_id_14  = "1ff5ccd1-8103-49b8-81e5-88977ed2305b"
single_select_option_id_15  = "188fc04b-118f-4b28-a288-1440889d8530"

# single select option IDs for Multi-Select Question: "Do you regularly provide care—either on your own or with someone else—to any of the following people"
single_select_option_id_16  = "8f8b4d79-1c31-4b84-8fd5-a51adc619761"
single_select_option_id_17  = "2e6dc0d4-6bc4-4a1f-ae1e-d90d491fc385"
single_select_option_id_18  = "8ac92a6c-ddfa-49fb-ae9b-38473768dc29"
single_select_option_id_19  = "24f60998-6e9f-4a36-9eb6-31b7b5a933a9"
single_select_option_id_20  = "f8089702-01d3-4e27-a6b8-1e743b7fb828"

# single select option IDs for Multi-Select Question: "Please check all that apply regarding your financial safety net"
single_select_option_id_21  = "05788879-016d-4f8c-b174-7a1474b700ec"
single_select_option_id_22  = "4353d9e7-d667-4cef-83af-8d49faa600d8"
single_select_option_id_23  = "9da6b73d-6795-4f0d-8f56-6da65d78783b"
single_select_option_id_24  = "4f81b635-c1e2-4565-82fd-3ad0c7511cd0"
single_select_option_id_25  = "c4379de6-8c00-45c1-83af-9bdef092678c"

# ------------------------------ DEMO ACCOUNT SETTINGS ------------------------------ #
'''
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

# multi select initial form field IDs
multi_select_id_1  = "eac76052-0e95-4116-ba19-a5bb6b8b2c8b"
multi_select_id_2  = "7eb3e60a-46d4-4af4-a7d3-da3e16bb9668"
multi_select_id_3  = "d4b5d654-b49a-4bbc-83bb-108b5ce3720f"
multi_select_id_4  = "3e7b727d-3673-4188-9e9f-8c8fd63acea2"

# multi select option IDs
multi_options_ids_1  = ["0fb42b6f-4ee8-4e6c-9b6b-e533265db81d", "e54dbccd-77d3-4a6f-917d-cc6f17f7e455", "48aed253-acb2-4df0-98f7-40241a94234a",
                        "496ac6ce-d878-4502-a6c5-83785b955a1f", "342db86a-c143-4fe4-920e-4f55e3c2fbae"]

multi_options_ids_2  = ["ab5c0380-4469-4978-afbe-031b9603c441", "70949d68-c837-4aa3-b635-87d9bd518029", "b981be25-ac64-4185-89e3-13af19cc320c",
                        "96c3879c-e574-4a55-b3bf-1485803e627a", "f095a8a8-a5cf-45cd-b19e-889e0b35893b", "768db764-ff17-492e-8c24-8876b81a9ba0"]

multi_options_ids_3  = ["c5d8bcca-a895-42f9-94b3-93b429abb95c", "12100b3c-e0a7-4c41-90b6-12c84852087f", "25a58ba3-bb29-4de1-8879-0c39e4b8af39",
                        "6b52484a-5c65-45ca-8b3d-32d86bbf63dc", "a102482e-912f-42d8-ad2e-5412abc65a35", "fad906d2-13cf-459b-b1fb-6329a724c13e",
                        "0ca564d6-bfdb-4dae-9fba-1c276de4afc8", "1edc7f65-f9a7-4771-a5e5-8029f648e615", "e2099bb8-5b46-4e0f-9ff3-bfba5ff57db7"]


multi_options_ids_4  = ["5d4c6e58-cb49-4ea0-ba88-7e98f12ffc5b", "6b2afce6-69bd-412d-bdff-32e76c9751d4", "ce8dd191-f6c1-4849-95bd-b4cd464adad0",
                        "cbd863f0-d915-4f0e-8e4b-48125b0c85b8", "111a90e1-626c-4276-906b-0df290c47f47", "70ca1382-90d6-4f26-8f05-0d921d1b17ea"]


# single select internal form IDs 1-25
#
# single select form field IDs for Multi-Select Question: "Which of the following best describes you"
single_select_id_1   = "0df8cde3-7b60-456d-9a8d-9bcf94de39d8"
single_select_id_2   = "9bb8c05d-e110-45eb-af5c-9254f3d276a7"
single_select_id_3   = "fab97e78-8d3c-4d99-9e32-caded4ec3780"
single_select_id_4   = "fedc23b7-0c77-4b9b-b983-6fd0618c845f"
single_select_id_5   = "033d42ef-9a74-4c37-89da-4c269b145f50"
single_select_id_6   = "29ac22dd-0169-4190-b12d-63df8c0c1b2d"
single_select_id_7   = "dc223b53-b0cd-40ae-acca-3360c8110cdc"
single_select_id_8   = "7c3d509c-ed2a-4d11-9e26-19ae08aac766"
single_select_id_9   = "ea306fa1-c211-48b5-b8be-316d3d2268bd"

# single select option IDs for Multi-Select Question: "What is your gender identity"
single_select_id_10  = "560187e5-99ad-4bf6-8fa1-fb3c830ccc98"
single_select_id_11  = "838b1d52-06b0-420c-9069-785a32b36640"
single_select_id_12  = "06a6f618-2410-4680-8931-f6e9bc063881"
single_select_id_13  = "ec6de2b6-abfc-478b-9399-dd78a2060f5a"
single_select_id_14  = "5dd965c1-2809-48a5-8339-bb43ded7e878"
single_select_id_15  = "51c758ff-5205-454b-9497-5c629a606e89"

# single select option IDs for Multi-Select Question: "Do you regularly provide care—either on your own or with someone else—to any of the following people"
single_select_id_16  = "c05ab297-03eb-41ff-8e91-d9aa6d42bfdb"
single_select_id_17  = "3aeecaa8-0608-408b-adc2-3cd4aefb098a"
single_select_id_18  = "88ca33f4-f8cc-4806-84b1-7d4affe94b99"
single_select_id_19  = "236ac594-a3f1-41b9-a6fd-594f21b94d4b"
single_select_id_20  = "fe98ef83-afbd-47f7-a7c7-7cecfce1e8bf"

# single select option IDs for Multi-Select Question: "Please check all that apply regarding your financial safety net"
single_select_id_21  = "5888a141-55e2-423c-a907-72285b907715"
single_select_id_22  = "0a3516d6-b6e5-4db9-9063-721b186b63b4"
single_select_id_23  = "8777383c-0d9d-43db-8890-cf04b243617e"
single_select_id_24  = "210f9793-4679-4dcc-83a0-9f857b54981a"
single_select_id_25  = "f8e75bbe-7a1a-49fa-b4a4-5afdf363a726"

# single select option IDs for Multi-Select Question: "Which of the following best describes you"
single_select_option_id_1   = "69b10947-53d8-44fd-9cc3-985dbabdac08"
single_select_option_id_2   = "1d524d33-6ffe-473f-a092-f5cde8344ace"
single_select_option_id_3   = "a30a5f94-f5eb-452b-8f36-70e0be188af3"
single_select_option_id_4   = "01c9c092-531f-4fa8-ac1a-2b0f39c3ffae"
single_select_option_id_5   = "f1995bda-1af9-4985-93a5-ad943acdcf0"
single_select_option_id_6   = "b8b55099-e04b-43cb-b3c0-9dd7862ed631"
single_select_option_id_7   = "1b0bda08-4cd2-4187-975b-72a473c19c6d"
single_select_option_id_8   = "9b9d188d-4ce3-4934-8cc5-4fab11dd3534"
single_select_option_id_9   = "74086302-c798-41a6-80f1-af9713689e68"

# single select option IDs for Multi-Select Question: "What is your gender identity"
single_select_option_id_10  = "e56a4b97-8366-416e-94b5-cac3b7342186"
single_select_option_id_11  = "49b49e36-d4df-41eb-a872-e8337372c799"
single_select_option_id_12  = "be5165de-da41-4e98-82f6-9f3185c2a60c"
single_select_option_id_13  = "3e85025f-d33f-49f3-a2c6-a031b191cd7e"
single_select_option_id_14  = "cac8ea1d-7558-48e6-879d-e4eede278e44"
single_select_option_id_15  = "fdef6ee7-b648-44ce-a90d-7e4437123728"

# single select option IDs for Multi-Select Question: "Do you regularly provide care—either on your own or with someone else—to any of the following people"
single_select_option_id_16  = "37d02e9b-3cbd-4f3f-b104-366a88d61944"
single_select_option_id_17  = "2b02dc9d-52fa-44cd-874c-3b2107d548a3"
single_select_option_id_18  = "b14282a7-bce4-4aa9-838f-ba474c52bc6c"
single_select_option_id_19  = "55325721-b58f-44be-9cf1-45b617a9ce18"
single_select_option_id_20  = "efaa0517-6f89-4521-adb5-6b9075adfbad"

# single select option IDs for Multi-Select Question: "Please check all that apply regarding your financial safety net"
single_select_option_id_21  = "089bba69-5b9b-4507-a707-d29fc642ce09"
single_select_option_id_22  = "ee872fe1-3239-4e6d-abf3-190b3e59fd87"
single_select_option_id_23  = "cb6c77b1-aa07-4c09-be90-f0256604841c"
single_select_option_id_24  = "2f28ed22-3306-4265-9894-bb7ee469ff90"
single_select_option_id_25  = "67e2e1e9-e773-46ce-9143-17f9b9dd5c2a"
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