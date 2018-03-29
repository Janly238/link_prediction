# -*- coding: utf-8 -*-
"""
random_forest2
减少无连边的训练，提高1%
"""
import pandas as pd
from numpy import *
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from pyfm import pylibfm
from sklearn.feature_extraction import DictVectorizer
from sklearn.cross_validation import train_test_split
import numpy as np

def random_forest2(ttt,Enum):
    print 'RF is running'  
    train_test_order=arange(0,Enum*2,1)    
    xtrain=zeros((int(Enum*2*0.9),18))
    xtrain_fm=zeros((int(Enum*2*0.9),2))
    ytrain=[]
    for i in train_test_order[0:int(Enum*2*0.9)]:
        xtrain[i,:]=ttt[i,2:20]
        xtrain_fm[i,:]=ttt[i,0:2] 
        ytrain.append(ttt[i,22])        
    	

#==============================================================================
#     xtest=zeros((int(Enum*2*0.1)+1,18))
#     xtest_fm=zeros((int(Enum*2*0.1)+1,2)) #有无连边都测试
#     ytest=[]
#     index=0
#     for i in train_test_order[int(Enum*2*0.9):]:   #有无连边都测试
#         xtest[index,:]=ttt[i,2:20]
#         xtest_fm[index,:]=ttt[i,0:2] 
#         ytest.append(ttt[i,21])
#         index +=1
#     
#     AUCscore=[]
#     for i in range(0,18):
#             AUCscore.append(metrics.roc_auc_score(ytest, xtest[:,i]))	  #roc_auc_score
#             
#     ######################    
# 
# #==============================================================================
# #     xtrain_fm_data = [ {v: k for k, v in dict(zip(i, range(len(i)))).items()}  for i in xtrain_fm]
# #     xtest_fm_data = [ {v: k for k, v in dict(zip(i, range(len(i)))).items()}  for i in xtest_fm]
# #     v = DictVectorizer()
# #     xtrain_fm_data = v.fit_transform(xtrain_fm_data)
# #     xtest_fm_data = v.transform(xtest_fm_data)
# #     fm = pylibfm.FM(num_factors=100, num_iter=10, verbose=False, task="classification", initial_learning_rate=0.01, learning_rate_schedule="optimal")
# #     fm.fit(xtrain_fm_data,ytrain)
# #     fm_pred=fm.predict(xtest_fm_data)
# #     #xtrain[:,15]=fm_pred
# #     AUCscore.append(metrics.roc_auc_score(ytest,fm_pred))
# #==============================================================================
#     
#     
#     md = RandomForestClassifier(n_estimators = 50, n_jobs = 4)
#     md.fit(xtrain, ytrain)
#     phat2 = md.predict_proba(xtest)[:,1]
#     score=metrics.roc_auc_score(ytest, phat2)
# 
#     AUCscore.append(score)
#==============================================================================

    md = RandomForestClassifier(n_estimators = 50, n_jobs = 4)
    md.fit(xtrain, ytrain)
    AUCscore=md.feature_importances_
    
    return AUCscore,0
    
    
    
    
    
    
    
    