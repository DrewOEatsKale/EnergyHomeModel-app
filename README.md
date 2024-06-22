# Home Energy Use Model

## Webapp for using the model

## Overview
This model is intended to predict energy use in a residential property based on thermostat data and energy meter data. With the switch to electrification of all home appliances and at-home EV charging, power companies may be shifting to performance-based electricity consumption. Modeling energy use on a smaller set of available data would be a cheaper method to predict energy usage. Of course, individual measurements could be taken at the electrical panel at the house and then historical energy use could be directly monitored over time.

This model was lackluster in predicting much of the variability in the response. This is likely due to the fact that the response variable was *whole* home energy use while the predictor data only came from the HVAC use. This means there was no data one when I was running my other large appliances in the home or plugging in other space heaters. According to the U.S Energy Information Administation (https://www.eia.gov/energyexplained/use-of-energy/homes.php), a smaller percentage of total energy use can be atrributed to HVAC in apartment buildings compared to single-family homes. There may be better options for applying models like this to single-family homes where HVAC is a bigger portion of total energy use. The model may also be improved by using something like an Emporia (https://shop.emporiaenergy.com/collections/in-panel-energy-monitors) or Sense (https://sense.com/buy/) energy meter. This would somewhat defeat the purpose of the model since all energy use could be directly measured anyways. One of the purposes of this model was to creat an accurate usage prediction without adding hardware to directly measure all energy use.

This model avoided using a timeseries approach due to the content covered in the class and my skill level. It is possible that the method used is less accurate than just using a timeseries model. My (and other's) energy use is likely cyclically connected with the time of day and time of year.

## Data Description
### Ecobee "5-min" thermostat data
In my home, I had an Ecobee thermostat installed. Ecobee provides users with an option to download their usage data: https://support.ecobee.com/s/articles/Using-the-HomeIQ-System-Monitor. Most of the data comes from this data source.

### Power Company 1-hour energy meter data
My energy provider, AES Indiana, also allows the customer download their usage data. This data is in 1-hour increments.

### Other data details
* thermostat data applied to only a subset of known predictors (i.e. now water heater usage predictors)
* Data spans from September 2023 to March 2024

### Predictors

### Response


## Algorithm Description



## Tools Used


## Ethical Concerns and Considerations
The data comes from disconnected sources with different goals in mind which makes integration difficult. power companies may get this data as part of their incentive programs. Power companies face many technical, legal, and political barriers to make payment schedules based on a model. Models would have to be extremely accurate to charge

---

## Notebooks

### Notebook 1 - Preconditioning
All of the data comes from standard sources, however, the data still needs to be transformed into something usable. In this case, it is a pandas dataframe. I included this notebook, but the input data will not be present to hide some potentially sensitive data. Ecobee and AES Indiana both report some identifying informations which will not be saved in this repository.

This model is trained on a single house, or rather, a single unit in a multi-family condo building. This is significant since 