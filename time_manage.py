import time
import os



def imput_time():
    
    # Get the start time
    start_time = time.time()

    # Get Client name
    client_name  = input("Client: ")
    
    # Get description of the task
    task_description = input("Task: ")

    # Get the end time
    end_time = time.time()

    # Calculate the time taken
    time_taken = end_time - start_time

    #write the time taken to a file
    w_imput_time(client_name, task_description, time_taken, start_time, end_time)

    return time_taken



def w_imput_time(client_name, task_description, time_taken, start_time, end_time):
    # Check if the file exists in the times folder
    if not os.path.exists("times"):
        os.mkdir("times")

    # Create a file with the current date in the times folder
    date = time.strftime("%Y-%m-%d")
    file_name = "times_" + date + ".txt"

    if os.path.exists("times/" + file_name):
        # Open the file in append mode
        file = open("times/" + file_name, "a")
    else:
        # Open the file in write mode
        file = open("times/" + file_name, "w")

    # Write the time taken to the file
    file.write("S_Hour: " + time.strftime("%H:%M:%S", time.localtime(start_time)) + "\n")
    file.write("E_Hour: " + time.strftime("%H:%M:%S", time.localtime(end_time)) + "\n")
    #Tiempo total en formato HH:MM:SS
    file.write("Total time: " + time.strftime("%H:%M:%S", time.gmtime(time_taken)) + "\n")
    file.write("Client: " + client_name + "\n")
    file.write("Task: " + task_description + "\n")
    file.write("\n")

    # Close the file
    file.close()


def progres_bar():
    
    Hours = 7
    block = "█"
    color_code = 32
    #Check if the file exists in the times folder
    if not os.path.exists("times") or not os.path.exists("times/times_" + time.strftime("%Y-%m-%d") + ".txt"):
        print(">-||", end="")
        for i in range(Hours * 4):
            print("█", end="")
        print("||-<", end="")

    else:
        #Open the file in read mode
        file = open("times/times_" + time.strftime("%Y-%m-%d") + ".txt", "r")
        #Read the file
        lines = file.readlines()

        #Get the total time worked from the Total time line
        total_time = 0
        for line in lines:
            if "Total time" in line:
                total_time = total_time + int(line.split(": ")[1].split(":")[0])*3600 + int(line.split(": ")[1].split(":")[1])*60 + int(line.split(": ")[1].split(":")[2])

        #Close the file
        file.close()

        #Print the progress bar with the total time worked

        # Complete Day 
        if total_time > Hours * 3600:
            color_code = 33

        print(">|", end="")
        #Green part
        for i in range(total_time//900):
            print(f"\033[{color_code}m{block}\033[0m", end="")
        
        #white part
        for i in range((Hours*4)-(total_time//900)):
            print("█", end="")
        print("|<", end="")
