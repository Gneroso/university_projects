#ifndef DIJKSTRA_H
#define DIJSTRA_H

#include "strategy.h"
#include "station.h"
#include "types.h"

class Dijstra : public Strategy {
  int something;
  public:
    Dijstra(graph g): Strategy(g), something(1) {};
    void findRoute(Station start, Station end);
};

#endif
