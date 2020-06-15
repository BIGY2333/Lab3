from collections import namedtuple

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def List(root=None):
    root = root

    def head(list):
        try:
            return list.value
        except Exception as e:
            print("Linked list does not exist")


    def tail(list):
        try:
            while list.next :
                list = list.next
            return list.value
        except Exception as e:
            print("Linked list does not exist")

    def length(list):
        count = 0
        while list is not None:
            count += 1
            list = list.next
        return count

    def map(list, function):
        cur = list
        while cur is not None:
            cur.value = function(cur.value)
            cur = cur.next
        return list

    def reduce(list, function, initial_state):
        state = initial_state
        cur = list
        while cur is not None:
            state = function(state, cur.value)
            cur = cur.next
        return state

    def mempty():
        return None

    def heade(n):
        assert type(n) is Node
        return n.value

    def taile(n):
        assert type(n) is Node
        return n.next

    def reverse(n, acc=None):
        if n is None:
            return acc
        return reverse(taile(n), Node(heade(n), acc))

    def con(head, tail):
        return Node(head, tail)

    def mconcat(a, b):
        if a is None:
            return b
        tmp = reverse(a)
        res = b
        while tmp is not None:
            res = con(tmp.value, res)
            tmp = tmp.next
        return res

    def from_list(lst):
        if len(lst) == 0:
            root = None
            return root
        root = None
        for e in reversed(lst):
            root = Node(e, root)
        return root

    def to_list(root):
        res = []
        cur = root
        while cur is not None:
            res.append(cur.value)
            cur = cur.next
        return res

    def iterator(list):
        cur = list

        def foo():
            nonlocal cur
            if cur is None: raise StopIteration
            tmp = cur.value
            cur = cur.next
            return tmp

        return foo

    #The function from_generator(gen) can make a generator be a list
    #So that it can be test in other functions
    #We also using closures to make it up to the mustard
    def from_gen(gen):
        res = None
        def from_gene():
            nonlocal res
            res = con(next(gen), res)
            return res

        return from_gene

    def _iterator(lst):
        cur = lst
        if cur != None:
            cur = cur()
        def foo():
            nonlocal cur
            if cur is None:
                raise StopIteration
            tmp = cur.value
            cur = lst()
            return tmp

        return foo

    # Return no instantiated accumulation_list.
    def acc_list(idx):
        n = 0
        res = None
        while n <= idx:
            res = con(n, res)
            n += 1
        return res

    # Return no instantiated accumulation_list.
    def hof_list(idx):
        n = 0
        left = None
        right = None
        while n < idx:
            if n == 0:
                left = con(0, left)
                right = con(1, right)
            else:
                tmp_l = right
                for _ in range(n - left.value - 1):
                    tmp_l = tmp_l.next
                tmp_l_value = n - tmp_l.value

                tmp_r = left
                for _ in range(n - right.value - 1):
                    tmp_r = tmp_r.next
                tmp_r_value = n - tmp_r.value

                left = con(tmp_l_value, left)
                right = con(tmp_r_value, right)
            n += 1
        return left, right

    return {
        'Node':Node,
        'from_list':from_list,
        'to_list':to_list,
        'head':head,
        'tail':tail,
        'length':length,
        'map':map,
        'reduce':reduce,
        'mempty':mempty,
        'mconcat':mconcat,
        'iterator':iterator,
        'from_generator':from_gen,
        'iterator_gen':_iterator,
        'accumulation_list':acc_list,
        'hofstadter_list':hof_list,
    }

