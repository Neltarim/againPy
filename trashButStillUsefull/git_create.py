#!/bin/python3
# coding:Utf-8

import os
import sys


def git_config(name_dir):
    config_path = name_dir + "-config.sh"
    touch = "touch " + config_path
    get_key = "cat ~/.ssh/id_rsa.pub"

    os.system(touch)
    with open(config_path, "w") as config_file:
        config_file.write("touch README.md\n")
        config_file.write("git init\n")
        config_file.write("git add README.md\n")
        config_file.write("git commit -m \"first commit\"\n")
        config_file.write("git remote add -f origin git@github.com:Neltarim/{}.git\n".format(name_dir))
        config_file.write("curl -u Neltarim:MDP https://api.github.com/user/repos -d \'{\"name\":\"" + name_dir + "\"}\'\n")
        config_file.write("eval $(ssh-agent -s)\n")
        config_file.write("ssh-keygen -t rsa -b 4096 -C \"kyurann@gmail.com\"\n")
        config_file.write("ssh-add ~/.ssh/id_rsa\n")
        
        key = open("~/.ssh/id_rsa.pub").readline()
        key.rstrip('\n')
        os.system(get_key)
        config_file.write("curl -u Neltarim:MDP https://api.github.com/user/keys -d \'{\"title\":\"LAPTOP-UBUNTU\", \"key\":\"" + key + "\"}\'")
        config_file.write("git push -u origin master")

def git_init(name_dir):
    path = "./" + name_dir + "-config.sh"
    os.chmod(path, 0o111) #RWE usr
    os.system(path)