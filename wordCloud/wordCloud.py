import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba.posseg as pseg

f = open(r'C:\Users\dell\Desktop\31878\all.txt', 'r', encoding='UTF-8').read()
words = pseg.cut(f)

nameDict = dict()
strName = " "
i = 0
for word, flag in words:
    if flag == "nr":
        if word in nameDict:
            nameDict[word] += 1
        else:
            nameDict.setdefault(word, 1)

nameDictSorted = sorted(nameDict.items(), key=lambda x: x[1], reverse=True)
for key, value in nameDictSorted:
    strName += key + ","
    i += 1
    if i == 50:
        break

wordcloud = WordCloud(background_color="white"
                      , font_path="msyh.ttc"
                      , width=1000
                      , height=860
                      , margin=2).generate(strName)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file('test.png')
