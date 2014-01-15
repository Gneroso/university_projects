/* Write a program to print all input lines that are longer than 50 characters  */

#include <stdio.h>
#include <string.h>

#define LINE_SIZE 25000
#define LIMIT 50

int main() {
  char line[LINE_SIZE];
  FILE *fin = fopen("input.txt", "r");

  while(fgets(line, sizeof line, fin) != NULL) {
    if(strlen(line) >= LIMIT) {
      printf("%s\n", line);
    }
  }

  return 0;
}
