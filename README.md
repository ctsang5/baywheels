# How does the expansion of Bay Wheels affect bus ridership in San Francisco?

I investigate whether the expansion of the Bay Wheels bikeshare network acts as a substitute or a complement to SFMTA (Muni) bus ridership, using geospatial mapping and a fixed effects (two way) model. 

To standardize inconsistent station names across years of Bay Wheels data, I created a custom matching algorithm. I mapped out which bikeshare stations were within 400 meters of a bus route to see how they connected. I ran an OLS regression with route and year-month fixed effects to control for time and route specific heterogeneity. 

<div align="center">
  <img src="method_treatment_definition.gif" alt="Treatment Definition">
  <br>
  <em>A visualization of how I defined the treatment. The blue line represents the bus route for the 18. The orange zone is the treatment area (400 meters). A green dot is a bikeshare station within the treatment zone.</em>
</div>




**I find that adding one more bikeshare station within 400 meters of a bus route is associated with a 1.47 percent increase in average daily bus ridership on that route.** So my result is consistent with the idea that Bay Wheels stations act as a complement, rather than a substitute, to Muni buses.

<div align="center">
  <img src="event_study_baywheels.png" alt="Treatment Definition">
  <br>
  <em></em>
</div>

# Data 
- [Baywheels](https://www.lyft.com/bikes/bay-wheels/system-data) (download all csv files up to August 2025 (including) and place into `data/raw/`)
- [SFMTA (monthly average weekday ridership)](https://www.sfmta.com/reports/average-daily-muni-boardings-route-and-month-pre-pandemic-present) (throw into `data/raw/`)
- [SFMTA (stops/trips/routes/shapes)](https://www.sfmta.com/reports/gtfs-transit-data) (unzip into `data/raw/`)
