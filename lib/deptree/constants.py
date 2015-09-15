'''
Library constants.
'''

# Default regular expression used for depedency scanning.
# Matches the following:
# import MODULE_NAME = require('RELATIVE_PATH')
# import MODULE_NAME = require("RELATIVE_PATH")
# where RELATIVE_PATH must begin with ./ or ../
DEFAULT_DEPENDENCY_REGEX = '''^import\s+\w+\s*=\s*require\(\s*(?P<quote>['"])(?P<path>(\./|\.\./)[\.\w\-\s/]+)(?P=quote)\s*\)'''

# Default file extension used when resolving source file references.
DEFAULT_EXTENSION = '.ts'

# Output format for Python logging messages.
LOGGER_FORMAT = 'deptree: %(levelname)s %(message)s'
