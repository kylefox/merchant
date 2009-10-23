import unittest
import re
from merchant.billing.credit_card import CreditCard

class TestCreditCard(unittest.TestCase):
    
    def testValidMastercard(self):
        "Ensures `CreditCard.type` returns `'master'` for valid Mastercard numbers."
        nums = ['6771890000000000', '5413031000000000']
        for num in nums:
            self.assertEqual(CreditCard.type(num), 'master')

    def testValidVisa(self):
        "Ensures `CreditCard.type` returns `'visa'` for valid Visa numbers."
        nums = ['4175001000000000',]
        for num in nums:
            self.assertEqual(CreditCard.type(num), 'visa')

if __name__ == "__main__":
    unittest.main()