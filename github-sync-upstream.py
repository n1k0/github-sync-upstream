import os
import subprocess
import sys

from github3.api import login

GITHUB_USERNAME = os.environ.get('GITHUB_USERNAME')
GITHUB_PASSWORD = os.environ.get('GITHUB_PASSWORD')
GITHUB_ORGANIZATION = os.environ.get('GITHUB_ORGANIZATION')
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
REPOS_ROOT_DIR = os.path.join(ROOT_DIR, 'repos')


def command(cmd):
    try:
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as err:
        print "Error invoking `%s`:" % ' '.join(err.cmd)
        print err.output
        sys.exit(1)


def check_repo_dir(repo):
    repo_dir = os.path.join(REPOS_ROOT_DIR, repo.name)
    if not os.path.exists(repo_dir):
        print u"Checking out repo %s from %s..." % (repo.name, repo.ssh_url)
        print command(['git', 'clone', repo.ssh_url, repo_dir])
        os.chdir(repo_dir)
        print command(['git', 'remote', 'add', 'upstream', repo.parent.git_url])
        os.chdir(ROOT_DIR)
    return repo_dir


def update_repo(repo):
    repo_dir = check_repo_dir(repo)
    os.chdir(repo_dir)
    print command(['git', 'fetch', 'upstream'])
    print command(['git', 'merge', 'upstream/%s' % repo.master_branch])
    print command(['git', 'push'])
    os.chdir(ROOT_DIR)
    print 'Updated %s' % repo.name


def run():
    if not all([GITHUB_USERNAME, GITHUB_PASSWORD]):
        print 'Missing github username and/or password.'
        sys.exit(1)

    gh = login(GITHUB_USERNAME, password=GITHUB_PASSWORD)

    if GITHUB_ORGANIZATION:
        q = (u'Sync all forked repositories for the "%s" organization? (yN): '
             % GITHUB_ORGANIZATION)
        organization = gh.organization(GITHUB_ORGANIZATION)
        repos = organization.iter_repos()
    else:
        q = u"Sync all %s's forked repositories? (yN): " % GITHUB_USERNAME
        repos = gh.iter_repos()

    if not raw_input(q) in ('y', 'Y', 'yes'):
        print 'Aborted.'
        sys.exit(1)

    repos = [r.refresh() for r in repos if r.is_fork()]

    for repo in repos:
        update_repo(repo)

    print 'All done.'


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        print '\nAborted.'
        sys.exit(1)
