import time

date = time.strftime("%d-%m")

def menu():	
    print("Opciones:")
    #add times
    print("     1.-Add times")
    #load times from file
    print("     2.-Return to this " + date + " times")
    #exit
    print("     3.-Exit")

