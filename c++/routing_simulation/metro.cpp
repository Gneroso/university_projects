#include <string.h>
#include <iostream>

#include "metro.h"


Metro::Metro(const char *ptr) {
  name = new char[strlen(ptr)];
  strcpy(name, ptr);
}

void Metro::printSegments() {
  for(unsigned int i=0;i<segments.size();i++)
    segments[i].print();
}

void Metro::addSegment(Segment *segment) {
  segments.push_back(*segment);
}

std::vector<Segment> Metro::getSegments() {
  return segments;
}
