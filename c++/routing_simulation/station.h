#ifndef STATION_H
#define STATION_H

class Station {
    char *name;
  public:
    Station(const char* ptr);
    char* getName();
    void printName();
    bool operator<(const Station &rhs) const;
};

#endif
