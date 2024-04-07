# Program weekday.py
# This program reads in the day that is today
# and outputs whether or not is a weekday.
# Author: Filipe Carvalho

#import datetime
from datetime import datetime

# get current datetime
day_time = datetime.now()
# print('Datetime is: ', dt) - This was used to test the imported function.

# define the days of the weekend
# the group of weekend is easier 
# to define as there are just two days
weekend = ('Saturday','Sunday')

# use if to confirm if today's day is a weekend
if day_time.strftime('%A') in weekend:
   # print message that's a weekend.
   print('It is the weekend, yay!')
# else is used in case the previous check is not true,
# which the day then would be a weekday.
else:
   # print message that's a weekday.
   print ('Yes, unfortunately today is a weekday.')

# End of the program