# Program to create a timer.
import time


my_time = int(input("Enter the time in seconds: "))

for i in range(my_time, 0, -1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hour = int(i / 3600) # dont add % 24 as we dont have days
    print(f"{hour:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time up!!")

