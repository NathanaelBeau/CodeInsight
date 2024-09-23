from packaging.version import Version

def test(lst0):
    return sorted(lst0, key=Version)

