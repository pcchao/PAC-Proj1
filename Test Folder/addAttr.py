try:
    import networkx as nx
except ImportError:
    print 'Fail to import networkx! Programing terminates'
    print 'Please install by: pip install networkx'
    sys.exit()

import copy

G=nx.DiGraph()
#G.add_node(1, time='5PM', name='Elon')
G.add_node(1)
G.node[1]['name']='Elon'
G.node[1]['time']='1AM'
print G.nodes()
print G.node[1]['time']


seen_attributes = set()
