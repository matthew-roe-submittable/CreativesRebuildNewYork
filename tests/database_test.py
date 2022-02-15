import config
from lib.controller import *

print("create model obj")
model = Creative(config.mysql_conn)
model.primary_unique_id = "1"
model.submission_id     = "12"
model.submitter_id      = "123"
model.form_response_id  = "1234"
model.entry_id          = "12345"
model.collab_unique_id_1 = "123456"
model.collab_unique_id_2 = "1234567"
model.collab_unique_id_3 = "1234568"
model.collab_unique_id_4 = "1234569"
model.collab_unique_id_5 = "1234560"
model.collab_unique_id_6 = "1234561"
model.collab_unique_id_7 = "1234562"
model.collab_unique_id_8 = "1234563"
model.collab_unique_id_9 = "1234564"
model.date_last_checked  = datetime.now().strftime("%Y-%m-%d %H:%M:%SZ")

model.save()


model.load_by_submission_id(12)

model.collab_unique_id_1 = "999999999999999"

model.save()
