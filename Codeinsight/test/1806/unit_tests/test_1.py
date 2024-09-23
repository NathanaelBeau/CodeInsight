class Obj:
    def __init__(self, modified):
        self.modified = modified
lst0_1 = [Obj(modified=3), Obj(modified=1), Obj(modified=2)]
var0_1 = "modified"
expected_output_1 = [Obj(modified=3), Obj(modified=2), Obj(modified=1)]
result_1 = test(lst0_1, var0_1)
assert all(x.modified == y.modified for x, y in zip(result_1, expected_output_1)), 'Test failed'