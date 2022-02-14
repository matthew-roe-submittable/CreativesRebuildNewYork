import mysql.connector

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
submittable_token = "5379d0ca57f64c1f827f3d0a0b476554"

# Project: AEP
project_id_1                      = "f5b5299e-149b-40fe-9764-f41fa3c57330"
# Initial form
project_1_formId                  = "17b94926-61e9-4ec6-95be-df32c0176ea6"
project_1_artist_or_org_field_id  = "04a1f75a-31f5-4e3a-8f60-10a503c0939f"
# Artist
project_1_artist_options_id       = "a36e0dc6-a3d4-451d-8f41-713def6da95f"
# Org
project_1_org_options_id          = "e3327582-06b5-40e4-8684-4e484ba1e793"

# Initial Form Artist UID fields
project_1_artist_last_name  = "edfb62ed-9f31-49d6-bcf6-dce8ec0589b6"
project_1_artist_zipcode    = "254429d2-640b-4c8b-9839-73c3e5ba12a7"
project_1_artist_dob        = "a3c4efb3-c45b-4efc-bee5-6b5c94ed2592"

# Reference form to hold up to 9 UID per submission
reference_form_id_1         = "8990f98a-7f90-49e8-819e-ef100781e11c"
reference_form_id_2         = "a5a47e3e-1aae-4eee-808f-d580aa38fb21"

# Form field id of the reference form in the internal form
reference_form_field_id_1   = "2f5df106-e782-422b-9c39-a3345788b715"
reference_form_field_id_2   = "da35f4fc-3219-4731-91ed-3e5a46ddc4ef"
reference_form_field_id_3   = "605e57c4-5488-4a75-a7ed-ad6399ee2085"
reference_form_field_id_4   = "eed9b6d8-119d-41e2-8763-6054b56a145c"
reference_form_field_id_5   = "99047e07-340b-4872-9f7e-3f9f08e29592"
reference_form_field_id_6   = "68900200-361f-416c-8fb4-4a5de1a92f89"
reference_form_field_id_7   = "53497706-6517-439c-83fd-430df1b8efac"
reference_form_field_id_8   = "6290ab16-2344-4fcd-b794-bedc3b576903"
reference_form_field_id_9   = "12b3eda5-25e6-45d8-bbee-4a8a37118ad9"

reference_form_name_id      = "2434c406-1ea5-48e0-935a-51e65f7c179b"
reference_form_dob_id       = "186190bc-113d-4490-a751-218314bdba29"
reference_form_zipcode_id   = "0e846040-cf76-4609-a107-be4b911ab18e"

# Project: GI
project_id_2                = "a29ca1b8-2121-446e-aa93-e6739e77f09c"
project_2_formId            = "00df1db3-ae6c-446b-aaa0-7dea64388643"
project_2_name_field_id     = "582e9043-8977-447b-a569-cbc2e5df12ed"
project_2_dob_field_id      = "b5e07e17-8d0b-4705-9628-ba35de352804"
project_2_zipcode_field_id  = "d533967d-d72b-4266-a502-577b6ae6db81"

# internal form
internal_form_id           = "f2911a5d-1293-4f84-85b2-63ec0a1e6282"
internal_form_field_id_1   = "77667d07-9c56-461b-9e80-243b806a4882"
internal_form_field_id_2   = "1a97b9d8-a8ef-4270-b378-5c82a6d7b75c"
internal_form_field_id_3   = "f4d45c72-5f00-4358-bd8e-02d19710c442"
internal_form_field_id_4   = "bc6a7400-b138-499c-b6f8-fb4b5082e08c"
internal_form_field_id_5   = "9f37e441-cf00-458d-857a-a9bd22bc6b57"
internal_form_field_id_6   = "c13061e4-f3b9-4cee-96c8-981b3c6a4976"
internal_form_field_id_7   = "f386b80b-9842-4746-800e-86fa6d3d2dda"
internal_form_field_id_8   = "e6105f2a-3041-44a5-b0f2-42261a42436a"
internal_form_field_id_9   = "a402fa0e-e106-4630-aac8-9550b262db0b"
internal_form_field_id_10  = "9a02a624-26e2-4f8a-84fb-222f710b1079"

# label "Pending Duplicate"
label_id_1 = "320527"
# label "Not Awarded Duplicate"
label_id_2 = ""
# label "Pending Duplicate"
label_id_3 = ""
'''

# ------------------------------ DEMO ACCOUNT SETTINGS ------------------------------ #
# demo account
# submittable_token = "700b04eccae244679785a0e8f13c786e"

# Demo Account
# Project: Oct 6 US Bank Test Project
project_id_1                = "47b5697e-a7bb-4096-a708-b576cb218bc5"
project_1_formId            = "f2e0743c-ffde-4ad7-8407-c1b4c8ee220e"
project_1_name_field_id     = "dca6592c-dd72-4996-b718-8c7773341e11"
project_1_date_field_id     = "969d426a-14bd-4e4e-9110-2c9e0bb69276"
project_1_address_field_id  = "6a5f815a-3ef4-4a31-912b-3d9ad3bc2824"
project_1_text_only_field_id = "91abd27e-d69b-41f2-acdd-b640c52968d0"

# Project: Demo1
project_id_2                 = "d6be950d-9c18-436f-883a-d560a12226dd"
project_2_formId             = "c8175a1b-4b98-4bdb-9237-23cfec4543f3"
project_2_name_field_id      = "1ea7418a-976c-4096-b9d0-709925604fa9"
project_2_date_field_id      = "a19c5c72-93cc-441d-aea6-7e9c5b6c4736"
project_2_address_field_id   = "f6f2c7a6-0d97-4a5e-869d-51b6e885aa11"
project_2_text_only_field_id = "38d80d28-33e5-4827-961e-7e0aa949530c"

# internal form to hold up to 10 UID per submission
internal_form_id          = "d051aa12-614b-4f30-a9eb-db9f934a317a"

# 10 UID fields
internal_form_field_id_1  = "b8f1e240-3b57-4c05-8acb-566c79ac5d95"
internal_form_field_id_2  = "3357efb7-9412-42f0-9109-ddb3b1decff7"
internal_form_field_id_3  = "d339ff5b-f35c-4e1c-8cc3-8868a5fc99d6"
internal_form_field_id_4  = "530eff6b-d74e-4c84-9e1c-967fd1d25ae4"
internal_form_field_id_5  = "29dbacf9-01f0-4213-92bc-b4ea018bcae5"
internal_form_field_id_6  = "a66b68f9-448c-4e8a-8521-5c824aea10e1"
internal_form_field_id_7  = "59a845ff-83ab-4ffd-a204-d8247335bb73"
internal_form_field_id_8  = "bf13719d-85da-4acc-83dd-fd16cb196ee5"
internal_form_field_id_9  = "05bc0950-98c1-4822-bcd8-dc35e3fd4ca9"
internal_form_field_id_10 = "f7f704be-5ea5-4a68-8f0b-9e4cb5bdd0ab"


# label "Awarded Duplicate"
label_id_1 = "317974"

# label "Not Awarded Duplicate"
label_id_2 = "317973"

# label "P"ending Duplicate"
label_id_3 = "317972"
