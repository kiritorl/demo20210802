import numpy as np
import jieba

words = [["你是一个好人，真是个大好人"],
         ["中国是个和平的国家，让世界和平"],
         ["你是一只猪"],
         ["你真的太好了"],
         ["你是个坏人"],
         ["坏蛋!喜欢干坏事!"],
         ["什么时候吃饭"],
         ["你吃饭了吗"],
         ["吃什么"]]
labels = np.array([1, 1, 0, 1, 0, 0, 2, 2, 2])  # y: y1,y2...


def wordDict(words):
    dictList = []  # x(1~n)
    wd = []
    for w in words:
        data = list(jieba.cut(w[0]))
        wd.append(data)
        for t in data:
            if t not in dictList:
                dictList.append(t)
                pass
            pass
        pass
    print(dictList)
    print(wd)
    return dictList, wd
    pass


dictList, wd = wordDict(words)


# 统计词频，计算先验概率
def wordCount(dictList=[], wd=None):
    countw = []
    for row in wd:
        r = np.zeros(shape=(len(dictList)))
        for t in row:
            if t in dictList:
                index = dictList.index(t)
                if index > -1:
                    r[index] += 1
                    pass
                pass
            pass
        countw.append(r)
        pass
    print(np.array(countw))
    return np.array(countw)
    pass


countw = wordCount(dictList, wd)


# 计算先验概率  P(x1="你"|y=1)  P(y=0)=3/6  P(y=1)=3/6
def train(countw, label, dictList):
    p0 = np.zeros(len(dictList))
    p1 = np.zeros(len(dictList))
    p2 = np.zeros(len(dictList))
    for row, t in zip(countw, label):
        if t == 0:
            p0 += row
            pass
        elif t == 1:
            p1 += row
            pass
        elif t == 2:
            p2 += row
            pass
        pass
    py0 = 3 / 9
    py1 = 3 / 9
    py2 = 3 / 9
    return (p0 + 1) / (np.sum(p0)+len(dictList)), (p1 + 1) / (np.sum(p1)+len(dictList)), \
           (p2 + 1) / (np.sum(p2)+len(dictList)), py0, py1, py2
    pass


p0, p1, p2, py0, py1, py2 = train(countw, labels, dictList)


def predict(x, p0, p1, p2, py0, py1, py2):
    x = list(jieba.cut(x[0]))
    print(x)
    xList = wordCount(dictList, [x])
    logp0 = [np.log(x) if x > 0 else 0 for x in p0]
    logp1 = [np.log(x) if x > 0 else 0 for x in p1]
    logp2 = [np.log(x) if x > 0 else 0 for x in p2]
    r0 = np.sum(xList * logp0) + np.log(py0)
    r1 = np.sum(xList * logp1) + np.log(py1)
    r2 = np.sum(xList * logp2) + np.log(py2)
    if max(r0, r1, r2) == r0:
        return 0
    elif max(r0, r1, r2) == r1:
        return 1
    elif max(r0, r1, r2) == r2:
        return 2
    pass


x0 = ["你是不是猪"]
x1 = ["大好人"]
x2 = ["你今天吃饭了吗"]
print(predict(x0, p0, p1, p2, py0, py1, py2))
print(predict(x1, p0, p1, p2, py0, py1, py2))
print(predict(x2, p0, p1, p2, py0, py1, py2))
