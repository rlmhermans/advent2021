from math import floor, ceil
import itertools as it

class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.children = []
    
    def add_tree(self, tree):
        new_parent = Node(None, None)
        new_parent.add_child(self)
        new_parent.add_child(tree)
        self.parent = new_parent
        tree.parent = new_parent
        return new_parent

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def depth(self):
        if self.parent is None: return 1
        else: return self.parent.depth() + 1

    def split(self):
        self.add_child(Node(floor(self.value/2), self))
        self.add_child(Node(ceil(self.value/2), self))
        self.value = None

    def find_leaves(self, found):
        if self.value is not None: found.append(self)
        else:
            for c in self.children:
                found = c.find_leaves(found)
        return found

    def explode(self):
        left, right = self.children
    	
        leaves = current_tree.find_leaves([])
        index_left = leaves.index(left)-1
        index_right = leaves.index(right)+1

        if index_left >= 0:
            leaves[index_left].value += left.value

        if index_right < len(leaves):
            leaves[index_right].value += right.value

        self.children = []
        self.value = 0

    def find_explosives(self):
        if self.depth() > 4 and len(self.children) > 0:
            self.explode()
            return True
        elif len(self.children) != 0:
            for c in self.children:
                exploded = c.find_explosives()
                if exploded: return True

        return False

    def find_splits(self):
        if len(self.children) != 0:
            for c in self.children:
                split = c.find_splits()
                if split: return True
        elif self.value > 9:
            self.split()
            return True

        return False

    def magnitude(self):
        if self.value is not None:
            return self.value

        return 3 * self.children[0].magnitude() + 2 * self.children[1].magnitude()

    def __str__(self):
        if self.value is not None:
            return str(self.value)
        return f'[{self.children[0]},{self.children[1]}]' 

def build_tree(input):
    top_node = Node(None, None)
    current_node = top_node
    number = ''

    for c in input[1:]:
        if c in '[':
            new_node = Node(None, current_node)
            current_node.add_child(new_node)
            current_node = new_node
        elif c in ']':
            if number != '':
                new_node = Node(int(number), current_node)
                current_node.add_child(new_node)
                number = ''
            current_node = current_node.parent
        elif c in ',':
            if number != '':
                new_node = Node(int(number), current_node)
                current_node.add_child(new_node)
                number = ''
        else:
            number += c

    return top_node

with open('input') as f:
    first, *input = f.read().splitlines()

current_tree = build_tree(first)
for line in input:
    t = build_tree(line)
    current_tree = current_tree.add_tree(t)

    changed = True

    while changed:
        if current_tree.find_explosives(): continue
        changed = current_tree.find_splits()        

print('Part 1:', current_tree.magnitude())

largest = 0

for left in input:
    for right in input:
        if left is not right:
            left_tree = build_tree(left)
            right_tree = build_tree(right)
            current_tree = left_tree.add_tree(right_tree)

            changed = True

            while changed:
                if current_tree.find_explosives(): continue
                changed = current_tree.find_splits()   

            mag = current_tree.magnitude()
            if mag > largest: largest = mag

print('Part 2:', largest)