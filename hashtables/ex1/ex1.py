def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # TODO list -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    #* init dict
    #* Given a weights list smaller than 2 should return None
    #* work correctly with lists with 2 of the same numbers adding up to the total
    #* return numbers in the correct order
    #! Optimize and clean code
    #! Spell check comments or make them in the first place

    dictionary = dict()
    if len(weights) <= 1: #? Ensure list of reasonable size
        return None
    else:
        for i, weight in enumerate(weights):
            if weight not in dictionary:
                dictionary[weight] = i #? add things to dictionary to look up efficiently
            elif weight * 2 == limit: #? if there is a duplicate we dont want to add it but should still check
                return (i, dictionary[weight])

    for weight in dictionary:
        delta = limit - weight
        if delta in dictionary:
            return (dictionary[delta], dictionary[weight])