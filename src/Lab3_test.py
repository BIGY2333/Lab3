import unittest

from hypothesis import given
import hypothesis.strategies as st

from Lab3 import *


class TestSLList(unittest.TestCase):
    def test_head(self):
        lst = [1, 2, 3, 4]
        D = List()
        root = D['from_list'](lst)
        self.assertEqual(D['head'](root), 1)
        root = root.next
        self.assertEqual(D['head'](root), 2)

    def test_tail(self):
        lst = [1, 2, 3, 4]
        D = List()
        self.assertEqual(D['tail'](D['from_list'](lst)), 4)

    def test_length(self):
        lst = [1, 2, 3, 4]
        D = List()
        self.assertEqual(D['length'](D['from_list'](lst)), 4)

    def test_map(self):
        lst = [1, 2, 3, 4]
        D = List()
        h = D['from_list'](lst)

        def func(v):
            v = v * v
            return v

        self.assertEqual(D['to_list'](D['map'](h, func)), [1, 4, 9, 16])

    def test_reduce(self):
        # sum of list
        lst = [1, 2, 3, 4]
        D = List()
        s = D['from_list'](lst)
        self.assertEqual(D['reduce'](s, lambda st, e: st + e, 0), 10)

    def test_mconcat(self):
        l1 = [1, 2, 3, 4]
        l2 = [5, 6, 7, 8]
        D = List()

        h1 = D['from_list'](l1)
        h2 = D['from_list'](l2)
        c = D['mconcat'](h1, h2)
        self.assertEqual(D['to_list'](c), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_to_list(self):
        D = List()
        self.assertEqual(D['to_list'](Node('a')), ['a'])
        self.assertEqual(D['to_list'](Node('a', Node('b'))), ['a', 'b'])

    def test_from_list(self):
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]

        for e in test_data:
            D = List()
            self.assertEqual(D['to_list'](D['from_list'](e)), e)

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        D = List()
        self.assertEqual(D['to_list'](D['from_list'](a)), a)

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        D = List()
        a = D['from_list'](lst)
        self.assertEqual(D['to_list'](D['mconcat'](D['mempty'](), a)), D['to_list'](a))
        self.assertEqual(D['to_list'](D['mconcat'](a, D['mempty']())), D['to_list'](a))

    def test_iter(self):
        x = [1, 2, 3]
        l = List()
        l1 = l['from_list'](x)
        tmp = []

        try:
            get_next = l['iterator'](l1)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(x, tmp)
        self.assertEqual(l['to_list'](l1), tmp)

    @given(st.integers())
    def test_infinite_list(self, idx):
        D=List()
        if idx < 10000:
            out_list = list(range(idx, -1, -1))
            self.assertEqual(D['to_list'](D['accumulation_list'](idx)), out_list)

    def test_infinite_list(self):
        D=List()
        def tmp_infinite_list(i):
            while True:
                yield i
                i += 1

        lst = []
        i = D['iterator_gen'](D['from_generator'](tmp_infinite_list(0)))
        while True:
            x = i()
            if len(lst) > 50: break
            lst.append(x)
        print(lst)

    @given(st.integers())
    def test_Hofstadter_list(self, idx):
        D = List()
        def tmp_hof_list(k):
            left = []
            right = []
            for i in range(k):
                if i == 0:
                    left.append(0)
                    right.append(1)
                else:
                    left.append(i - right[left[i - 1]])
                    right.append(i - left[right[i - 1]])
            return left, right

        if idx < 500:
            left_res, right_res = D['hofstadter_list'](idx)
            left_res, right_res = D['to_list'](left_res), D['to_list'](right_res)
            left_list, right_list = tmp_hof_list(idx)
            left_list, right_list = list(reversed(left_list)), list(reversed(right_list))
            self.assertEqual(left_res, left_list)
            self.assertEqual(right_res, right_list)

if __name__ == '__main__':
    unittest.main()