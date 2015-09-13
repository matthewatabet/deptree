from argparse import ArgumentParser
from logging import basicConfig

from . constants import DEFAULT_DEPENDENCY_REGEX
from . constants import LOGGER_FORMAT
from . tree import get_deptree


def run(args):
    '''
    Parse command line arguments, run dependencies, print results.
    '''
    parser = ArgumentParser()
    parser.add_argument('src_file',
                        nargs='+',
                        help='Source files to parse for depedencies.')
    parser.add_argument('-p', '--pattern',
                        help='Regular expression used to find depdencies.',
                        default=DEFAULT_DEPENDENCY_REGEX)
    args = parser.parse_args(args)

    # Set up basic logging configuration.
    basicConfig(format=LOGGER_FORMAT)

    # Get reverse-depedency tree and print.
    resolved_tree = get_deptree(args.src_file, pattern=args.pattern)
    for source_file, depdencies in resolved_tree.items():
        print source_file, '<-', ' '.join(depdencies)
