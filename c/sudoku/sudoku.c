#include <stdio.h>
#include <string.h>

#define LINE_SIZE 50

int sudoku[20][20];

void print_sudoku(){
  int i,j;

  for(i=0; i<9; i++) {
    for(j=0; j<9; j++) {
      printf("%d", sudoku[i][j]);
    }
    printf("\n");
  }

}

void build_sudoku(char line[LINE_SIZE], int line_number) {
  int index;

  for(index=0; index<strlen(line)-1; index++) {
    sudoku[line_number][index] = (int)line[index]-'0';
  }

}

int main() {
  int line_number=0;
  char line[LINE_SIZE];

  FILE *fin = fopen("input.txt", "r");

  while(fgets(line, sizeof line, fin) != NULL) {
    build_sudoku(line, line_number);
    line_number++;
  }

  solve_sudoku();

  return 0;
}
