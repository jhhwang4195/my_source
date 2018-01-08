# -*- coding: utf-8 -*-
#!/usr/bin/python
# Refernce: https://github3py.readthedocs.io/en/0.9.3/github.html

import github3
import os
import pytz
import datetime
import sys

local_tz = pytz.timezone('Asia/Seoul')


def init_github3(user, password):
    gh = github3.login(user, password)
    return gh


def get_repo_last_commit_delta_time(gh, user, repo):
    repo = gh.repository(user, repo)
    return repo.pushed_at.astimezone(local_tz)


def get_delta_time(last_commit):
    now = datetime.datetime.now(local_tz)
    delta = now - last_commit
    return delta.days


def get_repository_info(gh, user, repo):
    repo = gh.repository(user, repo)
    print "### user:%s, repository:%s" % (user, repo)
    print "name: %s" % repo.name
    print "owner: %s" % repo.owner
    print "description: %s" % repo.description
    print "created_at: %s" % repo.created_at
    print "pushed_at: %s" % repo.pushed_at.astimezone(local_tz)


def get_repository_commit(gh, user, repo):
    last_commit = get_repo_last_commit_delta_time(gh, user, repo)
    delta_time = get_delta_time(last_commit)

    if(delta_time == 0):
        print ('%s/%s commited today.' % (user, repo))
    else:
        print ('%s/%s has not committed for %s days.' % (user, repo, delta_time))


def get_all_repository_commit(gh, user):
    repos = gh.iter_repos(type="owner", sort="pushed")
    for repo in repos:
        get_repository_commit(gh, user, repo.name)


if __name__ == '__main__':
    try:
        user = os.environ['GITHUB_USERNAME']
        password = os.environ['GITHUB_PASSWORD']
    except:
        print ("[ERROR] Add the GITHUB_USERNAME and GITHUB_PASSWORD environment variables.")
        print ("- export GITHUB_USERNAME=_YOUR_GITHUB_ID_")
        print ("- export GITHUB_PASSWORD=_YOUR_GITHUB_PASSWORD_")
        sys.exit(-1)

    gh = init_github3(user, password)

    # print TIL repository info
    print "============================================="
    print (">>> TIL repository info")
    get_repository_info(gh, user, "TIL")

    # print repository info
    print "============================================="
    print (">>> repository info")
    get_repository_commit(gh, user, "TIL")
    get_repository_commit(gh, user, "my_config")
    get_repository_commit(gh, user, "slackbot")
    get_repository_commit(gh, user, "commitbot")
    get_repository_commit(gh, user, "my_source")

    # print all repository info
    print "============================================="
    print (">>> all repository info")
    get_all_repository_commit(gh, user)
    print "============================================="
