#ifndef STRATEGY_H
#define STRATEGY_H

#include <vector>
#include "segment.h"
#include "types.h"

class Strategy {
  protected:
    graph g;
  public:
    Strategy(graph g);
    virtual void findRoute();
};

#endif
