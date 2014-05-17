#ifndef TRANSPORTATION_SYSTEM_H
#define TRANSPORTATION_SYSTEM_H

#include <vector>
#include "strategy.h"
#include "metro.h"

class TransportationSystem {
    std::vector<Metro> metros;
    Strategy *strategy;
  public:
    TransportationSystem(): strategy(NULL) {};
    void setRoutingStrategy(const char *type);
    void addMetro(Metro *metro);
};

#endif
