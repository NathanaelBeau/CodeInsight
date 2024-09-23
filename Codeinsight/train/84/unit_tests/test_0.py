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
result = test(   {'car': [7, 6, 3],    'bike': [2, 10, 3],      'truck': [19, 4]}  )
assert result  ==   dict( (item, list(sorted(value)))  for (item,value) in   {'car': [7, 6, 3],    'bike': [2, 10, 3],      'truck': [19, 4]} .items() ), 'Test failed'