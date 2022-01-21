from lib.submittable import *

print("create submittable obj")
submittable = Submittable()

submission_response = submittable.getListOfSubmissions()
for sub_item in submission_response:
    print("sub item:", sub_item)
    submission_id = sub_item.getSubmissionId()
    sub_response  = submittable.getSubmission(submission_id)
    label_ids     = sub_response.getLabels()
    if len(label_ids) > 0:
        for id in label_ids:
            print(id.getLabelId())
            submittable.deleteLabel(submission_id, id.getLabelId())
