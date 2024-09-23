def test(parent_dict):
    return {k: parent_dict[k] for k in range(2, 5) if k in parent_dict}
