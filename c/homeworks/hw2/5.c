/*
 * The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
 * Find the sum of all numbers, less than 5 000 000, which are palindromic in
 * base 10 and base 2. (Please note that the palindromic number, in either base,
 * may not include leading zeros.)
 */

#include <stdio.h>
#include <string.h>

#define MAXIM 5000000

char * strrev(char number[]){
  int length, index=0, tmp;

  length = strlen(number)-1;

  while(index<length) {
    tmp = number[index];
    number[index] = number[length];
    number[length] = tmp;
    index++; length--;
  }

  return number;
}

int *to_base(int base, char repr[], int number) {
  int remainder, length;

  static char new_number[] = "";
  new_number[0] = '\0';

  while(number) {
    remainder = number % base;
    number /= base;

    length = strlen(new_number);
    new_number[length] = repr[remainder];
    new_number[length+1] = '\0';
  }

  return atoi(strrev(new_number));

}

int check_palindrom(int number) {
  
  return 1;
}

int generate_palindroms() {
  int number, sum=0;

  for(number=11; number<=MAXIM; number++){
    if (check_palindrom(number) && check_palindrom(to_base(2, "01", number))) {
      sum += number;
    }
  }

  return sum;
}

int main() {
  generate_palindroms();
  return 0;
}
