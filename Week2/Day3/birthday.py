""" Exercise 6 : Birthday and minutes
Instructions

    Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.
 """
import datetime

def time_alive(d,m,y, hour = 0, minute = 0):
    if hour<10:
        hour = f"0{hour}"
    if minute<10:
        minute =f"0{minute}"    
    time_al = datetime.datetime.now()-datetime.datetime.fromisoformat(f'{y}-{m}-{d} {hour}:{minute}:00.000')
    days = time_al.days
    hours, remainder = divmod(time_al.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"Time alive from {d}/{m}/{y} is {days} days, {hours} hours, and {minutes} minutes")
    print(f"In minutes, that is {days*1440 + hours*60 + minutes} minutes.")

time_alive(28,11,1996, 7, 30)