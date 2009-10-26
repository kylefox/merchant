import re
from merchant.billing.credit_card_validator import CreditCardValidator
from merchant.billing.expiry_date import ExpiryDate

class CreditCard(object):
    
    CARD_COMPANIES = {
        'visa': r'^4\d{12}(\d{3})?$',
        'master': r'^(5[1-5]\d{4}|677189)\d{10}$',
    }

    def __init__(self, number, month, year, first_name, last_name):
      self.number = re.sub('[^\d]', '', str(number))
      self.expiry_date = ExpiryDate(month, year)
      self.first_name = first_name
      self.last_name = last_name
      self.validator = CreditCardValidator(self)
     
    @classmethod
    def type(cls, number):
        "Returns a string indicating the issuing company of the `number`."
        for name, cc_re in cls.CARD_COMPANIES.items():
            if re.compile(cc_re).match(number):
                return name
        return 'unknown'

    def is_expired(self):
        "Returns True/False indicating if this card has expired."
        return self.expiry_date.is_expired()
    
    def validate(self):
        return len(self.errors) == 0
        
    @property
    def errors(self):
        self.validator.validate()
        return self.validator.errors
