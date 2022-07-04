#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include"coeffs.h"

int main(){
    char* str="gau.dat";
    double m=mean(str);
    double v=var(str);
    printf("Mean:%lf,Variance:%lf",m,v);
    //Mean:0.000326,Variance:1.000906
}