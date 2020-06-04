import unittest
from hypothesis import given
import hypothesis.strategies as st



class Node(object):

    def __init__(self, value=None, builder=None):

        self.builder = builder
        self.is_cached = False
        self.value = value
        self.next = None
def lazy_single_linked_list(node = None,node_b = None):

    def _evaluate():
        nonlocal node

        node.value, next_builder = node.builder()

        node.next = Node(None,next_builder)

        node.is_cached = True

    def _value():
        nonlocal node

        if not node.is_cached: _evaluate()

        return node.value

    def _next():
        nonlocal node

        if not node.is_cached: return _evaluate()

        node = node.next

    def head():
        nonlocal node
        try:
            return node.value
        except Exception as e:
            print("Linked list does not exist")
    def tail():
        nonlocal node
        try:
            cur = node
            while cur.next:
                cur = cur.next
            return  cur.value
        except Exception as e:
            print("Linked list does not exist")

    def length():
        nonlocal node
        cur = node
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def map(f):
        nonlocal node
        cur = node
        for i in range(length()):
            a = node.value
            node.value = f(a)
            cur = cur.next

    def reduce(f, initial_state):
        nonlocal node
        state = initial_state
        cur = node
        for i in range(length()):
            a = node.value
            state = f(state, a)
            cur = cur.next
        return state

    def append(value):
        # 尾插
        nonlocal node
        n = Node(value)
        cur = node
        if length() == 0:
            node = n
        else:
            while cur.next:
                cur = cur.next
            cur.next = n

    def to_list():
        nonlocal node
        res = []
        src = node
        for i in range(length()):
            res.append(src.value)
            src = src.next
        return  res

    def from_list(lft):
        nonlocal node
        if len(lft)==0:
            return node
        else:
            for i in lft:
                append(i)
            return node


    def mempty():

        return None

    def mconcat():
        nonlocal node
        if node is None:
            return node_b
        cur = node
        while cur.next :
            cur = cur.next
        cur.next = node_b
        return to_list()

    def iterator():
        cur = node
        def foo():
            nonlocal cur
            if cur is None: raise StopIteration
            tmp = cur.value
            cur = cur.next
            return tmp
        return foo



    return {
        'head':head,
        'tail':tail,
        'length':length,
        'map':map,
        'append':append,
        'to_list':to_list,
        'from_list':from_list,
        'mempty':mempty,
        'mconcat':mconcat,
        'iterator':iterator,
        'reduce':reduce,
        "_evaluate":_evaluate,
        '_value':_value,
        '_next':_next,

}









