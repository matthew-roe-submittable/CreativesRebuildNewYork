import config
from lib.controller import *

print("create controller obj")
controller = CreativesRebuildController()
print("laod the databaes")
# load Primary Artist from AEP and GI projects to database and internal form
controller.loadArtistsToDatabase()
# load the collaborator artist to database and internal form
# controller.load_ref_forms_data()
print("finished")
