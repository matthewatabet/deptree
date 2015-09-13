#! /usr/bin/env python2
'''
Tests for tree.py
'''

from collections import OrderedDict
from mock import call
from mock import patch
import os
import unittest

from deptree.tree import get_deptree

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
SIMPLE_TEST = os.path.join(DATA_DIR, 'simple')
MISSING_TEST = os.path.join(DATA_DIR, 'missing')
MULTIPLE_TEST = os.path.join(DATA_DIR, 'multiple')


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

    @patch('deptree.tree.getLogger')
    def test_bad_references(self, log_mock):
        '''
        Test references which don't exist on disk.
        The logger should issue warnings in this case.
        Also tests that the extension is not added twice to files.
        '''
        log = log_mock.return_value
        file_a = os.path.join(MISSING_TEST, 'a.ts')
        result = get_deptree([file_a])
        expected = OrderedDict([('lib/deptree/test/data/missing/a.ts',
                                 []),
                                ('lib/deptree/test/data/missing/b.ts',
                                 ['lib/deptree/test/data/missing/a.ts']),
                                ('lib/deptree/test/data/missing/c.ts',
                                 ['lib/deptree/test/data/missing/a.ts'])])
        self.assertEqual(result, expected)
        log.warning.assert_has_calls(
            [call('Could not open lib/deptree/test/data/missing/c.ts'),
             call('Could not open lib/deptree/test/data/missing/b.ts')])

    def test_multiple_files(self):
        '''
        Test passing multiple files to get_deptree.
        Exercises referencing files in parent directory.
        '''
        file_a = os.path.join(MULTIPLE_TEST, 'sub', 'a.ts')
        file_b = os.path.join(MULTIPLE_TEST, 'sub', 'b.ts')
        result = get_deptree([file_a, file_b])
        expected = OrderedDict([('lib/deptree/test/data/multiple/sub/a.ts',
                                 []),
                                ('lib/deptree/test/data/multiple/c.ts',
                                 ['lib/deptree/test/data/multiple/sub/a.ts',
                                  'lib/deptree/test/data/multiple/sub/b.ts']),
                                ('lib/deptree/test/data/multiple/d.ts',
                                 ['lib/deptree/test/data/multiple/sub/a.ts',
                                  'lib/deptree/test/data/multiple/c.ts',
                                  'lib/deptree/test/data/multiple/sub/b.ts']),
                                ('lib/deptree/test/data/multiple/f.ts',
                                 ['lib/deptree/test/data/multiple/d.ts']),
                                ('lib/deptree/test/data/multiple/sub/b.ts',
                                 [])])
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
