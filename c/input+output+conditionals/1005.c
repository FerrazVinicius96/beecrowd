#include <stdio.h>

int main(void){
    double a, b, media;
    double peso_1 = 3.5, peso_2 = 7.5;

    scanf("%lf", &a);
    scanf("%lf", &b);

    media = (a * peso_1 + b * peso_2) / (peso_1 + peso_2);

    printf("MEDIA = %.5lf\n", media);

    return 0;
}