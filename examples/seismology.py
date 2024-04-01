import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(r"C:/Users/carla/Repos/goph420-w2024-lab03-stCA/examples/M_data.txt") #Loading Data from .txt

time = data[:,0] # First column of data (time [hours])
magnitude = data[:,1] # Second column of data (magnitude)


for day in range(1, 6): # Loop from day 1 to day 5
    day_time = time[(time >= (day-1)*24) & (time < day*24)]
    day_magnitude = magnitude[(time >= (day-1)*24) & (time < day*24)]
    
    plt.figure(figsize=(10, 6)) # Create a new figure for each day
    plt.plot(day_time, day_magnitude, 'g.') # Plot magnitude against time
    plt.title(f'Day {day}: Magnitude vs Time') # Set the title for each plot
    plt.xlabel('Time (hours)') # Label the x-axis
    plt.ylabel('Magnitude') # Label the y-axis
    plt.grid(True) # Add a grid for better readability
    plt.savefig (f'figures/magnitude_days{day}.png')
    
