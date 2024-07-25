import os
import time

date = time.strftime("%d-%m")

def menu():	
    print("")
    print("Opciones:")
    #add times
    print("     1.-Add times")
    #load times from file
    print("     2.-Api")
    #exit
    print("     3.-Exit")



def salute():

    if os.path.exists("times"):
        return
    
    print("Hello user this program is going to help you to manage your time")
    print ("Funiconality:")
    print ("     press 1 or enter to add times")
    print ("     press 2  IN DEVELOPMENT")

    print("")
    input("Press enter to continue")
    os.system('cls' if os.name == 'nt' else 'clear')

