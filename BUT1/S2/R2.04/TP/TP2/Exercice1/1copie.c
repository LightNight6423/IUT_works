//
// Created by duc64 on 11/02/2025.
//
//Programme permettant de copier une chaine de caractère dans une autre chaine
//en utilisant des notions de tableau puis de pointeur
#include <stdio.h>

int main() {
    char chaine1[100], chaine2[100];
    int i = 0;
    printf("Entrez une chaine de caractere : ");
    scanf("%s",chaine1);
    while (chaine1[i] != '\0') {
        chaine2[i] = chaine1[i];
        i++;
    }
    chaine2[i] = '\0';
    printf("La chaine copiee est : %s", chaine2);
    return 0;
}