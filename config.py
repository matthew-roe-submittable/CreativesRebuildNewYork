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
project_id_1                = "f5b5299e-149b-40fe-9764-f41fa3c57330" # Artist Employment Program 2022
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
project_id_2                 = "a29ca1b8-2121-446e-aa93-e6739e77f09c"  # Guaranteed Income for Artists 2022
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
dup_label_id   = "320527"
# label "Migrated"
migrated_label = "325691"



# AEP multi select initial form field IDs
project_1_multi_select_id_1  = "028936dd-a753-4201-909c-38e4f6122c1a"  # Which of the following best describes you
project_1_multi_select_id_2  = "94f117db-9536-4892-ab88-e8d4d60babe9"  # What is your gender identity
project_1_multi_select_id_3  = "cad583dc-a922-4746-8db5-1ad7559a5dbf"  # Do you regularly provide care—either on your own or with someone else—to any of the following people
project_1_multi_select_id_4  = "8f21320b-c09f-42dd-9a18-781470c0e101"  # At what scale do your services or programs operate
project_1_multi_select_id_5  = "d04f1e3e-169e-4bd4-8d13-0f9a36007dc4"  # How do you approach your practice as an artist, culture bearer, or culture maker
project_1_multi_select_id_6  = "6a0521d4-5111-4199-8b54-b9663a904551"  # In what capacity has your organization worked with artists?
project_1_multi_select_id_7  = "9baa2709-d5e2-4aa0-abe1-4b62ff81c37b"  # Which of the following communities does your organization explicitly serve
project_1_multi_select_id_8  = "a674b07b-5fce-4d86-a558-53cd0569c77c"  # Which of the following did you receive
project_1_multi_select_id_9  = "a8b213cf-634f-4927-8bb6-56e9f94792f2"  # If yes, does it include the following

# multi select option IDs
project_1_multi_options_ids_1  = ["91ceece7-c757-45d1-8596-33c9b38c103d", "87a30d36-0550-49eb-84ce-2de922506cf7", "5cf12f61-ec64-415f-b2ae-9bc242e5efec",
                                  "a9142c59-79fc-4e6d-a3a1-7b97cb61bcca", "b20a0284-4ddf-4588-82c8-fbc5dfc8d9ed", "85cb5937-1cb2-499f-8ffa-8d3a06f7f33c",
                                  "4330a73a-1ae9-4fa7-8e97-99b66d23ac92", "708ccca7-571e-4a55-a68c-7a1689125287", "d5f06b5c-5257-4fb5-a739-60785fba2aa2"]

project_1_multi_options_ids_2  = ["b00c64b9-5291-4f78-a1ae-10a498e5d566", "7a380a61-c348-4193-9db8-030f5799ad98","16a007c4-20b6-4911-a8ff-852dad20d2bf",
                                  "8b9ca158-27a2-4e42-94f0-ddd47ac95ca5", "6276f882-1985-4fdb-8b1e-af0776ebf4bd", "ad7991d1-1f9c-4791-a90a-5c5014ab79a0"]

project_1_multi_options_ids_3  = ["637ec5f0-2eff-4831-92a4-5fe81261622d", "e2f20a0e-b0e2-4ecf-8626-7b21f36916fb", "95aec17a-4eda-4f86-b3e3-8e1e18851a90",
                                  "89cf1db1-08ff-4496-84e8-75ba3fbedbbf", "8c9f4e92-2430-417c-8071-168805ad984a"]

project_1_multi_options_ids_4  = ["dd74db01-944f-4e60-a9ad-83846a8740c4", "9985c072-ab99-40d3-99df-03ab547953e8", "ffd42ca3-67c0-4149-98c0-d31b20f2df34",
                                  "683af09d-6c09-4100-9231-843b58054d39", "f8e7d91c-3dcc-4c59-b695-34e474208365"]

project_1_multi_options_ids_5  = ["6a782b6b-fa61-433e-9a8b-cf0a1f88ade1", "14757995-2ce5-4902-9de6-70da31cc78d0", "b4a7a3e7-a15b-4cd8-b781-3b70be1f95b5",
                                  "a3092d24-5493-443a-9950-d4c860dacea9", "9dcea11d-1829-4ba6-b27c-9224ca856236",  "7eed346b-2900-424c-901a-cd1797b66cb6"]

project_1_multi_options_ids_6  = ["e7149032-947e-4f91-99fa-c9d84a164fc6", "d9d84ba7-9b05-4c7b-ac5b-d8b3c8ea9b08", "12bd0210-1c22-458e-ab6e-425f3acea5e6",
                                  "27c3042c-742f-4915-80d2-07f205f95f83", "fad990d0-e83f-4ec9-a99e-2743fc3e6a50"]

project_1_multi_options_ids_7  = ["87066c94-81d6-49ae-8800-4c934a91af79", "1b51e25f-731c-4a88-b02e-f35973ef0a23", "15683710-931b-453a-bca1-e2d5f5afc839",
                                  "6439d360-c52f-4b34-bef6-301165c1b783", "4d649913-c52e-4012-b5cc-ca96f4f87e70", "ec9f7e5c-9fea-48ca-8bd1-35c5e774d228",
                                  "5dbcf425-6271-4d1c-9c9b-b1a42fc9d739",  "96e48837-0269-427a-befe-719b1268d927"]

project_1_multi_options_ids_8  = ["6c6c9c68-bb94-425d-af2c-de0a0091bd1d", "e4a0633e-8dbe-41b7-85b0-dfd91d6eb0de", "fe4d8a94-cc30-4d6b-85a9-cf2a9d4b707f",
                                  "1cd781a5-8d74-42bd-8888-fa9e52397494"]

project_1_multi_options_ids_9  = ["fa9fba85-32a4-4fea-bdd3-25a88257bc88", "40464179-7568-462c-88fa-8fc0c36e6450", "65fefc57-57d5-4f69-a94e-a687d849e4b3",
                                  "1214af96-e2e3-4793-9ba6-f3d94b11dace"]


# GI multi select initial form field IDs
project_2_multi_select_id_1  = "758c4332-05cd-4bc4-aa8c-29608f25aa23"  # Which of the following best describes you
project_2_multi_select_id_2  = "4c251fd1-79f1-4f2e-9cf2-c2ba4a3e978b"  # What is your gender identity
project_2_multi_select_id_3  = "7958711d-5b0a-47b2-bb18-626c85aeb810"  # Do you regularly provide care—either on your own or with someone else—to any of the following people
project_2_multi_select_id_4  = "57229736-c2e0-4394-8741-4456e0aa4afc"  # Please check all that apply regarding your financial safety net
project_2_multi_select_id_5  = "80accf26-bdf4-4767-afa1-516e04db34ca"  # How do you approach your practice as an artist, culture bearer, or culture maker
project_2_multi_select_id_6  = "19965a1f-c95f-4e0f-99e2-2f67ae6ba96d"  # To the best of your knowledge, in which of the following are you currently enrolled

# multi select option IDs
project_2_multi_options_ids_1  = ["c0a1fa70-2901-4dba-9fd2-01c7e9411940", "d102efb5-5855-4fb6-a55e-cbdbbb590255", "0acea73a-cde1-44c6-8e91-ca2179461651",
                                  "bab9b368-671a-416d-b796-58d33ce2e6c4", "df7fbb0a-8b13-4ba9-be60-5548f9359a33", "718b9f71-3eab-475d-b621-ca720970a791",
                                  "a103d095-d51f-420e-a017-ab49a6cc0421", "49fff122-a902-482c-91d6-4178d8e73f87", "c09931d0-422d-4697-9833-73b98efdb444"]

project_2_multi_options_ids_2  = ["b4a52ba9-6961-48a0-9e40-84ec49847e72", "1c7a9ad7-f6ba-44f4-aa27-d4299dd698e9", "7314db42-ccfd-474b-aaea-e10be26d9529",
                                  "cc4611cd-e7ba-4df4-bcac-85f6f81f59d2", "4ea1d978-b361-4595-a758-f1bd0d251718", "7525a512-64fc-4a97-a282-ff50609704f9"]

project_2_multi_options_ids_3  = ["2e6dfc90-8106-4107-a910-552d4197a8c6", "702b6585-a1c8-4d99-8e16-d1d797c92d36", "ec6fb886-5ca3-47f6-908f-d4a5c7f00347",
                                  "c491e047-30f8-4e7c-8754-417e50e3f8aa", "f45bd78a-08fc-41c7-b5a8-8dab724d52b9"]

project_2_multi_options_ids_4  = ["ba27ef1b-2b26-4a14-bed4-e9ebc34b0248", "db505e3b-d0df-485e-9e80-851dac87821c", "ef9d1bf4-37c6-4c79-93bf-a154a4f17dc0",
                                  "13f70502-7549-4dc6-86f7-d04ca4b05134", "a0bd6179-bbb6-422d-8cb2-1ab8a1a1f8cd"]

project_2_multi_options_ids_5  = ["c10cd09c-1f42-43fb-9add-27624bc97fa3", "f055e486-69f0-45ef-b399-26f392f405b2", "e228897b-1010-4fb7-8e4f-9e112e2b5b76",
                                  "691fc1fb-4f83-4448-9820-b52edbba5549", "7a25a1c7-307f-4c16-b9d1-9dc81b4fd9fc", "715fde81-243d-49c1-be4a-1d0540ba13a5"]

project_2_multi_options_ids_6  = ["9f73f8df-1782-4587-bcf4-b45e34dcda7f", "a25b7983-91e4-4307-b074-621b1cea6b16", "25296dd2-fffd-4d71-9d8f-296191f5c9bc",
                                  "fbd30fda-dd46-4461-9db6-c425bfdfe570", "232a8147-dc83-4d68-a050-13dbfc4157ef", "50eeb188-cdd8-431b-aec9-c9da09f5c82c",
                                  "76611988-c8a8-4f1c-b9dc-835900dd15f8", "bcdf3a4b-8618-40bf-a470-0d809a4a14dc", "7d15fdbf-e10b-4877-8790-52fcb8cdd142",
                                  "5aa38ae1-8f03-41a7-8a92-f8df39ba8000", "66baf3b0-4794-44bb-a33e-a3b61fd49a47", "afc2f52c-c667-4d41-a5c3-1aee670aae20",
                                  "3cc63592-708d-4b92-ae37-4ca987846bc7", "e78453f5-89e7-40bd-bef6-9e60d3555311"]

# Ineligible Survey multi select initial form field IDs
ineligible_survey_multi_select_id_1   = "edcccd65-8a54-4cff-81b3-1cfa83f2f1a9"
ineligible_survey_multi_select_id_2   = "062a66a3-27ab-4375-92f5-21376467ea7e"
ineligible_survey_multi_select_id_3   = "392fb2f0-bd2a-4b69-8f79-d04f7c74dd5e"
ineligible_survey_multi_select_id_4   = "9e5a3a5e-6dcb-4ff4-a250-c782495d7702"
ineligible_survey_multi_select_id_5   = "4dfba398-4b2f-40aa-8c42-fe39a8d1f315"
ineligible_survey_multi_select_id_6   = "4e435746-6ed0-44e4-8e51-a78d40d2f036"
ineligible_survey_multi_select_id_7   = "3e245f86-e612-402b-9582-e0bcafb52aaa"
ineligible_survey_multi_select_id_8   = "7c822478-5db9-4a80-af1c-36fa2184d22d"
ineligible_survey_multi_select_id_9   = "ddfa547e-4926-4a35-9639-f427c2fe21f8"
ineligible_survey_multi_select_id_10  = "38ed7303-483d-4e90-a788-f38045e3dcb6"
ineligible_survey_multi_select_id_11  = "e5f2ddf6-d9d3-4539-a0ad-6be9a30a6456"

# Ineligible Survey multi select option IDs
ineligible_survey_multi_options_ids_1   = ["5f95bb5d-8742-42c3-a3a8-989bbf9ef2a9", "96f609fc-aec5-4683-bbaf-bdb8e0bb1215", "882e2ead-2105-4351-938d-eeaefbe5701a",
                                           "8a391ec2-cfb4-4b63-b935-82ed7f28adbf", "9b00c71e-af53-469a-992a-1e059fd5bd91", "04f5149e-ba58-4196-8ba1-56f3a1db4e15"]

