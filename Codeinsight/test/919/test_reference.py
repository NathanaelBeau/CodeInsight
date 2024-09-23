def test(lst0):
    def extract_first_elements(lst):
        if isinstance(lst[0], list):
            return [extract_first_elements(sublist) for sublist in lst]
        return lst[0]
    return extract_first_elements(lst0)

