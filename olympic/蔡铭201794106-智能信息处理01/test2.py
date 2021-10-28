import pandas as pd
import numpy as np
events = pd.read_csv('120-years-of-olympic-history-athletes-and-results/athlete_events.csv')
regions = pd.read_csv('120-years-of-olympic-history-athletes-and-results/noc_regions.csv')
country = regions[['NOC']]
country = country.values.tolist()
countryMap = []
for i in range(len(country)):
    countryMap.append([i + 1, country[i]])

eventsSelect = events[['Sex', 'Age', 'Height', 'Weight', 'NOC', 'Year', 'Sport', 'Medal']]

attr_arr = eventsSelect.values.tolist()

eventsFilter = []
for i in attr_arr:
    if pd.isnull(i[1]) or pd.isnull(i[2]) or pd.isnull(i[3]):
        pass
    else:
        eventsFilter.append(i)

eventsFilter2 = [i for i in eventsFilter if i[6] == i[6] == "Basketball"]

for i in range(len(eventsFilter2)):
    eventsFilter2[i][1] = float(eventsFilter2[i][1])
    eventsFilter2[i][2] = float(eventsFilter2[i][2])
    eventsFilter2[i][3] = float(eventsFilter2[i][3])
    eventsFilter2[i][5] = float(eventsFilter2[i][5])
    if eventsFilter2[i][0] == 'M':
        eventsFilter2[i][0] = 0
    elif eventsFilter2[i][0] == 'F':
        eventsFilter2[i][0] = 1

    if eventsFilter2[i][7] == 'Gold':
        eventsFilter2[i][7] = 3
    elif eventsFilter2[i][7] == 'Silver':
        eventsFilter2[i][7] = 2
    elif eventsFilter2[i][7] == 'Bronze':
        eventsFilter2[i][7] = 1
    else:
        eventsFilter2[i][7] = 0
for i in range(len(eventsFilter2)):
    for j in range(len(countryMap)):
        if eventsFilter2[i][4] == countryMap[j][1][0]:
            eventsFilter2[i][4] = countryMap[j][0]


dataMat = np.mat(eventsFilter2)
arrMat = dataMat[:, 0:5]
resultMat = dataMat[:, 7:8]
arrNp = np.array(arrMat)
resultNp = np.array(resultMat)
# print(resultNp)
# print(type(resultNp[0][0]))
attr_names = ['sex', 'age', 'height', 'width', 'NOC', '']
from sklearn import svm

clf = svm.SVC()
clf.fit(arrNp, np.ravel(resultNp))
resultSVM = clf.predict([[0, 28, 185, 80, 217]])
print(resultSVM)

from sklearn.ensemble import RandomForestClassifier
rlf = RandomForestClassifier()
rlf.fit(arrNp, np.ravel(resultNp))
resultRF = rlf.predict([[0, 24, 185, 69, 217]])
print(resultRF)


