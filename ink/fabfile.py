#! /usr/bin/env python

import os
# import sys
import datetime
from fabric import state
from fabric.api import local, env, abort
from fabric.operations import prompt

env.hosts = ['localhost']

state.output.warnings = False
state.output.running = False
state.output.user = False
state.output.status = False


def lsdb():
    local("mysql --host=%(mysql_host)s --user=%(mysql_root_user)s --password=%(mysql_root_pass)s --port=%(mysql_port)s --socket=%(mysql_socket)s -e 'show databases;'" % env)


def kill_ds_store(path):
    local('rm -rf %s/.DS_Store --preserve-root' % path)


def fetch_latest_db():
    path = "%(ink_path)s/%(project)s" % env
    kill_ds_store(path)
    dirList = sorted_ls(path)
    print "FILE", dirList[len(dirList)-1]
    return dirList[len(dirList)-1]


def ls(project=''):
    print "\n=== Ink Projects ==="
    env.project = project
    path = "%(ink_path)s/%(project)s" % env
    kill_ds_store(path)
    dirList = os.listdir(path)
    for fname in dirList:
        print "-- %s" % fname
    print "\n"


def update(project=False, db=False):
    if(not project):
        fetch_project()
    else:
        env.project = project

    if(not db):
        fetch_db()
    else:
        env.db = db

    env.db_file = fetch_latest_db()

    if(exists(env.project)):
        print "== importing the latest database for %(project)s into %(db)s ===" % env
        local("mysql --host=%(mysql_host)s --user=%(mysql_root_user)s --password=%(mysql_root_pass)s --socket=%(mysql_socket)s --port=%(mysql_port)s %(db)s < %(ink_path)s/%(project)s/%(db_file)s" % env)

        print "\nLoaded %(ink_path)s/%(project)s/%(db_file)s into %(db)s/" % env
    else:
        abort("project '%s' does not exist!" % project)


def save(project=False, db=False):
    if(not project):
        fetch_project("dump from")
    else:
        env.project = project

    if(not db):
        fetch_db("dump")
    else:
        env.db = db

    env.sql_filename = "%s_%s.sql" % (env.db, datetime.datetime.now().strftime(env.dt_format))

    local("mysqldump --host=%(mysql_host)s --user=%(mysql_root_user)s --password=%(mysql_root_pass)s --socket=%(mysql_socket)s --port=%(mysql_port)s --lock-all-tables %(db)s > %(ink_path)s/%(project)s/%(sql_filename)s" % env)

    print "\nDumped %(sql_filename)s into %(ink_path)s/%(project)s/ from %(db)s" % env


def exists(p=''):
    projectList = os.listdir("%s/" % (env.ink_path))
    return any((True for x in [p] if x in projectList))


def sorted_ls(path):
    mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
    return list(sorted(os.listdir(path), key=mtime))


def fetch_project(action="import from"):
    ls()
    env.project = prompt("Which project would you like to %s?" % action)


def fetch_db(action="replace"):
    lsdb()
    env.db = prompt("Which database would you like to %s? (database must exist)" % action)
