import webbrowser
class Node:
    def __init__(self, name=None, pre=None, neighbor={}, dis=None):
        self.name = name
        self.pre = pre
        self.neighbor = neighbor
        self.dis = dis
    #  setting parameters (pre,neighbor,dis,name)
    def setname(self,name):
        self.name = name
    def setdis(self, dis):
        self.dis = dis
    def setpre(self, pre):
        self.pre = pre
    def addneighbor(self, name, weight):
        self.neighbor.setdefault(name, weight)
    #  getting parameters(pre,neighbor,dis,name)
    def getpre(self):
        return self.pre
    def getneighbor(self):
        return self.neighbor
    def getdis(self):
        return self.dis
    def getname(self):
        return self.name
    #  delete
    def delneighbor(self, name):
        if self.neighbor.keys():
            print 'Neighbor list is NULL'
        else:
            del self.neighbor[name]
# add vertex for graph G
def add_vertex(G):
    while 1:
        show_vertex(G)
        name = hint('please input the nodes name or "exit" to exit:').upper()
        if name == 'EXIT':
            break
        elif not G.has_key(name):
            G.setdefault(name)
            G[name] = Node(name, neighbor={name: 0}, pre=None, dis=0)
            print 'node %s successfully added !!!!!!!!!!' % name
        else:
            print 'this name is already used, please change another one!!!'
            continue
# add links for graph G
def add_newlink(G):
    while 1:
        show_neighbors(G)
        src_des_wgt = hint('please input a link by using format this format:V(vertex),V,W(weight);V,V,W...\n and '
                           'input "exit" to back:').upper()
        if src_des_wgt == 'EXIT':
            break
        else:
            src_des_wgt = src_des_wgt.strip().split(';')
            try:
                src_des_wgt.remove('')
            except ValueError:
                pass
        r_src_des_wgt = []
        for item in src_des_wgt:
            item = item.split(',')
            r_src_des_wgt.append(item)
        for item in r_src_des_wgt:
            try:
                head_node = item[0]
                tail_node = item[1]
                node_weight = int(item[2])
            except (IndexError, ValueError):
                print '!'*5+'your input is illegal!!!!!!!!!!!'+'!'*5
                continue
            try:
                G[head_node].addneighbor(tail_node, node_weight)
                G[tail_node].addneighbor(head_node, node_weight)
            except KeyError:
                print 'the nodes %s or %s you input may not added yet, please check it' % (head_node, tail_node)
def delete_vertex(G):
    while 1:
        show_vertex(G)
        d_node = hint('please input the name of vertex,and input "exit" to back:').upper()
        if d_node == 'EXIT': break
        elif d_node in G.keys():
            ist = G.pop(d_node)
            if ist.getneighbor() != {d_node:0}:
                for ngb in ist.getneighbor():
                    delete_link(G, head=d_node, tail=ngb)
                print 'vertex %s is successfully deleted!!!!!' % d_node
            else:
                print 'vertex %s is successfully deleted!!!!!' % d_node
        else:
            print '%s is not exist in graph'%d_node
def delete_link(G, head=None, tail=None):
    while 1:
        if head is not None and tail is None:
            tail = hint('the head is %s, please input the tail' % head).upper()
            if tail == 'EXIT':
                break
        elif tail is not None and head is None:
            head = hint('the tail is %s, please input the head' % tail).upper()
            if head == 'EXIT':
                break
        elif head is None and tail is None:
            tail = hint('please input the tail,or exit to back:').upper()
            if tail == 'EXIT':
                break
            head = hint('please input the head,or exit to back:').upper()
            if head == 'EXIT':
                break
        try:
            G[head].delneighbor(tail)
            G[tail].delneighbor(head)
            print 'successfully delete link %s -- %s' % (head, tail)
        except ValueError:
            print 'Something is wrong'
