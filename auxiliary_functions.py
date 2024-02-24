def find_max_index(lst):
    if not lst:
        return None  # Return None for an empty list
    
    max_index = 0  # Start by assuming the first element is the maximum
    for i in range(1, len(lst)):
        # Compare each element with the current maximum
        if lst[i] > lst[max_index]:
            max_index = i  # Update the index if a larger element is found
    
    return max_index

# Example usage:
my_list = [5, 8, 3, 9, 6]
print("Index of the biggest element:", find_max_index(my_list))