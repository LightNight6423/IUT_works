//
// Created by duc64 on 04/02/2025.
//
#include <stdio.h>
int main(void){
  short tab[10];
  int i;

  for (i=0; i<10; i++){
    printf("Entrez un entier : ");
    scanf("%d",&tab[i]);
  }

  for (i=0; i<10; i++){
    printf("L'entier en position %d est %d et son adresse est %x\n",i, tab[i], &tab[i]);
  }
}