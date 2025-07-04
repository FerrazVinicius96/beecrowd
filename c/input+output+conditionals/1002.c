#include <stdio.h>

int main(void){
    double area, raio, quadrado_raio, pi;
    pi = 3.14159;


    scanf("%lf", &raio);
    quadrado_raio = raio * raio;
    area = pi * quadrado_raio;

    printf("A=%.4f\n", area);

    
    return 0;
}