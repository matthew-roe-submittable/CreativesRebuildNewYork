import config
from lib.submittable import *

print("create controller obj")
submittable = Submittable()
print("get list of submissions")
submittable.getListOfSubmissions()
# get list of ref responses
submittable.getReferenceResponses()
print("finished")
