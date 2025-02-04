//
// Created by duc64 on 04/02/2025.
//
#include <stdio.h>
int main(void){
  char *p;
  int i=0;
  char chaine[81];
  p = &chaine;

  printf("Entrez une chaine de caracteres : ");
  scanf("%s",chaine);

  while(*(p+i) != '\0'){
    printf("car %d : %c\n",i,*(p+i));
    i++;
  }

  printf("La chaine de caracteres contient %d caracteres\n",i);
}