#!/usr/bin/python3
from fabric import task, local
@task
def host_type():
    local('echo Hello!')
