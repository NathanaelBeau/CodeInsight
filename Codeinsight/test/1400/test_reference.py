import re
import unittest

def test(str0):
    return re.sub(r'\((\w+)\)', r'\1', str0)