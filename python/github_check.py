# -*- coding: utf-8 -*-
#!/usr/bin/python
# Refernce: https://github3py.readthedocs.io/en/0.9.3/github.html

import github3
import os
import pytz
import datetime
import sys
import getopt

local_tz = pytz.timezone('Asia/Seoul')


def init_github3(user, password):
    gh = github3.login(user, password)
    return gh


def get_repo_last_commit_delta_time(gh, user, repo):
    try:
        repo = gh.repository(user, repo)
        if repo is None:
            print ("[Error]: Not Found repository(user=%s, repoistory=%s)" % (user, repo))
            sys.exit(1)

        return repo.pushed_at.astimezone(local_tz)
    except Exception as err:
        print ("[Error] %s" % (str(err)))


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
        print ("%s/%s commited today." % (user, repo))
    else:
        print ("%s/%s has not committed for %s days." % (user, repo, delta_time))


def get_all_repository_commit(gh, user):
    repos = gh.iter_repos(type="owner", sort="pushed")
    for repo in repos:
        get_repository_commit(gh, user, repo.name)


def usage():
    print ("================================================================================")
    print ("* User Input: %s" % sys.argv[1:])
    print ("================================================================================")
    print ("%s [u:p:r:ah]\n" % sys.argv[0])
    print ("-u, --user        Set github username")
    print ("-p, --password    Set github password")
    print ("-r, --repo        Set github repository")
    print ("-a, --all         Set all github repository")
    print ("-h, --help        Print usage")

    print ("\n")
    print ("* ex) python github_test.py -u jhhwang4195 -p password -r TIL,my_source")
    print ("* ex) python github_test.py -u jhhwang4195 -p password -a")
    print ("================================================================================")

if __name__ == '__main__':

    user = None
    password = None
    repos = None
    all_repo = None

    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   "u:p:r:ah",
                                   ["user=", "password=", "repo=", "all=", "help"])

    except getopt.GetoptError, err:
        print(err)
        sys.exit(-1)

    for o, val in opts:
        if o in ("-u", "--user"):
            user = val
        elif o in ("-p", "--password"):
            password = val
        elif o in ("-r", "--repo"):
            repos = val
        elif o in ("-a", "--all"):
            all_repo = val
        elif o in ("-h", "--help"):
            usage()
            sys.exit(-1)
        else:
            assert False, "unhandled option"
            usage()
            sys.exit(-1)

    if user is None:
        print ("[Error] -u option is None")
        sys.exit(-1)
    elif password is None:
        print ("[Error] -p option is None")
        sys.exit(-1)
    elif repos is None and all_repo is None:
        print ("[Error] -r option or -a option is None")
        sys.exit(-1)

    gh = init_github3(user, password)

    if repos is not None:
        print (">>> Selected repository info")
        repo = repos.split(",")
        for r in repo:
            get_repository_commit(gh, user, r)

    if all_repo is not None:
        print (">>> All repository info")
        get_all_repository_commit(gh, user)
