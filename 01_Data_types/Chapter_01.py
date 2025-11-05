# mutable and immutable in python

# immutable


# variable = value
sugar_amount = 2 # immutable

#output statement
print(f"Initial sugar : {sugar_amount}")
print(id(sugar_amount)) # id for value 2

sugar_amount = 12 # immutable

print(f"New Initial sugar : {sugar_amount}")
print(id(sugar_amount)) # 12 has different id then 2  # id for value 12

# Above code shows that initial sugar_amount variable is pointing at value 2 first, but after changing to 12 the reference to is shifted to 12 value without changing first value 2
# always check mutable or immutable for "id" not for "Values"