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

maxnum,originalMat,addMat,Lineslength=init.file2matrix('roadNet-PA.txt') 

G=nx.Graph()
allnotes=arange(1,maxnum+1,1)
G.add_nodes_from(allnotes)
G.add_edges_from(originalMat) 


nx.draw(G) 
plt.show()  #画G
