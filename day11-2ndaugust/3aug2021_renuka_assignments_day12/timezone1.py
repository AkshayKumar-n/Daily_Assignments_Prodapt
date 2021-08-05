import pytz
from datetime import datetime                    #for indian timezone just import time
standard_time=pytz.utc
time_zone=pytz.timezone("Asia/Kolkata")
time_zone1=pytz.timezone("America/Mexico_city")
time_zone2=pytz.timezone("Africa/Harare")
print(datetime.now(standard_time))
print(datetime.now(time_zone).strftime("%Y:%m:%d-%H:%M:%S"))
print(datetime.now(time_zone1).strftime("%Y:%m:%d-%H:%M:%S"))
print(datetime.now(time_zone2).strftime("%Y:%m:%d-%H:%M:%S"))#timeint module displays time taken by the each line in programm
