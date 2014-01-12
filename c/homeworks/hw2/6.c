/*
 In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

  High Card: Highest value card.
  One Pair: Two cards of the same value.
  Two Pairs: Two different pairs.
  Three of a Kind: Three cards of the same value.
  Straight: All cards are consecutive values.
  Flush: All cards of the same suit.
  Full House: Three of a kind and a pair.
  Four of a Kind: Four cards of the same value.
  Straight Flush: All cards are consecutive values of same suit.
  Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
  The cards are valued in the order:
  2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

  If two players have the same ranked hands then the rank made up of the
 highest value wins; for example, a pair of eights beats a pair of fives
 (see example 1 below). But if two ranks tie, for example, both players have a
 pair of queens, then highest cards in each hand are compared (see example 4
 below); if the highest cards tie then the next highest cards are compared,
 and so on.
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define LINE_SIZE 50
#define CARD_TYPES 4
#define CARD_NUMBER 16

char translate(char character) {
  switch(character) {
   case 'H': return 0;
   case 'C': return 1;
   case 'S': return 2;
   case 'D': return 3;
   case 'T': return 10;
   case 'J': return 11;
   case 'Q': return 12;
   case 'K': return 13;
   case 'A': return 14;
   default:
     return (int)(character - '0');
  }
}

int max(int a, int b) {return a>b?a:b;}

double analyze_hand(int hand[CARD_TYPES][CARD_NUMBER]) {
  int i,j, consecutive=0, full, same_type;
  double value=0.0, extra=0;
  int cards_number[CARD_NUMBER] = {0};

  for(i=0;i<CARD_TYPES; i++) {
    same_type = 0;
    for(j=0;j<CARD_NUMBER; j++){
      if (hand[i][j] == 1) {
        // count for pairs
        cards_number[j] += 1;

        //check for consecutive cards with the same type
        consecutive = 0;
        while(j<CARD_NUMBER && hand[i][j] == 1) {
          consecutive++; j++;
        }

        //royal flush or straight flush
        if(consecutive == 5) {
          if(j-1 == 13) value = max(value, 10*100 + 13);
          else
            value = max(value, 9*100 + j - 1);
        }

        //flush
        same_type += consecutive;
        if (same_type == 5) {
          value = max(value, 6*100 + j - 1);
        }
        value = max(value, 100 + j);

        //same result for both hands
        extra += (j*1.0)/1000;
      }
    }
  }

  full=0;
  for(i=0; i<CARD_NUMBER; i++) {
    // full house
    if(cards_number[i] == 2) {
      for(j=0; j<CARD_NUMBER; j++) {
        if(cards_number[j] == 3) {
          if (value < (7 * 100 + j)){
            value = max(value, (7 * 100 + j));
            full = 1;
          }
        // two pairs
        } else if(cards_number[j] == 2 && i != j){
          value = max(value, (3 * 100 + max(i,j)));
          full = 1;
        }
      }
      // one pair
      if(!full) {
        value = max(value, 3*100 + i);
      }
    // three of a kind
    }else if(cards_number[i] == 3) {
      value = max(value, 4*100 + i);
    }
  }

  return value+extra;

}

void build_hands(char line[LINE_SIZE]) {
  //   Player #1          Player #2
  // 5H 5C 6S 7S KD     2C 3S 8S 8D TD
  int index, card_value, card_type, i,j;

  int first_hand[CARD_TYPES][CARD_NUMBER] = {0};
  int second_hand[CARD_TYPES][CARD_NUMBER] = {0};

  for(index=0; index<strlen(line); index+=3){

    card_value = translate(line[index]);
    card_type = translate(line[index+1]);

    if(index >= 13) {
      second_hand[card_type][card_value] = 1;
    } else {
      first_hand[card_type][card_value] = 1;
    }
  }

  if (analyze_hand(first_hand) > analyze_hand(second_hand))
    printf("PLAYER 1\n");
  else
    printf("PLAYER 2\n");

}

void play(char line[LINE_SIZE]) {
  build_hands(line);
}

int main() {
  FILE *fin = fopen("input.txt", "r");
  char line[LINE_SIZE];

  while(fgets(line, sizeof line, fin) != NULL) {
    play(line);
  }

  return 0;
}
