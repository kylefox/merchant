import unittest
import datetime
import calendar
from merchant.billing.expiry_date import ExpiryDate

class TestExpiryDate(unittest.TestCase):

    def testMonthAndYearAsInteger(self):
        "Integers are valid month/year parameters."
        expiry = ExpiryDate(month=10, year=2009)
        self.assertEqual(expiry.month, 10)
        self.assertEqual(expiry.year, 2009)
    
    def testMonthAndYearCastToIntegersFromStrings(self):
        "Strings are valid month/year parameters."
        expiry = ExpiryDate(month="10", year="2009")
        self.assertEqual(expiry.month, 10)
        self.assertEqual(expiry.year, 2009)
    
    def testCorrectExpirationDate(self):
        """
        Expiration date should equal to the last second
        of the last day of the month/year specified.
        """
        now = datetime.datetime.now()
        expiry = ExpiryDate(month=now.month, year=now.year)
        expected = datetime.datetime(
                    now.year, now.month, 
                    calendar.monthrange(now.year, now.month)[1],
                    23, 59, 59, 59)
        self.assertEqual(expiry.expiration(), expected)
    
    def testNotExpired(self):
        "Dates in the future should be expired."
        now = datetime.datetime.now()
        month = now.month
        year = now.year + 2
        expiry = ExpiryDate(month=month, year=year)
        self.assertFalse(expiry.is_expired())
    
    def testTodayNotExpired(self):
        "Today should not be expired."
        now = datetime.datetime.now()
        expiry = ExpiryDate(month=now.month, year=now.year)
        self.assertFalse(expiry.is_expired())

    def testExpired(self):
        "Dates in the past should be expired."
        now = datetime.datetime.now()
        month = now.month
        year = now.year - 2
        expiry = ExpiryDate(month=month, year=year)
        assert expiry.is_expired()
    
if __name__ == "__main__":
    unittest.main()