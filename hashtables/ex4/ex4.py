def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # TODO list
    #* init dict
    #* build dict
    #* init results list
    #* populate results list
    #! Optimize and clean code
    #! Spell check comments or make them in the first place

    dictionary = dict()

    for num in a:
        if abs(num) not in dictionary:
            dictionary[abs(num)] = 0
        dictionary[abs(num)] += 1

    result = []

    for num, value in dictionary.items():
        if value >= 2:
            result.append(num)

    return result


if __name__ == "__main__":
    test = [-1, -2, 1, 2, 3, 4, -4]
    print(has_negatives(test))
    for num in test:
        print(abs(num))

