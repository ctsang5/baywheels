# How does the expansion of Bay Wheels affect bus ridership in San Francisco?

I investigate whether the expansion of the Bay Wheels bikeshare network acts as a substitute or a complement to SFMTA (Muni) bus ridership, using geospatial mapping and a fixed effects (two way) model. To standardize inconsistent station names across years of Bay Wheels data, I created a custom matching algorithm. I mapped out which bikeshare stations were within 400 meters of a bus route to see how they connected. I ran an OLS regression with route and year-month fixed effects to control for time and route specific heterogeneity. 

![Treatment Definition](method_treatment_definition.gif)

*The blue line is the bus route for the 18 and the orange boundary represents the 400 meter buffer zone around its stops. The red dots are active Bay Wheels stations outside the buffer zone, and the green dots are active stations inside the buffer zone.*

**I find that adding one more bikeshare station within 400 meters of a bus route is associated with a 1.47 percent increase in average daily bus ridership on that route.** So my result is consistent with the idea that Bay Wheels stations act as a complement, rather than a substitute, to Muni buses.

# Data sources
- Baywheels: https://www.lyft.com/bikes/bay-wheels/system-data
- SFMTA (monthly average weekday ridership): https://www.sfmta.com/reports/average-daily-muni-boardings-route-and-month-pre-pandemic-present
- SFMTA (stops/trips/routes/shapes): https://www.sfmta.com/reports/gtfs-transit-data
