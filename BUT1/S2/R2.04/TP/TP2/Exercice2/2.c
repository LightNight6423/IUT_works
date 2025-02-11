//
// Created by duc64 on 11/02/2025.
//
#include <stdio.h>
#include <stdlib.h>

int main(){
  char str1[100], str2[100], str3[100];
  char *p1, *p2, *p3;
  int i = 0;
  p1 = str1;
  p2 = str2;
  p3 = str3;
  printf("Enter the first string: ");
  gets(str1);
  printf("Enter the second string: ");
  gets(str2);
  while ( *p1 != '\0') {
    *p3 = *p1;
    p1++;
    p3++;
  }
  printf("Third string: %s\n", str3);
  while ( *p2 != '\0') {
    *p3 = *p2;
    p2++;
    p3++;
  }
  *p3 = '\0';
  printf("Third string: %s\n", str3);
  return 0;
}