import numpy as np
import matplotlib.pyplot as plt
from goph420_lab03.regression import multi_regress

data = np.loadtxt(r"C:/Users/carla/Repos/goph420-w2024-lab03-stCA/examples/M_data.txt") #Loading Data from .txt

time = data[:,0] # First column of data (time [hours])
magnitude = data[:,1] # Second column of data (magnitude)

plt.figure(figsize=(10, 6)) 
plt.plot(time, magnitude, '.') # Plot magnitude against time
plt.title('Magnitude vs Time') # Set the title for the plot
plt.xlabel('Time (hours)') # Label the x-axis
plt.ylabel('Magnitude') # Label the y-axis
plt.grid(True) # Add a grid for better readability
plt.savefig ('figures/magnitude_time.png')

day_times = []
day_magnitudes = []
for day in range(1, 6): # Loop from day 1 to day 5
    day_time = time[(time >= (day-1)*24) & (time < day*24)]
    day_magnitude = magnitude[(time >= (day-1)*24) & (time < day*24)]
    day_times.append(day_time)
    day_magnitudes.append(day_magnitude)

    plt.figure(figsize=(10, 6)) # Create a new figure for each day
    plt.plot(day_time, day_magnitude, '.') # Plot magnitude against time
    plt.title(f'Day {day}: Magnitude vs Time') # Set the title for each plot
    plt.xlabel('Time (hours)') # Label the x-axis
    plt.ylabel('Magnitude') # Label the y-axis
    plt.grid(True) # Add a grid for better readability
    plt.savefig (f'figures/magnitude_days{day}.png')

for m, (dt, dm) in enumerate (zip(day_times, day_magnitudes)):
    # Extracting values from day_times[0] between 10 to 22 hours and their respective day_magnitudes
    filtered_times_0 = [dt for dt in day_times[0] if 10 <= dt < 22]
    filtered_magnitudes_0 = [dm for dt, dm in zip(day_times[0], day_magnitudes[0]) if 10 <= dt < 22]

    # Extracting values from day_times[1] between 25 to 35 hours and their respective day_magnitudes
    filtered_times_1 = [dt for dt in day_times[1] if 25 <= dt < 35]
    filtered_magnitudes_1 = [dm for dt, dm in zip(day_times[1], day_magnitudes[1]) if 25 <= dt < 30]

    # Extracting values from day_times[2] between 50 to 55 hours and their respective day_magnitudes
    filtered_times_2 = [dt for dt in day_times[2] if 50 <= dt < 55]
    filtered_magnitudes_2 = [dm for dt, dm in zip(day_times[2], day_magnitudes[2]) if 50 <= dt < 55]

    # Extracting values from day_times[3] between 80 to 88 hours and their respective day_magnitudes
    filtered_times_3 = [dt for dt in day_times[3] if 80 <= dt < 88]
    filtered_magnitudes_3 = [dm for dt, dm in zip(day_times[3], day_magnitudes[3]) if 80 <= dt < 88]

    # Extracting values from day_times[4] between 98 to 105 hours and their respective day_magnitudes
    filtered_times_4 = [dt for dt in day_times[4] if 98 <= dt < 105]
    filtered_magnitudes_4 = [dm for dt, dm in zip(day_times[4], day_magnitudes[4]) if 98 <= dt < 105]

# List of filtered times lists
filtered_times = [filtered_times_0, filtered_times_1, filtered_times_2, filtered_times_3, filtered_times_4]

# List of filtered magnitudes lists
filtered_magnitudes = [filtered_magnitudes_0, filtered_magnitudes_1, filtered_magnitudes_2, filtered_magnitudes_3, filtered_magnitudes_4]

dif_mang = np.arange(-0.6, 0.4, 0.1)
values_times = []
values_magnitudes = []

for m, (vt, vm) in enumerate(zip(filtered_times, filtered_magnitudes)): 
    for mag in dif_mang: 
        values_magnitudes.append([m for m in vm if m > mag]) 
        values_times.append([t for t, m in zip(vt, vm) if m > mag])

N = []

for i, (times, magnitudes) in enumerate(zip(values_times, values_magnitudes)):
    count_times = len(times)
    count_magnitudes = len(magnitudes)
    if i % len(dif_mang) == 0:
        N.append([])
    N[-1].append(count_times)

print (N)

for i in range(len(N)):
    plt.figure(figsize=(10, 6))
    plt.plot(dif_mang, N[i], '.') # Plot magnitude against time
    plt.title(f'Day {i+1}: Magnitude vs Number of Events') 
    plt.xlabel('Magnitudes') 
    plt.ylabel('Number of Events') 
    plt.grid(True) 
    plt.savefig (f'figures/MvsN_days{i}.png')

for i in range(len(N)):
    plt.figure(figsize=(10, 6))
    plt.semilogy(dif_mang, N[i], '.') # Plot magnitude against time
    plt.title(f'Day {i+1}: Magnitude vs Number of Events') 
    plt.xlabel('Magnitudes') 
    plt.ylabel('Number of Events') 
    plt.grid(True) 
    plt.savefig (f'figures/Logscale_MvsN_days{i}.png')
    
log_N = np.log10(N)

coeficients = []
residuals_list = [] 
r2 = []

for i in range(len(log_N)):
    coeffs, residuals_i, r2_i = multi_regress(log_N[i], (-dif_mang)) 
    coeficients.append(coeffs)
    residuals_list.append(residuals_i) 
    r2.append(r2_i)
    
# print (f'Coefficients: {coeficients}')
# print (f'Residuals: {residuals_list}') 
# print (f'R2: {r2}')


prediction = []
for i in range(len(log_N)):
    a = coeficients[i][0]
    b = coeficients[i][1] 
    model =  10 ** (a - b * dif_mang)
    prediction.append(model)
    
for i in range(len(N)):
    plt.figure(figsize=(10, 6))
    plt.semilogy(dif_mang, prediction[i], 'r-', label = f'Predicted values: Coefficients: a = {coeficients[i][0]:.3f}, b = {coeficients[i][1]:.3f}, $r^2$ = {r2[i]:.3f}') # Plot magnitude against number of events 
    plt.semilogy(dif_mang, N[i], '.', label = 'Measured values ')
    # plt.semilogy(dif_mang, residuals_list[i], 'r.', label='Residuals')
    plt.title(f'Day {i+1}: Magnitude vs Number of Events') 
    plt.xlabel('Magnitudes') 
    plt.ylabel('Number of Events') 
    plt.legend()
    plt.grid(True) 
    plt.savefig (f'figures/Prediction_MvsN_days{i}.png')
