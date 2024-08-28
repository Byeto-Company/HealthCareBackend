from django.db import models
import django_jalali.db.models as jmodels
class Customer(models.Model):
    name = models.CharField(max_length=100)
    corporate_date = jmodels.jDateField()
    program_name = models.CharField(max_length=100)
    # addreess of the customer
    def __str__(self):
        return self.name
    
    def persian_corporate_date(self):
        return convert_to_persian_numbers(str(self.corporate_date))





def convert_to_persian_numbers(date_string):
    # Mapping of English digits to Persian digits
    english_to_persian = {
        '0': '۰',
        '1': '۱',
        '2': '۲',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹'
    }
    
    # Replace each English digit with its Persian equivalent
    persian_date_string = ''.join(english_to_persian.get(char, char) for char in date_string)
    
    return persian_date_string
