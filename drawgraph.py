# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 13:57:09 2017

@author: jj
"""
from numpy import *
import networkx as nx
import matplotlib.pyplot as plt
from numpy import *
import operator

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = 20000
    originalMat = zeros((numberOfLines,2))
    index =0
    for i in range(0,20000):
            arrayOLines[i] = arrayOLines[i].strip()
            listFromLine =arrayOLines[i].split('\t')
            originalMat[index,:]=(int(listFromLine[0]),int(listFromLine[1]))
            index +=1
        
    return originalMat

#==============================================================================
# originalMat=file2matrix('roadNet-PA.txt')     
# G=nx.Graph()
# G.add_edges_from(originalMat) 
#==============================================================================

GG=nx.read_gpickle('road20000.gpickle')
nx.draw(GG) 
plt.show()
