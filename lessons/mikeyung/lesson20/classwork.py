import numpy as np
import pandas
import matplotlib.pyplot as plt
from sklearn import linear_model
from statsmodels.iolib.table import SimpleTable

import statsmodels.api as sm
from scipy import stats
from statsmodels.graphics.api import qqplot

print sm.datasets.sunspots.NOTE

dta = sm.datasets.sunspots.load_pandas().data

dta[:2]

dta.plot(x="YEAR", y="SUNACTIVITY", figsize=(12,3));
plt.show()

regr = linear_model.LinearRegression()

years = [ [x] for x in dta["YEAR"].values]
sunsp = dta["SUNACTIVITY"].values

yearsTrain = years[:250]
yearsTest  = years[251:]
sunspTrain = sunsp[:250]
sunspTest  = sunsp[251:]

regr.fit(yearsTrain, sunspTrain)

regr.predict(yearsTest)

dta.plot(x="YEAR", y="SUNACTIVITY", figsize=(12,3));
plt.plot(years, regr.predict(years), color='red', linewidth=3)
plt.show()

print "regr.score ...", regr.score(yearsTest, sunspTest)
# This literally means that we did worse than a flat line -- yikes, time to try something else

import random

sampleSize = 5000

x = []

for i in range(sampleSize):
    x.append(random.normalvariate(0,1))

resid = pandas.DataFrame([ [x[i] ] for i in range(len(x))])

resid.plot()

plt.show()
# Note: These aren't actual residuals just normally distributed random data 
# (which is how we want our actual residuals to look). 
# Pretend the X axis is time rather than just an index.

# Now that we have a pretty new picture I know you're itching to plot some thing 
# with some other thing but first we should clean up our data a bit:

dta[:2]

dta.index = pandas.Index(sm.tsa.datetools.dates_from_range('1700', '2008'))

dta[:2]

del dta["YEAR"]

dta[:2]

dta.plot(figsize=(12,3))

plt.show()

sta = dta
sta.index = pandas.Index(sm.tsa.datetools.dates_from_range('1700', '2008'))
# del sta["YEAR"]

# If the timeseries's resolution was too high, say with dailymeasurements, we could have used the resample method.
# dta = dta.resample('W', how='mean')

# Check the distribution
sta.hist()
plt.show()

# Let's confirm the assumption of normal distribution. For this purpose in there are a function of jarque_bera() which returned values of g statistics:
# source : http://en.wikipedia.org/wiki/Jarque%E2%80%93Bera_test

row =  [u'JB', u'p-value', u'skew', u'kurtosis']
jb_test = sm.stats.stattools.jarque_bera(sta)
a = np.vstack([jb_test])
itog = SimpleTable(a, row)
print itog

# Many methods and models was based on assumptions of stationarity of
# a row but as it were not earlier our row by that most likely are not.
# Therefore for check of check of stationarity let's carry out the 
# generalized test of Dickey Fuller for presence of unit roots
# http://en.wikipedia.org/wiki/Dickey%E2%80%93Fuller_test

test = sm.tsa.adfuller(sta['SUNACTIVITY'].values)
print 'adf: ', test[0] 
print 'p-value: ', test[1]
print 'Critical values: ', test[4]
if test[0] > test[4]['10%']: 
    print 'has unit roots , the series is not stationary'
else:
    print 'has no unit roots , the series is stationary'

# Now that we've stared at statistics for a while it's time to make some pretty pictures.

fig = plt.figure(figsize = (12, 6))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dta.values, lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(dta, lags=40, ax=ax2)

plt.show()

arma_mod20 = sm.tsa.ARMA(dta, (2, 0)).fit()
print arma_mod20.params

# Akaike Information Criterion -2*llf+2* df_model where df_model includes all AR parameters, MA parameters, constant terms parameters on constant terms and the variance.
print "AIC: ", arma_mod20.aic
# Bayes Information Criterion -2*llf + log(nobs)*df_model Where if the model is fit using conditional sum of squares, the number of observations nobs does not include the p pre-sample observations.
print "BIC: ", arma_mod20.bic
# Hannan-Quinn Information Criterion -2*llf + 2*(df_model)*log(log(nobs)) Like bic if the model is fit using conditional sum of squares then the k_ar pre-sample observations are not counted in nobs.
print "HQIC:", arma_mod20.hqic
# (Minimize these -- "___ Information Criterion")

