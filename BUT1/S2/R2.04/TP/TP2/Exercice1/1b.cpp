//
// Created by duc64 on 11/02/2025.
//
// Programme permettant de copier une chaine de caractère dans une autre chaine avec des pointeurs dans une fonction
#include <stdio.h>

char *copiechaine(char *dest, char *src) {
    char *p1, *p2;
    p1 = src;
    p2 = dest;
    while (*p1 != '\0') {
        *p2 = *p1;
        p1++;
        p2++;
    }
    *p2 = '\0';
    return dest;
}

int main() {
    char chaine1[100], chaine2[100];
    printf("Entrez une chaine de caractere : ");
    scanf("%s",chaine1);
    printf("La chaine copiee est : %s", copiechaine(chaine2, chaine1));
    return 0;
}