import os
import time
from time_manage import *
from api_parser import *
from various import *


def main():
 
    while True:
        progress_bar()
        menu()
        option = input("Option: ")

        if option == "1":
            imput_time()

        elif option == "2":
            #load_times()
            print("Coming soon")
        elif option == "3":
            break
        else:
            print("Invalid option")
        #Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')


main()