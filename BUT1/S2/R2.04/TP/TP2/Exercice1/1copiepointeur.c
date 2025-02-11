//
// Created by duc64 on 11/02/2025.
//
// Programme permettant de copier une chaine de caractère dans une autre chaine avec des pointeurs

#include <stdio.h>

int main() {
    char chaine1[100], chaine2[100];
    char *p1, *p2;
    int i = 0;
    printf("Entrez une chaine de caractere : ");
    scanf("%s",chaine1);
    p1 = chaine1;
    p2 = chaine2;
    while (*p1 != '\0') {
        *p2 = *p1;
        p1++;
        p2++;
    }
    *p2 = '\0';
    printf("La chaine copiee est : %s", chaine2);
    return 0;
}