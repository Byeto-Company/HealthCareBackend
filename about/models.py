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

    class Meta:
        verbose_name = "حوزه کاری"
        verbose_name_plural = "حوزه‌های کاری"

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

    def delete(self, *args, **kwargs):
        raise ValidationError("حذف نمونه‌های مدیر مجاز نیست.")

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