def transform(legacy_data):
    result = {}
    for key,value in legacy_data.items():
        for value_item in value:
            result[value_item.lower()] = key
    return result
