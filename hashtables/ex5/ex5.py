# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # TODO list
    #* init dict
    #* build dict
    #* init results list
    #* populate results list
    #* if the same item appears more than once save its location as well
    #! Optimize and clean code
    #! Spell check comments or make them in the first place

    dictionary = dict()
    for file in files:
        name = file.split("/")[-1]
        if name not in dictionary:
            dictionary[name] = [file]
        else:
            dictionary[name].append(file)

    result = []

    for query in queries:
        if query in dictionary:
            for path in dictionary[query]:
                result.append(path)

    print(result)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
