# These functions are supposed to support a git deploy process.
# The deploy branch contains generated content; the generated
# content should be committed to a branch, then pushed to github.

from fabric.api import local, puts, settings
from time import strftime, localtime

SOURCE_BRANCH = "dev"
DEPLOY_BRANCH = "master"

def change_branch(branch):
    """ Switch to specified Branch """
    local("git checkout {}".format(branch))


def commit_all(msg = None):
    """ Commit generated content to branch """
    if not msg:
        timestamp = strftime("%Y-%m-%d %H:%I:%S", localtime())
        msg = "Published Blog at {0}".format(timestamp)
    local("git add .")
    cmd = "git commit -a -m {0!r}".format(msg)
    with settings(warn_only=True):
        result = local(cmd)
    if result.failed:
        puts("Nothing to commit")
        return False
    else:
        return True


def merge(merge_target):
    """ Merge target branch into current """
    local("git merge --no-edit {0}".format(merge_target))


def push(target):
    """ Push the generated content to the specified target """
    local("git push origin {0}".format(target))
