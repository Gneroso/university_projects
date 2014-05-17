#include <iostream>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <string.h>
#include <climits>

#include "dijstra.h"
#include "types.h"

#define pp std::pair<Station, int>

class Prioritize {
  public:
    int operator() ( const std::pair<Station, int>& p1, const std::pair<Station, int>& p2 ) {
      return p1.second < p2.second;
    }
};

void Dijstra::findRoute(Station start, Station end){
  graph costs;
  std::priority_queue<pp, std::vector<pp>, Prioritize> queue;

  // all the stations have int_max as cost
  for(graph::iterator it=g.begin(); it!=g.end(); it++) {
    costs[it->first][it->first] = INT_MAX;

    for(distance::iterator jt=it->second.begin(); jt!=it->second.end(); ++jt){
      costs[jt->first][jt->first] = INT_MAX;
    }
  }

  // set first station to cost 0
  costs[start][start] = 0;
  queue.push(pp(start, 0));
  while(!queue.empty()) {
    // get the station with the lowest cost
    Station station = queue.top().first;
    queue.pop();

    for(graph::iterator it=costs.begin(); it!=costs.end(); ++it) {
      int cost = costs[it->first].begin()->second;

      // go through all stations and get edge cost
      if(g[station].find(it->first) != g[station].end())
        cost = g[station][it->first];
      else if(g[it->first].find(station) != g[it->first].end())
        cost = g[it->first][station];

      // check for a cheaper option
      if (costs[it->first].begin()->second > costs[station].begin()->second + cost) {

        Station old = costs[it->first].begin()->first;
        costs[it->first].erase(old);

        costs[it->first][station] = costs[station].begin()->second + cost;
        queue.push(pp(it->first, costs[it->first].begin()->second));
      }
    }
  }

  std::cout<<"cost "<<costs[end].begin()->second<<"\n";
  std::cout<<"station "<<end.getName()<<"\n";

  Station station = costs[end].begin()->first;

  while(costs[station].begin()->second != 0){
    std::cout<<"station "<<station.getName()<<"\n";
    station = costs[station].begin()->first;
  }

  std::cout<<"station "<<start.getName()<<"\n";
};
