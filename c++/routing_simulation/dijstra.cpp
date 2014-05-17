#include <iostream>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <string.h>
#include "dijstra.h"
#include "types.h"

#define pp std::pair<Station, int>

typedef std::map<Station, int> Cost;

class Prioritize {
  public:
    int operator() ( const std::pair<Station, int>& p1, const std::pair<Station, int>& p2 ) {
      return p1.second < p2.second;
    }
};

void Dijstra::findRoute(Station start, Station end){
  Cost costs;



  for(graph::iterator it=g.begin(); it!=g.end(); it++) {
    costs[it->first] = 99999;

    for(distance::iterator jt=it->second.begin(); jt!=it->second.end(); ++jt)
      costs[jt->first] = 99999;
  }

  costs[start] = 0;


  std::priority_queue<pp, std::vector<pp>, Prioritize> queue;

  queue.push(pp(start, 0));
  while(!queue.empty()) {
    // get the station with the lowest cost
    Station station = queue.top().first;
    queue.pop();

    for(Cost::iterator it=costs.begin(); it!=costs.end(); ++it) {

      int cost = costs[it->first];
      if(g[station].find(it->first) != g[station].end())
        cost = g[station][it->first];
      else if(g[it->first].find(station) != g[it->first].end())
        cost = g[it->first][station];

      if (costs[it->first] > costs[station] + cost) {
        costs[it->first] = costs[station] + cost;
        queue.push(pp(it->first, costs[it->first]));
      }
    }
  }

  std::cout<<"start"<<costs[end];
};
