//
// Created by duc64 on 04/02/2025.
//
#include <stdio.h>
int main(void){
  char chaine[81];
  int i=0;


  printf("Entrez une chaine de caracteres : ");
  scanf("%s",chaine);

  while(chaine[i] != '\0'){
    printf("car %d : %c\n",i,chaine[i]);
    i++;
  }

  printf("La chaine de caracteres contient %d caracteres\n",i);
}