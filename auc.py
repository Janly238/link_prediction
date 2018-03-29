# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 22:01:18 2016

@author: jj
"""
from numpy import *
def auc2(finalLable):
    print 'AUC is running'
    maxnum=len(finalLable)    
    aucScore=[]
    sortOrder=zeros((maxnum,2))
    for i in range(2,12):
        sortOrder[:,0]=argsort(finalLable[:,i],axis=0)
        for j in range(0,len(sortOrder)):
            sortOrder[sortOrder[j,0],1]=j
        aaa=sortOrder[argwhere(finalLable[:,13]==1),1] #Tp排名
        bbb=sortOrder[argwhere(finalLable[:,13]==0),1] #M排名
        sum=0
        for x in aaa:
            for y in bbb:
                if(x>y):
                    sum+=1
        ccc=sum/float(len(aaa)*len(bbb))
        aucScore.append(ccc)
    return aucScore