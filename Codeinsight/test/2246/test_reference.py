def test(dict0):
    def count_elements(d):
        if isinstance(d, dict):
            return len(d) + sum(count_elements(v) for v in d.values())
        return 0
    
    return count_elements(dict0)


