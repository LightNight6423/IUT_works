//
// Created by duc64 on 04/02/2025.
//
#include <stdio.h>
int main(void){
  int a,b;
  printf("Entrez deux entiers a et b: ");
  scanf("%d %d",&a,&b);

  if (a>b){
    printf("Le plus grand des deux entiers est %d\n",a);
  }
  else {
    printf("Le plus grand des deux entiers est %d\n",b);
  }
}