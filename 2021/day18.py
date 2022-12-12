from math import floor, ceil

class Value:
    def __init__(self, value):
        self.value = value
        self.parent = None

    def __repr__(self):
        return str(self.value)

    def find_left(self):
        curr = self
        while curr.parent != None and curr.parent.left is curr:
            curr = curr.parent
        if curr.parent == None:
            return None
        curr = curr.parent.left
        while isinstance(curr, Num):
            curr = curr.right
        return curr

    def find_right(self):
        curr = self
        while curr.parent != None and curr.parent.right is curr:
            curr = curr.parent
        if curr.parent == None:
            return None
        curr = curr.parent.right
        while isinstance(curr, Num):
            curr = curr.left
        return curr

    def split(self):
        p = self.parent
        left = Value(floor(self.value / 2))
        right = Value(ceil(self.value / 2))
        new = Num(left, right)
        if p is not None and p.left is self:
            p.left = new
        elif p is not None and p.right is self:
            p.right = new
        new.parent = p
        return new

    def magnitude(self):
        return self.value

class Num:
    def __init__(self, left, right):
        self.parent = None
        self.left = left
        self.right = right
        left.parent = self
        right.parent = self

    def __repr__(self):
        return f"[{self.left},{self.right}]"

    @staticmethod
    def of_string(s: str):
        assert s[0] == '['
        s = s[1:]
        if s[0].isdigit():
            acc = []
            i = 0
            while s[i].isdigit():
                acc.append(s[i])
                i += 1
            left = Value(int("".join(acc)))
            s = s[i:]
        else:
            left, s = Num.of_string(s)
        assert s[0] == ','
        s = s[1:]
        if s[0].isdigit():
            acc = []
            i = 0
            while s[i].isdigit():
                acc.append(s[i])
                i += 1
            right = Value(int("".join(acc)))
            s = s[i:]
        else:
            right, s = Num.of_string(s)
        assert s[0] == ']'
        return Num(left, right), s[1:]

    def add(self, other):
        self.reduce()
        x = Num(self, other)
        x.reduce()
        return x

    def reduce(self):
        to_explode = True
        to_split = True
        print(self)
        while to_explode or to_split:
            x = self.find_fourth_pair()
            if x is None:
                to_explode = False
            else:
                l, r = x.explode()
                if l.value >= 10:
                    new = l.split()
                if r.value >= 10:
                    new = r.split()
                print(self)
                to_split = True
            x = self.find_greater_10()
            if x is None:
                to_split = False
            else:
                x.split()
                print(self)
                to_explode = True

    def find_fourth_pair(self):
        def rec(n, node):
            if n == 4:
                return node
            if isinstance(node.left, Num):
                left = rec(n+1, node.left)
                if left is not None:
                    return left
            if isinstance(node.right, Num):
                right = rec(n+1, node.right)
                if right is not None:
                    return right
            return None
        return rec(0, self)

    def find_greater_10(self):
        def rec(node):
            if isinstance(node, Value):
                if node.value >= 10:
                    return node
                else:
                    return None
            else:
                l = rec(node.left)
                if l is not None:
                    return l
                r = rec(node.right)
                if r is not None:
                    return r
        return rec(self)

    def explode(self):
        l = self.left.find_left()
        if l is not None:
            l.value += self.left.value
        r = self.right.find_right()
        if r is not None:
            r.value += self.right.value
        if self.parent.left is self:
            self.parent.left = Value(0)
            self.parent.left.parent = self.parent
        elif self.parent.right is self:
            self.parent.right = Value(0)
            self.parent.right.parent = self.parent
        return l, r

    def magnitude(self):
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

with open("day18.in", 'r') as f:
    lines = f.readlines()
    x = Num.of_string(lines[0])[0]
    for l in lines[1:]:
        print(x)
        x = x.add(Num.of_string(l)[0])
    print(x)
