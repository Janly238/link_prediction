# -*- coding: utf-8 -*-
'''write by Janny in 2016.8.19
similarity2.py
'''
from __future__ import division
import networkx as nx
import math
from networkx.utils.decorators import *

def CommonNeighbors(G,dataSet):
        if dataSet is None:
				dataSet = nx.non_edges(G)

        def predict(u, v):
				cnbors = list(nx.common_neighbors(G, u, v))
				return len(cnbors)

        return (predict(u, v) for u, v in dataSet)
        
def Salton(G,dataSet):
        if dataSet is None:
				dataSet = nx.non_edges(G)

        def predict(u, v):
				cnbors = list(nx.common_neighbors(G, u, v))
				borsDg=(G.degree(u) * G.degree(v))**0.5
				if borsDg==0:
						return 0
				else:
						return len(cnbors)/borsDg

        return (predict(u, v) for u, v in dataSet)
        
def Jaccard(G,dataSet):
        if dataSet is None:
				dataSet = nx.non_edges(G)

        def predict(u, v):
				cnbors = list(nx.common_neighbors(G, u, v))
				union_size=len(set(G[u]) | set(G[v]))
				if union_size==0:
						return 0
				else:
						return len(cnbors)/union_size

        return (predict(u, v) for u, v in dataSet)
        
def Sorenson(G,dataSet):
        if dataSet is None:
				dataSet = nx.non_edges(G)

        def predict(u, v):
				cnbors = list(nx.common_neighbors(G, u, v))
				sumDg=G.degree(u) + G.degree(v)
				if sumDg==0:
						return 0
				else:
						return 2*len(cnbors)/sumDg

        return (predict(u, v) for u, v in dataSet)
        
def HubPromoted(G,dataSet):
        if dataSet is None:
				dataSet = nx.non_edges(G)

        def predict(u, v):
				cnbors = list(nx.common_neighbors(G, u, v))
				sumDg=min(G.degree(u),G.degree(v))
				if sumDg==0:
						return 0
				else:
						return len(cnbors)/sumDg

        return (predict(u, v) for u, v in dataSet)
        
def HubDepressed(G,dataSet):
        if dataSet is None:
				dataSet = nx.non_edges(G)

        def predict(u, v):
				cnbors = list(nx.common_neighbors(G, u, v))
				sumDg=max(G.degree(u),G.degree(v))
				if sumDg==0:
						return 0
				else:
						return len(cnbors)/sumDg

        return (predict(u, v) for u, v in dataSet)

def Leicht_Holme_Newman(G,dataSet):
        def predict(u, v):
				cnbors = list(nx.common_neighbors(G, u, v))
				borsDg=G.degree(u) * G.degree(v)
				if borsDg==0:
						return 0
				else:
						return len(cnbors)/borsDg

        return (predict(u, v) for u, v in dataSet)
        
def Preferential_attachment(G,dataSet):
        if dataSet is None:
				dataSet = nx.non_edges(G)

        return (G.degree(u) * G.degree(v) for u, v in dataSet)
        
def Adamic_Adar(G,dataSet):
        if dataSet is None:
            dataSet = nx.non_edges(G)

        def predict(u, v):
            return sum(1 / math.log(G.degree(w)) for w in nx.common_neighbors(G, u, v))

        return (predict(u, v) for u, v in dataSet)
				
        
def Resource_Allocation(G,dataSet):
        if dataSet is None:
            dataSet = nx.non_edges(G)

        def predict(u, v):
            return sum(1 / G.degree(w) for w in nx.common_neighbors(G, u, v))

        return (predict(u, v) for u, v in dataSet)


