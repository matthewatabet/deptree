'''
Utilities for parsing source file depedencies.
'''
from collections import OrderedDict
from logging import getLogger
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

    # Reverse the files to parse to produce more intuitive output.
    # The first source file listed should be the first popped from
    # the stack and parsed.
    files_to_parse = [s.replace(os.getcwd() + '/', '', 1) for s
                      in reversed(src_files)]

    # To avoid parsing files twice, we keep track of which files
    # have already been processed.
    parsed_files = set([])

    # Continue parsing until our stack is empty.
    while files_to_parse:
        file_to_parse = files_to_parse.pop()
        dependencies.setdefault(file_to_parse, [])
        parsed_files.add(file_to_parse)

        # Get the depdendencies of the current file, add any newly
        # found dependencies to the stack for processing.
        deps = _file_depedencies(file_to_parse, regex, extension)
        for dep in deps:
            if dep not in set(files_to_parse).union(parsed_files):
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
        getLogger(__name__).warning('Could not open %s' % (src_file))
        return []

    # The list of found depedencies we'll accumulate and eventually return.
    dependencies = []

    # Make all references relative to the current source file.
    parent_dir = os.path.dirname(src_file)

    # Get the groups found by the regular expression as a list of dictionaries.
    matches = [m.groupdict() for m in regex.finditer(text)]
    for match in matches:

        # Get the path group, which contains the path pointing to the
        # referenced file.
        path = match.get('path')
        if path is None:
            continue

        # Add the extension if the reference doesn't already contain it.
        if not path.endswith(extension):
            path += extension

        # Normalize the path to remove extraneous references to parent
        # and current directories.
        path = os.path.normpath(os.path.join(parent_dir, path))
        dependencies.append(path)
    return dependencies
