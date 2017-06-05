from logging import getLogger

from pordego_complexity.blocks import find_complex_blocks
from pordego_complexity.complexity_config import ComplexityConfig
from pordego_complexity.radon_lib import build_radon_config, run_radon_analysis

logger = getLogger(__name__)


def get_complex_blocks(complexity_config):
    """
    Gets a list of complex code blocks
    :type complexity_config: drawbridge_complexity.complexity_config.ComplexityConfig
    :return:
    """
    bad_blocks = []
    for path in complexity_config.source_paths:
        config = build_radon_config(ignore_files=complexity_config.ignore_paths)
        results = run_radon_analysis(path, config)
        complex_blocks = find_complex_blocks(results, complexity_config.ignore_blocks,
                                             complexity_config.complexity_threshold)
        bad_blocks.extend(complex_blocks)
    return bad_blocks


def build_config(config_dict):
    if config_dict is None:
        raise Exception("No config specified")
    if "source_paths" not in config_dict:
        raise Exception("Missing config parameter {}".format("source_paths"))
    return ComplexityConfig(**config_dict)


def analyze_complexity(config_dict):
    """
    Analyzes code complexity
    (Pordego complexity plugin entry point)

    :param config_dict: dictionary parsed from config file
    :return:
    """
    config = build_config(config_dict)
    complex_blocks = get_complex_blocks(config)
    if complex_blocks:
        raise AssertionError("Complexity check failed. "
                             "You need to refactor these code areas:\n{}".format(format_bad_blocks(complex_blocks)))
    logger.info("Complexity check complete. Ignoring {} bad blocks".format(len(config.ignore_blocks)))


def format_bad_blocks(bad_blocks):
    """Prints out block results in rows"""
    return "\n".join(sorted([str(b).replace("\\", "/") for b in bad_blocks]))
