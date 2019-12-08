# encoding: utf-8
"""Interchange program
This program will recive the names of the particpants that want to be on the interchange and will asociate each participant with another completly random
Methods
-------
restart()
    If the program gets to the point where the last participant haves only aviliable his name to give present the program will restart

get_results()
    It will give the result from the interchange making sure that no participant gets himself

ask_names()
    It will ask the user his name and then the program will print for only 5 seconds who the entered name must give present to, it will only show the result one time

start()
    It will ask for the participants names and then  call the get_results() and ask_results() methods

"""
from random import randint
import os
import time

def restart(participants):
    """Restarts the whole process
        Parameters
        ----------
        participants : list
            The participants in the interchange
        Returns
        -------
        dictionary
            The results for the interchange
     """
    return get_results(participants)

def get_results(participants):
    """Create the results for the interchange
        Parameters
        ----------
        participants : list
            The participants in the interchange
        Returns
        -------
        diccionary
            The results for the interchange
    """
    results = {}
    options = participants.copy()
    for name in participants:
        length = len(options)
        i = randint(0,length-1)
        lucky_one = options[i]
        while(name == lucky_one):
            if(length == 1):
                restart(participants)
                return;
            i = randint(0,length-1)
            lucky_one = options[i]
        results[name] = lucky_one
        options.remove(lucky_one)
    return results

def ask_names(participants, results):
    """Ask the names of the partcipants
        Parameters
        ----------
        participants : list
            The participants in the interchange
        results : dictionary 
            The results from the interchange
    """
    while(results):
        name = input("¿Who are you?\n")
        while(name not in participants):
            print("Im sorry, there is no participant with that name")
            name = input("¿Who are you?\n")    
        while(name not in results):
            print("¡Hey cheater!, this name has already been asked")
            name = input("¿Who are you?\n")
        result = results[name]    
        print("You give present to {}".format(result))
        time.sleep(5)
        os.system("clear")
        results.pop(name)

def start():
    """Starts the program
    """
    participants = input("¡Hello!, please tell me the names of the people who are in the interchange, each name separated by a coma \n")
    participants = participants.split(",")
    if (len(participants) == 1):
        print("You must give more than 1 name")
        start()
    results = get_results(participants)
    ask_names(participants, results)
        
if __name__ == "__main__":
    start()