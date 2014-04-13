#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <math.h>
#include <string.h>

#define LENGTH 15
#define COMBINATION_NUMBER 32768
#define NR_THREADS 4

struct point{
  int x, y;
} stack[10000];

char string[LENGTH+1];
char proteins[COMBINATION_NUMBER][LENGTH+1];

int optim[COMBINATION_NUMBER], combination, count;

// arguments needed to calculate the optim number of H-H connection
struct arg_struct{
  int start, end, n;
  struct point stack[10000];
};

void *calculate_optim(void *arguments) {
  struct arg_struct *args = (struct arg_struct *)arguments;

  int i, j, optimal=0, index;;
  int fold[2*LENGTH-1][2*LENGTH-1];
  struct point p;
  char protein[LENGTH+1];

  // compute optim for this batch
  for(index=args->start; index < args->end; index++) {
    strcpy(protein, proteins[index]);
    optimal = 0;

    // use an empty matrix to draw the shape
    for(i=0; i<2*LENGTH-1; i++) {
      for(j=0; j<2*LENGTH-1; j++) {
        fold[i][j] = 0;
      }
    }

    // fill the shape with points
    for(i=0; i<LENGTH; i++) {
      // we need to know only Hs
      if (protein[i] == 'H')
        fold[args->stack[i].x][args->stack[i].y] = 1;
    }

    for(i=0; i<LENGTH; i++) {
      // compute the total rank of the graph formed by this shape
      if (protein[i] == 'H'){
        p = args->stack[i];
        if (fold[p.x+1][p.y]) optimal++;
        if (fold[p.x][p.y+1]) optimal++;
        if (fold[p.x-1][p.y]) optimal++;
        if (fold[p.x][p.y-1]) optimal++;
      }
    }

    // number of connections in graph == rank/2
    // check for max number of connections
    if (optim[index] < optimal/2) optim[index] = optimal/2;
  }

  pthread_exit(NULL);
}

void init_fill() {
  int index, j;
  struct arg_struct arg[NR_THREADS];
  pthread_t threads[NR_THREADS];

  // copy stack
  for(j=0; index<NR_THREADS; index++) {
    for(index=0; index<LENGTH; index++) {
      arg[j].stack[index] = stack[index];
    }
  }
  // start threads
  for (index=0; index<NR_THREADS; index++) {
    arg[index].start = index*((int)pow(2, LENGTH-1))/NR_THREADS;
    arg[index].end = (index+1)*((int)pow(2, LENGTH-1))/NR_THREADS;
    pthread_create(&threads[index], NULL, calculate_optim, (void *)&arg[index]);
  }
  // wait until all threads are finished
  for (index=0; index<NR_THREADS; index++) {
    pthread_join(threads[index], NULL);
  }
}

int check_point(int x, int y, int stack_size) {
  int i;

  // the point should be in matrix
  if (x > 2*LENGTH-1 || y > 2*LENGTH-1 || x < 0 || y < 0) return 0;
  // stackoverflow
  if (stack_size >= LENGTH) return 0;

  // no duplicates
  for (i=0; i<stack_size; i++)
    if (stack[i].x == x && stack[i].y == y) return 0;

  return 1;
}

int generate_fold(int x, int y, int stack_size) {
  // if the point met the requirements, place it in stack
  if (check_point(x, y, stack_size)){
    stack[stack_size].x = x;
    stack[stack_size].y = y;
    stack_size++;
  }else{
    return -1;
  }

  // we found a shape, compute optima H-H points for each protein
  if (stack_size == LENGTH){
    stack_size--;

    init_fill();

    stack[LENGTH].x = 0;
    stack[LENGTH].y = 0;

  }
  else {
    // keep looking in each 4 directions
    generate_fold(x+1, y, stack_size);
    generate_fold(x, y+1, stack_size);
    generate_fold(x-1, y, stack_size);
    generate_fold(x, y-1, stack_size);
  }
}

int generate_proteins(int str_len) {
  int index;
  char raw_proteins[] = "HP";

  // we have a solution
  if (str_len == LENGTH){
    strcpy(proteins[combination++], string);
    return -1;
  }

  // generate new proteins
  for(index=0; index<=1; index++){
    string[str_len] = raw_proteins[index];
    string[str_len+1] = '\0';

    generate_proteins(str_len+1);
  }
}

int main() {
  int s=0, i;

  generate_proteins(0);

  generate_fold(LENGTH-1, LENGTH-1, 0);

  for(i=0; i<COMBINATION_NUMBER; i++) {
    s+=optim[i];
    printf("\n%d", optim[i]);

  }

  printf("\n%d", s);

  return 0;
}
