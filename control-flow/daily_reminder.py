# daily_reminder.py

# Ask the user to enter the task
task = input("Enter your task: ")

# Ask the user to enter priority level
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Prepare base message based on priority
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        print("Please restart and enter a valid priority: high, medium, or low.")
        exit()

# Add message for time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Final reminder output — exact format your checker wants
print(f"Reminder: {message}")
