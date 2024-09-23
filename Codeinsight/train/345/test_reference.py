import ast
def test(str0):
    return [ast.literal_eval(x) for x in str0.split(',')]