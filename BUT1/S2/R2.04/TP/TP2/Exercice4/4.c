//
// Created by duc64 on 11/02/2025.
//
#include <stdio.h>

char donner_majuscle(char c) {
    if (c >= 'a' && c <= 'z') {
        return c - 32;
    }
    return c;
}

void mettre_en_majuscule( char *str) {
    while (*str != '\0') {
        *str = donner_majuscle(*str);
        str++;
    }
}

int donner_longueur(char *str) {
    int i = 0;
    while (*str != '\0') {
        i++;
        str++;
    }
    return i;
}

void inverser(char *str) {
    int longueur = donner_longueur(str);
    for (int i = 0; i < longueur / 2; i++) {
        char temp = str[i];
        str[i] = str[longueur - i - 1];
        str[longueur - i - 1] = temp;
    }
}

void saisir(char *str) {
    printf("Saisir une chaine de caractere : ");
    scanf("%s", str);
}

void afficher(char *str) {
    printf("%s\n", str);
}

int sont_egales(char *str1, char *str2) {
    while (*str1 != '\0' && *str2 != '\0') {
        if (*str1 != *str2) {
            return 0;
        }
        str1++;
        str2++;
    }
    return 1;
}

int main(){
  char chaine1[81], chaine2[81];
  char *str1, *str2;
  int longueur;
  str1 = chaine1;
  str2 = chaine2;
  saisir(str1);
  saisir(str2);
  longueur = donner_longueur(str1);
  printf("Longueur de la chaine 1 : %d\n", longueur);
  mettre_en_majuscule(str1);
  afficher(str1);
  mettre_en_majuscule(str2);
  afficher(str2);
  sont_egales(str1, str2) ? printf("Les chaines sont egales\n") : printf("Les chaines ne sont pas egales\n");
  inverser(str2);
  afficher(str2);
  return 0;
}


