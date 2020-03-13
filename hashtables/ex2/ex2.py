#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    #run the tickets through the hashtable passing in source and destination
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    # initialize routes    
    routes = []
    # hash none and give it an index 
    d = hash_table_retrieve(hashtable, 'NONE')
    # if destination is not NONE, append the destination to the routes.
    while d is not 'NONE':
        routes.append(d)
        d = hash_table_retrieve(hashtable, d) 
    # return the routes       
    return routes    
