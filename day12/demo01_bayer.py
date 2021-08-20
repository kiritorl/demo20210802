from sklearn.naive_bayes import MultinomialNB
import numpy as np

# 1.加载训练数据集
def loadTrainData():
    trainData = [  ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid'],
                   ['you', 'are', 'a', 'clever', 'dog', 'good', 'dog']]
    classLabel = [0, 1, 0, 1, 0, 1, 0]
    return trainData, classLabel

# 构造词典（不重复的数据集合）
def wordDict(trainData):
    vocabSet = set()
    for row in trainData:
        vocabSet = vocabSet | set(row)
        pass
    return list(vocabSet)
    pass

def wordVector(trainData, vocabList,vocabSize):
    wordVectorList = []
    for row in trainData:
        vector = np.zeros(vocabSize)           # 拉普拉斯平滑
        for  word in row:
            index = vocabList.index(word)
            vector[index] += 1
            pass
        wordVectorList.append(vector)
    return np.array(wordVectorList)
    pass

trainData, labels = loadTrainData()
vocabList = wordDict(trainData)
vocabSize = len(vocabList)
wordVectorList = wordVector(trainData, vocabList,vocabSize)
print(wordVectorList)


model = MultinomialNB()
# 朴素贝叶斯算法是基础算法，商用的算法
model.fit(wordVectorList, labels)

test = [[ 'good', 'stupid', 'clever']]


testV = wordVector(test, vocabList,vocabSize)
print(model.predict(testV))