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

# Multi-select to single-select projects (no UID check)
project_id_3                 = "0566982c-934d-495e-a7ea-e408d44215fe"  # Portrait of New York State Artists
project_id_4                 = "ff3d1f76-8a37-4b7d-bfda-2651e940244c"  # Retrato de Artistas del Estado de Nueva York
project_id_5                 = "d5b24c6e-2cb1-45f2-94e9-9b0c199c32c3"  # Portrait of New York State Artists - Applicant Questionnaire
project_id_6                 = "649f06b5-636e-49fb-a103-78322effe0fb"  # Retrato de Artistas del Estado de Nueva York - Cuestionario para Solicitantes
project_id_7                 = "a7f25ed0-66b5-4f4b-991d-e9f0a771fb0a"  # AEP Manual submission
project_id_8                 = "46744312-6d9b-4b87-b8da-d129414cede5"  # GI Manual submission


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


# single select internal form IDs 1-25
#
# single select form field IDs for Multi-Select Question: "Which of the following best describes you"
single_select_id_1   = "90b7e584-a834-4bcd-948d-d0fcd90cdcdb"  # Arab or Middle Eastern
single_select_id_2   = "dbd9a5fc-f8ee-4486-a1d9-631952149f0e"  # Asian or Pacific Islander
single_select_id_3   = "b1bb0975-2256-442f-9f75-2fed4f8b1a17"  # Black or African American
single_select_id_4   = "ff294db0-b3e5-4394-a859-5dcdfb3cd2ee"  # Hispanic or Latin
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