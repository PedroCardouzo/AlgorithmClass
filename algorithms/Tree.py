from collections import deque

class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None

    def __str__(self):
        return str(self.value)

    def insert(self, value):
        current = self
        inserted = False
        while not inserted:
            if value > current.value:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = Tree(value)
                    inserted = True
            else:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = Tree(value)
                    inserted = True

    def connect_brothers_and_cousins(self):
        self._connect_to_next(self, 0, [])

    def _connect_to_next(self, node, level, next_list):
        if node is not None:
            if len(next_list) > level:
                node.next = next_list[level]
                next_list[level] = node
            else:
                next_list.append(node)  # first time a node at this level is added, so we need to make the list bigger

            self._connect_to_next(node.right, level+1, next_list)
            self._connect_to_next(node.left, level+1, next_list)

    # connects any node N from level i to the node M directly to its right (N.next = M) rightmost node points to None
    def connect_brothers_and_cousins_iter(self):
        next_list = []
        stack = [(self, 0)]
        while len(stack) > 0:
            node, level = stack.pop()
            if len(next_list) > level:
                node.next = next_list[level]
                next_list[level] = node
            else:
                next_list.append(node)  # first time a node at this level is added, so we need to append at the end of the list

            if node.left is not None:
                stack.append((node.left, level + 1))
            if node.right is not None:
                stack.append((node.right, level + 1))

    # connects any node N from level i to the node M directly to its left (N.next = M) leftmost node points to None
    def connect_brothers_and_cousins_inverse_iter(self):
        next_list = []
        stack = [(self, 0)]
        node = self
        while len(stack) > 0:
            node, level = stack.pop()
            if len(next_list) > level:
                node.next = next_list[level]
                next_list[level] = node
            else:
                next_list.append(node)  # first time a node at this level is added, so we need to append at the end of the list

            if node.right is not None:
                stack.append((node.right, level + 1))
            if node.left is not None:
                stack.append((node.left, level + 1))

    # prints from level 0 to h (height of tree), from right to left (following next pointer assuming it links to the left)
    def print_nexts_inverse(self, to_print=False):
        first = self
        l = []
        level = 0
        while first:
            aux = first
            row = []
            print("level " + str(level), end=': ')
            level += 1
            while aux:
                row.append(aux)
                if to_print:
                    print(aux, end=' ')
                aux = aux.next
            print('')
            first = self.find_next_first_inverse(first)
            l.append(row)

        return l

    # finds rightmost children of nodes of this level
    def find_next_first_inverse(self, node):
        while node:
            if node.right:
                return node.right
            elif node.left:
                return node.left
            else:
                node = node.next

    # prints from level 0 to h (height of tree), from left to right (following next pointer assuming it links to the right)
    def print_nexts(self, to_print=False):
        first = self
        l = []
        level = 0
        while first:
            aux = first
            row = []
            print("level " + str(level), end=': ')
            level += 1
            while aux:
                row.append(aux)
                if to_print:
                    print(aux, end=' ')
                aux = aux.next
            print('')
            first = self.find_next_first(first)
            l.append(row)
        return l

    # finds leftmost children of nodes of this level
    def find_next_first(self, node):
        while node:
            if node.left:
                return node.left
            elif node.right:
                return node.right
            else:
                node = node.next

    def print(self):
        if self.left:
            self.left.print()
        print(self.value)
        if self.right:
            self.right.print()

    def pretty_print(self):
        self._pretty_print(1)

    def _pretty_print(self, level):
        print(level * '\t' + self.__str__())
        if self.left is not None:
            self.left._pretty_print(level+1)
        if self.right is not None:
            self.right._pretty_print(level+1)

    def __iter__(self):
        self._iter_stack = [(self, False)]
        return self

    def __next__(self):
        while len(self._iter_stack) > 0:
            node, processed = self._iter_stack.pop()
            if not processed:
                if node.right:
                    self._iter_stack.append((node.right, False))
                self._iter_stack.append((node, True))
                if node.left:
                    self._iter_stack.append((node.left, False))
            else:
                return node
        raise StopIteration

    def __eq__(self, other):
        return self.value == other.value and self.left == other.left and self.right == other.right

    def get_range(self, min_value, max_value):
        raise NotImplementedError

    def get_range_iter(self, min_value, max_value):
        raise NotImplementedError


def test():

    # util function
    def sorted_list_to_balanced_bst_iter(l):
        t = None
        if len(l) == 0:
            return 0
        elif len(l) == 1:
            return Tree(l[0])
        t = Tree(l[len(l)//2])
        queue = deque([(t, 0, len(l))])
        while len(queue) > 0:
            current, low, high = queue.pop()
            mid = (low+high)//2
            if low != mid:
                current.left = Tree(l[(low+mid)//2])
                queue.appendleft((current.left, low, mid))
            if mid+1 != high:
                current.right = Tree(l[(mid+1+high)//2])
                queue.appendleft((current.right, mid+1, high))
        return t

    # util function
    def sorted_list_to_balanced_bst(l):
        if len(l) == 0:
            return None
        elif len(l) == 1:
            return Tree(l[0])

        mid = len(l)//2
        t = Tree(l[mid])
        t.left = sorted_list_to_balanced_bst(l[:mid])
        t.right = sorted_list_to_balanced_bst(l[mid+1:])
        return t

    l = list(range(15))
    t = sorted_list_to_balanced_bst(l)
    t.connect_brothers_and_cousins_inverse_iter()
    t.pretty_print()
    t.print_nexts_inverse(True)
    print("#############################")
    for el in t:
        print(el, end=' ')
