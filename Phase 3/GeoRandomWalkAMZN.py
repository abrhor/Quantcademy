import matplotlib.pyplot as plt
import numpy as np
import pandas
import quandl
from statsmodels.graphics.tsaplots import plot_acf
from math import exp, sqrt

AMZN = quandl.get("WIKI/AMZN")
P = AMZN.loc[:, "Close"]
AMZN['Index'] = range(len(AMZN.index.get_values()))

plt.plot(AMZN.loc[:, "Close"], label='AMZN Closing Prices')
plt.show()

time = AMZN.index.values
price_array = AMZN["Close"].tolist()
price_array = np.array(price_array)

diffp = np.diff(price_array)

plot_acf(diffp)
plt.show()

plt.plot(time[:-1], diffp) 
plt.show()

print(np.nanmean(diffp), np.nanstd(diffp))
logp = np.log(price_array)
bottom = np.nanmin(logp)

"""
------------------------------------------------
Let's go from the beginning of this bull market. 
That is, the local minimum somewhere in 2009
------------------------------------------------
"""


# This is tricky. Now that we have the min, slice our time array to isolate the bottom forward, which is positive growth/trend
for t, price in zip(time, logp):
  if price==bottom: # If it's the min, I now have attained the minimum timestamp
    for i, ti in enumerate(time):
      if ti==t: 
      """
      Take the time from the min, and get its index (which is the same 
      in logp and time, would be more complicated if this was a difference)
      Now I can isolate my time and my trend. Bottomtime is the same as trendstart
      """
        trendstart = time[i]
        trendtime = time[i:]
        logptrend = logp[i:]

print(trendstart, trendtime)
plt.plot(trendtime, logptrend)

difflogptrend = np.diff(logptrend)

plot_acf(difflogptrend)

change = logptrend[-1:] - logptrend[0] # numerator
indices = len(logptrend) - 1 # denominator
alphacase = change / indices

forecasts = np.array([])
# forecast - get the drift alpha

def model(loggeddata, alpha, forecast):
  lastp = loggeddata[-1:]
  nextp = lastp + alpha
  return nextp
  
# forecast for 100 days
for i in range(100):
  np.append(forecasts, model(logptrend, alphacase, forecasts))

def confidence(loggeddata, forecast):
  standard_error = np.nanstd(loggeddata)
  confidenceu = np.array([])
  confidencel = np.array([])
  for i, price in enumerate(forecast):
    u = price[i] + standard_error + sqrt(i+1)
    l = price[i] - standard_error - sqrt(i+1)
    np.append(confidenceupper, u)
    np.append(confidencelower, l)

    
confidenceupper, confidencelower = confidence(logptrend, forecasts)
      

realpredicton = np.exp(forecasts), 
realconfidenceu = np.exp(confidenceupper)
realconfidencel = np.exp(confidencelower)

datadict = {
  'Close': realprediction
  'Upper Confidence': realconfidenceu
  'Lower Confidence': realconfidencel
}

# create my new dataframe
forecastclosing = pd.Dataframe(
                  data=datadict
                  index=pd.date_range(
                        start=P.index[len(P.index)]
                        periods=100
                        freq=P.index.freq
                  )
)

plt.plot(P, label='Historical', color='b')
plt.plot(forecastclosing.loc[:, "Close"], label='Forecast', color='r')
plt.plot(forecastclosing.loc[:, "Upper Confidence"], '--', label='Confidence Intervals', color='r')
plt.plot(forecastclosing.loc[:, "Lower Confidence"], '--', color='r')
plt.legend(loc='upper left')
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Geometric Random Walk with Drift of AMZN')
plt.show()
