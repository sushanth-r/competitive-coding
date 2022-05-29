# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
from queue import Queue


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

    def breadthFirstSearch(self, array):
        q = Queue()
        q.put(self)
        while q.qsize() > 0:
            vertex = q.get()
            array.append(vertex.name)
            for child in vertex.children:
                q.put(child)
        return array


class DFS:
    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")
    print(graph.depthFirstSearch([]))
    print(graph.breadthFirstSearch([]))
