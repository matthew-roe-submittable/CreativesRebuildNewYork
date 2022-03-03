from lib.controller import *

print("create controller obj")
controller = CreativesRebuildController()
# load Primary Artist from AEP and GI projects to database and internal form
controller.checkForDupUID()
print("finished")
