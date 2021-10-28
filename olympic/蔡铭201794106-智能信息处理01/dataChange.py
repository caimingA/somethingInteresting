import pandas as pd
regions = pd.read_csv('120-years-of-olympic-history-athletes-and-results/noc_regions.csv')
country = regions[['NOC', 'region']]

country = country.values.tolist()
countryMap = []
for i in range(len(country)):
    countryMap.append([i + 1, country[i]])

print(countryMap)
import pandas as pd
GDP = pd.read_csv(r'countries-of-the-world/countries of the world.csv')
GDP = GDP[['Country', 'Population', 'GDP ($ per capita)']]
# print(GDP.head())

GDPList = GDP.values.tolist()
# for i in range(len(GDPList)):
#     for j in range(len(countryMap)):
#         if GDPList[i] == countryMap[j][1]:
#             GDPList[i] = countryMap[j][0]
#             print(1)

GDPList = sorted(GDPList, key=lambda x: x[2], reverse=True)
print(GDPList)

from pyecharts import Bar
bar = Bar("GDP Top 50", width=1600, height=600)
GDPListTop = []
for i in range(50):
        GDPListTop.append([GDPList[i][0], GDPList[i][2]])

print(GDPListTop)

attr = []
for i in range(len(GDPListTop)):
    attr.append(GDPListTop[i][0])
    # print(GDPListTop[i])

bar.add("country", attr, GDPListTop, is_stack=False, is_label_show=True, is_datazoom_show=True)

bar.render('GDP.html')

PopulationList = sorted(GDPList, key=lambda x: x[1], reverse=True)
PopulationTopList = []
for i in range(50):
    PopulationTopList.append(PopulationList[i])

attr2 = []
for i in range(len(PopulationTopList)):
    attr2.append(PopulationTopList[i][0])

bar2 = Bar("Population Top 50", width=1600, height=600)
bar2.add("country", attr2, PopulationTopList, is_stack=False, is_label_show=True, is_datazoom_show=True)

bar2.render('Population.html')
