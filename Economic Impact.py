from forex_python.converter import CurrencyRates
import datetime
import pandas
import matplotlib.pyplot as plt
import numpy
from statistics import mean

def slope_int_calc(x,y):
    xs = numpy.array(x)
    ys = numpy.array(y)
    m = ( ((mean(xs)*mean(ys)) - mean(xs*ys)) /
              ((mean(xs)**2) - mean(xs**2)) )
    c = mean(ys) - m*mean(xs)
    return m,c

currency = 'KRW'
num_corresponding_to_country = 143


c = CurrencyRates()
conv_values = []
#currencies = ['INR','AUD','EUR','CAD','KRW']
date = datetime.datetime(2018, 1, 22)
    for j in range(66):        
        print(date)
        conv_values.append(c.get_rates(currency,date)['USD'])
        date = date + datetime.timedelta(days=1)
print(conv_values)

data = pandas.read_csv("file:///C:/Users/HP/Desktop/Athul/Academics B.Tech/Semester 6/Introduction to Data Communication/Assignment 1 - COVID19 Analysis/time_series_covid19_confirmed_global.csv")
headers = data.columns

confirmed = []

for j in range (4,71):
    confirmed.append(data[headers[j]][num_corresponding_to_country])
print(confirmed)

plt.plot(confirmed)
plt.xlabel('Days')
plt.ylabel('No: of Cases')
plt.title('Confirmed Cases of Infection in South Korea')
plt.show()
plt.plot(conv_values)
plt.xlabel('Days')
plt.ylabel('Value in USD')
plt.title('Value of Korean Won')
plt.show()


