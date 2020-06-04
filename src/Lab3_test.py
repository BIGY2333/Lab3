import unittest
from hypothesis import given
import hypothesis.strategies as st
from Lab3 import *

def nat_builder(x):

    return x, lambda: nat_builder(x+1)

class test(unittest.TestCase):

    def test_tail(self):
        n = Node('1')
        D = lazy_single_linked_list(n)
        D['append'](2)
        self.assertEqual(D['tail'](),2)

    def test_length(self):
        n = Node('1')
        D = lazy_single_linked_list(n)
        D['append']('2')
        self.assertEqual(D['length'](),2)

    def test_map(self):
        n = Node('1')
        D = lazy_single_linked_list(n)
        D['append']('2')

        D['map'](str)
        self.assertEqual(D['to_list'](), ['1','2'])

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        D = lazy_single_linked_list()
        D['from_list'](a)
        b = D['to_list']()
        self.assertEqual(a, b)

    def test_mconcat(self):
        n1 = Node('1')
        n2 = Node('1')
        D = lazy_single_linked_list(n1,n2)
        D['append']('2')

        self.assertEqual(D['mconcat'](), ['1', '2','1'])

    def test_iter(self):
        n = Node('1')
        D = lazy_single_linked_list(n)
        D['append']('2')
        tmp = []
        try:
            get_next = D['iterator']()
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(['1','2'], tmp)

    def test_monoid(self):
        n1 = Node('1')
        n2 = Node('1')
        D = lazy_single_linked_list(n1, n2)
        D['append'](D['mempty']())
        self.assertEqual(D['mconcat'](), ['1', None, '1'])

    def test_laziness(self):
        root = Node(None,lambda: nat_builder(0))
        cur = lazy_single_linked_list(root)
        for i in range(10):
            self.assertEqual(cur['_value'](), i)
            cur['_next']()






