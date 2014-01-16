#include <stdio.h>
#include <string.h>

#define LINE_SIZE 50

int sudoku[9][9];
int stack[1000];

void print_sudoku(){
  int i,j;

  for(i=0; i<9; i++) {
    for(j=0; j<9; j++) {
      printf("%d", sudoku[i][j]);
    }
    printf("\n");
  }

}

int check_number(int i, int line, int column, int sudoku[9][9]) {
  int j, k;

  for(j=0; j<9; j++) if(sudoku[line][j] == i) return 0;
  for(j=0; j<9; j++) if(sudoku[j][column] == i) return 0;
  /*
  printf("%d %d %d\n", line, column, i);
  for(j=((line+1)/3)*3-1; j< ((line+1)/3)*3-1+3; j++) {
    for(k=((column+1)/3)*3-1; k< ((column+1)/3)*3-1+3; k++) {
      if(sudoku[j][k] == i) return 0;
    }
  }
*/
  return 1;
}

int solve_sudoku(int line, int column, int sudoku[9][9]) {
  int i,j, copy_sudoku[9][9], good=0;

  for(i=0; i<9; i++) {
    for(j=0; j<9; j++) {
      copy_sudoku[i][j] = sudoku[i][j];
      printf("%d ", sudoku[i][j]);
    }
    printf("\n");
  }

  while(copy_sudoku[line][column] && line > 9) {
    if (column >= 8) {
      column = 0; line++;
    } else {
      column++;
    }
  }
  if (line >= 8) return 1;

  for(i=1; i<=9; i++) {
    if (check_number(i, line, column, copy_sudoku)) {
      good = 1;
      copy_sudoku[line][column] = i;
      solve_sudoku(line, column+1, copy_sudoku);
    }
  }

  if (!good) return 0;

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

  solve_sudoku(0, 0, sudoku);

  return 0;
}
