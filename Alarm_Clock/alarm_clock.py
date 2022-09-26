class AlarmClock:

    def __init__(self, current_time, alarm_set_to, is_alarm_on):
        self.current_time = current_time
        self.alarm_set_to = alarm_set_to
        self.alarm_on = is_alarm_on

    def change_current_time(self, change_current_time):
        self.current_time = change_current_time
    

    def toggle_alarm_on_or_off(self, toggle_alarm_on):
        self.alarm_on = toggle_alarm_on
        
             
    def set_alarm_time(self, set_alarm_time):
        self.alarm_set_to = set_alarm_time
        