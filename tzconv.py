import pytz
from datetime import datetime

timezones = pytz.all_timezones

# list of time zones
for timezone in timezones:
    print(timezone)

tz=input('Enter current timezone')
t=input('Enter target timezone')
c_tz = pytz.timezone(tz)
t_tz = pytz.timezone(t)

# Get the current time in the local timezone
timeNow = datetime.now(c_tz)
print(f'Local time: {timeNow}')

# Convert the local time to the target timezone
tz_time = timeNow.astimezone(t_tz)
print(f'Target time: {tz_time}')

