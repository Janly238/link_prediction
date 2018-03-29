# -*- coding: utf-8 -*-
#2017.3.17 已改为最大连通分量为考虑范围
import similarity 
import similarity2 
import init
import networkx as nx
import matplotlib.pyplot as plt
from numpy import *
import operator
import plotRoc
import auc
from sklearn import metrics
import random_forest2
import time

maxnum,originalMat,addMat,Lineslength=init.file2matrix('roadNet-PA4000.txt') 
#后期可删除maxnum、addmat,Lineslength
#originalMat 数据集中有连边二维矩阵
#addMat 在originalMat基础上加上所有节点本身，自己跟自己的连边
G=nx.Graph()
allnotes=arange(1,maxnum+1,1)
G.add_nodes_from(allnotes)
G.add_edges_from(originalMat)    #画G

#==============================================================================
# degreeMat=[]
# for i in allnotes:
#     degreeMat.append(G.degree(i))
#     
# print max(degreeMat),min(degreeMat)
#==============================================================================
temp_connection=nx.connected_components(G)
temp_connection=list(temp_connection)  #找出G的所有连通分量  
#==============================================================================
# max=0
# for i in temp_connection:
#     if(len(i)>max):
#         max=len(i)
#         index=temp_connection.index(i)
# biggest_connection=temp_connection[index]
# temp_connection=None          #找出G的最大连通分量“所有元素”
#==============================================================================
biggest_connection=set()
for i in temp_connection:
    if(len(i)>20):
        biggest_connection=biggest_connection|i
                                #找出G的连通分量大于20的“所有元素”        
		
biggest_Mat_temp=zeros((len(originalMat),2))
index=0
for i in originalMat:
    u,v=i
    if (u in biggest_connection)&(v in biggest_connection):
        biggest_Mat_temp[index,:]=i
        index+=1              		
biggest_Mat=zeros((index,2))   
biggest_Mat[0:index,:]=biggest_Mat_temp[0:index,:]#得出最大连通分量biggest_Mat矩阵，作为原始矩阵
biggest_Mat_temp=None         

connected_node_List=sorted(list(set(biggest_Mat[:,0])|set(biggest_Mat[:,1]))) #排序后的最大连通分量所有元素的列表
connected_node_number=len(connected_node_List)   

lableMat = zeros((connected_node_number+1,connected_node_number+1))#lable矩阵，连边为1，没连边为0
biggest_Mat_length=len(biggest_Mat)
finalLable=zeros((biggest_Mat_length*2,23))   #缩小范围的特征Lable,有连边数的2倍
ULable=zeros((connected_node_number*(connected_node_number-1)/2,3)) #三维矩阵，全集节点，两两结合，第三维是有无连边标记位

index=0
for i in range(0,connected_node_number):
	j=i+1
	while(j<connected_node_number):
		ULable[index,0:2]=(connected_node_List[i],connected_node_List[j])
		j+=1
		index+=1    #建立用所有坐标的全集ULable
		
for i in range(0,biggest_Mat_length):
	u,v=biggest_Mat[i,:]
	lableMat[connected_node_List.index(u),connected_node_List.index(v)]=1
	lableMat[connected_node_List.index(v),connected_node_List.index(u)]=1  #lableMat有连边就做标记1
				  
for i in range(0,len(ULable)):
	ULable[i,2]=lableMat[connected_node_List.index(ULable[i,0]),connected_node_List.index(ULable[i,1])]   #在全集ULable中第三维做上有无连边标记				  

trainProportion=0.9				  
EtLable,EpLable,MtLable,MpLable,TrainLable,TestLable,lableMat=init.divideSet(biggest_Mat,lableMat,trainProportion,biggest_Mat_length,ULable)
#EtLable  90%的有连边；EpLable  剩下的10%的有连边（不用于录入图） 
Train_TestLable=concatenate((TrainLable,TestLable)) 
#G.add_edges_from(addMat) 
#Train_TestLable组成顺序：  EtLable,EpLable,MtLable,MpLable 				  

G=nx.Graph()
G.add_edges_from(biggest_Mat)  #重画G
				  
finalLable[:,0:2]=Train_TestLable[:,:]
for i in range(0,len(finalLable)):
	u,v=finalLable[i,0:2]
	finalLable[i,21:23]=lableMat[connected_node_List.index(u),connected_node_List.index(v)]
	if(len(list(nx.common_neighbors(G, u, v)))==0):
		finalLable[i,22]=0
	#没有共同邻居lable设为0       				  
print 'finished init' 

testarray=similarity2.CommonNeighbors(G,Train_TestLable)
index=0
for i in testarray:
        finalLable[index,2]=i
        index+=1
print 'finished 1st'

testarray=similarity2.Salton(G,Train_TestLable)
index=0
for i in testarray:
        finalLable[index,3]=i
        index+=1
print 'finished 2nd'

testarray=similarity2.Jaccard(G,Train_TestLable)
index=0
for i in testarray:
        finalLable[index,4]=i
        index+=1
print 'finished 3rd'

testarray=similarity2.Sorenson(G,Train_TestLable)
index=0
for i in testarray:
        finalLable[index,5]=i
        index+=1
print 'finished 4th'

testarray=similarity2.HubPromoted(G,Train_TestLable)
index=0
for i in testarray:
        finalLable[index,6]=i
        index+=1
