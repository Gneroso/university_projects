#include <string.h>
#include <iostream>
#include <map>

#include "transportation_system.h"
#include "dijstra.h"
#include "metro.h"
#include "segment.h"
#include "types.h"

void TransportationSystem::addMetro(Metro *metro) {
  metros.push_back(*metro);
}

void TransportationSystem::setRoutingStrategy(const char *type){
  std::vector<Segment> segments = metros[0].getSegments();

  if(!strcmp(type, "DIJSTRA")) {
    strategy = new Dijstra(this->dumpGraph());
  }
}

void TransportationSystem::findRoute(Station start, Station end) {
  strategy->findRoute(start, end);
}

graph TransportationSystem::dumpGraph(){
  graph g;

  for(unsigned int i=0; i<metros.size(); i++) {
    std::vector<Segment> segments = metros[i].getSegments();
    for(unsigned int segment=0; segment<segments.size(); segment++){
      Station start = segments[segment].getStartStation();
      Station end = segments[segment].getEndStation();

      g[start][end] = segments[segment].getLength();
    }
  }

  return g;
}
