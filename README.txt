* deptree

deptree is a simple utility for printing the reverse depedency tree of a set
of source files. By default, deptree is configured to parse TypeScript files,
but can be configured to handle other formats.


* Installation

From within an activated Python virtualenv, cd to the deptree project root and
run:

./setup.py install

This will install the deptree library, the deptree executable, and all external
depedencies. If errors occur, please verify that you have the latest version
of pip and virtualenv installed and are able to install third party packages
from PyPi. For more information, please see:

https://pip.pypa.io
https://virtualenv.pypa.io


* Tests

Once deptree is installed, you may run the unittests against the development
code within the project root by running:

./bin/runtests

This will use Python's unittest discovery functionality to locate and execute
all unittests.


* Usage

deptree is straightforward. Simply run:

deptree myscript.ts

myscript.ts <- 
fs.ts <- myscript.ts
os.ts <- myscript.ts

Multiple source files may be specified. The regular expression used to find
depedencies may be overridden using the --pattern flag. If an alternate
expression is specified, it must include a named capturing group called
"path" which represents the relative path to the referenced file. Extensions
besides ".ts" may be used by employing the --extension option. For more
usage information, please see:

deptree -h


* The deptree Library

Deptree may be used within other Python applications:

import deptree
from pprint import pprint
dependencies = deptree.get_deptree(['myscript.ts'])


This will reutrn an OrderedDictionary mapping source files to their depedents:

OrderedDict([('myscript.ts', []),
             ('fs.ts', ['myscript.ts']),
             ('os.ts', ['myscript.ts'])])


* Implementation notes

- While a more abstract implementation is certainly possible, I've chosen for
a concrete solution which solves the problem at hand. In other words, some
type of DepdendencyTree class could have a number of DepdendencyNode children,
each with its own children. A DepdendencyVisitor class could then walk this
tree in arbitrary ways to produce forward or reverse depdendency graphs, etc.
However, such an abstract design carries its own maintenance cost and risks
(primarily a steep learning curve for other developers and additional lines of
code, each with the potential for their own additional bugs). Given that the 
current implementation is so terse, it can easily be swapped later for a more
generic and abstract solution if needed.

- deptree was written to be pep8 compliant within reason. Exceptions are
occasionally made for readability.

- Tests are written using Python's unittest and mock libraries. Thus, mock
and its dependencies will be installed when ./setup.py install is run. mock
allows for consistent and coherent 'monkey patching' of code by reassigning
objects at runtime. See https://pypi.python.org/pypi/mock for more info.

- The project structure is:
    ./ <- root
    ./bin <- executables
    ./lib <- libraries
    ./lib/deptree <- the deptree package
    ./lib/deptree/test <- unittests and test data

- git was used for source control, virtualenv for environment configuration,
and setuptools for deployment. flake8 was used for linting.

- The 'deptree' executable is a very thin wrapper around deptree.main.run.
Housing most of the executable logic within the 'deptree' package allows
for the executable logic to by easily tested.

- To keep code terse, dot notation from imported libraries is avoided as much
as possible. Thus, 'from argparse import ArgumentParser' is preferred over
'import argparse'.
