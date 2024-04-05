#!/usr/bin/python3
from fabric import *
def host_type():
    run('uname -s')
