#include <stdio.h>
#include <string.h>

#define LINE_SIZE 50

int sudoku[9][9];
int stack[1000];

void print_solution(int sudoku[9][9]) {
  int index_line, index_column;

  for(index_line=0; index_line<9; index_line++) {
    for(index_column=0; index_column<9; index_column++) {
      printf("%d ", sudoku[index_line][index_column]);
    }
    printf("\n");
  }

  printf("\n");
}

int check_number(int number, int line, int column, int sudoku[9][9]) {
  int index, index_column, start_line=(line/3)*3, start_column=(column/3)*3;

  // check if the number exists in this line
  for(index=0; index<9; index++) if(sudoku[line][index] == number) return 0;

  // check if the number exists in this column
  for(index=0; index<9; index++) if(sudoku[index][column] == number) return 0;

  // check if the number exists in this square (3*3)
  for(index=start_line; index < start_line+3; index++) {
    for(index_column=start_column; index_column<start_column+3; index_column++) {
      if(sudoku[index][index_column] == number) return 0;
    }
  }

  return 1;
}

int solve_sudoku(int line, int column, int sudoku[9][9]) {
  int index_line, index_column, copy_sudoku[9][9], good=0, number;

  // create a sudoku matrix copy
  for(index_line=0; index_line<9; index_line++) {
    for(index_column=0; index_column<9; index_column++) {
      copy_sudoku[index_line][index_column] = sudoku[index_line][index_column];
    }
  }

  // go to the first 0 element
  while(copy_sudoku[line][column] != 0 && line < 9) {
    if (column == 8) {
      column = 0; line++;
    } else {
      column++;
    }
  }

  // if we are at the last line + 1 => we found a solution
  if (line >= 9) {
    print_solution(copy_sudoku);
    return 1;
  }

  // we are at 0-element in matrix, so we try to change that element with the
  // right non-0 element
  for(number=1; number<=9; number++) {
    // if the number meet thoese 3 condition, go to next position
    if (check_number(number, line, column, copy_sudoku)) {
      good = 1;
      copy_sudoku[line][column] = number;
      // continue solving for next position
      if (column == 8) {
        solve_sudoku(line+1, 0, copy_sudoku);
      } else {
        solve_sudoku(line, column+1, copy_sudoku);
      }
    }
    // if no solution was found, go back and try with another number
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