fig = plt.figure(figsize=(12,3))
ax = fig.add_subplot(111)
ax = arma_mod20.resid.plot(ax=ax)

plt.show()

resid = arma_mod20.resid
# Tests whether a sample differs from a normal distribution.
# It is based on D'Agostino and Pearson's test that combines
# skew and kurtosis to produce an omnibus test of normality.

stats.normaltest(resid)
stats.kurtosistest(resid)
stats.skewtest(resid)

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)
fig = qqplot(resid, line='q', ax=ax, fit=True)

plt.show()

fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(resid, lags=40, ax=ax2)

plt.show()

bestResult = [np.inf, 0, 0]

for i in range(15):
    arma_mod = sm.tsa.ARMA(dta, (i,0)).fit()
#    print i, arma_mod.aic

    if arma_mod.aic < bestResult[0]:
        bestResult[0] = arma_mod.aic
        bestResult[1] = i

print bestResult

arma_mod = sm.tsa.ARMA(dta, (bestResult[1],0)).fit()
resid = arma_mod.resid

"""
fig = plt.figure(figsize = (12,3))
ax = fig.add_subplot(111)
ax = arma_mod.resid.plot(ax=ax)
plt.show()

stats.normaltest(resid)
stats.kurtosistest(resid)
stats.skewtest(resid)

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)
fig = qqplot(resid, line='q', ax=ax, fit=True)

plt.show()

fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(resid, lags=40, ax=ax2)

plt.show()
"""

predict_sunspots = arma_mod.predict('1980', '2050', dynamic=True)

ax = dta.ix['1950':].plot(figsize=(12,3))
ax = predict_sunspots.plot(ax=ax, style='r--', label='Dynamic Prediction');
ax.legend();
ax.axis((-20.0, 38.0, -4.0, 200.0));
ax.set_xlim(0, 50)
plt.show()

# Ljung-Box test, tests whether any of a group of autocorrelations 
# of a time series are different from zero. Instead of testing randomness 
# at each distinct lag, it tests the 'overall' randomness based on a number 
# of lags

r, q, p = sm.tsa.acf(resid.values.squeeze(), qstat=True)
data = np.c_[range(1,41), r[1:], q, p]
table = pandas.DataFrame(data, columns=["lag", "AC", "Q", "Prob(>Q)"])
print table.set_index('lag')

def mean_forecast_err(y, yhat):
    return y.sub(yhat).mean()

mean_forecast_err(dta.SUNACTIVITY, predict_sunspots)

from statsmodels.tsa.arima_process import arma_generate_sample, ArmaProcess

np.random.seed(1234)
arparams = np.array([1, .75, -.65, -.55, .9])
maparams = np.array([1, .65])

arma_t = ArmaProcess(arparams, maparams)

arma_t.isinvertible()

arma_t.isstationary()

fig = plt.figure(figsize=(12,3))
ax = fig.add_subplot(111)
ax.plot(arma_t.generate_sample(size=50));

arparams = np.array([1, 0])
maparams = np.array([1, .5])
arma_t = ArmaProcess(arparams, maparams)
arma_t.isstationary()

arma_rvs = arma_t.generate_sample(size=500, burnin=250, scale=2.5)

fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(arma_rvs, lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(arma_rvs, lags=40, ax=ax2)

plt.show()

arma1 = sm.tsa.ARMA(arma_rvs, (1,1)).fit()
resid = arma1.resid
r, q, p = sm.tsa.acf(resid, qstat=True)
data = np.c_[range(1,41), r[1:], q, p]
table = pandas.DataFrame(data, columns=["lag", "AC", "Q", "Prob(>Q}"])
print table.set_index("lag")

## Macroeconomic data

macrodta = sm.datasets.macrodata.load_pandas().data
macrodta.index = pandas.Index(sm.tsa.datetools.dates_from_range('1959Q1', '2009Q3'))

cpi = macrodta["infl"]
macrodta

fig = plt.figure(figsize=(12,3))
ax = fig.add_subplot(111)
ax = cpi.plot(ax=ax)
ax.legend()

plt.show()

print sm.tsa.adfuller(cpi)