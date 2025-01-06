import time,datetime
import schedule
from datetime import date
import random

def add(num1,num2):
    print(num1+num2)

#add job
# schedule.every(2).seconds.do(add,val1,val2)

while True:
    val1 = random.randint(0,9)
    val2 = random.randint(0,9)  
    d=date.today()
    day_of_week=d.isoweekday()

    if day_of_week not in [6,7]:
        add(val1,val2)
    #sleep for 1 second
    time.sleep(1)