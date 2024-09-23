def test(lst0):
    return any(d.get("name") == "Test" for d in lst0)
