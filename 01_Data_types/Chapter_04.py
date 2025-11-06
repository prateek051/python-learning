# Booleans in python

is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling  # upcasting -> here is_boiling value is converted form True -> 1 and added to 5

print(f"Total actions : {total_actions}")

milk_present = 0 # no milk
print(f"Is there milk? {bool(milk_present)}")

# logical operations
# AND , OR , NOT
# AND = both needs to be true
#OR = either one need to be true 
# NOT = reverses the result, If result is True then changes to False

water_hot = True
tea_added = False

can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}")