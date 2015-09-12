'''
Utilities for parsing source file depedencies.
'''
from collection import OrderedDict
import os
import re

from . import constants


def get_deptree(src_files, pattern=constants.DEFAULT_DEPENDENCY_REGEX):
    '''
    Given a list of source files and a regular expression string
    representing the dependency pattern, return an ordered dictionary
    mapping source files to their upstream dependencies.
    '''
    regex = re.compile(pattern)
    depedencies = OrderedDict()
    files_to_parse = src_files[:]
    while files_to_parse:
        file_to_parse = files_to_parse.pop()
        deps = _file_depedencies(file_to_parse, regex)
        depedencies.setdefault(file_to_parse, []).extend(deps)
        for dep in deps:
            if dep not in files_to_parse:
                files_to_parse.append(dep)
    return depedencies


def _file_depedencies(src_file, regex):
    '''
    Given the path to a source file, parse the file for depedencies.
    Return a list of dependent files.
    '''
    try:
        with open(src_file) as f:
            text = f.read()
    except IOError:
        return []  # TODO: what to do with missing files?

    parent_dir = os.path.dirname(src_file)
    dependencies = []
    for dependency in regex.findall(text):
        dependencies.append(os.path.normpath(os.path.join(parent_dir,
                                                          dependency)))
    return dependencies
