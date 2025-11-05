# mutable and immutable in python

# mutable

# variable = value
spice_mix = set() # set is a mutable datatype to element can be added and removed

print(f"Initial spice mix  id : {id(spice_mix)}") # same id
spice_mix.add("Ginger")
spice_mix.add("Cardamom")

print(f"after spice mix id : {id(spice_mix)}") # same id

# set have index value for every element in it and for new element/value without changing the id value of the set