ineligible_survey_multi_options_ids_2   = ["9fce1ac4-a1c7-401e-b091-b10230f40a58", "9cc3fa2c-678b-4169-a04a-1a4fc875f014", "988e5328-16dc-4c62-a0af-1c33a393dfa8",
                                           "71bf108f-018e-43c9-a4cf-de8483af857f", "00c0f6de-325b-4f77-8ecb-d90c6c88e3fb", "61228b47-2252-4af5-b6e9-609eaa727ba0",
                                           "eb03277f-79e8-46b4-bc6d-aa388d358d42"]

ineligible_survey_multi_options_ids_3   = ["1bb49643-a5c9-47f6-b536-462826126831","946c1f53-ca01-4f44-9cab-e068c65e4099", "ffa238ca-61ff-4481-b449-911e35fb150a",
                                           "6b4cf741-d002-4e46-987e-6c4ceca84b12", "6866580e-f680-458e-9aaf-d5086fccc241"]

ineligible_survey_multi_options_ids_4   = ["3371c768-b379-4c76-aa00-995d73898a05", "28880ad4-90d4-498b-8dbc-e066beafdbe3", "7c5e6808-af72-49b8-9a22-a6f9f4ba816e",
                                           "8489646d-d1c5-44f4-951a-a06adf9ab77f", "3a371055-058a-42a2-b92f-eab34beca99a", "051e3126-cbe4-4d24-9e56-bd267f6ad8d2",
                                           "5de53202-1092-4aab-a90e-b66e7bbc6ad8", "8ec081e1-4d6d-49bf-b6e9-9394c693995e", "4ae6cce0-fe15-4d28-aaf6-e52536bea9ef",
                                           "b6ecd06c-2a28-476d-8e3e-cc456ad5d17c"]

ineligible_survey_multi_options_ids_5   = ["dc328f7c-e396-4521-b169-26c739714e6a", "025e93d4-82fd-4b4b-ab9f-f85fbc0a702e", "2e23a1f5-9ab8-4d36-ae20-c929a9fc7355",
                                           "b08747a0-ad27-44be-9e3b-e1e3a8b47eb2", "4a7dad5d-af05-439e-9569-05120aeac4dd", "ecb3c6ec-5e63-46b0-a4ee-9051baa6a007"]

ineligible_survey_multi_options_ids_6   = ["d040dd17-e6ea-4bec-aa5d-5249aaf21625", "0888dd72-751c-447d-ba82-e12bf065f4dc", "73a27b11-9876-4526-83d2-ef8c42d7708e",
                                           "a41c2ace-86ad-4318-b1cf-54e2fc5302e6", "d8fbb428-ed4d-4b74-b6f7-e69fe795945f", "0ab50e97-450a-4a63-9a88-c505cabb6a19",
                                           "bcd3ae54-d6de-443a-b380-59733a6d2733", "ecb71ae2-bb2d-4114-9e6c-0d38ea8038ee", "5371c239-45b0-4c11-950a-dfed738c70e4"]

ineligible_survey_multi_options_ids_7   = ["38f8ef10-76af-4e88-bebe-5f6cfa05f946", "ec37b4ff-b0f6-4d76-9304-fca632b7fb2d", "023d08ec-8889-4e2d-abd0-7d5187e25a58",
                                           "7a315d49-62e9-42a6-9377-e11e379c4e15", "404649ba-a240-40fc-94ba-cfea3a61eedf", "5b09679d-c98f-407f-8a36-dfadc4a302e7",
                                           "8a02aa52-7b8d-4fad-90d7-3dcb2c6d5c99", "b783525c-4e6a-4eed-9f74-0bd9ed1779e4", "208e1400-7d80-42be-86d9-b3db0de628b0",
                                           "d4ec0866-bd07-47dc-99b7-0a4a579492e9", "0fa0d72f-1c7c-4d84-bf75-c74b9892860a", "96831260-cc5d-4830-9497-0af788a0ddbf",
                                           "e07fe0d5-c57b-49fd-a01b-3fc800b948fa", "0ba990f6-ea28-4deb-ad78-2796770f2661"]

ineligible_survey_multi_options_ids_8   = ["f2f0cb4f-15e6-438a-90d1-b7e289e1e09b", "0565f941-f1f3-43b9-bc4a-b172c05ef803", "e5da4926-dbef-4502-8555-2902ae00050b",
                                           "ee471a0f-644f-48a2-b169-fd431f973089", "8f94da72-6d4b-4bb9-ae0e-9521b9256e07", "a0fc0ae3-847d-48ab-9cc7-927bfc70f756",
                                           "2cc17ce8-aca3-4fcb-a4ae-205b06250b82", "732d3591-9501-4be0-9847-54362cb5d09c", "1f08b94e-45fa-484e-b1fb-3559e14be398",
                                           "3d7eb0ca-e3fd-4439-af15-e9091659e748", "0e34aeb4-0f05-4ce4-bb66-c290bca4845c", "a7ea3986-1dae-47e2-9565-9acf4c1f3d4e",
                                           "5b4a1d6b-d7af-4d65-8667-0720976817ec"]

ineligible_survey_multi_options_ids_9   = ["14ec7818-bf12-46e1-adc9-4ef02bfb2eee", "b4c4ebcc-0ff9-4b85-811e-61cac4d9a5b1", "374bf0bc-906c-4757-ba0f-5b9eadaf1799",
                                           "fc639ff5-565d-45b1-887b-8f54cb95e26b", "dc2b8060-0b56-4ff7-b6d6-feb0b1dd0a6e", "48335a63-21b4-42cf-aab0-1914005d24cd",
                                           "5c660633-2997-462c-aa46-bec2cd61915d", "e1b135ee-0ec1-42f4-9adc-9e986274af34", "ebfd00b9-425e-49d5-a6f5-85f2181a61c2"]

ineligible_survey_multi_options_ids_10  = ["1d2e5a20-e651-48d4-b1ee-e06840c8123c", "20c61689-0202-475f-9fc5-27ed91b2baa9", "2ccca08c-2acb-403a-aecf-28910e7128e3",
                                           "37a2f3ef-8267-49e2-97e8-ecb4fb4555d1", "50509510-a3f8-4cc2-8c2e-86ac30139c74", "dc6892a7-6f14-45bd-a4ae-6a0e9654eb2c"]

ineligible_survey_multi_options_ids_11  = ["ba34723d-43ad-467f-b268-47628d1be2d8", "d322091c-2e4b-41d4-9197-94e285383c36", "312121f5-a493-4cae-83dc-46680e46ac9b",
                                           "c0a423ef-f426-4df9-a970-44cb8917b8c5", "dff80b54-909c-4fb7-8b8c-4b0704ab2630"]


# Applicant Survey multi select initial form field IDs
app_survey_multi_select_id_1  = "fdb4e9c2-d4ff-448d-b273-b4913a817315"
app_survey_multi_select_id_2  = "0ff425b2-e52a-4a61-bf1f-d57b1a86d0e3"
app_survey_multi_select_id_3  = "4ea18a73-9b23-4189-a639-a84543aeb555"
app_survey_multi_select_id_4  = "828e0f70-7df8-47d0-b72a-473ce40a379d"
app_survey_multi_select_id_5  = "8c0279f9-d18b-4d19-acc6-763e68118b28"
app_survey_multi_select_id_6  = "1dfdce13-1cab-4dd3-9142-b483abeeef1b"
app_survey_multi_select_id_7  = "6c532c53-aa2f-4b09-939a-f22293af4bf0"

# Applicant Survey multi select option IDs
app_survey_multi_options_ids_1  = ["efdf3c25-fd41-4347-9524-2c6bded7679b", "8de7a620-cae4-42d0-b49d-69118a2742a9", "d5a227ee-140a-486e-94be-3b2efdda8b54",
                                   "8e9e2a9a-2bfd-437e-bb22-0bc1a20f90ba", "43a956b0-dcb6-449e-bed3-4d097eefe164", "d555cefd-8baf-4ef2-929a-843bb8e0390c",
                                   "783c6514-1e95-4dc5-bea6-9a56210d3669"]

app_survey_multi_options_ids_2  = ["d22b7e72-73b3-43b0-a24c-b7d0e2bf0808", "0c8829f4-c5e1-4f52-aeb7-368f89830d34", "fe2b6b61-c3bf-4479-b695-dee7bf0abc1f",
                                   "92d93f17-9196-43c2-a6db-39842468da46", "3bc48952-8e53-4211-9c43-9b9338468cc2"]

app_survey_multi_options_ids_3  = ["40424037-bf54-40da-9fe0-6316a0737a78", "c32fb0d1-f36e-4418-9177-4a3deac9f758", "2d54d58c-7faa-45ca-b0d0-b3f81f874e0d",
                                   "361a19c4-1db5-4141-b1bb-9d257fad6308", "a7e8ee89-2ee3-4190-9d75-6a4174cb21ec", "6d9be88e-8d83-479a-93c8-e3ac58559e51",
                                   "209dd0b0-6a64-43c8-8ec6-dc5efd800268", "bd82d82f-2b97-4f52-8853-f3ef2f2f715b", "e75e4227-6fa1-4f66-b3b6-5654a0bae5f8",
                                   "25231213-6ca2-45ed-95e3-6824e59c4e57"]

app_survey_multi_options_ids_4  = ["e647fbd3-f198-438c-88a2-072c0c5df7a2","23e672f9-9254-4de1-8ea4-c3e0414ed99e", "053a282f-bcbb-4a91-aee1-bf32ad0efbc6",
                                   "debb386e-beda-41f2-ac10-4bafc3e192f7", "5e09b5e5-9831-42f5-89f1-f1afbf9ae375", "feaf721b-ced2-48ae-8a7a-c13813d35f58"]

app_survey_multi_options_ids_5  = ["aaf9afbe-b8fd-4dfb-94f6-dffe263e5cb6", "0b07dcc7-9295-4cfc-9349-f69e0485e8aa", "6be7dbbf-6f70-455c-b3ce-9595921b2bad",
                                   "06246ada-c167-4b2d-a47e-abf62d856cf5", "5c5a5557-5c7f-47c4-92f7-947ebd66433d", "5f297a16-b021-47ad-9d8e-d2ed864695e3",
                                   "53eee354-348a-47c9-841a-00092e5d2ec5", "d3edeca3-1221-4be0-bdd0-8e8d68dbb3ae", "ae91953e-cf51-4b1b-bd7f-9298bbf806e8"]

app_survey_multi_options_ids_6  = ["075c1402-c341-4122-9b93-979c1086ff05", "fafd9f56-6ba7-4a56-a4ab-83f69c5f196f", "c948da99-e7b7-479c-adbd-1d551117f77d",
                                   "b558af70-5be9-43e7-bacc-7c1364ff0f02", "abc968a8-475c-4f3d-831f-38fe6c93b1ee", "1c5c4f67-cea6-4a0d-98d3-50f63ce7c3c2",
                                   "fcd33d52-8b9c-4454-bf39-2b384614dd8a", "945fb5b8-7779-4924-bb8c-c1a283538a78", "3f78a28b-df09-4676-96c8-4c35f9779d47",
                                   "bb2d0862-e020-406d-8e2d-9ebdcd4ce4bf", "91144b6c-0319-44ef-b071-abaf4d4c512a", "3033dbc0-a516-43e9-bf1b-0f2c72f868d7",
                                   "51ae0db9-a436-4fdc-8df3-21ad483e3a46", "a5a9e007-817a-44b0-b597-92f2860020f6"]

app_survey_multi_options_ids_7  = ["91994fbb-c6da-4227-811e-68606fea7309", "d2bc01df-024f-470a-ae8b-aec6e1ec5fb7", "056e6118-82fb-4b49-92a6-778d866743f3",
                                   "99e5c0fa-7fcb-4a5b-a81f-cf1c11eb5abf", "bcb0d11a-c101-4c9a-9d78-154721f25e99", "77a19cc1-a0fd-4e40-888b-073e152da91c",
                                   "b59275dc-8457-4aec-8748-67fc5b449b6f", "8cf91576-8e68-457b-9360-cbd90468441b", "7dc17eb1-bf0a-48ac-9f6a-5d6b74c78b94",
                                   "b5454284-b9a6-4106-ae0c-62dca231c120", "78ae5db0-bd04-46b9-aa8c-56d2ecfc2b55", "1b091c09-05cc-4824-b476-a7236322669b",
                                   "6c8d6976-1c8b-4125-a68d-f2ee565fbcb1"]


