
def find_minimum():
    all_values = [90,4,0.1,5]
    
    current_min = all_values[0]
    for i in all_values:
        if i < current_min:
            current_min = i

    return current_min


print(find_minimum())
