class Obj:
    def __init__(self, modified):
        self.modified = modified
lst0_2 = [Obj(modified=5), Obj(modified=5), Obj(modified=2)]
var0_2 = "modified"
expected_output_2 = [Obj(modified=5), Obj(modified=5), Obj(modified=2)]
result_2 = test(lst0_2, var0_2)
assert all(x.modified == y.modified for x, y in zip(result_2, expected_output_2)), 'Test failed'