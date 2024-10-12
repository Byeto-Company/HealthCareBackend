from django.db import models
import django_jalali.db.models as jmodels


class Province(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="نام استان")

    class Meta:
        verbose_name = "استان"
        verbose_name_plural = "استان‌ها"

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام شهر")
    province = models.ForeignKey(Province, related_name='cities', on_delete=models.CASCADE, verbose_name="استان")
    latitude = models.CharField(max_length=20, verbose_name="عرض جغرافیایی")
    longitude = models.CharField(max_length=20, verbose_name="طول جغرافیایی")

    class Meta:
        unique_together = ('name', 'province')
        verbose_name = "شهر"
        verbose_name_plural = "شهرها"

    def __str__(self):
        return self.name


class Customer(models.Model):
    objects = jmodels.jManager()
    name = models.CharField(max_length=100, verbose_name="نام مشتری")
    corporate_date = jmodels.jDateField(verbose_name="تاریخ همکاری")
    program_name = models.CharField(max_length=100, verbose_name="نام برنامه")
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True, verbose_name="استان")
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name="شهر")

    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتریان"

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