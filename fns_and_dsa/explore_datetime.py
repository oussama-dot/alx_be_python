import datetime 

def display_current_datetime():
   global current_dateTime
   current_dateTime = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
   print("current date :",current_dateTime)
display_current_datetime()


def calculate_future_date():
    number_of_days = int(input("enter a number of days"))
    current_dateTime = datetime.datetime.now()
    future_days = datetime.timedelta(number_of_days) +  current_dateTime
    formatted_date = future_days.strftime("%Y %m %d")
    print(formatted_date)
    

calculate_future_date()