# Ineligible Survey single select form field IDs
#
# Multi-Select Question: "How do you approach your practice as an artist, culture bearer, or culture maker"
ineligible_single_select_id_1    = "863c25a2-67b5-4f99-ae19-b9643df55cd5"  # I work as a solo artist
ineligible_single_select_id_2    = "f97aada7-9357-483e-8ae3-d3d53bffbfd5"  # I collaborate regularly with other artists
ineligible_single_select_id_3    = "de919207-0a93-4061-b51d-ef67b9e6c09c"  # I collaborate regularly with other non-arts practitioners
ineligible_single_select_id_4    = "12b4ac3b-46ce-4982-b3f9-f1223e9711e5"  # My practice requires public or community involvement to have meaning
ineligible_single_select_id_5    = "ab5d4e6b-ad1a-4be4-9204-25e774d6531f"  # Performing, presenting, or exhibiting to an audience or viewers is core to my practice.
ineligible_single_select_id_6    = "5d329ca2-a86f-459a-a5be-ff8aa234d5b3"  # # Teaching or educating others is core to my practice

# Multi-Select Question: "How do you currently earn money"
ineligible_single_select_id_7    = "90b7e584-a834-4bcd-948d-d0fcd90cdcdb"  # I have one or more part-time jobs (less than 30 hours per week)
ineligible_single_select_id_8    = "456c97ef-8c15-49d4-a1b5-8a337b1c180e"  # I have a full-time job (more than 30 hours per week)
ineligible_single_select_id_9    = "dcca3742-45c2-4e78-b606-4f3581d0a9e6"  # I have a series of gigs, contracts, and temporary jobs
ineligible_single_select_id_10   = "f2709e28-b611-4003-960e-48bea8f257f3"  # I am primarily or entirely supported by family or by my spouse/partner
ineligible_single_select_id_11   = "53286bb9-5075-4f1e-82b7-702f0fc3e8ea"  # I am currently unemployed
ineligible_single_select_id_12   = "fd74bf2d-0a64-4b0a-8f76-2ab943e33825"  # I earn 100% of my living through my art practice.
ineligible_single_select_id_13   = "d50ff3be-fdbf-4ff8-904e-1f978b89c73f"  # Other (please describe)

# Multi-Select Question: "How are your wages currently paid"
ineligible_single_select_id_14   = "696ba359-4add-4440-a8bb-e6c92658cfe3"  # I am an employee who receives an IRS Form W-2.
ineligible_single_select_id_15   = "25539d6c-1f43-4208-a3a1-5228ec879049"  # I am a freelance/independent contractor who receives an IRS Form 1099.
ineligible_single_select_id_16   = "34209196-e237-4218-a985-00aaa26f88e0"  # Both of the above.
ineligible_single_select_id_17   = "bfeaf8fb-0e19-4091-ad0a-8710c73ccdb3"  # I don’t know.
ineligible_single_select_id_18   = "02e8c4c9-4010-4293-b259-a9ecf2b62906"  # I prefer not to answer.

# Multi-Select Question: "What coalitions or causes do you actively participate in as a supporter or advocate"
ineligible_single_select_id_19   = "ea7016b8-2cb1-4dde-bc94-e97543f120b9"  # Arts/culture
ineligible_single_select_id_20   = "dc08eaa6-2ea5-497f-a538-cd6a20e9d00c"  # Childcare access
ineligible_single_select_id_21   = "5d5eb361-3279-4d5e-bb68-4865860d8103"  # Disability justice
ineligible_single_select_id_22   = "12337f3c-5352-4125-b9bf-26e9bcc80623"  # Economic justice"
ineligible_single_select_id_23   = "a3a8351a-92d1-49b2-8f85-5dce8f73f3c1"  # Environment/Climate justice
ineligible_single_select_id_24   = "8c2a052a-b907-4c97-89c8-721295fc2a82"  # Housing/Tenants’ rights
ineligible_single_select_id_25   = "8661d3e9-6a6f-415b-bcdc-d45e5dd6ad5d"  # Labor/Workers’ rights
ineligible_single_select_id_26   = "719e4858-ae83-461c-98aa-8a50c0be2734"  # Social and racial justice
ineligible_single_select_id_27   = "34ab9112-fc44-4ffb-ab66-52da1c9e9512"  # Other (please describe)
ineligible_single_select_id_28   = "e99d8475-185e-45ba-aed2-7aa842bd18c3"  # None at this time

# Multi-select Question: "At any time between March 2020 and February 2022, did you receive any kind of emergency financial assistance?
#                         If yes, which of the following types of emergency financial assistance did you receive"
ineligible_single_select_id_29   = "5ad1d3d8-369a-4417-bd8b-b453c4d6893c"  # Federal relief legislation (ie., American Rescue Plan, Paycheck Protection Program, etc.)
ineligible_single_select_id_30   = "324aa8fc-b383-4962-9d41-b15db5ef721b"  # Unemployment benefits
ineligible_single_select_id_31   = "6f2b503b-7d9c-4b60-a3a6-ee42a15bff22"  # An emergency grant
ineligible_single_select_id_32   = "1afaa147-deea-4450-87a1-bbfff0e7d5d9"  # Mutual aid or other grassroots contributions
ineligible_single_select_id_33   = "912a4ed5-ed5d-4ff8-a27f-e646ffcaa965"  # Family/personal assistance
ineligible_single_select_id_34   = "e864f113-01ef-4642-a4ed-0071184cd6e5"  # Other (please describe)

# Multi-Select Question: "How, if at all, was your employment impacted between March 2020 and February 2022"
ineligible_single_select_id_35   = "684036cc-6446-4b6f-85a7-5ab22c47ea93"  # I was furloughed or my hours were reduced.
ineligible_single_select_id_36   = "9353704c-33b2-4c2c-902c-010a70e76eb0"  # I was laid off or fired from a job.
ineligible_single_select_id_37   = "99e6b4cf-fca5-4dd9-836b-93e31cd4fbed"  # I left a job or reduced hours to attend to family caregiving.
ineligible_single_select_id_38   = "3328ca59-2a2c-421c-8f61-ce782f7f05f3"  # My freelance work, gigs, and/or contracts were canceled.
ineligible_single_select_id_39   = "8800cf19-6b10-4c51-b274-7aed30d71a17"  # My entire industry was shut down.
ineligible_single_select_id_40   = "b540ff2b-4e50-4a11-af76-b086d2a1e885"  # I started a new full-time or part-time job.
ineligible_single_select_id_41   = "b31647ed-1369-46fc-ae48-4fbf29f8fcd9"  # I picked up new freelance work, gigs, and/or contracts.
ineligible_single_select_id_42   = "4ebcb65f-7606-4501-a013-c00c3b8535a2"  # Other (please describe)
ineligible_single_select_id_43   = "6cd78b01-1534-4178-b015-06e0ced65c03"  # My employment was not affected by the pandemic.

# Multi-select Question: "How has your artistic practice been affected by the COVID19 pandemic"
ineligible_single_select_id_44   = "34d8975d-a1e8-45b9-a11c-5f3e8c4448ff"  # My scheduled exhibitions/shows/performances/gigs were canceled.
ineligible_single_select_id_45   = "54698e38-bb69-4794-bf9b-b65612d8b4a0"  # Canceled travel prevented me from attending my exhibitions/shows/performances/gigs.
ineligible_single_select_id_46   = "fdb5a5f8-4245-4cd7-883c-5f8d57760bdd"  # My studio/rehearsal space closed due to the pandemic.
ineligible_single_select_id_47   = "5123d201-d91d-4416-b38c-a2cb8fe02f37"  # I could no longer afford a studio/rehearsal space.
ineligible_single_select_id_48   = "b43e2e3a-4875-4fd0-ba01-b7c60b13c75a"  # I could no longer collaborate safely with others.
ineligible_single_select_id_49   = "14322e43-d0da-4d41-beb8-e5b1262d6239"  # I was less motivated to pursue my artistic practice.
ineligible_single_select_id_50   = "222d7389-42b0-402e-a86c-b12bcc346b03"  # I was more motivated to pursue my artistic practice.
ineligible_single_select_id_51   = "401cfe68-a777-490d-b2c4-a45c592ad407"  # I sought out new collaborators, communities, or professional networks.
ineligible_single_select_id_52   = "963a5e45-4250-42d3-8b7f-1daa66fc6a95"  # I evolved my artistic practice to address community needs.
ineligible_single_select_id_53   = "3a024b3c-bee7-4c51-a705-c692c83ab7b8"  # I embraced new opportunities to present my work online.
ineligible_single_select_id_54   = "0447e994-a41c-4e96-9845-0f3119e92e5d"  # I created a new series of work.
ineligible_single_select_id_55   = "01adb9c2-bb37-4ba6-a723-f1643e65051d"  # I picked up new exhibitions/shows/performances/gigs.
ineligible_single_select_id_56   = "d9a3944d-2540-4404-9a90-b96647545649"  # Other (please describe)
ineligible_single_select_id_57   = "199e45ec-8f61-4482-9eb3-ac2521ace593"  # My artistic practice was not impacted by the pandemic.

# Multi-select Question: "How, if at all, was your well-being impacted between March 2020 and February 2022"
ineligible_single_select_id_58   = "15be48e7-5d3b-4c55-857f-ffe62c7f328f"  # I experienced anxiety or depression.
ineligible_single_select_id_59   = "a791517e-eef6-499e-95a4-655a13aa795a"  # I experienced loneliness.
ineligible_single_select_id_60   = "17c2031a-36e8-4493-a0f3-45d818fc7cdd"  # I got sick.
ineligible_single_select_id_61   = "4556dee1-424b-46a7-9aa6-cdbf4a6e2cf8"  # I experienced food insecurity.
ineligible_single_select_id_62   = "5cf92c6d-199c-4530-a26d-250484d71fc1"  # I experienced housing insecurity.
ineligible_single_select_id_63   = "e2ef521d-6990-4e6b-a19a-298f0ba1df8c"  # I had to move.
ineligible_single_select_id_64   = "73d9a21a-77fc-49b5-aca7-5911ac36bbcb"  # I accumulated debt.
ineligible_single_select_id_65   = "12dd2f7f-dc70-495b-a285-a3be37f293e2"  # I became a part- or full-time caregiver.
ineligible_single_select_id_66   = "de1662a7-ee1e-4bda-88bc-09c2e8f15f8b"  # My self-care improved.
ineligible_single_select_id_67   = "74bd2a25-9b99-41f6-9299-6c97dc0a2a97"  # My mental health improved.
ineligible_single_select_id_68   = "584e5201-e626-47d8-8766-44c78c92784a"  # My physical health improved.
ineligible_single_select_id_69   = "27df2c5f-068f-4167-bcee-b35b42972346"  # Other (please describe):
ineligible_single_select_id_70   = "b5c16620-8484-43d0-8a01-85b7e79d4859"  # My well-being was not impacted by the pandemic.

# Multi-Select Question: "Which of the following best describes you"
ineligible_single_select_id_71   = "dbd9a5fc-f8ee-4486-a1d9-631952149f0e"  # Arab or Middle Eastern
ineligible_single_select_id_72   = "27f26774-0831-41ee-994a-ae5c642615f0"  # Asian or Pacific Islander
ineligible_single_select_id_73   = "b1bb0975-2256-442f-9f75-2fed4f8b1a17"  # Black or African American
ineligible_single_select_id_74   = "ff294db0-b3e5-4394-a859-5dcdfb3cd2ee"  # Hispanic or Latinx
ineligible_single_select_id_75   = "f642f43e-832f-4be9-9ebd-05f700b0ee36"  # Indigenous American, First Nation, or Alaska Native
ineligible_single_select_id_76   = "936c0d42-01ca-4356-89f2-5504c6d6d6b8"  # Pacific Islander or Native Hawaiian
ineligible_single_select_id_77   = "77002d8f-7d56-44f1-a3b6-262888449130"  # White
ineligible_single_select_id_78   = "1e6826d3-ada0-4161-92cf-e8673cdc7fc6"  # Other (please describe)
ineligible_single_select_id_79   = "13aa0a48-b6df-4d73-9996-f2ee48ef5eb8"  # I prefer not to answer

