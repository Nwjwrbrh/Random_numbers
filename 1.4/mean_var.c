#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include"coeffs.h"

int main(){
    char* str="uni.dat";
    double m=mean(str);
    double v=var(str);
    printf("Mean:%lf,Variance:%lf",m,v);
    //Mean:0.500007,Variance:0.083301
}