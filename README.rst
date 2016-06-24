pordego-complexity
==================

Summary
-------
`Pordego <https://github.com/ttreptow/pordego>`_ plugin that analyzes code using the `Radon <https://pypi.python.org/pypi/radon>`_ library.

If the code does not meet a specified threshold, it will print the complex blocks and cause the pordego tool to return an error code.

Configuration
-------------

source_paths
^^^^^^^^^^^^
There is one required parameter "source_paths". This parameter should be a list of paths to directories containing Python source code (other types of code are ignored). The paths are searched recursively, so only the top level folder need be specified.
The paths can be absolute or relative to the directory where pordego is run.

ignore_paths
^^^^^^^^^^^^
Optional. A list of file patterns to ignore, such as "*test*" which will ignore all files containing "test"

complexity_threshold
^^^^^^^^^^^^^^^^^^^^
Optional (default "B"). The maximum allowable complexity. See `<https://radon.readthedocs.io/en/latest/api.html#radon.complexity.cc_rank>`_ for a description of the ranks.

ignore_block_list
^^^^^^^^^^^^^^^^^
Optional. For lsiting all that legacy code that hasn't been refactored yet.

Each entry in the list should be a string formatted like so:
<path to file> <class name.method name or function name> <Max complexity grade>

<Path to file> should start with one of the paths specified in source_paths, so if the source path is relative, this should be as well
Functions are specified with just the function name, methods that are part of a class (including class/staticmethods) are joined to the class name with a '.'
<Max complexity grade> specifies the worst grade that is allowed for the block of code. If the calculated grade is at or above the threshold grade, it will pass.

The easiest way to generate the ignore_block_list is to run the complexity plugin without ignore_block_list. The plugin prints the list of complex blocks in the same format as the ignore_block_list.

Example:
path/to/my/src/mymodule.py MyClass.some_method D
path/to/my/src/mymodule.py some_free_function E

