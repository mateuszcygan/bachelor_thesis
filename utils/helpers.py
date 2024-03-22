# Returns an index of a number that is the biggest in the given array
def find_max_index(lst):
    if not lst:
        return None  # Return None for an empty list
    
    max_index = 0  # Start by assuming the first element is the maximum
    for i in range(1, len(lst)):
        # Compare each element with the current maximum
        if lst[i] > lst[max_index]:
            max_index = i  # Update the index if a larger element is found
    
    return max_index

def flatten_list(original_list):
    """
    Flatten a nested list using list comprehension.

    Args:
        original_list (list): The nested list to flatten.

    Returns:
        list: The flattened list.
    """
    return [item for sublist in original_list for item in sublist]