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
  Station aem = Station("aem");

  Segment aem_cluj = Segment(&aem, &cluj, 2);
  Segment aem_maria = Segment(&aem, &maria, 2);

  Segment maria_cluj = Segment(&maria, &cluj, 10);
  Segment maria_buzias = Segment(&maria, &buzias, 1);

  Segment cluj_buzias = Segment(&cluj, &buzias, 5);
  Segment cluj_traian = Segment(&cluj, &traian, 5);

  Segment traian_buzias = Segment(&traian, &buzias, 3);

  Metro tram8 = Metro("8");
  tram8.addSegment(&maria_cluj);
  tram8.addSegment(&maria_buzias);
  tram8.addSegment(&cluj_buzias);
  tram8.addSegment(&cluj_traian);
  tram8.addSegment(&traian_buzias);
  tram8.addSegment(&aem_cluj);
  tram8.addSegment(&aem_maria);

  ratt.addMetro(&tram8);

  ratt.setRoutingStrategy("DIJSTRA");
  ratt.findRoute(aem, traian);

  return 0;
}
