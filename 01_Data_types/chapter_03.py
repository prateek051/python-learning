# Data types in python

# Integers

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams #addition
print(f"Total grams of base tea is : {total_grams}") 

remaining_tea = black_tea_grams - ginger_grams # substraction
print(f"Total grams of remaining tea is {remaining_tea}")

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings # division
print(f"Milk per serving is {milk_per_serving}")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots #  // -> is used to remove the decimal value
print(f"While tea bags per pot : {bags_per_pot}")


total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = 10 % 3  #  ( %  <- modulo operator)-> this is used to get the reminder from the division calculation
print(f"The leftover pods : {leftover_pods}")

base_flavor_strength = 2
scale_factor = 3
powrfull_flavour = base_flavor_strength ** scale_factor # (**  <- exponinatioal operator) -> used to calculate the power of a number
print(powrfull_flavour)