#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)
    
    # YOUR CODE HERE
    
    # declare base case, if result is == None
    result = None

    # loop through the weights array
    for index, weight in enumerate(weights):
        # if not the base case
        if hash_table_retrieve(ht, weight) != None:
            # retrieve hash table and key
            result = [index, hash_table_retrieve(ht, weight)]
            # result should have higher value in 0th index and smaller value in the 1st index. swap if not the case
            if result[0] < result[1]:
                temp = result[0]
                result[0] = result[1]
                result[1] = temp
                return result
        # finally, insert the key and value into the hash table
        else:
            hash_table_insert(ht, limit-weight, index)

    return result


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
