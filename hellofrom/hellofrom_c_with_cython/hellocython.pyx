cdef extern from "hellofunctions.h" :
    void sqrt_array_c(double* vect, int vect_len, double* res)
    void say_hello_c()

def sqrt_array(double[::1] vect, double[::1] res):
    sqrt_array_c(&vect[0], len(vect), &res[0])

def say_hello():
    say_hello_c()	
