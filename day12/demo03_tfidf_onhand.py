import numpy as np

texts = ['人工智能 学习 自然 语言 人工智能',
         '我 喜欢 吃鸡',
         '人工智能 是 未来 的 重点 学科',
         '我 爱 人工智能 还是 人工智能 自然 语言 好啊',
         '我 爱 中国']


def wordDict(texts):
    dictList = []
    wordText = []
    for text in texts:
        textArray = text.split(" ")
        wordText.append(textArray)
        for t in textArray:
            if t not in dictList:
                dictList.append(t)
                pass
            pass
        pass
    return dictList, wordText
    pass


def wordCount(dictList, wordText):
    wordCountList = []
    for row in wordText:
        array = np.zeros(len(dictList))
        for w in row:
            index = dictList.index(w)
            array[index] += 1
            pass
        wordCountList.append(array)
        pass
    return np.array(wordCountList)
    pass


dictList, wordText = wordDict(texts)
print(dictList, wordText)
wordCountList = wordCount(dictList, wordText)
print(wordCountList)


def tfidf(wordCountList):
    tf = (wordCountList.T/np.sum(wordCountList, axis=1)).T
    print(tf)
    rowCount = np.array([np.count_nonzero(row)+1 for row in wordCountList.T])
    idf = np.log(len(wordCountList)/rowCount)
    print(idf)
    tfidf = tf * idf
    print(tfidf)
    return tfidf
    pass


tfidfs = tfidf(wordCountList)


# 计算余弦相似度
def predict(tfidf, tfidfs):
    cos = [np.sum(tfidf*row)/(np.sqrt(np.sum(tfidf**2))*np.sqrt(np.sum(row**2))) for row in tfidfs]
    return cos
    pass


cos = predict(tfidfs[0], tfidfs[1:])
print(cos)
