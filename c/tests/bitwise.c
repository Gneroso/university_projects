#include <stdio.h>

int invert(int x, int p, int n) {
  while(n) {
    x ^= 1 << p;
    p++; n--;
  }
  return x;
}

int main() {
  printf("%d\n", invert(121, 1, 3));
  return 0;
}
