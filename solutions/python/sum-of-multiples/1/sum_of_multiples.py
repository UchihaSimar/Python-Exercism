def sum_of_multiples(limit, multiples):
    result_set = set()
    for multiple_item in multiples:
        if multiple_item == 0:
            continue
        multiple_item_sum = multiple_item
        while multiple_item_sum < limit:
            result_set.add(multiple_item_sum)
            multiple_item_sum = multiple_item_sum + multiple_item

    return sum(result_set)