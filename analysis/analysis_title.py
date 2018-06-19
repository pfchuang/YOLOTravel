# -*- coding: UTF-8 -*-
import sqlite3
import re
import jieba
import numpy as np
import pandas as pd
import math
import operator
import matplotlib.pyplot as plt
from pyspark import SparkContext
from pyspark.ml.feature import Word2Vec
from pyspark.ml.feature import PCA
from pyspark.sql import SparkSession
from mpl_toolkits.mplot3d import Axes3D

def getTitleList(month):
    connection = sqlite3.connect('../trip_db.sqlite3')
    c = connection.cursor()
    c.execute('SELECT title,price FROM item_itinerary WHERE month=?', (month,))
    dataList = c.fetchall()
    return dataList

def titleClean(listOfTitleMoney):
    newTitleList = []
    for title in listOfTitleMoney:
        newTitleList.append(
        re.sub("[〈〉～《》▪￭◆．等日無 A-Za-z0-9「」ｘ『』•【】\x08;\s+\.\!\<>/_,$%^*(+\"\'+——！，\[\]Xx｜。１２３４５６７８９？、~@#￥%……&*（）＋；〜－)®：●♥★™🏆‧-]",
        "", title[0]))
    # print(newTitleList)
    return newTitleList

def separateTitle(inputList):
    sep_list = []
    for title in inputList:
        sep_list.append(' '.join(list(jieba.cut(title))))
    # print(sep_list)
    return sep_list

def wordToVector(separateWordsList):
    sc = SparkContext("local", "TitileVector")
    spark = SparkSession.builder.master("local").getOrCreate()
    wordsList = sc.parallelize(separateWordsList).flatMap(lambda line: line.split(" "))

    word_freq = wordsList.countByValue()
    word_freq = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
    for i in range(20):
        print(word_freq[i])
    # print(wordsList.collect())
    # print(wordsList.count())
    wordDF = spark.createDataFrame([(wordsList.collect(),)], ["title"])
    word2Vec = Word2Vec(vectorSize=100, seed=42, inputCol="title", outputCol="model")
    model = word2Vec.fit(wordDF)
    modelDF = model.getVectors()
    # print(modelDF.count())
    dfw2v = modelDF.select('vector').withColumnRenamed('vector', 'features')
    numComponents = 3
    pca = PCA(k=numComponents, inputCol='features', outputCol='pcaFeatures')
    pcaModel = pca.fit(dfw2v)
    dfComp = pcaModel.transform(dfw2v).select("pcaFeatures")

    word = "溫泉"
    n = 100
    dfCompRDD = dfComp.rdd.map(list)
    r = topNwordsToPlot(dfCompRDD, modelDF, word, n)

    fs=20 #fontsize
    w = r['word']
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    height = 10
    width = 10
    fig.set_size_inches(width, height)

    ax.scatter(r['X'], r['Y'], r['Z'], color='red', s=100, marker='o', edgecolors='black')
    for i, txt in enumerate(w):
        if(i<2):
            ax.text(r['X'].ix[i],r['Y'].ix[i],r['Z'].ix[i], '%s' % (txt), size=30, zorder=1, color='k')

    ax.set_xlabel('1st. Component', fontsize=fs)
    ax.set_ylabel('2nd. Component', fontsize=fs)
    ax.set_zlabel('3rd. Component', fontsize=fs)
    ax.set_title('Visualization of Word2Vec via PCA', fontsize=fs)
    ax.grid(True)
    plt.show()
    # return model.getVectors()


def topNwordsToPlot(dfComp,wordVectorsDF,word,nwords):
    compX = np.asarray(dfComp.map(lambda vec: vec[0][0]).collect())
    compY = np.asarray(dfComp.map(lambda vec: vec[0][1]).collect())
    compZ = np.asarray(dfComp.map(lambda vec: vec[0][2]).collect())

    words = np.asarray(wordVectorsDF.select('word').toPandas().values.tolist())
    Feat = np.asarray(wordVectorsDF.select('vector').rdd.map(lambda v: np.asarray(v[0])).collect())

    Nw = words.shape[0]                # total number of words
    ind_star = np.where(word == words) # find index associated to 'word'
    wstar = Feat[ind_star,:][0][0]     # vector associated to 'word'
    nwstar = math.sqrt(np.dot(wstar,wstar)) # norm of vector assoicated with 'word'

    dist = np.zeros(Nw) # initialize vector of distances
    i = 0
    for w in Feat: # loop to compute cosine distances between 'word' and the rest of the words
        den = math.sqrt(np.dot(w,w))*nwstar  # denominator of cosine distance
        dist[i] = abs( np.dot(wstar,w) )/den   # cosine distance to each word
        i = i + 1

    indexes = np.argpartition(dist,-(nwords+1))[-(nwords+1):]
    di = []
    for j in range(nwords+1):
        di.append(( words[indexes[j]], dist[indexes[j]], compX[indexes[j]], compY[indexes[j]], compZ[indexes[j]] ) )

    result=[]
    for elem in sorted(di,key=lambda x: x[1],reverse=True):
        result.append((elem[0][0], elem[2], elem[3], elem[4]))

    return pd.DataFrame(result,columns=['word','X','Y','Z'])

def countWords(sep_list):
    sc = SparkContext('local')
    wordsList = sc.parallelize(sep_list).flatMap(lambda line: line.split(" "))
    word_freq = wordsList.countByValue()
    word_freq = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
    for i in range(20):
        print(word_freq[i])


wordToVector(separateTitle(titleClean(getTitleList('09'))))
