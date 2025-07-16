task = input ("Enter your task: ")
Priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match Priority :
    case "high" : 
        message = f"Reminder: '{task}' is a high priority task"
    case "meduim":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case(_):
        message = f"'{task}' has an unknown priority level. Please check your input."
if time_bound =="yes":
    message += f" that requires immediate attention today!"
elif time_bound =="non":
    message+= f". Consider completing it when you have free time."
    
print (message)

