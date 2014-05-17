#include <string.h>
#include <iostream>

#include "transportation_system.h"
#include "dijstra.h"
#include "metro.h"
#include "segment.h"


void TransportationSystem::addMetro(Metro *metro) {
  metros.push_back(*metro);
}

void TransportationSystem::setRoutingStrategy(const char *type){
  std::vector<Segment> segments = metros[0].getSegments();
  if(!strcmp(type, "DIJSTRA")) {
    strategy = new Dijstra(&segments);
    strategy->findRoute();
  }
}
