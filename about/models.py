from django.db import models
from django.core.exceptions import ValidationError


class WorkTags(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    link = models.URLField()
    class Meta:
        verbose_name = "برچسب کاری"
        verbose_name_plural = "برچسب‌های کاری"

    def __str__(self):
        return self.title


class WorkField(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان حوزه")
    description = models.TextField(verbose_name="توضیحات حوزه")
    tags = models.ManyToManyField(WorkTags, verbose_name="برچسب‌ها")
    ordering = models.PositiveIntegerField(unique=True, verbose_name="ترتیب")
    image = models.ImageField(blank=True, null=True)
    class Meta:
        verbose_name = "حوزه کاری"
        verbose_name_plural = "حوزه‌های کاری"

    def save(self, *args, **kwargs):
        if self.pk is None and WorkField.objects.count() >= 3:
            raise ValidationError("حداکثر می‌توانید ۳ حوزه ایجاد کنید.")

        if not (1 <= self.ordering <= 3):
            raise ValidationError("ترتیب باید بین ۱ و ۳ باشد.")


        # ?

        # if self.pk is not None:
        #     original = WorkField.objects.get(pk=self.pk)
        #     if original.ordering != self.ordering:
        #         super().save(*args, **kwargs)
        #     else:
        #         raise ValidationError("فقط می‌توانید فیلد ترتیب را به‌روزرسانی کنید.")
        # else:  
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title


class Manager(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام مدیر")
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="عکس")
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

        # if self.pk is not None:
        #     original = Manager.objects.get(pk=self.pk)
        #     if original.ordering != self.ordering:
        #         super().save(*args, **kwargs)
        #     else:
        #         raise ValidationError("فقط می‌توانید فیلد ترتیب را به‌روزرسانی کنید.")
        # else:
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


class Hero(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


class HeroButton(models.Model):
    hero = models.ForeignKey(Hero, related_name="buttons", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link = models.URLField()


class HeroImage(models.Model):
    hero = models.ForeignKey(Hero, related_name="images", on_delete=models.CASCADE)
    alt = models.CharField(max_length=255)
    link = models.FileField(upload_to='photos/images/%Y/%m/%d/')


class HeroLogo(models.Model):
    hero = models.OneToOneField(Hero, related_name="logo", on_delete=models.CASCADE)
    alt = models.CharField(max_length=255)
    link = models.FileField()

class HeroBodyLogo(models.Model):
    hero = models.OneToOneField(Hero, related_name="bodylogo", on_delete=models.CASCADE)
    alt = models.CharField(max_length=255)
    link = models.FileField()


class Demo(models.Model):
    image = models.ImageField(upload_to='demo/')
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()


class DemoForm(models.Model):
    demo = models.OneToOneField(Demo, related_name='form', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()


class AboutUs(models.Model):
    image = models.ImageField(upload_to='about/')
    title = models.CharField(max_length=255)
    description = models.TextField()


class AboutProject(models.Model):
    about = models.ForeignKey(AboutUs, related_name='projects', on_delete=models.CASCADE)
    count = models.IntegerField()
    title = models.CharField(max_length=255)


class Footer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    copyright = models.CharField(max_length=255)


class FooterSocial(models.Model):
    footer = models.ForeignKey(Footer, related_name="socials", on_delete=models.CASCADE)
    icon = models.CharField(max_length=100)
    alt = models.CharField(max_length=100)
    link = models.URLField()


class FooterEmail(models.Model):
    footer = models.ForeignKey(Footer, related_name="emails", on_delete=models.CASCADE)
    email = models.EmailField()


class FooterPhone(models.Model):
    footer = models.ForeignKey(Footer, related_name="phones", on_delete=models.CASCADE)
    phone = models.CharField(max_length=30)
