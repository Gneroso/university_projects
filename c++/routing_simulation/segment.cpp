#include <iostream>

#include "segment.h"
#include "station.h"


Segment::Segment(Station *s, Station *e, int _length){
  start = s;
  end = e;
  length = _length;
}

Station Segment::getEndStation() {
  return *end;
}

Station Segment::getStartStation() {
  return *start;
}

int Segment::getLength() {
  return length;
}

void Segment::print() {
  std::cout<<length<<"\n";
}
