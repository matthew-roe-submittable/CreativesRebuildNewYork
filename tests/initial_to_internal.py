from initial_form_to_internal import *

print("create controller obj")
initial_to_internal = InitialToInternal()
# populate internal form with multi-select to single select
initial_to_internal.initial2internal()
print("finished")
