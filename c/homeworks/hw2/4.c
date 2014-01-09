/*
 * Write a program to remove all comments from a C program. Don't forget to
 * handle quoted strings and character constants properly. C comments don't
 * nest.
 */

#include <stdio.h>
#include <string.h>

#define LINE_SIZE 200

int comment_lock;

char *comment_free(char line[LINE_SIZE]) {
  int index, new_index=0;
  static char new_line[LINE_SIZE];

  new_line[new_index] = '\0';

  for(index=0; index<strlen(line); index++) {
    if (comment_lock) {
      if(line[index] == '*' && index+1<strlen(line) && line[index+1] == '/') {
        comment_lock = 0;
      }
    }else if(line[index] == '/' && line[index+1] == '*'){
      comment_lock = 1;
    }else if(line[index] != '/' && line[index+1] != '/'){
      new_line[new_index++] = line[index];
    }else{
      return new_line;
    }
  }

  return new_line;
}

int main() {
  FILE *fin  = fopen("input.txt", "r");
  FILE *fout = fopen("output.txt", "w");

  char line[LINE_SIZE];

  while(fgets(line, sizeof line, fin) != NULL) {
    strcpy(line, comment_free(line));
    line[strlen(line)+1] = '\0';

    fprintf(fout, "%s", line);
  }

  return 0;
}
