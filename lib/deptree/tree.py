'''
Utilities for parsing source file depedencies.
'''
from collections import OrderedDict
import os
import re

from . constants import DEFAULT_DEPENDENCY_REGEX
from . constants import DEFAULT_EXTENSION


def get_deptree(src_files,
                pattern=DEFAULT_DEPENDENCY_REGEX,
                extension=DEFAULT_EXTENSION):
    '''
    Given a list of source files and a regular expression string
    representing the dependency pattern, return an ordered dictionary
    mapping source files to their upstream dependencies.
    '''
    regex = re.compile(pattern, re.MULTILINE)
    dependencies = OrderedDict()
    files_to_parse = [s.replace(os.getcwd() + '/', '', 1) for s in src_files]
    while files_to_parse:
        file_to_parse = files_to_parse.pop()
        dependencies.setdefault(file_to_parse, [])
        deps = _file_depedencies(file_to_parse, regex, extension)
        for dep in deps:
            if dep not in files_to_parse:
                files_to_parse.append(dep)
            dependencies.setdefault(dep, []).append(file_to_parse)
    return dependencies


def _file_depedencies(src_file, regex, extension):
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
        filename = dependency + extension
        filepath = os.path.normpath(os.path.join(parent_dir, filename))
        dependencies.append(filepath)
    return dependencies
