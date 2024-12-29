import time
import winsound
freq=1000
dur=2000
text = str(input("What should i remmind you of?\n:"))
local_time = float(input("In how many minutes?\n:"))
local_time = local_time * 60

for i in range(6):
    time.sleep(local_time)
    print(text)
    # print('Beep\a')
    winsound.Beep(freq,dur)