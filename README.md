# Does the expansion of Bay Wheels bikeshare stations affect San Francisco Muni's average daily bus ridership? 

I investigate whether the expansion of the Bay Wheels bikeshare network acts as a substitute or a complement to SFMTA bus ridership. Using geospatial mapping and a Difference in Differences framework, I analyze monthly average ridership trends from January 2019 to August 2025.

**I find that adding one more bikeshare station within 400 meters of a bus route is associated with a 1.47 percent increase in average daily bus ridership on that route.** So my result is consistent with the idea that Bay Wheels stations act as a complement, rather than a substitute, to Muni buses.

### How did I define the treatment?
In short, I checked if a bus route passed near a bikeshare station that was active during that specific month. A bus route has many bus stops. So for each bus route, I applied a 400 meter buffer around each of its stops to identify which Bay Wheels stations fell within those buffer zones and calculated the total number of _unique_ stations. Of those unique stations, I only counted the stations that were actually open during the month in question. The result is the number of bikeshare stations actually available to a rider at that specific month. 

![Treatment Definition](method_treatment_definition.gif)
*The blue line is the bus route for the 18 and the orange boundary represents the 400 meter buffer zone around its stops. The red dots are active Bay Wheels stations outside the buffer zone, and the green dots are active stations inside the buffer zone.*

# Data sources
- Baywheels: https://www.lyft.com/bikes/bay-wheels/system-data
- SFMTA (monthly average weekday ridership): https://www.sfmta.com/reports/average-daily-muni-boardings-route-and-month-pre-pandemic-present
- SFMTA (stops/trips/routes/shapes): https://www.sfmta.com/reports/gtfs-transit-data
