import calendar
import datetime

class ExpiryDate(object):
    
    def __init__(self, month=None, year=None):
        self.month = int(month)
        self.year = int(year)
        
    def expiration(self):
        return datetime.datetime(self.year, self.month, calendar.monthrange(self.year, self.month)[1], 23, 59, 59, 59)
        
    def is_expired(self):
        return datetime.datetime.now() > self.expiration()