from item.models import *
from pyspark import SparkContext
import operator
import jieba
import re

replace_string = "[〈〉～《》▪￭◆．送小全程人系列飯店等日站直飛每月都自費的無天一二三四五六七八九十入住含稅美好特選停下成行感受世界 A-Za-z0-9「」ｘ『』•【】\x08;\s+\.\!\<>/_,$%^*(+\"\'+——！，\[\]Xx｜。１２３４５６７８９？、~@#￥%……&*（）＋；〜－)®：●♥★™🏆‧-]"
def analyze_title(year, month):
    start_date = year + '-' + month + '-' + '01'
    end_date = ''
    if month in ['1', '3', '5', '7', '9', '11']:
        end_date = year + '-' + month + '-' + '30'
    elif month is '2':
        end_date = year + '-' + month + '-' + '28'
    else:
        end_date = year + '-' + month + '-' + '31'
    titles = getTitleList(start_date, end_date)
    titles = titleClean(titles)
    titleWords = separateTitle(titles)
    topwords = countWords(titleWords)
    print(topwords)
    for word_count in topwords:
        TopWord.objects.create(word=word_count[0], count=word_count[1], year=int(year), month=int(month))

def getTitleList(start_date, end_date): 
    itinerary_ids = Travel_Date.objects.filter(departure_date__range=[start_date,end_date]).values('itinerary').distinct()
    titles = Itinerary.objects.filter(id__in=itinerary_ids).values('title')
    print(titles)
    return titles

def titleClean(listOfTitleMoney):
    newTitleList = []
    for titledict in listOfTitleMoney:
        print(titledict['title'])
        newTitleList.append(
        re.sub(replace_string, "", titledict['title']))
    return newTitleList

def separateTitle(inputList):
    sep_list = []
    for title in inputList:
        sep_list.append(' '.join(list(jieba.cut(title))))
    return sep_list

def countWords(sep_list):
    sc = SparkContext('local')
    wordsList = sc.parallelize(sep_list).flatMap(lambda line: line.split(" "))
    word_freq = wordsList.countByValue()
    word_freq = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
    return word_freq[:20]
