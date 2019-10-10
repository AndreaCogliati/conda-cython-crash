# distutils: language = c++
# cython: language_level=3

import numpy as np
cimport numpy as np

cdef extern from "numpytest.cpp":
    cdef void testNumPy()
    
def PyNumPyTest():
    testNumPy()