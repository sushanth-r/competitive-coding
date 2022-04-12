# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def get_ancestry_string(descendant: AncestralTree):
    ancestry_string = ""
    while descendant.ancestor is not None:
        ancestry_string = "{}{}".format(ancestry_string, descendant.name)
        descendant = descendant.ancestor
    return "{}{}".format(ancestry_string, descendant.name)


def getYoungestCommonAncestor(top_ancestor, descendant_one, descendant_two):
    d1 = get_ancestry_string(descendant_one)
    d2 = get_ancestry_string(descendant_two)
    youngest_common_ancestor = top_ancestor.name
    for char in d1:
        if d2.find(char) != -1:
            youngest_common_ancestor = char
            break
    ancestor = descendant_one
    while ancestor.name != youngest_common_ancestor:
        ancestor = ancestor.ancestor
    return ancestor


class YoungestCommonAncestor:
    tree = AncestralTree("A")
    B = AncestralTree("B")
    B.ancestor = tree
    D = AncestralTree("D")
    D.ancestor = B
    E = AncestralTree("E")
    E.ancestor = B
    i = AncestralTree("I")
    i.ancestor = D
    print(getYoungestCommonAncestor(tree, E, i))
