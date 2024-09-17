from django.db import models
from django.core.exceptions import ValidationError


class WorkTags(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")

    class Meta:
        verbose_name = "برچسب کاری"
        verbose_name_plural = "برچسب‌های کاری"

    def __str__(self):
        return self.title


class WorkField(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان حوزه")
    description = models.TextField(verbose_name="توضیحات حوزه")
    tags = models.ForeignKey(WorkTags, on_delete=models.CASCADE, verbose_name="برچسب‌ها")
    ordering = models.PositiveIntegerField(unique=True, verbose_name="ترتیب")
    class Meta:
        verbose_name = "حوزه کاری"
        verbose_name_plural = "حوزه‌های کاری"

    def save(self, *args, **kwargs):
        if self.pk is None and WorkField.objects.count() >= 3:
            raise ValidationError("حداکثر می‌توانید ۳ حوزه ایجاد کنید.")

        if not (1 <= self.ordering <= 3):
            raise ValidationError("ترتیب باید بین ۱ و ۳ باشد.")

        if self.pk is not None:
            original = WorkField.objects.get(pk=self.pk)
            if original.ordering != self.ordering:
                super().save(*args, **kwargs)
            else:
                raise ValidationError("فقط می‌توانید فیلد ترتیب را به‌روزرسانی کنید.")
        else:
            super().save(*args, **kwargs)


    def __str__(self):
        return self.title


class Manager(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام مدیر")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="عکس")
    description = models.TextField(verbose_name="توضیحات")
    ordering = models.PositiveIntegerField(unique=True, verbose_name="ترتیب")

    class Meta:
        verbose_name = "مدیر"
        verbose_name_plural = "مدیران"

    def save(self, *args, **kwargs):
        if self.pk is None and Manager.objects.count() >= 5:
            raise ValidationError("حداکثر می‌توانید ۵ مدیر ایجاد کنید.")

        if not (1 <= self.ordering <= 5):
            raise ValidationError("ترتیب باید بین ۱ و ۵ باشد.")

        if self.pk is not None:
            original = Manager.objects.get(pk=self.pk)
            if original.ordering != self.ordering:
                super().save(*args, **kwargs)
            else:
                raise ValidationError("فقط می‌توانید فیلد ترتیب را به‌روزرسانی کنید.")
        else:
            super().save(*args, **kwargs)

    # def delete(self, *args, **kwargs):
    #     raise ValidationError("حذف نمونه‌های مدیر مجاز نیست.")

    def __str__(self):
        return self.name


class Certificate(models.Model):
    image = models.ImageField(upload_to='photos/certificates/%Y/%m/%d/', verbose_name="عکس گواهینامه")
    title = models.CharField(max_length=100, verbose_name="عنوان گواهینامه")
    description = models.TextField(verbose_name="توضیحات گواهینامه")

    class Meta:
        verbose_name = "گواهینامه"
        verbose_name_plural = "گواهینامه‌ها"

    def __str__(self):
        return self.title



class Soical(models.Model):
    soical_choices = (
        ('اینستاگرام', 'instagram'),
        ('تلگرام', 'telegram'),
        ('واتساپ', 'whatsapp'),
        ('تویتر', 'twitter')
    )
    soical = models.CharField(max_length=100, choices=soical_choices, unique=True)
    link = models.URLField()

    class Meta:
        verbose_name = 'شبکه ی اجتماعی'
        verbose_name_plural = 'شبکه های اجتماعی'

    def __str__(self):
        return self.soical

class NumberModel(models.Model):
    number = models.CharField(max_length=30)
    ordering = models.PositiveIntegerField(unique=True, verbose_name="ترتیب")
    def __str__(self):
        return self.number


class EmailModel(models.Model):
    email = models.CharField(max_length=100)
    ordering = models.PositiveIntegerField(unique=True, verbose_name="ترتیب")

    def __str__(self):
        return self.email