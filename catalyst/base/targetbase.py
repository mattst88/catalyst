import os

from abc import ABC, abstractmethod
from pathlib import Path

from catalyst.support import addl_arg_parse


class TargetBase(ABC):
    """
    The toplevel class for all targets. This is about as generic as we get.
    """

    def __init__(self, myspec, addlargs):
        addl_arg_parse(myspec, addlargs, self.required_values,
                       self.valid_values)
        self.settings = myspec
        self.env = {
            'PATH': '/bin:/sbin:/usr/bin:/usr/sbin',
            'TERM': os.getenv('TERM', 'dumb'),
        }

        # Set snapshot
        snapshots_dir = Path(self.settings['storedir']) / 'snapshots'
        snapshots_dir.mkdir(mode=0o755, exist_ok=True)
        self.snapshot = snapshots_dir / \
            f"{self.settings['repo_name']}-{self.settings['snapshot_treeish']}.sqfs"

    @property
    @classmethod
    @abstractmethod
    def required_values(cls):
        return NotImplementedError

    @property
    @classmethod
    @abstractmethod
    def valid_values(cls):
        return NotImplementedError