# Multi-Select Question: "What is your gender identity"
ineligible_single_select_id_80   = "ef768aeb-5ab9-4b11-bb22-42f03e569548"  # Man
ineligible_single_select_id_81   = "5592c59e-c3fe-42dc-8214-92ce7a1c6ef2"  # Woman
ineligible_single_select_id_82   = "78ecc6d2-8c6b-43ce-aaab-2cf769dfa89c"  # Non-binary
ineligible_single_select_id_83   = "8f6ef29b-12be-41c6-82a5-565ce2ff1f23"  # Two-spirit
ineligible_single_select_id_84   = "2ecfe0c1-9119-4874-a54e-4f71a9743e14"  # Other (please describe)
ineligible_single_select_id_85   = "af0c3735-020b-4c2d-840a-ad6ed569a4b0"  # I prefer not to answer

# Multi-Select Question: "Do you regularly provide care—either on your own or with someone else—to any of the following people"
ineligible_single_select_id_86   = "9b378d16-a1bf-4276-9197-fd9b19d16ea2"  # Yes, a child or children
ineligible_single_select_id_87   = "275673c7-fd28-4990-b9b1-c30e25643fb8"  # Yes, a spouse or partner who is elderly, ill, or disabled
ineligible_single_select_id_88   = "9ecb2f4f-82d1-4e93-8647-2e30fec87f76"  # Yes, an adult/adults who is/are elderly, ill, or disabled
ineligible_single_select_id_89   = "664cd79a-d2cc-4bf8-9f3f-60e7545c87b9"  # No
ineligible_single_select_id_90   = "3ae3d3c6-49ef-4e47-b52b-7b8ea21eeaf6"  # I prefer not to answer

# Ineligible Survey single select option field IDs
#
# Multi-Select Question: "How do you approach your practice as an artist, culture bearer, or culture maker"
ineligible_single_select_option_id_1     = "2fc98d0d-9b84-4850-8741-434b4c9b575a"  # I work as a solo artist
ineligible_single_select_option_id_2     = "7fe8aa91-2218-4d54-a5d1-64e455fab7ee"  # I collaborate regularly with other artists
ineligible_single_select_option_id_3     = "9586582e-f0d5-4831-b713-857294dd12c9"  # I collaborate regularly with other non-arts practitioners
ineligible_single_select_option_id_4     = "841c84fb-6f5f-4262-a92a-8e1aefca7691"  # My practice requires public or community involvement to have meaning
ineligible_single_select_option_id_5     = "1ab9d66e-80d6-4475-9983-6ff355fa455c"  # Performing, presenting, or exhibiting to an audience or viewers is core to my practice.
ineligible_single_select_option_id_6     = "0f0762f4-c514-43c8-ba6c-66bb0cedaa0f"  # Teaching or educating others is core to my practice

ineligible_single_select_option_id_7     = "f89526fa-2498-4855-900c-3db5415b5cdb"  # I have one or more part-time jobs (less than 30 hours per week)
ineligible_single_select_option_id_8     = "7e14cfc8-97ce-4dee-b1a6-e4341a6a3e10"  # I have a full-time job (more than 30 hours per week)
ineligible_single_select_option_id_9     = "101d5cf0-b230-4794-84fa-1c49bf8110b8"  # I have a series of gigs, contracts, and temporary jobs
ineligible_single_select_option_id_10    = "fd233f81-af2a-426b-bf81-ddf16afb8f1a"  # I am primarily or entirely supported by family or by my spouse/partner
ineligible_single_select_option_id_11    = "1e3abf6a-ce5a-4adf-8f5c-139f0e8400f7"  # I am currently unemployed
ineligible_single_select_option_id_12    = "3e9e9ccb-52e4-44fe-94ff-1e1b064ce15e"  # I earn 100% of my living through my art practice.
ineligible_single_select_option_id_13    = "43af3dbe-c4d4-4f2e-bf45-3f9caeed522b"  # Other (please describe)

# Multi-Select Question: "How are your wages currently paid"
ineligible_single_select_option_id_14   = "bfe85389-0716-43a9-927f-7eea06ed597a"  # I am an employee who receives an IRS Form W-2.
ineligible_single_select_option_id_15   = "5d7b106e-cae1-40f3-89b1-19cc8fe5f185"  # I am a freelance/independent contractor who receives an IRS Form 1099.
ineligible_single_select_option_id_16   = "6a3f30b0-d3c5-4fc0-932c-7605d3a37158"  # Both of the above.
ineligible_single_select_option_id_17   = "603b6c6c-98a2-41f1-b61f-362396c291ed"  # I don’t know.
ineligible_single_select_option_id_18   = "9db81bb5-f29f-44fd-8305-92680e2e0381"  # I prefer not to answer.

# Multi-Select Question: "What coalitions or causes do you actively participate in as a supporter or advocate"
ineligible_single_select_option_id_19   = "20c2af53-d156-4583-83ae-fbbfe109269e"  # Arts/culture
ineligible_single_select_option_id_20   = "b278197a-d5ba-4250-9592-9e3e7083e77b"  # Childcare access
ineligible_single_select_option_id_21   = "c43ee769-92fa-4e06-820b-c06c566f97ce"  # Disability justice
ineligible_single_select_option_id_22   = "6bdcb6d0-7be6-4058-b490-41024429f5bc"  # Economic justice
ineligible_single_select_option_id_23   = "455edd58-b803-482f-b4c2-7fd93e171d73"  # Environment/Climate justice
ineligible_single_select_option_id_24   = "167c16cf-feaf-40cc-8b73-124ebd9e78d5"  # Housing/Tenants’ rights
ineligible_single_select_option_id_25   = "2e304c5c-8ada-44ee-baa3-3af3f0eca0f9"  # Labor/Workers’ rights
ineligible_single_select_option_id_26   = "4b24cf25-6714-4d87-a723-1bbc6ea41e81"  # Social and racial justice
ineligible_single_select_option_id_27   = "7f2228ed-de41-4cdc-861d-7cbb5ec6fbc4"  # Other (please describe)
ineligible_single_select_option_id_28   = "a90fb0ef-493b-4e49-b3c1-45b5f8da7a29"  # None at this time

# Multi-select Question: "At any time between March 2020 and February 2022, did you receive any kind of emergency financial assistance? If yes, which of the following types of emergency financial assistance did you receive"
ineligible_single_select_option_id_29   = "977720cb-bcde-4e22-ad81-e01b0a1e55ff"  # Federal relief legislation (ie., American Rescue Plan, Paycheck Protection Program, etc.)
ineligible_single_select_option_id_30   = "257bb985-ae69-41fd-9f90-f244e6e47efe"  # Unemployment benefits
ineligible_single_select_option_id_31   = "2980b816-e124-4c6b-b6f7-10571c1d3800"  # An emergency grant
ineligible_single_select_option_id_32   = "4a6edd5c-9a7d-43e4-b48a-60e09f9a9516"  # Mutual aid or other grassroots contributions
ineligible_single_select_option_id_33   = "1f356e24-8209-4d53-b86e-1a3e6f1bc2d5"  # Family/personal assistance
ineligible_single_select_option_id_34   = "4c8a31dc-7965-4e71-9981-9a1b2cc0a867"  # Other (please describe)

# Multi-Select Question: "How, if at all, was your employment impacted between March 2020 and February 2022"
ineligible_single_select_option_id_35   = "b63a23de-88f4-4872-86e9-e2f71e9c03cc"  # I was furloughed or my hours were reduced.
ineligible_single_select_option_id_36   = "9ed3977e-f05e-47c5-931e-a7bce84e72ca"  # I was laid off or fired from a job.
ineligible_single_select_option_id_37   = "aedd6ac1-1ab0-4286-a50b-cdeab7151ebc"  # I left a job or reduced hours to attend to family caregiving.
ineligible_single_select_option_id_38   = "74e8a016-8c4a-4c6f-867a-19e6272ae339"  # My freelance work, gigs, and/or contracts were canceled.
ineligible_single_select_option_id_39   = "1ef7b860-371e-4f54-857d-871348143f00"  # My entire industry was shut down.
ineligible_single_select_option_id_40   = "d5ab5990-1e08-49c0-ab39-a94ee3adc05b"  # I started a new full-time or part-time job.
ineligible_single_select_option_id_41   = "af5d6f40-8e87-4f64-b45c-63c16598b9a9"  # I picked up new freelance work, gigs, and/or contracts.
ineligible_single_select_option_id_42   = "3ae9f53b-eff6-4484-805c-c21ccac21c6e"  # Other (please describe)
ineligible_single_select_option_id_43   = "372cb096-87db-4edf-9d98-50abd84a9461"  # My employment was not affected by the pandemic.

# Multi-select Question: "How has your artistic practice been affected by the COVID19 pandemic"
ineligible_single_select_option_id_44   = "a0960714-e90d-4a03-9cba-74d8330806d7"  # My scheduled exhibitions/shows/performances/gigs were canceled.
ineligible_single_select_option_id_45   = "77622f8e-280b-4947-95af-c84ca1fd543e"  # Canceled travel prevented me from attending my exhibitions/shows/performances/gigs.
ineligible_single_select_option_id_46   = "c05d4b0e-65e4-410b-b153-b6c2820b7ef8"  # My studio/rehearsal space closed due to the pandemic.
ineligible_single_select_option_id_47   = "fddd5045-983f-4484-a85c-29716bfd0ce0"  # I could no longer afford a studio/rehearsal space.
ineligible_single_select_option_id_48   = "0e525c3d-3ee3-4855-be06-80811baf84a3"  # I could no longer collaborate safely with others.
ineligible_single_select_option_id_49   = "abca4782-4210-4551-981d-74b307bd28f8"  # I was less motivated to pursue my artistic practice.
ineligible_single_select_option_id_50   = "1fbef054-99f9-46af-b67b-14f10ce34fcc"  # I was more motivated to pursue my artistic practice.
ineligible_single_select_option_id_51   = "eddabeb0-f331-4f4a-9dfe-b5bb9013ba21"  # I sought out new collaborators, communities, or professional networks.
ineligible_single_select_option_id_52   = "40e01e2a-0179-4bf8-8c9b-164bef385169"  # I evolved my artistic practice to address community needs.
ineligible_single_select_option_id_53   = "1a92ec94-77a3-4b0e-878a-54c32598dbb6"  # I embraced new opportunities to present my work online.
ineligible_single_select_option_id_54   = "dafe8bfa-8eca-42f2-b77a-35bbad25f78d"  # I created a new series of work.
ineligible_single_select_option_id_55   = "1ccbe759-a90a-420d-beb6-958cc387c3ee"  # I picked up new exhibitions/shows/performances/gigs.
ineligible_single_select_option_id_56   = "2a0c6dad-236c-4fd1-9ad7-38480265eb0f"  # Other (please describe)
ineligible_single_select_option_id_57   = "bdb37e15-1171-4f7a-aab9-82eca6d29687"  # My artistic practice was not impacted by the pandemic.

# Multi-select Question: "How, if at all, was your well-being impacted between March 2020 and February 2022"
ineligible_single_select_option_id_58   = "98ab27c7-8d49-4498-b3d0-5b92405ff638"  # I experienced anxiety or depression.
ineligible_single_select_option_id_59   = "1516363a-ecbb-48e9-8a5d-77be18831705"  # I experienced loneliness.
ineligible_single_select_option_id_60   = "a291e76f-e485-46b4-ad3d-cd5daed1a82d"  # I got sick.
ineligible_single_select_option_id_61   = "0927b04b-80ea-4b9e-bb66-298b518a4899"  # I experienced food insecurity.
ineligible_single_select_option_id_62   = "e332ec76-e687-4b73-b713-a08bcd1ca189"  # I experienced housing insecurity.
ineligible_single_select_option_id_63   = "39627fcb-4f15-4fb8-892a-309a3bec4d8f"  # I had to move.
ineligible_single_select_option_id_64   = "b96c8656-d9ea-45ed-9514-3bd932d4c8cb"  # I accumulated debt.
ineligible_single_select_option_id_65   = "cf062389-582a-46c3-b8a2-e93e21523847"  # I became a part- or full-time caregiver.
ineligible_single_select_option_id_66   = "09b277a0-628e-48f0-98a9-cef4d1582025"  # My self-care improved.
ineligible_single_select_option_id_67   = "0a499f96-cf62-4f00-b36c-d068304f320c"  # My mental health improved.
ineligible_single_select_option_id_68   = "47b9b98c-3e73-43fe-bbcb-5f9e3650c853"  # My physical health improved.
ineligible_single_select_option_id_69   = "f22312c4-94dd-4ed6-a2ec-a462eed28852"  # Other (please describe):
ineligible_single_select_option_id_70   = "969d360c-d926-4537-a4c4-60cf35717cc1"  # My well-being was not impacted by the pandemic.

