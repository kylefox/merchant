import re
from merchant.billing.credit_card_validator import CreditCardValidator

class CreditCard(object):
    
    CARD_COMPANIES = {
        'visa': r'^4\d{12}(\d{3})?$',
        'master': r'^(5[1-5]\d{4}|677189)\d{10}$',
    }

    def __init__(self, number, month, year, first_name, last_name):
      self.number = re.sub('[^\d]', '', str(number))
      self.month = int(month)
      self.year = int(year)
      self.first_name = first_name
      self.last_name = last_name
      self.validator = CreditCardValidator(self)
     
    @classmethod
    def type(cls, number):
        """
        Returns a string indicating the issuing company of the `number`.
        """
        for name, cc_re in cls.CARD_COMPANIES.items():
            if re.compile(cc_re).match(number):
                return name
        return 'unknown'
        
    # def type(self):
    #     return CreditCard.type(self.number)