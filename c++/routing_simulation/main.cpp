#include "station.h"
#include "segment.h"
#include "metro.h"
#include "transportation_system.h"

int main() {
  TransportationSystem ratt = TransportationSystem();

  Station maria = Station("maria");
  Station cluj = Station("cluj");
  Station traian = Station("traian");
  Station buzias = Station("buzias");

  Segment traian_buzias = Segment(&traian, &buzias, 10);
  Segment maria_cluj = Segment(&maria, &cluj, 10);

  Metro tram8 = Metro("8");
  tram8.addSegment(&traian_buzias);
  tram8.addSegment(&maria_cluj);

  ratt.addMetro(&tram8);

  ratt.setRoutingStrategy("DIJSTRA");

  return 0;
}
