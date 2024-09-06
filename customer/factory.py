import factory
from .models import Province, City, Customer
import django_jalali.db.models as jmodels
from faker import Faker
from jdatetime import date as jdate

fake = Faker('fa_IR')  # Use Persian locale

class ProvinceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Province

    name = factory.Faker('city')  # You can use a different provider for more realistic province names

class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City

    name = factory.Faker('city')
    province = factory.SubFactory(ProvinceFactory)
    latitude = factory.LazyAttribute(lambda _: fake.latitude())
    longitude = factory.LazyAttribute(lambda _: fake.longitude())

class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    name = factory.Faker('name')
    corporate_date = factory.LazyFunction(lambda: jdate.today())
    program_name = factory.Faker('word')
    province = factory.SubFactory(ProvinceFactory)
    city = factory.SubFactory(CityFactory)
