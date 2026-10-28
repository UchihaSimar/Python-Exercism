def append(list1, list2):
    return [*list1, *list2]

def concat(lists):
    result = []
    for single_list in lists:
        result = append(result,single_list)
    return result


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    count = 0
    for _ in list:
        count += 1
    return count


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function, list, initial):
    accumulator = initial
    # Process items in reverse order for right fold
    for item in reverse(list):
        accumulator = function(accumulator,item )
    return accumulator


def reverse(list):
    # Traverses the list backwards using slice step -1
    return list[::-1]
