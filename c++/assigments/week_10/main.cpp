#include "sort.h"

int main(){
  vector<int> v;

  v.add(3);
  v.add(5);
  v.add(0);

  // specify the order
  //    >= 0 --> ascendent
  //    <  0 --> descendent
  v.sort(-1);

  v.print();

  return 0;
}
