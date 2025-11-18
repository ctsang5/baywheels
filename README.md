# Does the expansion of Bay Wheels bikeshare stations affect San Francisco Muni's average daily bus ridership? 

Using a route-month level panel data, I estimate a two way fixed effects model. The main idea is to compare changes in ridership over time on bus routes that gained a bikeshare station nearby to routes that did not.

I created a panel dataset of SF Muni bus routes with monthly average daily boardings (ridership) as the outcome variable and merged this panel to Bay Wheels station locations. For each bus route and month, I found the number of unique Bay Wheels stations located within 400 meters of any bus stop on that route. I then estimate a regression of log average daily ridership on the bikeshare treatment variable, including route fixed effects and year-month fixed effects. 

Controlling for route fixed effects and year-month fixed effects, **I find that adding one more bikeshare station within 400 meters of a bus route is associated with a 1.47 percent increase in average daily bus ridership on that route.** Put in another way, my result is consistent with the idea that bikeshare stations complement, rather than substitute, Muni bus services.


