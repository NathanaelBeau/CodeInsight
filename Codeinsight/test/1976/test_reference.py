def test(lst0):
    def flatten(lst):
        for item in lst:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item
    return [str(item) for item in flatten(lst0)]
