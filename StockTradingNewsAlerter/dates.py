import datetime

class Dates:
    
    # Setting default values.
    def __init__(self):
        self.today = datetime.date.today()
        self.last_business_day = None
        self.second_last_business_day = None
        self.fill_days()
    
    # Calculating dates of previous two business days, then storing them.
    def fill_days(self):
        subtract_time = max(1, (self.today.weekday() + 6) % 7 - 3)
        self.last_business_day = self.today - datetime.timedelta(subtract_time)
    
        subtract_time = max(1, (self.last_business_day.weekday() + 6) % 7 - 3)
        self.second_last_business_day = self.last_business_day - datetime.timedelta(subtract_time)
