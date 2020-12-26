#ifndef HELLOFUNCTIONS_H
#define HELLOFUNCTIONS_H

#include <math.h>
#include <stdio.h>

void sqrt_array_c(double* vect, int vect_len, double* res); 

inline void say_hello_c() {
    printf("Hello from C with cython!\n");
    fflush(stdout);
}

#endif
