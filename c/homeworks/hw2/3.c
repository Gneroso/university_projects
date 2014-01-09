/*
 *  Write a function reverse(s) that reverses the character string s. Use it to
   write a program that reverses its input a line at a time.
 */

#include <stdio.h>
#include <string.h>

#define LINE_SIZE 200

int comment_lock;

void reverse(char line[LINE_SIZE]) {
  int index;
  char aux;

  for(index=0; index<strlen(line)/2; index++) {
    aux = line[strlen(line)-index-1];
    line[strlen(line)-index-1] = line[index];
    line[index] = aux;
  }
}

int main() {
  FILE *fin  = fopen("input.txt", "r");
  FILE *fout = fopen("output.txt", "w");

  char line[LINE_SIZE];

  while(fgets(line, sizeof line, fin) != NULL) {
    reverse(line);
    fprintf(fout, "%s", line);
  }

  return 0;
}
