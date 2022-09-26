from alarm_clock import AlarmClock


my_alarm_clock = AlarmClock(1200, 600, True)

print(my_alarm_clock.current_time)
print(my_alarm_clock.alarm_set_to)
print(my_alarm_clock.alarm_on)

my_alarm_clock.change_current_time(1000)
print(f"The current time is now: {my_alarm_clock.current_time}")

if my_alarm_clock.alarm_on == True:
    print("Alarm is set!")
else:
    print("Alarm not set")

my_alarm_clock.set_alarm_time(630)
print(f"The new alarm is set to: {my_alarm_clock.alarm_set_to}")