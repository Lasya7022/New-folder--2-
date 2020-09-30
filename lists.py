duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
# Removal of duplicates a list
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list  
print(Remove(duplicate))

# Copying a list
new_list=duplicate.copy()
print(new_list)

# Copying contents in reverse order
duplicate.reverse()
print(duplicate)