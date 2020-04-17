"""
Snapshot target
"""

import subprocess
import sys

from pathlib import Path

from catalyst import log
from catalyst.base.targetbase import TargetBase
from catalyst.lock import write_lock
from catalyst.support import command

class snapshot(TargetBase):
    """
    Builder class for snapshots.
    """
    required_values = frozenset([
        'target',
    ])
    valid_values = required_values | frozenset([
        'snapshot_treeish',
    ])

    def __init__(self, myspec, addlargs):
        TargetBase.__init__(self, myspec, addlargs)

        treeish = self.settings['snapshot_treeish']
        self.ebuild_repo = Path(self.settings['repos'],
                                self.settings['repo_name']).with_suffix('.git')

        self.git_cmd = [command('git'), '-C', self.ebuild_repo, 'archive',
                        '--format=tar', treeish]
        self.tar2sqfs_cmd = [command('tar2sqfs'), str(self.snapshot), '-q',
                             '-f', '-c', 'gzip']

    def update_ebuild_repo(self):
        repouri = 'https://anongit.gentoo.org/git/repo/sync/gentoo.git'
        gitdir = str(self.ebuild_repo)
        git = command('git')

        if self.ebuild_repo.is_dir():
            git_cmds = [
                [git, '-C', gitdir, 'fetch', '--quiet', '--depth=1'],
                [git, '-C', gitdir, 'gc', '--quiet'],
            ]
        else:
            git_cmds = [
                [git, 'clone', '--quiet', '--depth=1', '--bare',
                 '-c', 'gc.reflogExpire=0',
                 '-c', 'gc.reflogExpireUnreachable=0',
                 '-c', 'gc.rerereresolved=0',
                 '-c', 'gc.rerereunresolved=0',
                 '-c', 'gc.pruneExpire=now',
                 '--branch', 'stable',
                 repouri, gitdir],
            ]

        for cmd in git_cmds:
            subprocess.run(cmd)

        cp = subprocess.run([git, '-C', gitdir, 'rev-parse', 'stable'],
                            subprocess.PIPE, encoding='utf-8')
        self.settings['snapshot_treeish'] = cp.stdout.rstrip()

    def run(self):
        if not self.settings['snapshot_treeish']:
            self.update_ebuild_repo()

        log.notice('Creating %s tree snapshot %s from %s ...',
                   self.settings['repo_name'],
                   self.settings['snapshot_treeish'],
                   str(self.ebuild_repo))

        lockfile = self.snapshot.with_suffix('.lock')
        with write_lock(lockfile):
            git = subprocess.Popen(self.git_cmd,
                                   stdout=subprocess.PIPE,
                                   stderr=sys.stderr,
                                   close_fds=False)
            tar2sqfs = subprocess.Popen(self.tar2sqfs_cmd,
                                        stdin=git.stdout,
                                        stdout=sys.stdout,
                                        stderr=sys.stderr,
                                        close_fds=False)
            git.stdout.close()
            git.wait()

        if not tar2sqfs:
            log.error('Failed to create snapshot')
        return bool(tar2sqfs)
