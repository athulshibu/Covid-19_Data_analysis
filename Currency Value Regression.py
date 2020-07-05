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

c = CurrencyRates()
conv_values = []
currencies = ['INR','AUD','EUR','CAD','KRW']
currency_multiplier = [500,10,6,10,10000]
num_of_values = 66
date = datetime.datetime(2018, 1, 22)
for i in range(len(currencies)):
    conv_values.append([])
    date = datetime.datetime(2018, 1, 22)
    for j in range(num_of_values):        
        print(date, end=" ")
        print(currencies[i])
        conv_values[i].append(c.get_rates(currencies[i],date)['USD']*currency_multiplier[i])
        date = date + datetime.timedelta(days=1)
print(conv_values)

for i in range(len(currencies)):
    slope,b_int = slope_int_calc(conv_values[i],range(1,num_of_values+1))
    regression_line = [slope * x + b_int for x in range(1,num_of_values+1)]
    plt.plot(regression_line, label = currencies[i])
plt.xlabel('Days')
plt.ylabel('Value')
plt.title('Regression Value of each currency')
plt.legend()
plt.show()
