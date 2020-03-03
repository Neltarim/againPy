import os
import pickle

from const import *


class Agn():

    def __init__(self):
        self.name = ""
        self.type = ""
        self.path = ""
        self.config_path = ""
        self.agn_path = ""
    

    ################ GET METHODS ######################

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_path(self):
        return self.path

    ################ SET METHODS ######################

    def set_name(self):
        prompt("Choose a name for your new project :")
        self.name = input(USR)

    def set_type(self):

        prompt("Please enter the type of project :")

        while LOOP:

            prType = input(USR)

            for elm in PR_TYPE:
                prType.upper()
                if prType == elm:
                    self.type = prType
                    return 0

            prompt("ERROR: this type of project is not currently available.")

    def set_path(self):

        self.path = DOC_PATH + self.name
        self.config_path = self.path + ".agn/"
        self.agn_path = self.config_path + "/config"

    ################# AGN MAKE ########################

    def virtualenv(self, make=False):
        prompt("Building virtual environnement ...")
        os.system("virtualenv -p python3 env")
        prompt("Virtual env created.")

        if make == False:

            os.system("source env/bin/activate")
            prompt("virtual env started.")

    def git_push(self, make=False):
        os.chdir(self.path)

        prompt("Initialising git repository...")
        os.system("hub init && hub create")
        os.system("git add *")

        if make == False:
            prompt("Commit :")
            com = input(USR)
            os.system("git commit -m \"{}\"".format(com))

        else:
            os.system("git commit -m \"commit by [PyAgain]\"")

        os.system("git push origin master")
        prompt("Pushed successfully.")

    
    def make_django(self):

        prompt("Name your web app :")
        app_name = input(USR)
        os.system("django-admin startproject" + app_name)


    def make(self):

        self.virtualenv()

        if self.type == "DJANGO":
            prompt("Project set up to Django.")
            self.make_django()

        elif self.type == "AI":
            prompt("project set up to AI.")
            pass####

        elif self.type == "SYSTEM":
            prompt("Project set up to System.")
            pass####

        else:
            prompt("ERROR: No such project type.")
            return 0

        self.git_push(first=True)
        os.mkdir(self.path + "test_zone")

    ################ SAVE && IMPORT ######################

    def save_config(self):

        os.chdir(self.agn_path)

        with open(self.config_path, "wb") as file:
            my_pickler = pickle.Pickler(file)

            my_pickler.dump(self.name)
            my_pickler.dump(self.type)

        prompt("Project saved successfuly.")
        os.chdir(self.path)

    def import_config(self):

        os.chdir(self.agn_path)

        with open(self.config_path, "rb") as file:
            my_unPickler = pickle.Unpickler(file)

            self.name = my_unPickler.load()
            self.type = my_unPickler.load()
            
            self.set_path()

        prompt("Project imported successfuly.")
        os.chdir(self.path)

    def add_pr(self):

        os.chdir(PYAGN_PATH)
        self.import_config()

        with open(PR_LIST_PATH, "rb") as file:
            my_unPickler = pickle.Unpickler(file)

            pr_list = my_unPickler.load()
            
        pr_list[self.name] = self.path

        with open(PR_LIST_PATH, "wb") as file:
            my_pickler = pickle.Pickler(file)

            my_pickler.dump(pr_list)

        prompt("Project added to your project list successfuly.")
        os.chdir(self.path)