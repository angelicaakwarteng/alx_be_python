from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future Date after", days, "days:", formatted_future_date)

# Calling the functions
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
