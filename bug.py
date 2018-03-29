# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
from numpy import *
import operator

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines,2))
    index =0
    for line in arrayOLines:
            line = line.strip()
            listFromLine =line.split('\t')
            returnMat[index,:]=(listFromLine[0],listFromLine[1])
            index +=1
    return returnMat

mat=file2matrix('netsience.net')