#  Multi-Select Question: "Which of the following best describes you"
ineligible_single_select_option_id_71   = "9c790d51-c08c-4630-8de8-650fefdd7f73"  # Arab or Middle Eastern
ineligible_single_select_option_id_72   = "33bfd756-68e9-4481-8986-b7585bc04b88"  # Asian or Pacific Islander
ineligible_single_select_option_id_73   = "30bed219-d669-471d-beca-a09d1bf152fc"  # Black or African American
ineligible_single_select_option_id_74   = "1c2680ef-7222-47fe-93a4-127cfc3c2285"  # Hispanic or Latinx
ineligible_single_select_option_id_75   = "7f9c0e65-2983-4e2a-b530-7c8f83135d1c"  # Indigenous American, First Nation, or Alaska Native
ineligible_single_select_option_id_76   = "7832c635-ae2b-407c-afd9-e7bb7230aed6"  # Pacific Islander or Native Hawaiian
ineligible_single_select_option_id_77   = "9347685b-b39a-4045-9b5e-92b024755206"  # White
ineligible_single_select_option_id_78   = "1ff30422-f5bb-4dd1-bbfd-ee945c63f502"  # Other (please describe)
ineligible_single_select_option_id_79   = "e8fe5a2b-a445-43b8-9156-fb96fa902906"  # I prefer not to answer

# Multi-Select Question: "What is your gender identity"
ineligible_single_select_option_id_80  = "5cc64c48-ec92-475a-bfbf-dc09a7294e5f"  # Man
ineligible_single_select_option_id_81  = "146aeb7f-506e-465c-92e0-115c9569d47f"  # Woman
ineligible_single_select_option_id_82  = "acb58eab-cb62-4a03-a547-c612cbebce04"  # Non-binary
ineligible_single_select_option_id_83  = "09a490a5-8adf-4fd1-a79e-8734f9af0b04"  # Two-spirit
ineligible_single_select_option_id_84  = "1ff5ccd1-8103-49b8-81e5-88977ed2305b"  # Other (please describe)
ineligible_single_select_option_id_85  = "188fc04b-118f-4b28-a288-1440889d8530"  # I prefer not to answer

# Multi-Select Question: "Do you regularly provide care—either on your own or with someone else—to any of the following people"
ineligible_single_select_option_id_86  = "8f8b4d79-1c31-4b84-8fd5-a51adc619761"  # Yes, a child or children
ineligible_single_select_option_id_87  = "2e6dc0d4-6bc4-4a1f-ae1e-d90d491fc385"  # Yes, a spouse or partner who is elderly, ill, or disabled
ineligible_single_select_option_id_88  = "8ac92a6c-ddfa-49fb-ae9b-38473768dc29"  # Yes, an adult/adults who is/are elderly, ill, or disabled
ineligible_single_select_option_id_89  = "24f60998-6e9f-4a36-9eb6-31b7b5a933a9"  # No
ineligible_single_select_option_id_90  = "f8089702-01d3-4e27-a6b8-1e743b7fb828"  # I prefer not to answer


# AEP single select form field IDs
#
# Multi-Select Question: "At what scale do your services or programs operate"
aep_single_select_id_1    = "3eff3cb4-23fa-4759-b612-03fe068e1998"  # Local - Neighborhood","
aep_single_select_id_2    = "8def6090-f646-4ca1-9bfb-083fb8d33ce9"  # Local - City, Town or Tribe-wide
aep_single_select_id_3    = "32a425d5-2ac0-4c2b-a723-e089378e0d06"  # Regional
aep_single_select_id_4    = "4fb5034b-c7a2-41f9-8c8a-3b1255a02515"  # Statewide
aep_single_select_id_5    = "cea866f2-3a35-4a6e-ac77-5e9cf4e1a929"  # National

# Multi-Select Question: "How do you approach your practice as an artist, culture bearer, or culture maker""
aep_single_select_id_6    = "7438ab49-8e2b-407b-b1e1-d94fae78d447"  # I work as a solo artist.
aep_single_select_id_7    = "1cfb749a-081b-4c8c-ae89-c1654a4c4f1f"  # I collaborate regularly with other artists.
aep_single_select_id_8    = "2f391ae5-9d0c-4868-a993-00f416d25f74"  # I collaborate regularly with other non-arts practitioners.
aep_single_select_id_9    = "98fc2e30-d24e-4b12-8e6d-e1abf4925037"  # My practice requires public or community involvement to have meaning.
aep_single_select_id_10   = "ef1812a2-5ebd-4a49-a49e-a6692455eb02"  # Performing, presenting, or exhibiting to an audience or viewers is core to my practice.
aep_single_select_id_11   = "3646de59-ca6c-498e-bf20-b5d82e81b01a"  # Teaching or educating others is core to my practice.

# Multi-Select Question: "Which of the following best describes you"
aep_single_select_id_12   = "06f540c3-3c27-45dc-9815-e592e2fe787a"  # Arab or Middle Eastern
aep_single_select_id_13   = "d91465fa-7ec5-4336-9ba4-53a3170e05bc"  # Asian or Pacific Islander
aep_single_select_id_14   = "98ac3066-b172-4534-86df-03eb6a2c966e"  # Black or African American
aep_single_select_id_15   = "43fdba1a-7882-48d9-8fb8-b9e0bb089e0f"  # Hispanic or Latin
aep_single_select_id_16   = "ca981e5b-2624-42e3-9cdb-8b7a4b2597d9"  # Indigenous American, First Nation, or Alaska Native
aep_single_select_id_17   = "1df928e4-3616-45bb-a2a5-7b0ed5fc925b"  # Pacific Islander or Native Hawaiian
aep_single_select_id_18   = "a63275d1-ca64-458d-acf7-12c9684cb1e2"  # White
aep_single_select_id_19   = "e4e10aba-9338-42a8-83b8-a95f5037acb2"  # Other (please describe)
aep_single_select_id_20   = "3d9ecb7e-e46e-46cb-af7e-8f9133487dad"  # I prefer not to answer

# Multi-Select Question: "What is your gender identity"
aep_single_select_id_21  = "8049ef2a-d7a4-405e-a3a1-3eaaebce2ac4"  # Man
aep_single_select_id_22  = "db40cedf-ff2a-43d5-a6ca-18d3cfe3f3a5"  # Woman
aep_single_select_id_23  = "2dd53519-9e0e-4ebc-970c-2429bd1d7e77"  # Non-binary
aep_single_select_id_24  = "0566aeb2-dedc-434e-907d-1c9ca34ba717"  # Two-spirit
aep_single_select_id_25  = "cb0a572b-5057-4348-9d30-ed6b6f099a84"  # Other (please describe)
aep_single_select_id_26  = "78fe1ea5-9b7b-49f3-9b94-7183202fade0"  # I prefer not to answer

# Multi-Select Question: "Do you regularly provide care—either on your own or with someone else—to any of the following people"
aep_single_select_id_27  = "bbf19e6d-61c3-434c-87af-114c54c11def"  # Yes, a child or children
aep_single_select_id_28  = "16b36642-cab0-4436-add2-dec5c7718a98"  # Yes, a spouse or partner who is elderly, ill, or disabled
aep_single_select_id_29  = "718ad964-d30a-48a5-9626-1331ea2fcc80"  # Yes, an adult/adults who is/are elderly, ill, or disabled
aep_single_select_id_30  = "16837b39-40f2-4cb4-93fb-c4a02e166538"  # No
aep_single_select_id_31  = "a8d1d448-d6e4-406e-bfab-f5efbf14346d"  # I prefer not to answer

# Multi-Select Question: "In what capacity has your organization worked with artists"
aep_single_select_id_32  = "c32aa66b-ea23-4de6-9c3c-02d27da3aa21"  # As employees
aep_single_select_id_33  = "3248c498-659c-450b-8999-9c7d1434caaa"  # As independent contractors
aep_single_select_id_34  = "2cd0f97a-be0a-42ae-887a-10d5b622826a"  # As volunteers
aep_single_select_id_35  = "192af84a-318a-4f44-a58a-169d6b0f2e58"  # Other (please describe)

# Multi-Select Question: "Which of the following communities does your organization explicitly serve"
aep_single_select_id_36  = "dbbc74b7-80e7-415a-bc03-0da15ac23fa3"  # Black
aep_single_select_id_37  = "dac52a3d-912b-4711-976d-e0645031eaf1"  # Indigenous
aep_single_select_id_38  = "0c469697-f957-468a-8734-9fb5f1a626b8"  # People of Color
aep_single_select_id_39  = "ffc1bd07-7996-44d4-acd1-c3c21a2daefd"  # Immigrant
aep_single_select_id_40  = "badd4dfb-4b70-432d-914b-7282409bfbc9"  # LGBTQIAP+
aep_single_select_id_41  = "c700c696-666a-4777-942f-f244cf7b6488"  # Deaf/Disabled
aep_single_select_id_42  = "4ac315b2-16d0-44e9-af8d-a2b700f73f07"  # Low-income
aep_single_select_id_43  = "68bab605-618a-4ba4-9bd2-747b4a961852"  # Rural

# Multi-Select Question: "Which of the following did you receive"
aep_single_select_id_44  = "4e655440-79f6-43fd-ae3e-2e6da6d37599"  # Emergency/relief funding from the federal government
aep_single_select_id_45  = "8764f8ae-9dea-4b73-af1a-604ee306065c"  # Emergency/relief funding from the New York State government
aep_single_select_id_46  = "f9570ee9-f774-4c46-9618-ade8af6b3f35"  # Emergency/relief grant from philanthropy
aep_single_select_id_47  = "31978b15-f63b-4e3d-9efe-5335490a0262"  # Other (please describe)

# Multi-Select Question: "Do you have an existing benefits package for your current employees? If yes, does it include the following"
aep_single_select_id_48  = "a9a48cd3-138a-4b69-a9df-f2c6af05f233"  # Medical
aep_single_select_id_49  = "6682352d-3a68-4199-afaa-bc93496083c8"  # Dental
aep_single_select_id_50  = "8b158226-4c5d-4e3e-99aa-f205657ab83c"  # Vision
aep_single_select_id_51  = "d8bc30be-c831-46b0-8485-66507e55670a"  # Other (please describe)

# AEP single select option field IDs
#
# Multi-Select Question: "At what scale do your services or programs operate"
aep_single_select_option_id_1    = "c74860dc-edc5-41c5-8ccc-1bf6a38a28c8"  # Local - Neighborhood","
aep_single_select_option_id_2    = "44a6d63a-8eb1-4124-ab97-5ee863174995"  # Local - City, Town or Tribe-wide
aep_single_select_option_id_3    = "8c196e5e-8358-45a1-81ce-4312ea0d8d13"  # Regional
aep_single_select_option_id_4    = "72f2556d-e1fc-491f-9cf2-2744ed852fa8"  # Statewide
aep_single_select_option_id_5    = "ff9fb52e-8b2f-479d-b409-34a1be19074a"  # National

# Multi-Select Question: "How do you approach your practice as an artist, culture bearer, or culture maker""
aep_single_select_option_id_6    = "f8ebf08f-410b-4704-adaf-429d02e45f89"  # I work as a solo artist.
aep_single_select_option_id_7    = "c408c425-883b-4668-b143-f7b8d49e5d7e"  # I collaborate regularly with other artists.
aep_single_select_option_id_8    = "d456222c-cd01-414c-8c68-34e2b92a1925"  # I collaborate regularly with other non-arts practitioners.
aep_single_select_option_id_9    = "89e1081e-8c40-44da-93da-0f0914600bb1"  # My practice requires public or community involvement to have meaning.
aep_single_select_option_id_10   = "7ff6322d-a05e-4d1b-b262-15e332ee5292"  # Performing, presenting, or exhibiting to an audience or viewers is core to my practice.
aep_single_select_option_id_11   = "033a340c-b3fe-4293-99b8-8c52ac45e861"  # Teaching or educating others is core to my practice.

