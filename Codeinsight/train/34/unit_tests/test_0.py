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
result = test( numpy.eye(3)*2 ,  numpy.arange(9).reshape(3,3) )
assert ( result == numpy.eye(3)*2 @ numpy.arange(9).reshape(3,3)  ).all(), 'Test failed'