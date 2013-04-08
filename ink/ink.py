#! /usr/bin/env python

import os
import sys
import fabfile


def help():
    print "Usage: ink.py [command]"
    print "\nCommands:"
    print " list projects\t\t\tlists all projects"
    print " list db\t\t\tlists all databases for a project"
    print " save [db] to [project]\n\t\t\t\tdumps a local database and places it in the Nib project directory"
    print " update [db] from [project]\n\t\t\t\ttakes a Nib project database and loads it into the local database"

if __name__ == "__main__":

    context = {}
    context['path_to_fab'] = "%s/fabfile.py" % os.path.dirname(fabfile.__file__)

    command = False

    args = sys.argv
    # print args

    l = len(args) - 1

    if(l is 0 or l is 1):
        print "Error: not enough arguments"
        help()
    elif(l >= 2):
        if(args[1] in ['update', 'save']):
            command = "%s:db=%s,project=%s" % (args[1], args[2], [args[3], args[4]][l > 2])
        elif(args[1] in ['list']):
            if('db' in args):
                command = "lsdb"
            elif('projects' in args):
                command = "ls"
            else:
                print "Error: command not found"
                help()

    if (not command):
        print "Error: command not found"
        help()
    else:
        context['command'] = command
        # print context
        os.system('fab %(command)s -c ~/.fabricrc -f %(path_to_fab)s' % context)
