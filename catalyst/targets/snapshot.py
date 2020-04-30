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

        self.git = command('git')
        self.ebuild_repo = Path(self.settings['repos'],
                                self.settings['repo_name']).with_suffix('.git')
        self.gitdir = str(self.ebuild_repo)

    def update_ebuild_repo(self) -> str:
        repouri = 'https://anongit.gentoo.org/git/repo/sync/gentoo.git'

        if self.ebuild_repo.is_dir():
            git_cmds = [
                [self.git, '-C', self.gitdir, 'fetch', '--quiet', '--depth=1'],
                [self.git, '-C', self.gitdir, 'update-ref', 'HEAD', 'FETCH_HEAD'],
                [self.git, '-C', self.gitdir, 'gc', '--quiet'],
            ]
        else:
            git_cmds = [
                [self.git, 'clone', '--quiet', '--depth=1', '--bare',
                 '-c', 'gc.reflogExpire=0',
                 '-c', 'gc.reflogExpireUnreachable=0',
                 '-c', 'gc.rerereresolved=0',
                 '-c', 'gc.rerereunresolved=0',
                 '-c', 'gc.pruneExpire=now',
                 '--branch=stable',
                 repouri, self.gitdir],
            ]

        for cmd in git_cmds:
            log.notice('>>> ' + ' '.join(cmd))
            subprocess.run(cmd,
                           encoding='utf-8',
                           close_fds=False)

        sp = subprocess.run([self.git, '-C', self.gitdir, 'rev-parse', 'stable'],
                            stdout=subprocess.PIPE,
                            encoding='utf-8',
                            close_fds=False)
        return sp.stdout.rstrip()

    def run(self):
        if self.settings['snapshot_treeish'] == 'stable':
            treeish = self.update_ebuild_repo()
        else:
            treeish = self.settings['snapshot_treeish']

        self.set_snapshot(treeish)

        git_cmd = [self.git, '-C', self.gitdir, 'archive', '--format=tar',
                   treeish]
        tar2sqfs_cmd = [command('tar2sqfs'), str(self.snapshot), '-q', '-f',
                        '-j1', '-c', 'gzip']

        log.notice('Creating %s tree snapshot %s from %s',
                   self.settings['repo_name'], treeish, self.gitdir)
        log.notice('>>> ' + ' '.join([*git_cmd, '|']))
        log.notice('    ' + ' '.join(tar2sqfs_cmd))

        lockfile = self.snapshot.with_suffix('.lock')
        with write_lock(lockfile):
            git = subprocess.Popen(git_cmd,
                                   stdout=subprocess.PIPE,
                                   stderr=sys.stderr,
                                   close_fds=False)
            tar2sqfs = subprocess.Popen(tar2sqfs_cmd,
                                        stdin=git.stdout,
                                        stdout=sys.stdout,
                                        stderr=sys.stderr,
                                        close_fds=False)
            git.stdout.close()
            git.wait()
            tar2sqfs.wait()

        if tar2sqfs.returncode == 0:
            log.notice('Wrote snapshot to %s', self.snapshot)
        else:
            log.error('Failed to create snapshot')
        return tar2sqfs.returncode == 0