def show_vertex(G):
    print 'The vertices list is showed below: '
    if sum(len(x)+1 for x in G.keys()) == 0 :
        print 'No vertex now'
    else:
        print '-' * sum(len(x) + 1 for x in G.keys())
        for item in G.itervalues():
            print item.getname(),
    print ''
    print '-' * sum(len(x)+1 for x in G.keys())
def show_neighbors(G):
    for item in G.itervalues():
        print "{}'s neighbors are {}".format(item.getname(),item.getneighbor())

'''def connectivity(vset):
    ver_set = vset
    temp_set = []
    try:
        start_v = vset[0]
    except IndexError:
        print 'None graph is built, progress shutdown'
        return False
    while 1:
        try:
            if len(ver_set.remove(start_v)) == 0:
                return True
            else:
                temp_set = G[start_v].getneighbor().keys()
        except ValueError:
            return False
 '''


def hint(x):
    while 1:
        cus_input = raw_input(x)
        if cus_input == '':
            continue
        else:
            break
    return cus_input
def graph_constructor():
    G = {}
    while 1:
        print '-----------------' * 7
        print '1.add new vertex | 2.add new link | 3.delete vertex | 4.delete link | 5.show vertex | 6.show neighbor ' \
              '| 7. dijkstra '
        print '-----------------' * 7
        cus_input = hint('please select one item:')
        if cus_input.isalnum() and cus_input in ['1', '2', '3', '4', '5', '6', '7']:
            if cus_input == '1':
                add_vertex(G)
            elif cus_input == '2':
                add_newlink(G)
            elif cus_input == '3':
                delete_vertex(G)
            elif cus_input == '4':
                delete_link(G)
            elif cus_input == '5':
                show_vertex(G)
            elif cus_input == '6':
                show_neighbors(G)
            else:
                break
        else:
            print 'None valid input, try again'
    return G
def dijkstra(G):
    while 1:
        source = raw_input("please input the source node").upper()
        if source in G.keys():
            snode = G.get(source)
            break
        else:
            print 'This vertex is not exist in graph, please try again'
    while 1:
        destination = raw_input("please input the destination node:").upper()
        if destination in G.keys():
            dnode = G.get(destination)
            break
        else:
            print 'This vertex is not exist in graph, please try again'
    #total cost calculation
    total_cost = 0
    for n in G.itervalues():
        total_cost += sum(n.getneighbor().values())
    INF = total_cost/2 + 10
    # init d(i)
    for n in G.itervalues():
        if n.getname() == snode.getname():
            continue
        elif n.getname() in snode.neighbor.keys():
            n.setdis(snode.neighbor[n.getname()])
        else:
            n.setdis(INF)
    G.get(source).setdis(0)
    # initial pre
    for n in G.itervalues():
        if n.getname() == snode.getname():
            continue
        else:
            n.setpre(source)
    # initial set S
    S = G.keys()
    S.remove(source)

    # step 2
    while 1:
        name, dis = None, INF
        for m in S:
            if dis > G[m].getdis():
                name, dis = G[m].getname(), G[m].getdis()
        # print visited_node
        try:
            S.remove(name)
        except ValueError:
            print 'something is wrong, system shutdown'
            return 0
        if name == source or S == []:
            break
        else:
            for temp3 in S:
                if temp3 in G[name].getneighbor().keys():
                    if G[name].getdis()+G[name].getneighbor()[temp3] < G[temp3].getdis():
                        G[temp3].setdis(G[name].getdis()+G[name].getneighbor()[temp3])
                        G[temp3].setpre(G[name].getname())
                    else:
                        continue
                else:
                    continue
    # print shortest path
    shortestpath = [destination]
    temp_node = dnode
    while 1:
        if temp_node.getpre() == source:
            break
        else:
            shortestpath.append(temp_node.getpre())
            temp_node = G[temp_node.getpre()]
    shortestpath.reverse()
    print "the shortest path from {} to {} is {}\n".format(source, destination,shortestpath)
    print "the cost is %f" % dnode.getdis()
if __name__ == '__main__':
    G = graph_constructor()
    dijkstra(G)