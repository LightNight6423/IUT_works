//
// Created by duc64 on 12/02/2025.
//
#include <stdio.h>

void main(void){
  int i;
  char *couleur[] = {"rouge", "vert", "bleu", "orange", "noir", "blanc", NULL};
  char *p = couleur;


  for(i = 0; couleur[i] != NULL; i++){
    printf("%s\n", couleur[i]);
  }

  printf("-------------------------\n");

  for(i = 0; couleur[i] != NULL; i++){
    printf("%s\n", couleur[i] + 1);
  }

  printf("-------------------------\n");

  while (couleur[i] != NULL){
    while (*p != '\0') {
      if (*p >= 'a' && *p <= 'z') {
        *p = *p - 32;
      }
      p++;
    }
    printf("%s\n", couleur[i]);
    i++;
    p = couleur[i];
  }


}