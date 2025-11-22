def combine_dicts(dict1, dict2):
    combined = {}
    for key, value in dict1.items():
        combined[key] = value
    for key, value in dict2.items():
        combined[key] = value
    return combined
