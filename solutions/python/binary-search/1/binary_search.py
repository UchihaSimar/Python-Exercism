def find(search_list, value):
    low = 0
    high = len(search_list) - 1

    while( low <= high):
        mid = low + (high - low)//2

        if search_list[mid] == value:
            return mid

        if search_list[mid] > value:
            high = mid - 1
        else:
            low = mid + 1

    raise ValueError("value not in array")
