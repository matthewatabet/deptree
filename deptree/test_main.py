#! /usr/bin/env python2
'''
Tests for main.py
'''

from mock import patch
import unittest

from . main import run
from . constants import DEFAULT_DEPENDENCY_REGEX


class TestRun(unittest.TestCase):
    '''
    Test main.run()
    '''
    @patch('deptree.main.argparse._sys.exit')
    @patch('deptree.main.get_deptree')
    def test_run_no_args(self, tree_mock, exit_mock):
        '''
        Test that the tree is not computed if no files were specified.
        '''
        exit_mock.side_effect = RuntimeError
        self.assertRaises(RuntimeError, run, [])
        self.assertTrue(exit_mock.called)
        self.assertFalse(tree_mock.called)

    @patch('deptree.main.get_deptree')
    def test_run_one_file(self, tree_mock):
        '''
        Test running command with one file.
        '''
        run(['myfile'])
        tree_mock.assert_called_once_with(['myfile'],
                                          pattern=DEFAULT_DEPENDENCY_REGEX)

    @patch('deptree.main.get_deptree')
    def test_run_multiple_files(self, tree_mock):
        '''
        Test running command with multiple files.
        '''
        run(['file_1', 'file_2', 'file_3'])
        tree_mock.assert_called_once_with(['file_1',
                                           'file_2',
                                           'file_3'],
                                          pattern=DEFAULT_DEPENDENCY_REGEX)

    @patch('deptree.main.get_deptree')
    def test_run_pattern_override(self, tree_mock):
        '''
        Test running with pattern override.
        '''
        run(['myfile', '-p', 'some_regex'])
        tree_mock.assert_called_once_with(['myfile'], pattern='some_regex')


if __name__ == '__main__':
    unittest.main()
