
#include <iostream>
#include <string.h>

#include "station.h"


Station::Station (const char* ptr){
  strcpy(name, ptr);
}

void Station::printName(){
  std::cout<<name;
}
