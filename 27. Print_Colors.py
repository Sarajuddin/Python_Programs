# 27. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

# Expected Output :
# {'Black', 'White'}

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
new_set = set()
for el in color_list_1:
    if el not in color_list_2:
        new_set.add(el)
    
print(f"New Set containing all elements which are not present in Color Set 2 : {new_set}")