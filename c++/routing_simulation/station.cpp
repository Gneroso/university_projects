#include <iostream>
#include <string.h>

#include "station.h"


Station::Station (const char* ptr){
  name = new char[strlen(ptr)];
  strcpy(name, ptr);
};

char* Station::getName() const{
  return name;
}

char* Station::getName(){
  return name;
}

void Station::printName(){
  std::cout<<name;
};

bool Station::operator!=(const Station& rhs) const {
  return strcmp(this->name, rhs.name) != 0;
}

bool Station::operator==(const Station& rhs) const {
  return strcmp(this->name, rhs.name) == 0;
}

bool Station::operator<(const Station& rhs) const {
  int cmp = strcmp(this->name, rhs.name);
  if (cmp < 0) return true;
  return false;
}
