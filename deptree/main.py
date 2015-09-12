from argparse import ArgumentParser

from . import constants
from . tree import get_deptree


def run(args):
    '''
    Parse command line arguments, run dependencies, print results.
    '''
    parser = ArgumentParser()
    parser.add_argument('src_files',
                        nargs='+',
                        help='Source files to parse for depedencies.')
    parser.add_argument('-p', '--pattern',
                        help='Regular expression used to find depdencies.',
                        default=constants.DEFAULT_DEPENDENCY_REGEX)
    args = parser.parse_args(args)
    resolved_tree = get_deptree(args.src_files, pattern=args.pattern)

    # Print tree
    for source_file, depdencies in resolved_tree.items():
        print source_file, ' '.join(depdencies)