print 'finished 5th'

testarray=similarity2.HubDepressed(G,Train_TestLable)
index=0 
for i in testarray:
        finalLable[index,7]=i
        index+=1
print 'finished 6th'

testarray=similarity2.Leicht_Holme_Newman(G,Train_TestLable)
index=0
for i in testarray:
        finalLable[index,8]=i
        index+=1
print 'finished 7th'

testarray=similarity2.Preferential_attachment(G,Train_TestLable)
index=0
for i in testarray:
        finalLable[index,19]=i
        index+=1
print 'finished 8th'

testarray=similarity2.Adamic_Adar(G,Train_TestLable)
index=0
for i in testarray:
        finalLable[index,9]=i
        index+=1
print 'finished 9th'

testarray=similarity2.Resource_Allocation(G,Train_TestLable)
index=0
for i in testarray:
        finalLable[index,10]=i
        index+=1
print 'finished 10th'
print 'finished similarity calculation'				  
				  
pagerank_score=nx.pagerank(G,alpha=0.9)	
#==============================================================================
# for i in range(0,len(finalLable)):
#     finalLable[i,11]=pagerank_score[finalLable[i,0]]*pagerank_score[finalLable[i,1]]
#==============================================================================
	
for i in range(0,len(finalLable)):
    finalLable[i,11]=pagerank_score[finalLable[i,0]]+pagerank_score[finalLable[i,1]]
	
	
hit_score,hit_authorities=nx.hits(G)
#==============================================================================
# for i in range(0,len(finalLable)):
#     finalLable[i,12]=hit_score[finalLable[i,0]]*hit_score[finalLable[i,1]]
#==============================================================================
	
#==============================================================================
# for i in range(0,len(finalLable)):
#     finalLable[i,14]=hit_score[finalLable[i,0]]+hit_score[finalLable[i,1]]
#==============================================================================
    
degree_centrality_score = nx.degree_centrality(G)   
for i in range(0,len(finalLable)):
    finalLable[i,13]=degree_centrality_score[finalLable[i,0]]*degree_centrality_score[finalLable[i,1]]
#==============================================================================
# for i in range(0,len(finalLable)):
#     finalLable[i,3]=degree_centrality_score[finalLable[i,0]]+degree_centrality_score[finalLable[i,1]]
#==============================================================================
    
closeness_centrality_score = nx.closeness_centrality(G)   
for i in range(0,len(finalLable)):
    finalLable[i,14]=closeness_centrality_score[finalLable[i,0]]*closeness_centrality_score[finalLable[i,1]]
#==============================================================================
# for i in range(0,len(finalLable)):
#     finalLable[i,5]=closeness_centrality_score[finalLable[i,0]]+closeness_centrality_score[finalLable[i,1]]
#==============================================================================

betweenness_centrality_score = nx.betweenness_centrality(G)   
#==============================================================================
# for i in range(0,len(finalLable)):
#     finalLable[i,6]=betweenness_centrality_score[finalLable[i,0]]*betweenness_centrality_score[finalLable[i,1]]
#==============================================================================
for i in range(0,len(finalLable)):
    finalLable[i,15]=betweenness_centrality_score[finalLable[i,0]]+betweenness_centrality_score[finalLable[i,1]]   
    
#==============================================================================
# current_flow_betweenness_score = nx.current_flow_betweenness_centrality(G)   
# for i in range(0,len(finalLable)):
#     finalLable[i,9]=current_flow_betweenness_score[finalLable[i,0]]*current_flow_betweenness_score[finalLable[i,1]]
# for i in range(0,len(finalLable)):
#     finalLable[i,10]=current_flow_betweenness_score[finalLable[i,0]]+current_flow_betweenness_score[finalLable[i,1]]  
#     
# current_flow_closeness_score = nx.current_flow_closeness_centrality(G)   
# for i in range(0,len(finalLable)):
#     finalLable[i,11]=current_flow_closeness_score[finalLable[i,0]]*current_flow_closeness_score[finalLable[i,1]]
# for i in range(0,len(finalLable)):
#     finalLable[i,12]=current_flow_closeness_score[finalLable[i,0]]+current_flow_closeness_score[finalLable[i,1]] 
#==============================================================================
    
eigenvector_centrality_score = nx.eigenvector_centrality(G)   
for i in range(0,len(finalLable)):
    finalLable[i,16]=eigenvector_centrality_score[finalLable[i,0]]*eigenvector_centrality_score[finalLable[i,1]]
#==============================================================================
# for i in range(0,len(finalLable)):
#     finalLable[i,14]=eigenvector_centrality_score[finalLable[i,0]]+eigenvector_centrality_score[finalLable[i,1]]      
#==============================================================================
    
#==============================================================================
# communicability_score = nx.communicability(G)   
# for i in range(0,len(finalLable)):
#     finalLable[i,18]=communicability_score[finalLable[i,0]][finalLable[i,1]]
#==============================================================================

    
AUCscore,fm_pred=random_forest2.random_forest2(finalLable,biggest_Mat_length) 				  
				  
#==============================================================================
# phat =random_forest2.random_forest2(finalLable,EpLable)
# print 'finished Random Forest'
# finalLable[:,12]=phat
# ddd=auc.auc2(finalLable,maxnum)
#==============================================================================

#nx.draw(G)
#plt.show(G)				  
				 				  