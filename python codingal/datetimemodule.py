#Check the current date and time?

# from datetime import date,time,datetime

# today=date.today()
# now=datetime.now()

# print("Todays date is",today)
# print("\nCurrent date and time is",now)
# print("\nDate components",today.year,today.month,today.day)

import random
import time

def getrandomdate(startDate,endDate):
    print("Printing random date beetween",startDate,"and",endDate)
    randomgenerator=random.random()
    dateFormat='%m/%d/%Y'

    startTime=time.mktime(time.strptime(time.startDate,dateFormat))
    endTime=time.mktime(time.strptime(time.endDate,dateFormat))

    randomTime=startTime+randomgenerator*(endTime-startTime)
    randomDate=time.strftime(dateFormat,time.localtime(randomTime))
    return randomDate

print("Random Date=",getrandomdate("1/1/2016","12/12/2018"))