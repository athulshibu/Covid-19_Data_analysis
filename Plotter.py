import matplotlib.pyplot as plt
import pandas
from sklearn import datasets, linear_model
import numpy
from statistics import mean

def locate(listOfElements, element):
    indexPosList = []
    for i in range(len(listOfElements)): 
        if listOfElements[i] == element:
            indexPosList.append(i)
    return indexPosList

def slope_int_calc(x,y):
    xs = numpy.array(x)
    ys = numpy.array(y)
    m = ( ((mean(xs)*mean(ys)) - mean(xs*ys)) /
              ((mean(xs)**2) - mean(xs**2)) )
    b = mean(ys) - m*mean(xs)
    return m,b

conc_countries = ['Australia','India','Italy','France','Korea, South','Canada'] 

#####################################################################################################################################################################

data = pandas.read_csv("file:///C:/Users/HP/Desktop/Athul/Academics B.Tech/Semester 6/Introduction to Data Communication/time_series_covid19_confirmed_global.csv")
headers = data.columns

countries = []
for i in range(253):
    countries.append(data[headers[1]][i])

confirmed = []
for i in range(253):
    confirmed.append([])
    for j in range (4,71):
        confirmed[i].append(data[headers[j]][i])

conc_countries_confirmed = []
for i in range(6):
    index = locate(countries,conc_countries[i])
    conc_countries_confirmed.append(confirmed[index[0]])
    if len(index)>1:
        for j in range(1,len(index)):
            for k in range (1,67):
                conc_countries_confirmed[i][k] = conc_countries_confirmed[i][k] + confirmed[index[j]][k]

conc_confirmed_increase = []
for i in range(len(conc_countries)):
    conc_confirmed_increase.append([])
    for j in range (1,len(conc_countries_confirmed[i])):
        conc_confirmed_increase[i].append(conc_countries_confirmed[i][j]-conc_countries_confirmed[i][j-1])

conc_conf_d_day = []
for i in range(len(conc_countries)):
    for j in range(0,len(conc_countries_confirmed[i])):
        if conc_countries_confirmed[i][j+1]>0:
            conc_conf_d_day.append(conc_countries_confirmed[i][j:len(conc_countries_confirmed[i])])
            break

conc_inc_d_day = []
for i in range(len(conc_countries)):
    conc_inc_d_day.append([])
    for j in range (1,len(conc_conf_d_day[i])):
        conc_inc_d_day[i].append(conc_conf_d_day[i][j]-conc_conf_d_day[i][j-1])

for i in range(len(conc_countries)):
    slope,b_int = slope_int_calc(conc_inc_d_day[i],range(1,len(conc_inc_d_day[i])+1))
    regression_line = [slope * x for x in range(1,len(conc_confirmed_increase[i])+1)]
    plt.plot(regression_line,label=conc_countries[i])
plt.xlabel('Days')
plt.ylabel('Increase in No: of Cases')
plt.legend()
plt.title('Regression Graph of Increase in Cases')
plt.show()

#####################################################################################################################################################################

data = pandas.read_csv("file:///C:/Users/HP/Desktop/Athul/Academics B.Tech/Semester 6/Introduction to Data Communication/time_series_covid19_recovered_global.csv")
headers = data.columns

countries = []
for i in range(239):
    countries.append(data[headers[1]][i])

recovered = []
for i in range(len(countries)):
    recovered.append([])
    for j in range (4,71):
        recovered[i].append(data[headers[j]][i])
        
conc_countries_recovered = []
for i in range(6):
    index = locate(countries,conc_countries[i])
    conc_countries_recovered.append(recovered[index[0]])
    if len(index)>1:
        for j in range(1,len(index)):
            for k in range (1,67):
                conc_countries_recovered[i][k] = conc_countries_recovered[i][k] + recovered[index[j]][k]

conc_recv_d_day = []
for i in range(len(conc_countries)):
    for j in range(0,len(conc_countries_recovered[i])):
        if conc_countries_recovered[i][j+1]>0:
            conc_recv_d_day.append(conc_countries_recovered[i][j:len(conc_countries_recovered[i])])
            break

conc_recovered_inc = []
for i in range(len(conc_countries)):
    conc_recovered_inc.append([])
    for j in range (1,len(conc_recv_d_day[i])):
        conc_recovered_inc[i].append(conc_recv_d_day[i][j]-conc_recv_d_day[i][j-1])
