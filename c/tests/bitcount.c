#include <stdio.h>

int bitcount(int number) {
  int bits=0;

  while(number) {
    number &= (number-1);
    bits += 1;
  }

  return bits;
}

int main() {

  printf("%d\n", bitcount(6));

  return 0;
}
