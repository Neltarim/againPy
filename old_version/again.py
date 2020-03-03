#!/bin/python3
# coding:Utf-8

##################################################################
#                                                                #
#       Bienvenue dans againPy 1.2.                              #
#   Ce petit programme permet de creer un nouveau projet python, #
#   Son repertoire git ainsi que les fichiers de base et un      #
#   environnement virtuel.                                       #
#                                                                #
#   Il ne fonctionne en revanche qu'avec oh-my-zsh et hub.       #
#                                                                #
##################################################################

import os
import sys

from mk import *


def new_dir(name_dir): #cree un nouveau dossier
    os.mkdir(name_dir)
    os.chdir(name_dir)

def rm_all(path): #supprime totalement le dossier cree
    rm_command = "sudo rm -rf " + path
    os.chdir("../")
    os.system(rm_command)

def git_init(name_dir): #github.com/github/hub
    os.system("hub init")
    os.system("hub create")


def main():
    name_usr = os.getlogin() #recupere le login du user
    print("[again]Hi {}, here we go again.".format(name_usr))
    name_dir = input("[again]please enter the name of directory : ")
    mode = input("[again]Do you want a NORMAL py project or a EMPTY directory? : ")
    path = "./" + name_dir #on ajoute ./ ppar securite sur le chemin d'acces

    print("[again]Creating the git directory ...")

    try:
        new_dir(path)
    except:
        print("[again]Can't create a new directory.")
        rm_all(path)
        sys.exit(0)

    print("[again]New directory created.\nCreating the repository ...")

    try:
        git_init(name_dir)
    except:
        print("[again]an error has occured in the init of git repository.")
        sys.exit(0)
    print("[again]Repo git created.")

    if mode == "EMPTY" or "empty":
        print("[again]Have a nice coding day and don't forget to push.")
        sys.exit(0)
        

    name_py = input("[again]chose a name for your first .py file : ")
    yesno_env = input("[again]Do you want a virtual env? (YES/no) : ")

    try:
        mk_py(name_py) #se referer a mk.py

        if yesno_env == "yes" or "YES":
            mk_env() #idem
    except:
        print("[again]an error has occured when creating files.")
        rm_all(path)
        sys.exit(0)


    path_py = name_py + ".py"
    print("[again]" + path_py + " file created successfuly.")
    print("[again]{}.py created successfully.")
    print("[again]Don't forget to push and have a nice coding day.".format(name_dir))
    os.system("code .") #ouvre visual code sur ce dossier

if __name__ == '__main__':
    main()