from alarm_clock import AlarmClock


my_alarm_clock = AlarmClock(12, 6, True)

print(my_alarm_clock.current_time)
print(my_alarm_clock.alarm_set_to)
print(my_alarm_clock.alarm_on)

my_alarm_clock.change_current_time(11)
print(my_alarm_clock.current_time)

my_alarm_clock.toggle_alarm_on_or_off("off")
print(my_alarm_clock.alarm_on)

my_alarm_clock.set_alarm_time(8)
print(my_alarm_clock.alarm_set_to)