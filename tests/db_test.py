import json
from lib.controller import *
from lib.submittable import *
from lib.model import *
import config

print("create controller obj")
controller = CreativesRebuildController()
print("laod the databaes")
controller.loadDatabase()
print("finished")
