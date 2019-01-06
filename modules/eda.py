import pandas as pd
import numpy as np

def getUniq(train, test, col):
    s1 = set(train[col].unique())
    s2 = set(test[col].unique())
    uniq = s1|s2
    return uniq, s1, s2

def valCnt(train, test, col):
    ret1 = train[col].value_counts(dropna=False)
    ret2 = test[col].value_counts(dropna=False)
    return ret1, ret2

def valCntGet(c, u):
    try : return c[u]
    except KeyError : return 0
    except TypeError : return c.iloc[c.index.isnull()][np.nan]

def valCntSum(train, test, col):
    dic = {}
    vc1, vc2 = valCnt(train, test, col)
    for uniq in col:
        t1 = valCntGet(vc1, uniq)
        t2 = valCntGet(vc2, uniq)
        dic[uniq] = t1+t2
    dic = list(sorted(zip(dic.keys(), dic.values()), key=lambda d: d[1], reverse=True))
    return dic

def printUniq(train, test, col, allUniq = None, valCnt=False):
    print(test[col].head(5))
    uniq, s1, s2 = getUniq(train, test, col)
    length = len(uniq)
    print("All Uniq : ", length)
    if allUniq : print(uniq)
    onlyTrain = s1-s2
    onlyTest = s2-s1
    if length<100 :
        print("Only Train : ", onlyTrain)
        print("Only Test : ", onlyTest)
    if valCnt :
        dic = valCntSum(train, test, col)
        i = 0
        for k,v in dic:
            print(k, " : ", v)
            i+=1
            if i == 10 : break
    # return dic, onlyTrain, onlyTest

def stripSB(x, S, B, y='logPrice'):
    fig = plt.figure(figsize=(30,15))
    fig.add_subplot(2,1,1)
    plt.xticks(rotation='vertical')
    sns.stripplot(x=x, y=y, data=S.sort_values(by=[x]), color='red', size=0.2)
    fig.add_subplot(2,1,2)
    plt.xticks(rotation='vertical')
    sns.stripplot(x=x, y=y, data=B.sort_values(by=[x]), color='blue', size=0.2)
    plt.show()

def colInfo(col, df):
    dtype = df[col].dtypes
    print(dtype)
    if dtype == 'float64' :
        print(df[col].describe())
    else:
        uniq = df[col].unique()
        if dtype == 'O' or len(uniq)<100:
            print(df[col].value_counts())
        else : print(df[col].describe())
