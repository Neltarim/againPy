#!/bin/python3
#coding:Utf-8

import os
import sys

def mk_py(name_py): #ecrit le fichier basique .py
    path = name_py + ".py"
    os.system("touch " + path)

    with open(path, 'w') as f:
        f.write("#!/bin/python3\n")
        f.write("#coding:Utf-8\n")
        f.write("\n\n\n")
        f.write("def main():\n")
        f.write("   pass")
        f.write("\n\n\n")
        f.write("if __name__ == \"__main__\":\n")
        f.write("   main()\n")
        f.write("elif:\n")
        f.write("   print(\"Importation of " + name_py + " succeed.\"")

def env_ignore(): #ecrit le .gitignore
    path = ".gitignore"

    with open(path, 'w') as f:
        f.write("env/\n")
        f.write("__pycache__\n")
        f.write(".vscode/")

def mk_env(): #cree l'environnement virtuel 
    os.system("virtualenv -p python3 env")
    print("[again]virtual environnement created.")
    #os.system("source env/bin/activate") <= not working yet (source not found)
    os.system("touch requirements.txt")
    os.system("touch .gitignore")
    env_ignore()
    print("[again].gitignore file created.")