# Using if/elif for conditional statements, the user is prompted to input the times (in minutes) they took for all three activities in the triathlon (their variables 'time_swimming', 'time_cycling' and 'time_running).
# Next, we find total time to complete these activities (variable 'time_triathlon') by adding the three times that are inputted.
# Now, we use the print function to display the total time taken in the triathlon and related message for that total time, dependent on the time range it falls within.
time_swimming = int(input("Please enter your swimming time : "))
time_cycling = int(input("Please enter your cycling time : "))
time_running = int(input("Please enter your running time : "))

time_triathlon = time_swimming + time_cycling + time_running
print(f"The total time taken for all three activities is {time_triathlon} minutes.") ,

if time_triathlon >= 0 and time_triathlon <=100:
    print("You're within the qualifying criteria and achieved the Provincial Colours award.")
elif time_triathlon >= 101 and time_triathlon <= 105:
    print("You're within 5 minutes of the qualifying criteria and achieved the Provincial Half Colours award.")
elif time_triathlon >= 106 and time_triathlon <= 110:
    print("You're within 10 minutes of the qualifying criteria and achieved the Provincial Scroll award.")
else:
    print("You're more than 10 minutes off from the qualifying criteria and achieved no award.")