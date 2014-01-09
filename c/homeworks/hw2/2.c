/*
 *  Write a program to remove trailing blanks and tabs from each line of input,
 *  and to delete entirely blank lines
 */

#include <stdio.h>
#include <string.h>

#define LINE_SIZE 50

char *trim(char line[LINE_SIZE]) {
  int index, change=0;
  static char new_line[LINE_SIZE];

  for(index=0; index<strlen(line); index++) {
    if(line[index] != '\t' && line[index] != ' ') {
      new_line[index] = line[index];
      change = 1;
    }
  }

  if (change){
    new_line[strlen(new_line)+1] = '\0';
    return new_line;
  }else{
    return "";
  }
}

int main() {
  FILE *fin  = fopen("input.txt", "r");
  FILE *fout = fopen("output.txt", "w");

  char line[LINE_SIZE];

  while(fgets(line, sizeof line, fin) != NULL) {
    fprintf(fout, "%s\n", trim(line));
  }

  return 0;
}
