def test(str0):
    lines = str0.split('\n')
    stripped_lines = [line.lstrip() for line in lines]
    return '\n'.join(stripped_lines)