#include <string.h>
#include <iostream>
#include <map>

#include "transportation_system.h"
#include "dijstra.h"
#include "metro.h"
#include "segment.h"

typedef std::map<Station, int> distance;

void TransportationSystem::addMetro(Metro *metro) {
  metros.push_back(*metro);
}

void TransportationSystem::setRoutingStrategy(const char *type){
  std::vector<Segment> segments = metros[0].getSegments();

  if(!strcmp(type, "DIJSTRA")) {
    strategy = new Dijstra(&segments);
  }

  strategy->findRoute();
}

void TransportationSystem::dumpAdiancyMatrix(){
  std::map<Station, distance> graph;
  distance a;

  for(unsigned int i=0; i<metros.size(); i++) {
    std::vector<Segment> segments = metros[i].getSegments();
    for(unsigned int segment=0; segment<segments.size(); segment++){
      Station start = segments[segment].getStartStation();
      Station end = segments[segment].getEndStation();

      graph[start][end] = segments[segment].getLength();
      std::cout<<graph[start][end]<<" "<<start.getName()<<"\n";
    }
  }
}
