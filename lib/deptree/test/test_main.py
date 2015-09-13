#! /usr/bin/env python2
'''
Tests for main.py
'''

from mock import patch
import unittest

from deptree.main import ArgumentParser
from deptree.main import run
from deptree.constants import DEFAULT_DEPENDENCY_REGEX
from deptree.constants import DEFAULT_EXTENSION


class TestRun(unittest.TestCase):
    '''
    Test main.run()
    '''
    @patch.object(ArgumentParser, 'exit')
    @patch.object(ArgumentParser, 'print_usage')
    @patch('deptree.main.get_deptree')
    def test_run_no_args(self, tree_mock, usage_mock, exit_mock):
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
                                          extension=DEFAULT_EXTENSION,
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
                                          extension=DEFAULT_EXTENSION,
                                          pattern=DEFAULT_DEPENDENCY_REGEX)

    @patch('deptree.main.get_deptree')
    def test_run_overrides(self, tree_mock):
        '''
        Test running with pattern and extension overrides.
        '''
        run(['myfile', '-p', 'some_regex', '-e', '.txt'])
        tree_mock.assert_called_once_with(['myfile'],
                                          pattern='some_regex',
                                          extension='.txt')


if __name__ == '__main__':
    unittest.main()
