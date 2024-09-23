def test(var1):
   punct = set(list('''!()-[]{};:'"\,<>./?@#$%^&*_~'''))
   return ''.join(c for c in var1 if c not in punct)