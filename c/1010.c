/* 
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1,
o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. 
Após, calcule e mostre o valor a ser pago.
*/
#include <stdio.h>

float calculo_compra(int qtd_peca, float preco_peca);

int main(void){
    int codigo_1, codigo_2, qtd_1, qtd_2;
    float preco_1, preco_2, total;

    scanf("%d%d%f", &codigo_1, &qtd_1, &preco_1);
    scanf("%d%d%f", &codigo_2, &qtd_2, &preco_2);

    total = calculo_compra(qtd_1, preco_1) + calculo_compra(qtd_2, preco_2);
    printf("VALOR A PAGAR: R$ %.2f\n", total);

    return 0;
}

float calculo_compra(int qtd_peca, float preco_peca){

    return qtd_peca * preco_peca;
}