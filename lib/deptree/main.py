'''
The main run function of our executable.
Parses arguments, configures logging, and prints output.
'''

from argparse import ArgumentDefaultsHelpFormatter
from argparse import ArgumentParser
from logging import basicConfig

from . constants import DEFAULT_DEPENDENCY_REGEX
from . constants import DEFAULT_EXTENSION
from . constants import LOGGER_FORMAT
from . tree import get_deptree


def run(args):
    '''
    Parse command line arguments, run dependencies, print results.
    '''
    # Create our argparser. Set the formatter_class to allow the defaults
    # for each argument to be printed.
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('src_file',
                        nargs='+',
                        help='Source files to parse for depedencies.')
    parser.add_argument('-p', '--pattern',
                        help='Regular expression used to find depdencies.'
                             'Must contain a named group called "path".',
                        default=DEFAULT_DEPENDENCY_REGEX)
    parser.add_argument('-e', '--extension',
                        help='Extension of referenced include files.',
                        default=DEFAULT_EXTENSION)
    args = parser.parse_args(args)

    # Set up basic logging configuration.
    basicConfig(format=LOGGER_FORMAT)

    # Get reverse-depedency tree and print.
    resolved_tree = get_deptree(args.src_file,
                                pattern=args.pattern,
                                extension=args.extension)
    for source_file, depdencies in resolved_tree.items():
        print source_file, '<-', ' '.join(depdencies)
