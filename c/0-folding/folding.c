#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <math.h>
#include <string.h>

struct point{
  int x, y;
} stack[10000];

char string[15];
char proteins[32768][16];

int optim[32768], combination;

int calculate_optim(int n, struct point stack[], char string[]) {
  int i, j, optimal=0;
  int fold[2*n-1][2*n-1];
  struct point p;

  for(i=0; i<2*n-1; i++) {
    for(j=0; j<2*n-1; j++) {
      fold[i][j] = 0;
    }
  }

  for(i=0; i<n; i++) {
    if (string[i] == 'H')
      fold[stack[i].x][stack[i].y] = 1;
  }

  for(i=0; i<n; i++) {
    if (string[i] == 'H'){
      p = stack[i];
      if (fold[p.x+1][p.y]) optimal++;
      if (fold[p.x][p.y+1]) optimal++;
      if (fold[p.x-1][p.y]) optimal++;
      if (fold[p.x][p.y-1]) optimal++;
    }
  }

  return optimal/2;
}

int generate_proteins(int n, int str_len) {
  int i;
  char raw_proteins[] = "HP";

  if (str_len == n){
    strcpy(proteins[combination++], string);
    return -1;
  }

  for(i=0; i<=1; i++){
    string[str_len] = raw_proteins[i];
    string[str_len+1] = '\0';

    generate_proteins(n, str_len+1);
  }
}

void init_fill(int n) {
  int i, result;
  struct point stack_copy[100];

  // copy stack
  for(i=0; i<n; i++) {
    stack_copy[i] = stack[i];
  }

  for(i=0; i<pow(2, n); i++) {
    result = calculate_optim(n ,stack, proteins[i]);

    if (result > optim[i]) optim[i] = result;
  }
}

int check_point(int x, int y, int n, int stack_size) {
  int i;

  if (x > 2*n-1 || y > 2*n-1 || x < 0 || y < 0) return 0;
  if (stack_size >= n) return 0;

  // check only last point
  for (i=0; i<stack_size; i++)
    if (stack[i].x == x && stack[i].y == y) return 0;

  return 1;
}

int generate_fold(int n, int x, int y, int stack_size) {
  int i,j;

  if (check_point(x, y, n, stack_size)){
    stack[stack_size].x = x;
    stack[stack_size].y = y;
    stack_size++;
  }else{
    return -1;
  }

  if (stack_size == n){
    stack_size--;

    init_fill(n);

    stack[n].x = 0;
    stack[n].y = 0;

  }
  else {
    generate_fold(n, x+1, y, stack_size);
    generate_fold(n, x, y+1, stack_size);
    generate_fold(n, x-1, y, stack_size);
    generate_fold(n, x, y-1, stack_size);
  }
}

int main() {
  int n=8, s=0, i;

  generate_proteins(n, 0);

  generate_fold(n, n-1, n-1, 0);

  for(i=0; i<258; i++) {
    s+=optim[i];
  }

  printf("\n%d", s);

  return 0;
}
