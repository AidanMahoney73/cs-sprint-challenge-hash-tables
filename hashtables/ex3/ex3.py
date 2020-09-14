def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # TODO list
    #* init dict
    #* build dict
    #* init results list
    #* find where the item occured a number of times equal to the length of arrays
    #! Optimize and clean code
    #! Spell check comments or make them in the first place

    dictionary = dict()

    for array in arrays:
        for num in array:
            if num not in dictionary:
                dictionary[num] = 0
            dictionary[num] += 1

    result = []

    for num, count in dictionary.items():
        if count == len(arrays):
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
