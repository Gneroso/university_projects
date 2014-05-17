#ifndef DIJKSTRA_H
#define DIJSTRA_H

#include "strategy.h"
#include <iostream>

class Dijstra : public Strategy {
  int something;
  public:
    Dijstra(std::vector<Segment> *segments): Strategy(segments), something(1) {};
    void findRoute();
};

#endif
