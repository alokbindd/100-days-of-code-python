from plyer import notification
import time

title = "Healthwala"
message = str(input("What should i remind of you?\n:"))
img = "D:/Python-lang/94-Day-94-Exercise-11/h.ico"
local_time = float(input("For how many minutes?\n:"))
local_time = local_time * 60

for i in range(6):
    notification.notify(title= title,message= message,app_icon = img ,timeout= 15,toast= False)
    time.sleep(local_time)