import os
from time_manage import *
from api_parser import *
from various import *


def main():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    salute()
    
    while True:

        progres_bar()
        
        menu()
        
        option = input("Option: ")

        if option == "1" or option == "":
            imput_time()

        elif option == "2":
            print("Coming soon")

        elif option == "3":
            break
        else:
            print("Invalid option")
            
        #Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')


main()