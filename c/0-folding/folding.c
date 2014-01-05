#include <stdio.h>
#include <math.h>

int (*copy(int n, int original[2*n-1][2*n-1]))[5] {
  int i, j;

  for(i=0; i<2*n-1; i++){
    for (j=0; j<2*n-1; j++){
      simple_copy[i][j] = original[i][j];
      printf("%d %d", i,j);
    }
  }

  printf("!!!!!!!!!!!!!!!\n");

  return simple_copy;
}

int check_point(int x, int y, int n, int fold[2*n-1][2*n-1]) {
  if (x > 2*n-1 || y > 2*n-1 || x < 0 || y < 0) return 0;
  if (fold[x][y] == 1) return 0;

  return 1;
}

int is_solution(int x, int y, int n) {
  int px, py;
  px=px=n;

  return (sqrt((x-px)*(x-px) + (y-py)*(y-py)) == n)?1:0;
}

int generate_fold(int n, int fold[2*n-1][2*n-1], int x, int y) {
  int i,j;

  if (check_point(x, y, n, fold))
    fold[x][y] = 1;
  else
    return -1;
  for(i=0; i<2*n-1; i++){
      for (j=0; j<2*n-1; j++){
        printf("%d ", fold[i][j]);
      }
      printf("\n");
    }

  printf("\n\n\n");

  if (is_solution(x, y, n)){
    for(i=1; i<=n; i++){
      for (j=1; j<=n; j++){
        printf("%d", fold[i][j]);
      }
      printf("\n");
    }
  }
  else {
    generate_fold(n, copy(n, fold), x+1, y);
    return -1;
    generate_fold(n, copy(n, fold), x, y+1);
    generate_fold(n, copy(n, fold), x-1, y);
    generate_fold(n, copy(n, fold), x, y-1);
  }
}

int fold1[5][5];

int main() {
  int n = 3;
  generate_fold(n, fold1, n-1, n-1);

  return 0;
}
