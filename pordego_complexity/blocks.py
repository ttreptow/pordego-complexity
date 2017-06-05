

class BlockComplexityResult(object):
    """Result of the complexity analysis for a block (function or class method)"""
    def __init__(self, block_result_dict, file_path):
        class_name = block_result_dict.get("classname")
        function_name = block_result_dict["name"]
        self.file_path = file_path
        self.method_name = ".".join([class_name, function_name]) if class_name else function_name
        self.rank = block_result_dict["rank"]
        self.lineno = block_result_dict["lineno"]
        self.complexity = block_result_dict["complexity"]

    def __str__(self):
        return " ".join([self.file_path, self.method_name, self.rank])


class SyntaxErrorResult(BlockComplexityResult):
    """Complexity test detected a syntax error"""
    def __init__(self, error_result_dict, file_path):
        block_result_dict = {"classname": "unknown",
                             "name": "unknown",
                             "rank": "F",
                             "lineno": unicode(error_result_dict),
                             "complexity": "unknown"
                             }
        super(SyntaxErrorResult, self).__init__(block_result_dict, file_path)

    def __str__(self):
        return "Syntax error in file {}".format(self.file_path)


def find_complex_blocks(analysis_output, ignore_blocks, abs_threshold):
    """
    Iterate the analysis output and filter ignored blocks as well as blocks not meeting the threshold

    :param analysis_output: dictionary of lists of complexity analysis results
    :param ignore_blocks: dictionary of blocks to ignore
    :param abs_threshold: complexity rank threshold
    :return: List of complex blocks
    """
    bad_blocks = []
    for file_path, blocks in analysis_output.iteritems():
        for block in blocks:
            if isinstance(block, basestring):
                block_result = SyntaxErrorResult(block, file_path)
            else:
                block_result = BlockComplexityResult(block, file_path)
            if filter_block_result(file_path, block_result, abs_threshold, ignore_blocks):
                continue
            bad_blocks.append(block_result)
    return bad_blocks


def filter_block_result(file_path, result, abs_threshold, ignore_blocks):
    """
    Return true if the block should be filtered

    :param file_path: path to the module
    :param result: BlockComplexityResult
    :param abs_threshold: Rank threshold
    :param ignore_blocks: dict of blocks to ignore
    :return:
    """
    if result is None:
        return True
    if result.rank <= abs_threshold:
        return True
    key = (file_path, result.method_name)
    if key in ignore_blocks and result.rank <= ignore_blocks[key]:
        return True
    return False