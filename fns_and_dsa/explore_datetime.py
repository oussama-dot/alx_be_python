from datetime import datetime, timedelta

def display_current_datetime():
   global current_dateTime
   current_dateTime = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
   print("Current date and time:",current_dateTime)
display_current_datetime()


def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date:"))
    current_dateTime = datetime.now()
    future_days = timedelta(number_of_days) +  current_dateTime
    formatted_date = future_days.strftime("%Y %m %d")
    print("Future date:",formatted_date)
    

calculate_future_date()