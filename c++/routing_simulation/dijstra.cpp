#include <iostream>
#include "dijstra.h"
#include "types.h"

void Dijstra::findRoute(){
  for(graph::iterator it=g.begin(); it!=g.end(); ++it){
    for(distance::iterator jt=it->second.begin(); jt!=it->second.end(); ++jt){
      std::cout<<jt->second;
    }
  }
};
