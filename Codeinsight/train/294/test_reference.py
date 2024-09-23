def test(lst0, var0):
    def custom_sort(item):
        return item.get(var0, '')
    
    return sorted(lst0, key=custom_sort)
