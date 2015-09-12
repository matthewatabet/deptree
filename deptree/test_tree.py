#! /usr/bin/env python2
'''
Tests for tree.py
'''

from collections import OrderedDict
import os
import unittest

from deptree.tree import get_deptree

DATA_DIR = os.path.join(os.path.dirname(__file__), 'test', 'data')
SIMPLE_TEST = os.path.join(DATA_DIR, 'simple')


class TestTree(unittest.TestCase):

    def test_simple_case(self):
        '''
        Test a very simple depedency case.
        '''
        file_a = os.path.join(SIMPLE_TEST, 'a.ts')
        result = get_deptree([file_a])
        expected = OrderedDict([('deptree/test/data/simple/a.ts',
                                 []),
                                ('deptree/test/data/simple/b.ts',
                                 ['deptree/test/data/simple/a.ts']),
                                ('deptree/test/data/simple/c.ts',
                                 ['deptree/test/data/simple/a.ts']),
                                ('deptree/test/data/simple/e.ts',
                                 ['deptree/test/data/simple/c.ts']),
                                ('deptree/test/data/simple/d.ts',
                                 ['deptree/test/data/simple/b.ts'])])
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
