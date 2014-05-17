#ifndef STRATEGY_H
#define STRATEGY_H

#include <vector>
#include "segment.h"
#include "station.h"
#include "types.h"

class Strategy {
  protected:
    graph g;
  public:
    Strategy(graph g);
    virtual void findRoute(Station start, Station end);
};

#endif
