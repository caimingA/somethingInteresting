import nltk
import re


def read(path):
    sentencList = list()
    file = open(path, 'r')
    lines = file.readlines()
    for line in lines:
        if line is not '\n':
            line = line[:-1]
            if re.search(r"(\d{4}-\d{1,2}-\d{1,2})",line):
                temp = re.split("@@@ | https", line)
                if temp[1] not in sentencList:
                    sentencList.append(temp[1])
            else:
                temp = re.split("https", line)
                if temp[0] not in sentencList:
                    sentencList.append(temp[0])
            
    return sentencList

if __name__ == '__main__':
    path = "earthquake evacuation.txt"
    words = list()
    result = read(path)
    print("-----------")
    # print(result)
    # for i in result:
    #     print(i)
    for sentence in result:
        words.extend(nltk.word_tokenize(sentence))
    # print(words)
    tags = nltk.pos_tag(words)
    # print(tags)

    word_after = list()
    for tag in tags:
        if tag[1] == 'NN':
            word_after.append(tag[0])
    print(word_after)

    dic = dict()
    for word in word_after:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    # print(dic)
    
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print(dic)

    file = open("result.txt", 'w')
    for item in dic:
        file.write(item[0]+' : '+str(item[1])+'\n')
    file.close()
