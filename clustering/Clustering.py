#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx;
from random import random;
import numpy as np;

# Read data from the dataset, and create graph G_fb
G_fb = nx.read_edgelist("facebook_combined.txt", create_using = nx.Graph(), nodetype=int);

# Show the number of edges in G_fb

print("edges = " + str(G_fb.number_of_edges()))

# Show number of nodes in G_fb
nodes = G_fb.number_of_nodes()
print("nodes = " + str(G_fb.number_of_nodes()))

# TASK1. Now your task is to compute the probability whether there is an edge between two vertices.
## edge_probab = ...
maximal_possible_number_of_edges = nodes*(nodes -1)/2
print("maximal_possible_number_of_edges ="+str(maximal_possible_number_of_edges))
edge_probability =  G_fb.number_of_edges() / maximal_possible_number_of_edges
print("edge_probabilty:"+ str(edge_probability))

# Now we have to generate a random graph. First we initialize it
G_rand = nx.Graph();

# TASK3. generate edges in G_rand at random:
k = nodes
for i in range(0,k) :
    for j in range(0,i) :
        if np.random.binomial(1, edge_probability):
            G_rand.add_edge(i,j)
        # Add an edge between vertices i and j, with probability edge_probab (as in G_fb)
        # ...
        
# Now we print out the number of edges and the ACC of the new graph
print("rgraph_edges = " + str(G_rand.number_of_edges()))

av_clust_coeff = nx.average_clustering(G_rand)

print("rgraph_acc = " + str(av_clust_coeff))

# The results which should be submitted to the grader include the ACC of G_fb and of G_rand. Good luck!


# In[ ]:





# In[ ]:




