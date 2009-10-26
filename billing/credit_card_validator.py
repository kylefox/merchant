class CreditCardValidator(object):
 
    def __init__(self, credit_card):
        self.credit_card = credit_card
        
    def validate(self):
        self.errors = {}
        self._validate_number_length()
        return len(self.errors) == 0
        
    def _validate_number_length(self):
        if len(self.credit_card.number) < 12:
            self._add_error(error_message=u'too short', field_name='number')
            return False
        return True
            
    def _add_error(self, error_message, field_name=None):
        if field_name is None:
            field_name = '_global'
        self.errors[field_name] = self.errors.get(field_name, [])
        self.errors[field_name].append(error_message)