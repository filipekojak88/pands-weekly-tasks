# weekday.py
# This program determines whether today is a weekday or weekend based on the current date.
# Author: Filipe Carvalho

# Import the datetime module from datetime library
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Define the days that constitute the weekend (Saturday and Sunday)
weekend_days = ('Saturday', 'Sunday')

# Check if today's day name (full name) is in the weekend_days tuple
if current_datetime.strftime('%A') in weekend_days:
    # Print a message indicating it's the weekend
    print('It is the weekend, yay!')
else:
    # Print a message indicating it's a weekday
    print('Yes, unfortunately today is a weekday.')

# End of the program