# Multi-Select Question: "Which of the following best describes you"
aep_single_select_option_id_12   = "33a72f37-db84-49b0-89b8-9139f535486c"  # Arab or Middle Eastern
aep_single_select_option_id_13   = "afdb991e-d07b-4430-a1ec-f9db4523879a"  # Asian or Pacific Islander
aep_single_select_option_id_14   = "492f1a74-04c9-4733-a0a8-c379a42d2c46"  # Black or African American
aep_single_select_option_id_15   = "31cb1636-4611-40d6-a7cc-d1dacc10e767"  # Hispanic or Latinx
aep_single_select_option_id_16   = "f9af8340-a200-4330-95d3-e3e76d59e3cd"  # Indigenous American, First Nation, or Alaska Native
aep_single_select_option_id_17   = "68cf34e2-99ee-431e-99e4-c33b4e290817"  # Pacific Islander or Native Hawaiian
aep_single_select_option_id_18   = "515bfe58-1a1b-428c-978f-52efe511a24a"  # White
aep_single_select_option_id_19   = "338f42bf-d429-45a8-ad36-0d09957f0159"  # Other (please describe)
aep_single_select_option_id_20   = "acd8d748-90c1-4128-a8e5-f71010532dcc"  # I prefer not to answer

# Multi-Select Question: "What is your gender identity"
aep_single_select_option_id_21  = "ec8838a5-4383-403d-91d7-18a86d4a991a"  # Man
aep_single_select_option_id_22  = "f008c61d-a896-47a8-8c50-6e147637cd59"  # Woman
aep_single_select_option_id_23  = "2ebd8295-37c8-4acc-9ef1-a06704c89e99"  # Non-binary
aep_single_select_option_id_24  = "2b3eccf8-1dd2-432f-9896-229a291eeb06"  # Two-spirit
aep_single_select_option_id_25  = "6610e8ea-c29a-492b-9884-899f90a51834"  # Other (please describe)
aep_single_select_option_id_26  = "65e47479-ef22-4915-96f8-830aee5171bb"  # I prefer not to answer

# Multi-Select Question: "Do you regularly provide care—either on your own or with someone else—to any of the following people"
aep_single_select_option_id_27  = "746bcec4-c739-45ca-aeda-9940c422471f"  # Yes, a child or children
aep_single_select_option_id_28  = "a2472a7f-e4de-47fa-b538-71955265aea2"  # Yes, a spouse or partner who is elderly, ill, or disabled
aep_single_select_option_id_29  = "6400e7ab-6fd4-48c7-a79c-10180aa017a1"  # Yes, an adult/adults who is/are elderly, ill, or disabled
aep_single_select_option_id_30  = "001d2051-b56a-4ed2-95e7-709f72dd8c09"  # No
aep_single_select_option_id_31  = "45796f76-8a48-4273-8540-9968f9b76072"  # I prefer not to answer

# Multi-Select Question: "In what capacity has your organization worked with artists"
aep_single_select_option_id_32   = "6707fe72-e1e1-4a33-9367-535395d0df52"  # As employees
aep_single_select_option_id_33   = "787ff70d-4d72-4e82-90c5-9e61837c3e2c"  # As independent contractors
aep_single_select_option_id_34   = "70b669f7-600e-47b1-b6fc-7f4ab94e4ebf"  # As volunteers
aep_single_select_option_id_35   = "872160c8-5f3e-414f-9850-d5115c39d32b"  # Other (please describe)

# Multi-Select Question: "Which of the following communities does your organization explicitly serve"
aep_single_select_option_id_36  = "4464c10d-8435-457d-a581-4d3bcdb6e9cb"  # Black
aep_single_select_option_id_37  = "76fae860-614a-4032-bf09-3b837a02c52f"  # Indigenous
aep_single_select_option_id_38  = "f50248c6-6561-46f3-84bf-6a534d4078e3"  # People of Color
aep_single_select_option_id_39  = "dd63ba80-a6f8-4b59-ac0a-32f8c0496f1e"  # Immigrant
aep_single_select_option_id_40  = "3375b363-253c-4f19-9bf9-c7a402cdd3cb"  # LGBTQIAP+
aep_single_select_option_id_41  = "c97bfccd-c4f4-4212-a837-9eb19a22feaa"  # Deaf/Disabled
aep_single_select_option_id_42  = "c9ed01f8-0493-4ae2-90d3-94757f7d7400"  # Low-income
aep_single_select_option_id_43  = "07dd47e0-9745-4f4a-b4f0-f8f0686ac66e"  # Rural

# Multi-Select Question: "Which of the following did you receive"
aep_single_select_option_id_44  = "c44abfd1-3103-4414-8eba-dfc5227cf8a7"  # Emergency/relief funding from the federal government
aep_single_select_option_id_45  = "9c1e527d-f9e8-4299-8fc2-50100b4d75a9"  # Emergency/relief funding from the New York State government
aep_single_select_option_id_46  = "712e609f-e018-4edd-aece-2fee5146b754"  # Emergency/relief grant from philanthropy
aep_single_select_option_id_47  = "922a2da3-bd80-4942-8e97-88fd8429408f"  # Other (please describe)

# Multi-Select Question: "Do you have an existing benefits package for your current employees? If yes, does it include the following"
aep_single_select_option_id_48  = "43e85796-f26e-4632-975d-2fc878881798"  # Medical
aep_single_select_option_id_49  = "dc9e6491-7f24-4628-b52b-04e188e99acc"  # Dental
aep_single_select_option_id_50  = "b98ac5b5-922a-4f7f-8a42-08d26deb87da"  # Vision
aep_single_select_option_id_51  = "a67f0d8d-07e6-4884-bf00-7c991204d408"  # Other (please describe)



# GI single select internal form IDs
#
# single select option IDs for Multi-Select Question: "Which of the following best describes you"
gi_single_select_id_1   = "e6a80c04-cf00-457a-85be-0cc6f51c2995"  # Arab or Middle Eastern
gi_single_select_id_2   = "b2795b62-e1b3-4047-b0f0-f31588fed67b"  # Asian or Pacific Islander
gi_single_select_id_3   = "a25caf1b-fee2-4b4f-a27a-63e0b6faea5b"  # Black or African American
gi_single_select_id_4   = "b0743141-f015-4759-a578-7482a4c877b4"  # Hispanic or Latinx
gi_single_select_id_5   = "16c84bc2-86f6-4b0d-acd2-c49f2732327d"  # Indigenous American, First Nation, or Alaska Native
gi_single_select_id_6   = "f71879c2-396d-443e-b3f5-d60437d0ef2e"  # Pacific Islander or Native Hawaiian
gi_single_select_id_7   = "f16f7b78-fe33-4609-980d-ff268be39835"  # White
gi_single_select_id_8   = "28a9e701-a7a9-4c84-96aa-0490abc359a0"  # Other (please describe)
gi_single_select_id_9   = "35f2ac42-cfe4-4371-acc2-9b25a34922b3"  # I prefer not to answer

# single select option IDs for Multi-Select Question: "What is your gender identity"
gi_single_select_id_10  = "0949f954-52f5-47be-8f1f-0e7b075b3e8f"  # Man
gi_single_select_id_11  = "be120d7c-e8dd-4c4a-941e-b43e02925c30"  # Woman
gi_single_select_id_12  = "ba5dfe25-c185-4c88-8291-8756f1d8bc2b"  # Non-binary
gi_single_select_id_13  = "ffdd8269-10d4-42f7-a90f-da6ba193d9d9"  # Two-spirit
gi_single_select_id_14  = "18258d27-6266-4c47-8046-c7241423bf6f"  # Other (please describe)
gi_single_select_id_15  = "6f75a9e0-b467-4716-8ffe-85f7f58a98e4"  # I prefer not to answer

# single select option IDs for Multi-Select Question: "Do you regularly provide care—either on your own or with someone else—to any of the following people"
gi_single_select_id_16  = "4e20af02-3c70-42ee-8802-162d3b32bdab"  # Yes, a child or children
gi_single_select_id_17  = "530d6138-73fa-4f6c-a7c3-05a4fbf8cde5"  # Yes, a spouse or partner who is elderly, ill, or disabled
gi_single_select_id_18  = "066bb242-7846-4711-9caa-eba2d3139cb7"  # Yes, an adult/adults who is/are elderly, ill, or disabled
gi_single_select_id_19  = "8f26e1d7-d930-4713-b707-3c09188496f8"  # No
gi_single_select_id_20  = "a5d195e8-f9a9-4de9-8017-1e5c84c490b5"  # I prefer not to answer

# single select option IDs for Multi-Select Question: "Please check all that apply regarding your financial safety net"
gi_single_select_id_22  = "4353d9e7-d667-4cef-83af-8d49faa600d8"
gi_single_select_id_23  = "9da6b73d-6795-4f0d-8f56-6da65d78783b"
gi_single_select_id_24  = "4f81b635-c1e2-4565-82fd-3ad0c7511cd0"
gi_single_select_id_25  = "c4379de6-8c00-45c1-83af-9bdef092678c"

# Multi-Select Question: "How do you approach your practice as an artist, culture bearer, or culture maker""
gi_single_select_id_26   = "80aefb5f-67da-4cc5-97c3-929699d8917e"  # I work as a solo artist.
gi_single_select_id_27   = "88576fc2-a677-4a4d-a56b-3b610c201b68"  # I collaborate regularly with other artists.
gi_single_select_id_28   = "31e90ca4-4865-4037-9971-80df68e70260"  # I collaborate regularly with other non-arts practitioners.
gi_single_select_id_29   = "14487b0b-4d81-4bf9-8bb3-33d6c28584f5"  # My practice requires public or community involvement to have meaning.
gi_single_select_id_30   = "9311dd9f-1498-46d6-b192-a025a25f7e41"  # Performing, presenting, or exhibiting to an audience or viewers is core to my practice.
gi_single_select_id_31   = "1128dd7b-00cb-4728-a70f-263ee0632ba4"  # Teaching or educating others is core to my practice.

# Multi-Select Question: "To the best of your knowledge, in which of the following are you currently enrolled"
gi_single_select_id_32   = "149d1620-2324-41a2-9779-8853b4532325"  # Childcare Subsidy (CCDF)
gi_single_select_id_33   = "f8e760ec-7a8e-44d3-be66-ad777738d7e2"  # Head Start/Early Head Start
gi_single_select_id_34   = "9fff7afb-92bc-4339-b13a-01339ecabd29"  # Supplemental Nutrition Assistance Program (SNAP)
gi_single_select_id_35   = "215ec455-54ca-42f4-9e45-5c96f49f453c"  # Women, Infants, and Children Nutrition Program (WIC)
gi_single_select_id_36   = "e06bd276-4990-4de6-b0cb-8203a72b19db"  # Section 8 Housing Voucher
gi_single_select_id_37   = "fc125909-3d8e-452a-9c52-7b82e46cc6da"  # Health Insurance Marketplace Subsidies
gi_single_select_id_38   = "4cedcbdf-38bc-41d1-bc66-18afb595c8d8"  # Medicaid for Adults and Child Health Plus
gi_single_select_id_39   = "2df2a40b-78dc-4541-9e26-edb96d43c9b8"  # Earned Income Tax Credit (EITC)
gi_single_select_id_40   = "a864eabe-8329-45f7-92a6-b7a6c660e3c6"  # Child Tax Credit (CTC)
gi_single_select_id_41   = "593dbb2f-d405-402a-a2a5-2041c98498bf"  # Federal Child and Dependent Care Tax Credit (CDCTC)
gi_single_select_id_42   = "27c6b983-b5b1-4f25-97fa-87d33d97e0d4"  # Temporary Cash Assistance (TANF)
gi_single_select_id_43   = "fd1126f2-207a-47fd-bff6-892c629bd734"  # Supplemental Security Income (SSI)
gi_single_select_id_44   = "7f7db88c-c36f-439a-be2c-d38b7ca10632"  # Social Security Disability Insurance (SSDI)
gi_single_select_id_45   = "931614b2-78b9-40ca-bbab-fdd914de5dc1"  # Other (please describe)


# GI single select option IDs
#
# Multi-Select Question: "Which of the following best describes you"
gi_single_select_option_id_1   = "e6a80c04-cf00-457a-85be-0cc6f51c2995"  # Arab or Middle Eastern
gi_single_select_option_id_2   = "b2795b62-e1b3-4047-b0f0-f31588fed67b"  # Asian or Pacific Islander
gi_single_select_option_id_3   = "a25caf1b-fee2-4b4f-a27a-63e0b6faea5b"  # Black or African American
gi_single_select_option_id_4   = "b0743141-f015-4759-a578-7482a4c877b4"  # Hispanic or Latinx
gi_single_select_option_id_5   = "16c84bc2-86f6-4b0d-acd2-c49f2732327d"  # Indigenous American, First Nation, or Alaska Native
gi_single_select_option_id_6   = "f71879c2-396d-443e-b3f5-d60437d0ef2e"  # Pacific Islander or Native Hawaiian
gi_single_select_option_id_7   = "f16f7b78-fe33-4609-980d-ff268be39835"  # White
gi_single_select_option_id_8   = "28a9e701-a7a9-4c84-96aa-0490abc359a0"  # Other (please describe)
gi_single_select_option_id_9   = "35f2ac42-cfe4-4371-acc2-9b25a34922b3"  # I prefer not to answer

