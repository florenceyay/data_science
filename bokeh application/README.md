created a bokeh dashboard with the New York City data division
(The data is trimmed down to only include the incidents that occurred in 2020 )

The goal of the dashboard is to allow a city official to evaluate the difference in response time to complaints filed through the 311 service by zipcode. Response time is measured as the amount of time from incident creation to incident closed. Using the dataset from the previous exercise, build a bokeh dashboard which provides in a single column, the following:
- A drop down for selecting zipcode 1
- A drop down for selecting zipcode 2
- A line plot of monthly average incident create-to-closed time (in hours)
o Don’t include incidents that are not yet closed o The plot contains three curves:
▪ For ALL 2020 data
▪ For 2020 data in zipcode 1
▪ For 2020 data in zipcode 2
▪ A legend naming the three curves
▪ Appropriate x and y axis labels

 When either of the zipcode dropdowns are changed, the plot should update as appropriate.

