import os

from lib.agn import *
from lib.const import *


class Manager():
    
    def __init__(self):
        self.loop = True


###################### LST ##################################################

    def new_pr(self):
        agn = Agn()
        agn.set_name()
        os.mkdir(agn.get_name)
        os.chdir(agn.get_name)
        os.mkdir(".agn")
        agn.set_type()
        agn.make()
        
        agn.save_config()
        
    def get_lst(self):

        ls = {}

        with open(PR_LIST_PATH, "rb") as file:
            rick = pickle.Unpickler(file)

            ls = rick.load()

        return ls

    def print_lst(self):
        
        ls = self.get_lst()

        prompt("Your projects list :\n")

        for key in ls:
            print(key)

    def pick_pr(self):

        choice = input(USR)

        ls = self.get_lst()
        path = "~/Documents/" + ls[choice]

        os.chdir(path)

###################### MAIN FUNCTION ###################################

    def run_project(self):
        
        agn = Agn()
        agn.import_config()
#in progress



    def start(self):
        
        prompt("Hi {}, here we go again.".format(USR_NAME))
        
        if os.path.exists(r'.agn') == False:
            prompt("You are not currently in a project. Do you want to make a new one ?")
            
            if yesno() == True:
                self.new_pr()

            else:
                prompt("Choose a project to open :")
                self.get_lst()
                self.pick_pr()

        self.run_project()
                



if __name__ == "__main__":
    mgr = Manager()
    mgr.start()