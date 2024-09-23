import ast

def test(str0, tpl0):
    return tpl0 + tuple(ast.literal_eval(str0))
