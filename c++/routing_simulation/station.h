#ifndef STATION_H
#define STATION_H

class Station {
    char *name;
  public:
    Station(const char* ptr);
    void printName();
};

#endif
