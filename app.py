# Task 1: Welcome message
print("Welcome to my Python program!")

# Task 2: Ask the user for input
hours = input("How many hours did you study today? ")

# Task 5 (placed early so it wraps conversion + Task 3):
# Add basic error handling in case user enters non-numeric input
try:
    # Task 3: Convert input to a number
    hours = float(hours)
except ValueError:
    print("Please enter a valid number next time.")
    exit()

# Task 3 (continued): Perform calculation
weekly_hours = hours * 7

# Task 4: Display clear output
print(f"\nIf you keep this pace, you will study about {weekly_hours} hours this week!")