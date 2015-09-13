#! /usr/bin/env python2
'''
Tests for tree.py
'''

from collections import OrderedDict
import os
import unittest

from deptree.tree import get_deptree

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
SIMPLE_TEST = os.path.join(DATA_DIR, 'simple')


class TestTree(unittest.TestCase):

    def test_simple_case(self):
        '''
        Test a very simple depedency case.
        '''
        file_a = os.path.join(SIMPLE_TEST, 'a.ts')
        result = get_deptree([file_a])
        expected = OrderedDict([('lib/deptree/test/data/simple/a.ts',
                                 []),
                                ('lib/deptree/test/data/simple/b.ts',
                                 ['lib/deptree/test/data/simple/a.ts']),
                                ('lib/deptree/test/data/simple/c.ts',
                                 ['lib/deptree/test/data/simple/a.ts']),
                                ('lib/deptree/test/data/simple/e.ts',
                                 ['lib/deptree/test/data/simple/c.ts']),
                                ('lib/deptree/test/data/simple/d.ts',
                                 ['lib/deptree/test/data/simple/b.ts'])])
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
