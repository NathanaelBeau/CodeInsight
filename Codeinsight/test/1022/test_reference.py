import numpy

def test(lst0, lst1):
	array0 = numpy.array(lst0)
	array1 = numpy.array(lst1)
	inds = array1.argsort()
	return list(array0[inds])