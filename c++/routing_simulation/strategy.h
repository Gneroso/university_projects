#ifndef STRATEGY_H
#define STRATEGY_H

#include <vector>
#include "segment.h"

class Strategy {
    std::vector<Segment> *segments;
  public:
    Strategy(std::vector<Segment> *segments);
    virtual void findRoute();
};

#endif
