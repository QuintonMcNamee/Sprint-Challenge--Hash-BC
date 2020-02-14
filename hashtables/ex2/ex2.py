#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = []

    # YOUR CODE HERE

    # loop through tickets array
    for ticket in tickets:
        # insert each key(source) and value(destination) into the hashtable
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    
    # retrieve the first index
    location = hash_table_retrieve(hashtable, "NONE")
    print('LOCATION: ', location)

    # while the location isnt "NONE", append the location to the route list and retrieve the next location
    while location != "NONE":
        route.append(location)
        location = hash_table_retrieve(hashtable, location)
    return route
