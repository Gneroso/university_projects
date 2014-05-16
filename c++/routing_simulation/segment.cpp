#include <iostream>

#include "segment.h"


Segment::Segment(Station *start, Station *end, int _length){
  start = start;
  end = end;
  length = _length;
}

void Segment::print() {
  std::cout<<length<<"\n";
}
