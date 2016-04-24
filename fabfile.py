# - * - coding:utf-8 -*-

from fabric.api import local

# please use: fab pu:'discription'
def pu(discription):
    local("git ad")
    local("git ci -m '%s' " % discription)
    local("git pu")

def ci(discription):
    local("git ad")
    local("git ci -m '%s' " % discription)