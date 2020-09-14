#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # TODO list -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    #* init dict
    #* build dict
    #* init route
    #* append items to route
    #! Optimize and clean code
    #! Spell check comments or make them in the first place

    dictionary = dict()
    for num in range(length):
        if tickets[num].source not in dictionary:
            dictionary[tickets[num].source] = tickets[num].destination

    route = []

    for _ in range(length):
        if route == []:
            route.append(dictionary["NONE"])
        else:
            route.append(dictionary[route[-1]])

    return route
