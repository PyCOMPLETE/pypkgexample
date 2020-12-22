cdef extern from "math.h" :
    double sqrt(double x)

@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)   # Deactivate negative indexing.
def sqrt_array(double[:] vect, double res[:]):
    cdef int NN = len(vect)
    cdef int ii
    for ii in range(NN):
        res[ii] = sqrt(vect[ii])

def say_hello():
    print('Hello from cython!')
		
