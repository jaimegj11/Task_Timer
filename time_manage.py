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

