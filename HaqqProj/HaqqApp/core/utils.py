def find_keys(data, target, path=None):
    if path is None:
        path = []
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = path + [key]
            result = find_keys(value, target, new_path)
            if result:
                return result
    elif isinstance(data, list):
        if target in data:
            return path
    return None


def get_score(skills, target, data):
    # Check level 1: exact match
    if target in skills:
        return 1

    keys_path = find_keys(data, target)

    # Check level 2: immediate parent category
    if keys_path and len(keys_path) > 1:
        parent_category = keys_path[-1]
        if any(skill in data[keys_path[0]][parent_category] for skill in skills):
            return 2

    # Check level 3: second level parent category
    if keys_path and len(keys_path) > 0:
        main_category = keys_path[0]
        if any(skill in [item for sublist in data[main_category].values() for item in sublist] for skill in skills):
            return 3

    return float('inf')  # In case no match is found, though the prompt assumes at least level 3 match