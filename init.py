# -*- coding: utf-8 -*-
from numpy import *

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    originalMat = zeros((numberOfLines,2))
    index =0
    for line in arrayOLines:
            line = line.strip()
            listFromLine =line.split('\t')
            originalMat[index,:]=(int(listFromLine[0]),int(listFromLine[1]))
            index +=1
            
    maxnum=int(amax(originalMat))
    addMat = zeros((numberOfLines+maxnum,2))
    addMat[0:numberOfLines,:]=originalMat[0:numberOfLines,:]
    index=1
    for i in range(numberOfLines,numberOfLines+maxnum):
            addMat[i,:]=(index,index)
            index+=1
    return maxnum,originalMat,addMat,numberOfLines
    
def divideSet(originalMat,lableMat,trainProportion,Lineslength, ULable):
#originalMat 二维原始有连边列表
#lableMat  真实值标记的n*n矩阵，有连边为1，无连边为0
#trainProportion 训练集比例
#Lineslength  有连边的边数
#Ulable 三维全集列表(前两维是全集边列表，第3维是真实值标记位)      
#MLable 二维无连边列表

    edgeOrder=arange(0,Lineslength,1)
    nonedgeOrder=argwhere(ULable[:,2]==0)
    random.shuffle(edgeOrder)
    random.shuffle(nonedgeOrder)
    EtLable=zeros((int(Lineslength*trainProportion),2))  #有连边的90%，画图
    EpLable=zeros((int(Lineslength*(1-trainProportion))+1,2)) #有连边10%，测试
    MtLable=zeros((int(Lineslength*trainProportion),2))  #无连边(1:1)的90%
    MpLable=zeros((int(Lineslength*(1-trainProportion))+1,2)) #无连边(1:1)10%，测试 
    
    for i in range(0,int(Lineslength*trainProportion)):
            EtLable[i,:]=originalMat[edgeOrder[i],:]            
            MtLable[i,:]=ULable[nonedgeOrder[i],0:2]            
            
    index=0
    for i in range(int(Lineslength*trainProportion),Lineslength):
            EpLable[index,:]=originalMat[edgeOrder[i],:]            
            MpLable[index,:]=ULable[nonedgeOrder[i],0:2]
            index +=1
    
    TrainLable=concatenate((EtLable,MtLable))
    TestLable=concatenate ((EpLable,MpLable))       
    return EtLable,EpLable,MtLable,MpLable,TrainLable,TestLable,lableMat
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
