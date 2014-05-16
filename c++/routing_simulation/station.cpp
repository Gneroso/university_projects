#include <iostream>
#include <string.h>

#include "station.h"


Station::Station (const char* ptr){
  name = new char[strlen(ptr)];
  strcpy(name, ptr);
};

void Station::printName(){
  std::cout<<name;
};
