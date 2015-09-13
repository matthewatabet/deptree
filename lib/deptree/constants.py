'''
Library constants.
'''

DEFAULT_DEPENDENCY_REGEX = (
    '''^import\s+\w+\s*=\s*require\(\s*(?P<quote>['"])'''
    '''(?P<path>\.[\.\w/]+)(?P=quote)\s*\)''')

DEFAULT_EXTENSION = '.ts'

LOGGER_FORMAT = 'deptree: %(levelname)s %(message)s'
