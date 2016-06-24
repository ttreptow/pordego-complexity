import os


class ComplexityConfig(object):
    def __init__(self, source_paths, ignore_paths=None, complexity_threshold="B", ignore_block_list=None, **kwargs):
        """
        :param source_paths: List of source paths to analyze
        :param ignore_paths: Path patterns to ignore (such as *tests*)
        :param complexity_threshold: Maximum allowed complexity. Defaults to "B"
        :param ignore_block_list: List of blocks to ignore. see parse_ignore_lines docs for description
        """
        self._source_paths = source_paths
        self._ignore_paths = ignore_paths or []
        self._complexity_threshold = complexity_threshold
        self._ignore_blocks = parse_ignore_lines(ignore_block_list or [])

    @property
    def source_paths(self):
        """Paths to source directories"""
        return self._source_paths

    @property
    def ignore_paths(self):
        """List of paths to ignore (can include glob patterns like "*tests*" """
        return self._ignore_paths

    @property
    def complexity_threshold(self):
        """Maximum allowed complixity. Should be a letter grade from 'A' (best) to 'F' (worst) """
        return self._complexity_threshold

    @property
    def ignore_blocks(self):
        """
        Dictionary of code blocks to ignore
        """
        return self._ignore_blocks


def parse_ignore_lines(ignore_block_list):
    """
    Parse the ignore blocks configuration

    Lines should have three columns separated by a space:
    <module path> <function, class, or method name> <rank>
    Lines marked with '#' are ignored as are empty lines or lines without the correct number of columns

    Conveniently, the lines are in the same format as is printed in the error logs

    Paths can be absolute or relative to the location that the tool is run from. Paths should use forward slashes,
     even on windows

    Examples:
    src/mypackage/mypackage/some_module.py SomeClass.mymethod C
    src/mypackage/mypackage/some_module.py myfunc F

    :return: dictionary of blocks to ignore
    """
    ignored_blocks = {}
    for line in ignore_block_list:
        parsed_tuple = parse_line(line)
        if parsed_tuple is not None:
            file_path, function_name = os.path.normpath(parsed_tuple[0]), parsed_tuple[1]
            grade = parsed_tuple[2]
            ignored_blocks[(file_path, function_name)] = grade
    return ignored_blocks


def parse_line(line):
    """
    Parse a line from the ignore config

    :param line: line
    :return: None if line is not in a valid ignore format, or a tuple of (file path, block name, rank)
    """
    if not line or line.strip().startswith('#'):
        return None
    line_parts = [l.strip() for l in line.split(" ")]
    return tuple(line_parts) if len(line_parts) == 3 else None
