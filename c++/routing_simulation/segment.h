#ifndef SEGMENT_H
#define SEGMENT_H

#include <cstddef>
#include "station.h"

class Segment {
    Station *start;
    Station *end;
    int length;
  public:
    Segment(): start(NULL), end(NULL), length(0) {};
    Segment(Station *start, Station *end, int length);
    void print();
};

#endif
