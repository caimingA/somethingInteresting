# bar = Bar("柱状图数据堆叠示例")
# bar.add("商家A", attr, v1, is_stack=True)
# bar.add("商家B", attr, v2, is_stack=True)
# bar.render()

import json
import numpy as np
import pandas as pd
events = pd.read_csv('120-years-of-olympic-history-athletes-and-results/athlete_events.csv')
regions = pd.read_csv('120-years-of-olympic-history-athletes-and-results/noc_regions.csv')
playerAndCounty = events[['ID', 'Name', 'NOC', 'Medal']]
goldPlayers = playerAndCounty[playerAndCounty['Medal'] == 'Gold']
silverPlayers = playerAndCounty[playerAndCounty['Medal'] == 'Silver']
bronzePlayers = playerAndCounty[playerAndCounty['Medal'] == 'Bronze']

# sns.pairplot(data=playerAndCounty)
# plt.show()

# ax = plt.subplot(1, 2, figsize=(18, 8))
# events['Medal'].value_counts().plot.pie(explode=[0, 0.1], ax=ax[0], shadow=True)

# print(events.describe())
# for i in goldPlayers:
#         if i[2] not in goldCounter[:, 0]:
#                 goldCounter.append([i[2]])
# problem 1
goldPlayers = list(goldPlayers["NOC"])
goldPlayersCountry = list(set(goldPlayers))
silverPlayers = list(silverPlayers["NOC"])
silverPlayersCountry = list(set(silverPlayers))
bronzePlayers = list(bronzePlayers["NOC"])
bronzePlayersCountry = list(set(bronzePlayers))
goldCounter = [[0 for j in range(5)] for i in range(len(goldPlayersCountry))]
print(goldCounter)
# silverCounter = [[0 for j in range(2)] for i in range(len(silverPlayersCountry))]
# bronzeCounter = [[0 for j in range(2)] for i in range(len(bronzePlayersCountry))]

for i in range(0, len(goldPlayersCountry)):
    # print(goldPlayers[i])
    goldCounter[i][0] = goldPlayersCountry[i]
for i in range(0, len(goldPlayers)):
    for j in range(0, len(goldCounter)):
        if goldPlayers[i] == goldCounter[j][0]:
            goldCounter[j][1] += 1

temp = [i[0] for i in goldCounter]
# print(temp)
for i in range(0, len(silverPlayersCountry)):
    # print(goldPlayers[i])
    if silverPlayersCountry[i] not in temp:
        goldCounter.append([silverPlayersCountry[i], 0, 0, 0, 0])
for i in range(0, len(silverPlayers)):
    for j in range(0, len(goldCounter)):
        if silverPlayers[i] == goldCounter[j][0]:
            goldCounter[j][2] += 1

temp = [i[0] for i in goldCounter]

# print(temp)
for i in range(0, len(bronzePlayersCountry)):
    # print(goldPlayers[i])
    if bronzePlayersCountry[i] not in temp:
        goldCounter.append([bronzePlayersCountry[i], 0, 0, 0, 0])
for i in range(0, len(bronzePlayers)):
    for j in range(0, len(goldCounter)):
        if bronzePlayers[i] == goldCounter[j][0]:
            goldCounter[j][3] += 1

for i in range(len(goldCounter)):
    goldCounter[i][4] = goldCounter[i][1] + goldCounter[i][2] + goldCounter[i][3]

goldCounter = sorted(goldCounter, key=lambda x: x[4], reverse=True)
medalCounter = [i for i in goldCounter if i[4] > 100]
# print(goldCounter)
goldCounters = []

from pyecharts import Bar
bar = Bar("medal count", width=1600, height=600)
attr = [i[0] for i in medalCounter]
vg = [i[1] for i in medalCounter]
vs = [i[2] for i in medalCounter]
vb = [i[3] for i in medalCounter]
vSum = [i[4] for i in medalCounter]
# print(attr)
bar.add("gold", attr, vg, label_color=["blue"], is_stack=True, is_datazoom_show=True, is_label_show=True)
bar.add("silver", attr, vs, label_color=["red"], is_stack=True, is_datazoom_show=True, is_label_show=True)
bar.add("bronze", attr, vb, label_color=["silver"], is_stack=True, is_datazoom_show=True, is_label_show=True)
bar.add("total", attr, vSum, label_color=["gold"], is_stack=False, is_datazoom_show=True, is_label_show=True)
bar.render("medal.html")




# attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 = [5, 20, 36, 10, 75, 90]
# v2 = [10, 25, 8, 60, 20, 80]




# print(goldPlayers)


#
# bar3D = Bar("柱状图数据堆叠示例")
# bar3D.add("商家A", attr, v1, is_stack=False)
# bar3D.add("商家B", attr, v2, is_stack=False)
#
# bar3D.render()
#
# from pyecharts import Bar3D
#
# bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
# x_axis = ["12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
#           "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"]
# y_aixs = ["Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]
# data = [[0, 0, 5], [0, 1, 1], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0], [0, 6, 0], [0, 7, 0],
#         [0, 8, 0],[0, 9, 0], [0, 10, 0], [0, 11, 2], [0, 12, 4], [0, 13, 1], [0, 14, 1], [0, 15, 3],
#         [0, 16, 4], [0, 17, 6], [0, 18, 4], [0, 19, 4], [0, 20, 3], [0, 21, 3], [0, 22, 2], [0, 23, 5],
#         [1, 0, 7], [1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0], [1, 6, 0], [1, 7, 0], [1, 8, 0],
#         [1, 9, 0], [1, 10, 5], [1, 11, 2], [1, 12, 2], [1, 13, 6], [1, 14, 9], [1, 15, 11], [1, 16, 6], [1, 17, 7],
#         [1, 18, 8], [1, 19, 12], [1, 20, 5], [1, 21, 5], [1, 22, 7], [1, 23, 2], [2, 0, 1], [2, 1, 1],
#         [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0], [2, 6, 0], [2, 7, 0], [2, 8, 0], [2, 9, 0], [2, 10, 3],
#         [2, 11, 2], [2, 12, 1], [2, 13, 9], [2, 14, 8], [2, 15, 10], [2, 16, 6], [2, 17, 5], [2, 18, 5],
#         [2, 19, 5], [2, 20, 7], [2, 21, 4], [2, 22, 2], [2, 23, 4], [3, 0, 7], [3, 1, 3], [3, 2, 0], [3, 3, 0],
#         [3, 4, 0], [3, 5, 0], [3, 6, 0], [3, 7, 0], [3, 8, 1], [3, 9, 0], [3, 10, 5], [3, 11, 4], [3, 12, 7],
#         [3, 13, 14], [3, 14, 13], [3, 15, 12], [3, 16, 9], [3, 17, 5], [3, 18, 5], [3, 19, 10], [3, 20, 6],
#         [3, 21, 4], [3, 22, 4], [3, 23, 1], [4, 0, 1], [4, 1, 3], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 1],
#         [4, 6, 0], [4, 7, 0], [4, 8, 0], [4, 9, 2], [4, 10, 4], [4, 11, 4], [4, 12, 2], [4, 13, 4], [4, 14, 4],
#         [4, 15, 14], [4, 16, 12], [4, 17, 1], [4, 18, 8], [4, 19, 5], [4, 20, 3], [4, 21, 7], [4, 22, 3],
#         [4, 23, 0], [5, 0, 2], [5, 1, 1], [5, 2, 0], [5, 3, 3], [5, 4, 0], [5, 5, 0], [5, 6, 0], [5, 7, 0],
#         [5, 8, 2], [5, 9, 0], [5, 10, 4], [5, 11, 1], [5, 12, 5], [5, 13, 10], [5, 14, 5], [5, 15, 7], [5, 16, 11],
#         [5, 17, 6], [5, 18, 0], [5, 19, 5], [5, 20, 3], [5, 21, 4], [5, 22, 2], [5, 23, 0], [6, 0, 1], [6, 1, 0],
#         [6, 2, 0], [6, 3, 0], [6, 4, 0], [6, 5, 0], [6, 6, 0], [6, 7, 0], [6, 8, 0], [6, 9, 0], [6, 10, 1],
#         [6, 11, 0], [6, 12, 2], [6, 13, 1], [6, 14, 3], [6, 15, 4], [6, 16, 0], [6, 17, 0], [6, 18, 0], [6, 19, 0],
#         [6, 20, 1], [6, 21, 2], [6, 22, 2], [6, 23, 6]]
# range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
#                '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
# bar3d.add("", x_axis, y_aixs, [[d[1], d[0], d[2]] for d in data], is_visualmap=True,
#           visual_range=[0, 20], visual_range_color=range_color, grid3d_width=200, grid3d_depth=80)
#
# bar3d.render()

