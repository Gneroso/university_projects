#include <stdio.h>
#include <math.h>

struct point{
  int x, y;
} stack[100];

int check_point(int x, int y, int n, int stack_size) {
  if (x > 2*n-1 || y > 2*n-1 || x < 0 || y < 0) return 0;
  if (stack_size >= n) return 0;

  return 1;
}

int generate_fold(int n, int x, int y, int stack_size) {
  int i,j;

  if (check_point(x, y, n, stack_size)){
    stack[stack_size].x = x;
    stack[stack_size].y = y;
    stack_size++;
  }else
    return -1;

  if (stack_size == n){
    stack_size--;

    printf("\n");
    for(i=0; i<n; i++){
      printf("%d %d\n", stack[i].x, stack[i].y);
    }

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
  int n = 3;
  generate_fold(n, n-1, n-1, 0);

  return 0;
}
