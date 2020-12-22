#include <math.h>

void sqrt_array(double* vect, int vect_len, double* res) {
    int ii;
    for (ii = 0; ii < vect_len; ii++) {
       res[ii] = sqrt(vect[ii]); 
    }
}

