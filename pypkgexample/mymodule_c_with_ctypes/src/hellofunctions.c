#include <hellofunctions.h>

void sqrt_array_c(double* vect, int vect_len, double* res) {
    int ii;
    for (ii = 0; ii < vect_len; ii++) {
       res[ii] = sqrt(vect[ii]); 
    }
}

void say_hello_c() {
    printf("Hello from C with ctypes!\n");
    fflush(stdout);
}
