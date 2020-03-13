#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    #weights_3 = [4,6,10,15,16]
    # answer= 21
    # indexes (1,3)
    # store each weights list index as its value
    for value, key in enumerate(weights):
        hash_table_insert(ht, key, value)
    # check if the hash table contains an entry for limit - weight    
    for key, value in enumerate(weights):
        if hash_table_retrieve(ht, limit-value) is not None:
            index = hash_table_retrieve(ht, limit - value)
            # if higher valued index place in zeroeth spot
            if index >= key:
                return (index, key)
            # else flip them 
            else:
                return (key, index)    
        
    # return none if the key does not exist in the hash table
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
