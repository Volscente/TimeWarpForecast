# Introduction
## Statistics in Time Series Forecasting
There exist several statistical tests that allow to understand the characteristics of a Time Series, in order to
further select the most appropriate model to train.

For example, these tests check:
- Stationary: A time series has constant mean, variance and covariance over time
- Causality: A time series can be used for forecasting another time series

# Check Stationary
## Augmented Dickey-Fuller Test
### General
It quantifies if a time series is stationary by a Null Hypothesis test.

Such Null Hypothesis test states that Phi is equal to one, implying the presence of a unit root and non-stationarity 
of the time series. If the p-value is less than the critical value, the Null Hypothesis is rejected, therefore 
asserting that the time series is stationary.

### Phi Value
It is also called the Coefficient of the lagged level. 
It quantifies the relationship between the current value of the
time series with its lagged value.

# Check Causality
## Granger Causality Test
### General
It is a classic hypothesis test that measure whether one time series can forecast another one.
Keep in mind that this test does not explain the factors and it requires field experts to extract the meaning out of it.