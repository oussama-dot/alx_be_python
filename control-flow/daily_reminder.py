task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input('Is it time-bound? (yes/no)')

match priority :
    case "high" if time_bound == "yes":
        print(f" reminder : {task} is  a high priority task.that requires immediate attention today!")
    case "high" if time_bound == "no":
        print(f" reminder : {task} is  a high priority task.that requires immediate attention today!")   
    case 'medium':
        print(f" note : {task} is  a medium priority task")
    case 'low':
        print(f" note : {task} is  a low priority task")

