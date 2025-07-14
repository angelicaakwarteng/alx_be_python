# Personal Daily Reminder
task = str(input("Enter a task: "))
priority = str(input("Enter task priority (high, medium, low): "))
time_bound = str(input("Is it time-bound, (yes or no): "))

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: 'Finish {task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print("Reminder: This is a {priority} priority task.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: 'Don't forget the deadline'. This is a {priority} priority task that requires attention!")
        else:
            print("Reminder: This is a {priority} priority task.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: This is a {priority} priority task but it is time-bound.")
        else:
            print("'Read a book' is a low priority task. Consider completing it when you have free time.")