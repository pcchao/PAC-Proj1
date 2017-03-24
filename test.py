try:
    import networkx as nx
except ImportError:
    print 'Fail to import networkx! Programing terminates'
    print 'Please install by: pip install networkx'
    sys.exit()

import copy
import codecs


path = 'C:\Users\JonyC\Desktop\NodeLists'

import os
for filename in os.listdir(path):
    print(filename)
    os.chdir(path)
    #data = codecs.open(filename,'r+','utf-8')
    data = codecs.open(filename, "r+", 'UTF-8')
    line = data.readline()
    while line:
        print line
        line = data.readline()

        #lines=data.readlines()

    #for line in lines
    #f=data.readlines()
        #print "file in line is: \n", line
    data.close

    #data = codecs.open(filename,'r','utf-8')
    #f=data.read()
    #print "fillename is: ", f

#G=nx.DiGraph()
#G.add_node(1, time ="5pm")
#print(G)
#print(G.node[1]['time'])
