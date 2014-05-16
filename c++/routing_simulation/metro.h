#ifndef METRO_H
#define METRO_H

#include <vector>
#include "segment.h"

class Metro {
  char* name;
  std::vector <Segment> segments;
  public:
    Metro(const char* ptr);
    void addSegment(Segment* segment);
    void printSegments();
};

#endif
