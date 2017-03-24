try:
    import networkx as nx
except ImportError:
    print 'Fail to import networkx! Programing terminates'
    print 'Please install by: pip install networkx'
    sys.exit()

import copy
import codecs
import os


def __find_k_cliques(G, k):
    rcl = nx.find_cliques_recursive(G)
    k_cliques_list = []
    while True:
        edge_list = []
        try:
            clique_list = next(rcl)
            if len(clique_list) != k:
                continue

            else:
                for i in range(len(clique_list)):
                    for j in range(i+1, len(clique_list)):
                        edge_list.append(G.has_edge(clique_list[i], clique_list[j]))
                        edge_list.append(G.has_edge(clique_list[j], clique_list[i]))

                if all( has_edge is True for has_edge in edge_list):
                    k_cliques_list.append(clique_list)

        except StopIteration:
            break

    if len(k_cliques_list) == 0:
        return None

    else:
        return k_cliques_list

def __calc_node_cnc(G_undirected, target_node, k_clique):
    sum_cnc = 0

    for node in k_clique:
        if target_node != node:
           sum_cnc += len(sorted(nx.common_neighbors(G_undirected, target_node, node))) - len(k_clique) + 2

    return float(sum_cnc)



def find_k_clique_seed(lgraph, rgraph, k, e):

    """Compute the k-clique seed selection
    This function is implemented based on NetworkX, please install it first!!!
    Args:
        lgraph is the left graph generated using NetworkX
        rgraph is the right graph generated using NetworkX
        k is the number of k-clique
        e is the threshold (epsilon)
    Returns:
        The list of mappings of seeds
    """

    lgraph_k_clqs = __find_k_cliques(lgraph, k)
    rgraph_k_clqs = __find_k_cliques(rgraph, k)

    lgraph_undirected = lgraph.to_undirected()
    rgraph_undirected = rgraph.to_undirected()

    ## mapping from lgraph to rgraph
    seed_mapping = dict()
    seed_mappings = []

    if lgraph_k_clqs is not None and rgraph_k_clqs is not None:
        for lgraph_k_clq in lgraph_k_clqs:
            for rgraph_k_clq in rgraph_k_clqs:
                for lnode in lgraph_k_clq:
                    for rnode in rgraph_k_clq:
                        lnode_cnc = __calc_node_cnc(lgraph_undirected, lnode, lgraph_k_clq)
                        rnode_cnc = __calc_node_cnc(rgraph_undirected, rnode, rgraph_k_clq)
                        lnode_degree = float(G.degree(lnode))
                        rnode_degree = float(G.degree(rnode))

                        if (1-e <= (lnode_cnc/rnode_cnc) <= 1+e) and \
                            (1-e <= (lnode_degree/rnode_degree) <= 1+e):
                            seed_mapping[lnode] = rnode

                if len(seed_mapping) == k:
                    seed_mappings.append(copy.copy(seed_mapping))
                    seed_mapping.clear()
                    rgraph_k_clqs.remove(rgraph_k_clq)
                    lgraph_k_clqs.remove(lgraph_k_clq)
                    break

        return seed_mappings

    else:
        print 'No k-cliques have been found'

def Gaux_never_seen_before (node_to_add, user_id, user_name):
    node = node_to_add #node_to_add
    global seen_attributes
    global Gaux
    global fileIndex

    #attribute = userID
    #print "userID, userName ", userID, userName
    if user_id in seen_attributes:
        for i in range(len(seen_attributes)):
            if Gaux.node[i]['userID']==user_id:
                fileIndex=i
                print "common user ID: ", userID
    #print "fileIndex 2 unchanged: ", fileIndex
    global nodeIndex
    if user_id not in seen_attributes:
        Gaux.add_node(node, userID = user_id)
        Gaux.node[node]['userName']=user_name
        fileIndex=node_to_add
        nodeIndex=nodeIndex+1
        seen_attributes.add(user_id)
        #print "fileIndex 3 changed: ", fileIndex

def never_seen_before (node_to_add, user_id, user_name):
    global nodeIndex
    if user_id not in seen_attributes:
        Gaux.add_node(node_to_add, userID = user_id)
        Gaux.node[node_to_add]['userName']=user_name
        nodeIndex=nodeIndex+1
        seen_attributes.add(user_id)
        return True
    return False


if __name__ == '__main__':
    path = 'C:\Users\JonyC\Documents\GitHub\PAC-Proj1\NodeLists'
    os.chdir(path)
    seen_attributes = set()
    Gsan = nx.DiGraph()
    Gaux = nx.DiGraph()

    '''Gaux Generation'''
    nodeIndex=0
    fileIndex=0
    for filename in os.listdir(path):
        ''' file Name Node'''
        #print(filename)
        userID = filename[:filename.find(' ')].encode('utf-8')
        userName = filename[filename.find(' ')+1:filename.find('.txt')].encode('utf-8')
        never_seen = never_seen_before(nodeIndex,userID,userName)

        if never_seen == True:
            fileIndex=nodeIndex-1
            #nodeIndex=nodeIndex+1
        if never_seen == False:
            for i in range(len(seen_attributes)):
                if Gaux.node[i]['userID'] == userID:
                    fileIndex=i

        #fileIndex=0
        #print "fileIndex 1, filename", fileIndex, filename

        data = codecs.open(filename,'r','utf-8')
        line = data.readline()

        while line:
            #print line.encode('utf-8')
            userID = line[:line.find(' ')].encode('utf-8')
            userName = line[line.find(' ')+1:].encode('utf-8')
            #Gaux_never_seen_before(nodeIndex, userID,userName)
            never_seen_before(nodeIndex,userID,userName)

            #Gaux.add_node(nodeIndex, userID=userID)
            #Gaux.node[nodeIndex]['userName']=userName

            Gaux.add_edge(fileIndex,nodeIndex)

            #print "userID, userName ", userID, userName
            #print "Gaux userID, userName", Gaux.node[nodeIndex]['userID'], Gaux.node[nodeIndex]['userName']
            line = data.readline()
        data.close
    ''' Gsan Generation'''
    Gsan=Gaux
    for i in range(nx.number_of_nodes(Gsan)):
        Gsan.node[i]['userName']=''

    print find_k_clique_seed(lgraph=Gsan, rgraph=Gaux, k=3, e=0.1)
