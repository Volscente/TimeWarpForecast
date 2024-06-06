# Time Series
## Definition
It is a set of subsequent observations recorded over time. They are typically recorded with a regular and fixed 
frequency (e.g., hourly, daily, monthly, etc.).

## Features
There are different types of features when talking about Time Series:
- *Time-Step Features*
- *Lag Features*

### Time-Step Features
Time-step features are features we can derive directly from the time index. 
The most basic time-step feature is the **Time Dummy**, which counts off time steps in the series from beginning to end.

For example, the **Time** column in the following example:

![Time Dummy](./images/time_step_features.png)

The Time-Step features model the so-called **Time Dependence**: series is time-dependent if its values can be predicted 
from the time they occurred. For example, in the *Hardcover Sales* series, the sales later in the month are
generally higher than sales earlier in the month.

### Lag Features
They shift the observations of the target series so that they appear to have occurred later in time.

![Time Dummy](./images/lag_features.png)

The Lag features model the so-called **Serial Dependence**: time series has serial dependence when an 
observation can be predicted from previous observations. In *Hardcover Sales*, we can predict that high sales on one 
day usually mean high sales the next day.

## Trend
The **Trend** component of a time series represents a persistent, long-term change in the mean of the series.
The trend is the slowest-moving part of a series, the part representing the largest timescale of importance.

![Trend](./images/trend.png)

One of the most common trend is in the **mean**.

### Moving Average Plot
It is a technique used to see what kind of trend a time series might have. 
It is plotted by computing the average of the values within a sliding window of some defined width.

![Moving Average](./images/moving_average.png)

The *Mauna Loa* series above has a repeating up and down movement year after year -- a short-term, 
seasonal change. For a change to be a part of the trend, it should occur over a longer period than any seasonal changes. 
To visualize a trend, therefore, we take an average over a period longer than any seasonal period in the series. 
For the *Mauna Loa* series, we chose a window of size 12 to smooth over the season within each year.

The Moving Average is used to see a trend without the "noise" added by seasonal changes.

### Feature Engineering
A Trend can be engineered through a time-step feature, either linear or quadratic, depending on the trend type:
- `target = a * time + b`
- `target = a * time ** 2 + b * time + c`

![Trend Feature Engineering](./images/trend_feature_engineering.png)

# Modeling
## Time-Step & Lag Features
The best time series models will usually include some combination of time-step features and lag feature.

## Linear Regression
Linear regression is widely used in practice and adapts naturally to even complex forecasting tasks.

$` y = x_1 \cdot w_1 + \ldots + x_n \cdot w_n + b `$

