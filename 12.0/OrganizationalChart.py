class Node:
    def __init__(self, name, parent, division, all_no):
        self.name = name
        self.parent = parent
        self.division = division
        self.all_no = all_no
        self.children = []
        self.division_lower = division
        self.division_upper = division
        self.all_lower = all_no
        self.all_upper = all_no


class Tree:
    def __init__(self, root):
        self.root = root


NQ = input()
NQ = [int(n.strip()) for n in NQ.split()]
tree = {}
for n in range(NQ[0]):
    line = input()
    line = [l.strip() for l in line.split()]
    node = Node(line[0], line[1], int(line[2]), int(line[3]))
    if line[1] in tree.keys():
        children = tree[line[1]]
        children.append(node)
    else:
        tree[line[1]] = [node]

tree_list = [tree["NONE"][0]]
while len(tree_list) > 0:
    node = tree_list.pop()
    if node.name in tree.keys():
        children = tree[node.name]
    else:
        continue
    tree_list += children
    level_all = node.division
    for child in children:
        level_all += child.all_no

    if level_all < node.all_no:
        for child in tree[node.name]:
            if child.all_no == 0:
                child.divisional_lower = 1
                child.all_lower = 1
                child.all_upper = node.all_no - level_all


for key in tree.keys():
    layer = tree[key]
    for node in layer:
        print(node.name, node.all_lower, node.all_upper, node.division_lower, node.division_upper)
        print()
