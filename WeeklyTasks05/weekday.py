# This program reads in the day that is today
# and outputs whether or not is a weekday.
# Author: Filipe Carvalho
# Website used: https://pynative.com/python-get-the-day-of-week/#h-get-the-weekday-name-of-a-date-using-strftime-method

#import datetime
from datetime import datetime

# get current datetime
dt = datetime.now()
# print('Datetime is: ', dt)

#get weekday name
# print ('Day of the week is:', dt.strftime('%A'))

# separate the days of the week 
weekend = ['Saturday','Sunday']

# use if and else to confirm if it is weekend or weekday.
if dt.strftime('%A') in weekend:
   print('It is the weekend, yay!')
else:
   print ('Yes, unfortunately today is a weekday.')