# Multi-Select Question: "What is your gender identity"
gi_single_select_option_id_10  = "0949f954-52f5-47be-8f1f-0e7b075b3e8f"  # Man
gi_single_select_option_id_11  = "be120d7c-e8dd-4c4a-941e-b43e02925c30"  # Woman
gi_single_select_option_id_12  = "ba5dfe25-c185-4c88-8291-8756f1d8bc2b"  # Non-binary
gi_single_select_option_id_13  = "ffdd8269-10d4-42f7-a90f-da6ba193d9d9"  # Two-spirit
gi_single_select_option_id_14  = "18258d27-6266-4c47-8046-c7241423bf6f"  # Other (please describe)
gi_single_select_option_id_15  = "6f75a9e0-b467-4716-8ffe-85f7f58a98e4"  # I prefer not to answer

# Multi-Select Question: "Do you regularly provide care—either on your own or with someone else—to any of the following people"
gi_single_select_option_id_16  = "4e20af02-3c70-42ee-8802-162d3b32bdab"  # Yes, a child or children
gi_single_select_option_id_17  = "530d6138-73fa-4f6c-a7c3-05a4fbf8cde5"  # Yes, a spouse or partner who is elderly, ill, or disabled
gi_single_select_option_id_18  = "066bb242-7846-4711-9caa-eba2d3139cb7"  # Yes, an adult/adults who is/are elderly, ill, or disabled
gi_single_select_option_id_19  = "8f26e1d7-d930-4713-b707-3c09188496f8"  # No
gi_single_select_option_id_20  = "a5d195e8-f9a9-4de9-8017-1e5c84c490b5"  # I prefer not to answer

# Multi-Select Question: "Please check all that apply regarding your financial safety net"
gi_single_select_option_id_22  = "4353d9e7-d667-4cef-83af-8d49faa600d8"
gi_single_select_option_id_23  = "9da6b73d-6795-4f0d-8f56-6da65d78783b"
gi_single_select_option_id_24  = "4f81b635-c1e2-4565-82fd-3ad0c7511cd0"
gi_single_select_option_id_25  = "c4379de6-8c00-45c1-83af-9bdef092678c"

# Multi-Select Question: "How do you approach your practice as an artist, culture bearer, or culture maker""
gi_single_select_option_id_26   = "4970981e-637d-4fda-951a-da59bf2e9772"  # I work as a solo artist.
gi_single_select_option_id_27   = "9a15a7a8-0606-425e-9e2e-231665046361"  # I collaborate regularly with other artists.
gi_single_select_option_id_28   = "e91dc053-16d6-4be9-abdc-4014eaaab5f9"  # I collaborate regularly with other non-arts practitioners.
gi_single_select_option_id_29   = "5273ee24-d766-4bb2-aa8b-b1c733eeb389"  # My practice requires public or community involvement to have meaning.
gi_single_select_option_id_30   = "dba5d6f7-4bc2-4bd7-b71f-404913871001"  # Performing, presenting, or exhibiting to an audience or viewers is core to my practice.
gi_single_select_option_id_31   = "8c55765a-a256-4fd5-a59c-783c28c084df"  # Teaching or educating others is core to my practice.

# Multi-Select Question: "To the best of your knowledge, in which of the following are you currently enrolled"
gi_single_select_option_id_32   = "ef897392-9867-4be0-997f-c73830f15b58"  # Childcare Subsidy (CCDF)
gi_single_select_option_id_33   = "a8f99dde-421b-4611-aac2-0edaa0fb6b80"  # Head Start/Early Head Start
gi_single_select_option_id_34   = "58545058-5442-48bf-b2f8-9f896284732a"  # Supplemental Nutrition Assistance Program (SNAP)
gi_single_select_option_id_35   = "0d0e404f-aaab-4b5a-baae-47ff623e556f"  # Women, Infants, and Children Nutrition Program (WIC)
gi_single_select_option_id_36   = "751cdc09-b490-424a-af0c-79a8a15a6cd8"  # Section 8 Housing Voucher
gi_single_select_option_id_37   = "0e4dfa72-c70b-4216-bad7-d4b7102e41f3"  # Health Insurance Marketplace Subsidies
gi_single_select_option_id_38   = "3d25e53e-b882-4f6e-b4c6-37e43ea2cb7d"  # Medicaid for Adults and Child Health Plus
gi_single_select_option_id_39   = "b31d84b3-1120-473b-b4ec-c2bb28e4123f"  # Earned Income Tax Credit (EITC)
gi_single_select_option_id_40   = "eee826b5-97a9-4b97-8f41-8be1549c784f"  # Child Tax Credit (CTC)
gi_single_select_option_id_41   = "bf13a3c1-be60-4f3b-8eac-ef4e4e2c2889"  # Federal Child and Dependent Care Tax Credit (CDCTC)
gi_single_select_option_id_42   = "7118ac33-bfe5-404c-8915-8e7be6452f75"  # Temporary Cash Assistance (TANF)
gi_single_select_option_id_43   = "fe2145f5-ab6e-47d5-aad1-f8bcd9f992b2"  # Supplemental Security Income (SSI)
gi_single_select_option_id_44   = "7f7db88c-c36f-439a-be2c-d38b7ca10632"  # Social Security Disability Insurance (SSDI)
gi_single_select_option_id_45   = "2d305547-b86c-4fe0-b10c-fcadbd5c479f"  # Other (please describe)


# Application Survey single select internal form IDs
#
# Multi-Select Question: "How do you currently earn money"
app_single_select_id_1  = "8c248661-1741-4881-86ca-4465778c4e5b"  # I have one or more part-time jobs (less than 30 hours per week).
app_single_select_id_2  = "17b35347-4bb5-4709-ac06-d3fae7915e53"  # I have a full-time job (more than 30 hours per week).
app_single_select_id_3  = "beaf260d-d343-4137-87b6-86ab754d684c"  # I have a series of gigs, contracts, and temporary jobs.
app_single_select_id_4  = "3b1b8d34-827b-48d2-af7f-04d3b12f9414"  # I am primarily or entirely supported by family or by my spouse/partner.
app_single_select_id_5  = "f43e4360-1325-4151-b64c-433bcda0fc06"  # I am currently unemployed.
app_single_select_id_6  = "5924ad30-6bd6-4350-bdcd-342beb3e43bf"  # I earn 100% of my living through my art practice.
app_single_select_id_7  = "cc7a4e97-d5be-4860-8f2b-839a5e1c8b5c"  # Other (please describe)

# Multi-Select Question: "How are your wages currently paid"
app_single_select_id_8   = "982a50a9-42f8-4576-af22-20adbc8f4ae0"  # I am an employee who receives an IRS Form W-2.
app_single_select_id_9   = "e79adbdb-7c73-4270-8fd3-f0f059ac2265"  # I am a freelance/independent contractor who receives an IRS Form 1099.
app_single_select_id_10  = "41fc2c88-24d7-434c-abd2-0bf5b1a1356c"  # Both of the above.
app_single_select_id_11  = "c482f3c2-cf4b-4ad7-872a-65c145a2baff"  # I don’t know.
app_single_select_id_12  = "6c7b3471-d9e5-4c7c-a878-149ac1f65dfc"  # I prefer not to answer.

# Multi-Select Question: "What coalitions or causes do you actively participate in as a supporter or advocate"
app_single_select_id_13  = "405bbe3e-e269-46ab-bbf4-e52f4eadd5cf"  # Arts/culture
app_single_select_id_14  = "193f2a2a-39dc-4131-b3e8-3811637119c0"  # Childcare access
app_single_select_id_15  = "52eb869f-71fa-4b1d-95a0-2f64af914863"  # Disability justice
app_single_select_id_16  = "555c13aa-1748-487d-bac6-a4cb7684277c"  # Economic justice
app_single_select_id_17  = "475e4b0b-2a24-43be-b17e-056990572bf8"  # Environment/climate justice
app_single_select_id_18  = "d1be6396-ab45-495e-8112-6bbe9354589e"  # Housing/tenants’ rights
app_single_select_id_19  = "7a44a715-9923-4749-a467-c0672922665d"  # Labor/workers’ rights
app_single_select_id_20  = "2b0deb84-9b6f-47b9-a6a3-05e1ad9dbef9"  # Social and racial justice
app_single_select_id_21  = "9b5b3210-f04c-4b1e-91e1-1a3b1ddfa587"  # Other (please describe)
app_single_select_id_22  = "bc4f7002-8d04-4feb-b8c9-aec226779954"  # None at this time

# Multi-Select Question: "At any time between March 2020 and February 2022, did you receive any kind of emergency financial assistance?
# If yes, which of the following types of emergency financial assistance did you receive"
app_single_select_id_23  = "39dc0c91-45e8-4046-91fa-54c44b37e409"  # Federal relief legislation (ie., American Rescue Plan, Paycheck Protection Program, etc.)
app_single_select_id_24  = "e151f0db-3186-4c64-b84c-c3106c0a5ce6"  # Unemployment benefits
app_single_select_id_25  = "750e9ed7-0bd7-44b9-adf6-3379cd1d8df7"  # An emergency grant
app_single_select_id_26  = "53356f73-bc84-43ac-8eb7-0f0fc6a8dc35"  # Mutual aid or other grassroots contributions
app_single_select_id_27  = "f6da2e28-ea24-4378-9ce2-d1bfe8200bea"  # Family/personal assistance
app_single_select_id_28  = "3bc30197-f7de-4d60-95f7-ac4faac161ee"  # Other (please describe)

# Multi-Select Question: "How, if at all, was your employment impacted between March 2020 and February 2022"
app_single_select_id_29  = "2e1e09cc-691b-411f-9407-4ea87f1884d5"  # I was furloughed or my hours were reduced.
app_single_select_id_30  = "a9cb4148-ff4c-4cf3-8948-0c20d3230c6b"  # I was laid off or fired from a job.
app_single_select_id_31  = "9c10bb27-1032-46b6-9da2-5fe292261528"  # I left a job or reduced hours to attend to family caregiving.
app_single_select_id_32  = "56ca5435-b31f-4cd9-8922-9d3324228db8"  # "My freelance work, gigs, and/or contracts were canceled.
app_single_select_id_33  = "39a6f069-d818-46da-ba61-20cbd6429931"  # My entire industry was shut down.
app_single_select_id_34  = "2bdd01b5-2ea9-44b2-a35e-44105c0b077b"  # I started a new full-time or part-time job.
app_single_select_id_35  = "918791f6-945c-4f21-ae02-67e8cc96d7a9"  # I picked up new freelance work, gigs, and/or contracts.
app_single_select_id_36  = "06743904-8fe3-4745-aa86-da89667c5e23"  # Other (please describe)
app_single_select_id_37  = "50bbc3e8-70eb-4c96-a641-8f65b38f1125"  # My employment was not affected by the pandemic.

