from radon.cli import Config
from radon.cli.harvest import CCHarvester
from radon.complexity import SCORE


def build_radon_config(ignore_files=None, exclude_paths=None, no_assert=False):
    return Config(
            exclude=",".join(exclude_paths) if exclude_paths else None,
            ignore=",".join(ignore_files) if ignore_files else None,
            order=SCORE,
            no_assert=no_assert,
            show_closures=False,
            min='A',
            max='F',
        )


def run_radon_analysis(file_path, radon_config):
    harvester = CCHarvester([file_path], radon_config)
    return harvester._to_dicts()
