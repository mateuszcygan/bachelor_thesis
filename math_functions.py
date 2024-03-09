# Normalization (probability) 

def normalize_and_round(probabilities):
    total = sum(probabilities)
    normalized_probabilities = [prob / total for prob in probabilities]
    rounded_probabilities = [round(prob, 2) for prob in normalized_probabilities]


    if sum(rounded_probabilities) == 1.0:
        return rounded_probabilities
    # Probabilities after rounding to two decimal places are not exactly equal 1.0
    else:
        surplus = sum(rounded_probabilities) - 1
        for elem in rounded_probabilities:
            if elem != 0:
                elem -= surplus
                return rounded_probabilities
            
def normalize(probabilities):
    total = sum(probabilities)
    normalized_probabilities = [prob / total for prob in probabilities]
    return normalized_probabilities

# Example to ask about
test = [0.4, 0.0, 0.45, 0.87, 5, 6]
test_arr = normalize(test)
print(test_arr)
print(sum(test_arr))


