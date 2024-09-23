import numpy
import math
import pandas
import string
import datetime
import json
import itertools
import random
import functools
import collections
result = test({'a' : 1 ,'b' : {'e':1, 'f':2}}, {'c':1,'d':2,'k':{10:10}})
assert result=={'a': 1, 'b': {'e': 1, 'f': 2}, 'c': 1, 'd': 2, 'k': {10: 10}}, 'Test failed'