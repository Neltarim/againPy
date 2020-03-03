from os import getlogin

########################## GLOBAL CONST #######################################

USR_NAME = getlogin()
PYAGN_PATH = "/home/{}/Documents/PyAgain/manager".format(USR_NAME)
PR_LIST_PATH = PYAGN_PATH + ".pr_list"
LOOP = True

PROMPT = "[PyAgain] "
USR  = ("<{}>".format(USR_NAME))


YES = ["yes", "Yes", "YES", "y", "Y", "yep"]
NO = ["no", "No", "NO", "n", "N", "nope"]

PR_TYPE = ["DJANGO", "AI", "SYSTEM"]

DOC_PATH = "/home/" + USR_NAME + "/Documents/"


######################## GLOBAL FUNCTIONS ####################################

def prompt(string):

    print(PROMPT + string)

def yesno():

    while LOOP:

        answer = input(USR)

        for elm in YES:
            if elm == answer:
                return True

        for elm in NO:
            if elm == answer:
                return False

        prompt("ERROR: Unknown answer.")