# Multi-Select Question: "How, if at all, was your artistic practice impacted between March 2020 and February 2022"
app_single_select_id_38  = "e195054b-cddb-46da-8a07-cb4b492aa090"   # My scheduled exhibitions/shows/performances/gigs were canceled.
app_single_select_id_39  = "e57e6e6e-4123-48b2-a852-c2be960de850"  # Canceled travel prevented me from attending my exhibitions/shows/performances/gigs.
app_single_select_id_40  = "71c7149f-01b6-4d17-8b36-fdc3b0bf10c5"  # My studio/rehearsal space closed due to the pandemic.
app_single_select_id_41  = "83285d24-4c23-4166-97b2-3dab006ebdbe"  # I could no longer afford a studio/rehearsal space.
app_single_select_id_42  = "453b0a3e-8e81-4aa2-97d8-13e7349edaa1"  # I could no longer collaborate safely with others.
app_single_select_id_43  = "5f55268c-79b8-4709-b05e-d8e93c6193f5"  # I was less motivated to pursue my artistic practice.
app_single_select_id_44  = "3185b9c5-4cc0-45a6-9a2f-12848ccf5244"  # I was more motivated to pursue my artistic practice.
app_single_select_id_45  = "23a3eed0-9d01-4f2c-901d-918cddc772f6"  # I sought out new collaborators, communities, or professional networks.
app_single_select_id_46  = "21bdb5c5-9de2-4351-a9a8-04d59c14b0d0"  # I evolved my artistic practice to address community needs.
app_single_select_id_47  = "49ce1f80-afa3-4080-94ef-d1fc68dcd044"  # I embraced new opportunities to present my work online.
app_single_select_id_48  = "22e40f50-e60e-4215-8e2a-34ccd2766fcb"  # I created a new series of work.
app_single_select_id_49  = "d1ec8e15-3ad7-4d87-b235-9f0a238e7aee"  # I picked up new exhibitions/shows/performances/gigs.
app_single_select_id_50  = "bd58be3b-008d-4bcd-a2a7-36fe5bdaddda"  # Other (please describe)
app_single_select_id_51  = "a2da604c-b576-441f-b901-64a7d18b96d8"  # My artistic practice was not impacted by the pandemic

# Multi-Select Question: "How, if at all, was your well-being impacted between March 2020 and February 2022"
app_single_select_id_52  = "bab5bf4d-c177-431b-a74c-86384727610c"  # I experienced anxiety or depression.
app_single_select_id_53  = "ac059e3e-28ea-48e4-8948-e2a41346c336"  # I experienced loneliness.
app_single_select_id_54  = "4c734bd1-307c-4952-bdd6-ce5be9630f29"  # I got sick.
app_single_select_id_55  = "eb24de5b-16cf-4aa3-88e3-5d5e46124036"  # I experienced food insecurity.
app_single_select_id_56  = "c33e0100-18bd-48cc-9629-7f9981367afe"  # I experienced housing insecurity.
app_single_select_id_57  = "31a80e92-7cba-43a1-b9b2-4d86c31c19a8"  # I had to move.
app_single_select_id_58  = "a0cc2cd1-ce65-4256-8528-f16008a8c74f"  # I accumulated debt.
app_single_select_id_59  = "fcf8d174-b395-4488-b5ff-1068e5bcff76"  # I became a part- or full-time caregiver
app_single_select_id_60  = "dcd5ef0f-a7e2-4495-87d2-7f32e206f650"  # My self-care improved.
app_single_select_id_61  = "2fddd4cc-2ea4-46a0-ab2f-79313375813b"  # My mental health improved.
app_single_select_id_62  = "eb8b30ca-4a57-4c4f-a860-8eeab7e2151b"  # My physical health improved.
app_single_select_id_63  = "144312cd-3dca-44fb-93d8-800fb29bc066"  # Other (please describe)
app_single_select_id_64  = "ab35ad5f-127b-44d8-9ff9-497635064682"  # My well-being was not impacted by the pandemic.


# Application Survey single select option IDs
#
# Multi-Select Question: "How do you currently earn money"
app_single_select_option_id_1   = "231aa812-b746-41ec-9992-d771108f4cd4"  # I have one or more part-time jobs (less than 30 hours per week).
app_single_select_option_id_2   = "5811efa8-3c73-48f7-b0fc-06f47720054f"  # I have a full-time job (more than 30 hours per week).
app_single_select_option_id_3   = "334d9aa3-9b05-476d-9700-b3635a1773a6"  # I have a series of gigs, contracts, and temporary jobs.
app_single_select_option_id_4   = "e2ebb6ee-78e7-4cce-be79-ee0744de9d46"  # I am primarily or entirely supported by family or by my spouse/partner.
app_single_select_option_id_5   = "5519c0b3-1e22-438b-ba1c-3f6055474dac"  # I am currently unemployed.
app_single_select_option_id_6   = "76b6eeab-0488-4812-ae86-809b6492fa4c"  # I earn 100% of my living through my art practice.
app_single_select_option_id_7   = "3807199c-3af2-4ee0-bc51-ac134c4dd407"  # Other (please describe)

# Multi-Select Question: "How are your wages currently paid"
app_single_select_option_id_8   = "46783581-3211-43f7-a4d8-43f574b2c2ba"  # I am an employee who receives an IRS Form W-2.
app_single_select_option_id_9   = "d1f93404-69c9-4ba0-84a2-171143c44529"  # I am a freelance/independent contractor who receives an IRS Form 1099.
app_single_select_option_id_10  = "5070649f-2c65-4a68-9099-2f6452865e47"  # Both of the above.
app_single_select_option_id_11  = "db513a3c-3210-4b7c-9bfa-04b0027ca9bd"  # I don’t know.
app_single_select_option_id_12  = "c7a58e63-d406-4152-a619-655b2d465d73"  # I prefer not to answer.

# Multi-Select Question: "What coalitions or causes do you actively participate in as a supporter or advocate"
app_single_select_option_id_13  = "69cc4226-1b17-488d-877a-79eaa322b1ce"  # Arts/culture
app_single_select_option_id_14  = "8eaebb71-acef-49c3-8fb2-0530cc97dab7"  # Childcare access
app_single_select_option_id_15  = "f1c588d1-ef95-4d5c-9d02-baf5e53ce7eb"  # Disability justice
app_single_select_option_id_16  = "a8a53e41-61b2-41bc-aa51-09371777e414"  # Economic justice
app_single_select_option_id_17  = "c0559d32-c926-4dc9-871c-54981cac2a08"  # Environment/climate justice
app_single_select_option_id_18  = "5018918f-5bd8-4a45-9384-28a301684dcc"  # Housing/tenants’ rights
app_single_select_option_id_19  = "9b8555ac-af1d-4e3a-be36-3e112df233bd"  # Labor/workers’ rights
app_single_select_option_id_20  = "7f23af6b-8678-44f2-9a6b-267014b0948b"  # Social and racial justice
app_single_select_option_id_21  = "9079facb-3cdf-45ea-8273-9f8ad33a0a61"  # Other (please describe)
app_single_select_option_id_22  = "c031796d-dcd0-475f-97e2-a99cc1bdac0c"  # None at this time

# Multi-Select Question: "At any time between March 2020 and February 2022, did you receive any kind of emergency financial assistance?
# If yes, which of the following types of emergency financial assistance did you receive"
app_single_select_option_id_23  = "cb5d1632-01d8-4749-9550-c158cf9bf033"  # Federal relief legislation (ie., American Rescue Plan, Paycheck Protection Program, etc.)
app_single_select_option_id_24  = "e35dab1c-9c27-4df5-a2aa-ca4b74753b13"  # Unemployment benefits
app_single_select_option_id_25  = "fe8f4cc0-7fbf-4b00-9103-43f4e1bc88fc"  # An emergency grant
app_single_select_option_id_26  = "c2ea295b-20fd-4e83-8515-b7195234c585"  # Mutual aid or other grassroots contributions
app_single_select_option_id_27  = "4d8fdff6-2c52-4d31-8413-ad81f83bae37"  # Family/personal assistance
app_single_select_option_id_28  = "9853c865-9bd1-4cac-8603-f796098f1083"  # Other (please describe)

# Multi-Select Question: "How, if at all, was your employment impacted between March 2020 and February 2022"
app_single_select_option_id_29  = "475a32f5-d803-41fe-84cd-4f79ededb1eb"  # I was furloughed or my hours were reduced.
app_single_select_option_id_30  = "c1513747-7778-477f-82c6-9da796f33062"  # I was laid off or fired from a job.
app_single_select_option_id_31  = "4acb7623-51aa-4b7c-b112-8cc2faa34452"  # I left a job or reduced hours to attend to family caregiving.
app_single_select_option_id_32  = "f661a7b2-0b04-4418-8a49-1c2302767bec"  # "My freelance work, gigs, and/or contracts were canceled.
app_single_select_option_id_33  = "c57404b2-0e01-47ca-ab22-8d856d4a3db2"  # My entire industry was shut down.
app_single_select_option_id_34  = "81842747-8efe-4995-b7b1-8145c82de4fa"  # I started a new full-time or part-time job.
app_single_select_option_id_35  = "76cb4ca9-32fe-4f30-9eee-334bd64097ea"  # I picked up new freelance work, gigs, and/or contracts.
app_single_select_option_id_36  = "9f00167d-8166-43a7-a13d-6650cedadfeb"  # Other (please describe)
app_single_select_option_id_37  = "401798a6-9c7b-4346-9e08-2c8594c63f51"  # My employment was not affected by the pandemic.

# Multi-Select Question: "How, if at all, was your artistic practice impacted between March 2020 and February 2022"
app_single_select_option_id_38  = "9fe68b47-cb6e-4e30-8d84-f0c446bd8bf3"  # My scheduled exhibitions/shows/performances/gigs were canceled.
app_single_select_option_id_39  = "d261b3f2-0bd0-4f21-acd9-240b675af9d4"  # Canceled travel prevented me from attending my exhibitions/shows/performances/gigs.
app_single_select_option_id_40  = "7e732238-3755-4758-bde7-7ee17b569821"  # My studio/rehearsal space closed due to the pandemic.
app_single_select_option_id_41  = "1736fffc-bcdf-4938-87b2-841770f4e164"  # I could no longer afford a studio/rehearsal space.
app_single_select_option_id_42  = "5a5e0e65-95fb-4f61-bf07-150c596fc741"  # I could no longer collaborate safely with others.
app_single_select_option_id_43  = "24228b14-e265-4b71-9188-a9527cd00432"  # I was less motivated to pursue my artistic practice.
app_single_select_option_id_44  = "9d152a65-8def-4578-bff8-5898e1b019a5"  # I was more motivated to pursue my artistic practice.
app_single_select_option_id_45  = "057e2ffb-0076-4d0f-a67d-3bce48384e33"  # I sought out new collaborators, communities, or professional networks.
app_single_select_option_id_46  = "ea956f04-ab95-495e-8875-4fe87d59b385"  # I evolved my artistic practice to address community needs.
app_single_select_option_id_47  = "e81f944d-5d60-42a1-b67a-273168fc969f"  # I embraced new opportunities to present my work online.
app_single_select_option_id_48  = "e251d10d-1f57-42c7-885c-6004617454a9"  # I created a new series of work.
app_single_select_option_id_49  = "3b445f7b-45d9-40a1-bd43-a36c0aeca2e4"  # I picked up new exhibitions/shows/performances/gigs.
app_single_select_option_id_50  = "e796e71e-bb0a-41d9-9d41-e21339f1a1cb"  # Other (please describe)
app_single_select_option_id_51  = "a535f02a-9ec3-4c02-9f6b-4985afb81552"  # My artistic practice was not impacted by the pandemic

# Multi-Select Question: "How, if at all, was your well-being impacted between March 2020 and February 2022"
app_single_select_option_id_52  = "da49f515-a993-48ca-bb13-e5b2f64392c6"  # I experienced anxiety or depression.
app_single_select_option_id_53  = "1da237e2-33e9-4920-a364-5ce84482499a"  # I experienced loneliness.
app_single_select_option_id_54  = "9830cc28-9102-4cd0-b077-0290b5bc2946"  # I got sick.
app_single_select_option_id_55  = "9b4498c7-a1ad-4da7-bb52-adf4662c4a54"  # I experienced food insecurity.
app_single_select_option_id_56  = "b1937259-a3ca-43a3-bfce-050d56eaaade"  # I experienced housing insecurity.
app_single_select_option_id_57  = "20052931-ae17-4cf0-9b31-1f7093960599"  # I had to move.
app_single_select_option_id_58  = "49d2a0a8-00b3-477e-aa19-9a6375823074"  # I accumulated debt.
app_single_select_option_id_59  = "bc108cdf-2c93-4d56-9c9b-90e534198f24"  # I became a part- or full-time caregiver
app_single_select_option_id_60  = "cc326105-c795-48ba-9e0b-f129fbf4101d"  # My self-care improved.
app_single_select_option_id_61  = "4825f8d3-a560-42b9-8135-ed4d186f27cc"  # My mental health improved.
app_single_select_option_id_62  = "162cc8a2-84ec-4f41-a76c-03db15669cc4"  # My physical health improved.
app_single_select_option_id_63  = "8cf0ba20-2701-48af-947a-7c41d1eca75b"  # Other (please describe)
app_single_select_option_id_64  = "05c78a1a-3762-4b8b-9753-e6f6139567fc"  # My well-being was not impacted by the pandemic.





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