from django.db import models
from django.core.exceptions import ValidationError

class WorkTags(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    link = models.URLField(verbose_name="لینک")

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
    image = models.ImageField(blank=True, null=True, verbose_name="تصویر")

    class Meta:
        verbose_name = "حوزه کاری"
        verbose_name_plural = "حوزه‌های کاری"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk is None and WorkField.objects.count() >= 3:
            raise ValidationError("حداکثر می‌توانید ۳ حوزه ایجاد کنید.")

        if not (1 <= self.ordering <= 3):
            raise ValidationError("ترتیب باید بین ۱ و ۳ باشد.")

        super().save(*args, **kwargs)

class WorkTitle(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    work_field = models.ForeignKey(WorkField, on_delete=models.CASCADE, verbose_name="حوزه کاری")

    class Meta:
        verbose_name = "عنوان کاری"
        verbose_name_plural = "عناوین کاری"

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

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk is None and Manager.objects.count() >= 5:
            raise ValidationError("حداکثر می‌توانید ۵ مدیر ایجاد کنید.")

        if not (1 <= self.ordering <= 5):
            raise ValidationError("ترتیب باید بین ۱ و ۵ باشد.")

        super().save(*args, **kwargs)

class ManagerTitle(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان مدیر")
    description = models.TextField(verbose_name="توضیحات مدیر")
    managers = models.ForeignKey(Manager, on_delete=models.CASCADE, verbose_name="مدیر")

    class Meta:
        verbose_name = "عنوان مدیر"
        verbose_name_plural = "عناوین مدیران"

    def __str__(self):
        return self.title

class Certificate(models.Model):
    image = models.ImageField(upload_to='photos/certificates/%Y/%m/%d/', verbose_name="عکس گواهینامه")
    title = models.CharField(max_length=100, verbose_name="عنوان گواهینامه")
    description = models.TextField(verbose_name="توضیحات گواهینامه")

    class Meta:
        verbose_name = "گواهینامه"
        verbose_name_plural = "گواهینامه‌ها"

    def __str__(self):
        return self.title

class CertificateTitle(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان گواهینامه")
    description = models.TextField(verbose_name="توضیحات گواهینامه")
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE, verbose_name="گواهینامه")

    class Meta:
        verbose_name = "عنوان گواهینامه"
        verbose_name_plural = "عناوین گواهینامه‌ها"

    def __str__(self):
        return self.title


class Hero(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")

    class Meta:
        verbose_name = "هیرو"
        verbose_name_plural = "هیروها"

    def __str__(self):
        return self.title

class HeroButton(models.Model):
    hero = models.ForeignKey(Hero, related_name="buttons", on_delete=models.CASCADE, verbose_name="هیرو")
    title = models.CharField(max_length=255, verbose_name="عنوان دکمه")
    link = models.URLField(verbose_name="لینک دکمه")

    class Meta:
        verbose_name = "دکمه هیرو"
        verbose_name_plural = "دکمه‌های هیرو"

    def __str__(self):
        return self.title

class HeroImage(models.Model):
    hero = models.ForeignKey(Hero, related_name="images", on_delete=models.CASCADE, verbose_name="هیرو")
    alt = models.CharField(max_length=255, verbose_name="متن جایگزین")
    link = models.FileField(upload_to='photos/images/%Y/%m/%d/', verbose_name="لینک تصویر")

    class Meta:
        verbose_name = "تصویر هیرو"
        verbose_name_plural = "تصاویر هیرو"

    def __str__(self):
        return self.alt

class HeroLogo(models.Model):
    hero = models.OneToOneField(Hero, related_name="logo", on_delete=models.CASCADE, verbose_name="هیرو")
    alt = models.CharField(max_length=255, verbose_name="متن جایگزین")
    link = models.FileField(verbose_name="لینک لوگو")

    class Meta:
        verbose_name = "لوگو هیرو"
        verbose_name_plural = "لوگوهای هیرو"

    def __str__(self):
        return self.alt

class HeroBodyLogo(models.Model):
    hero = models.OneToOneField(Hero, related_name="bodylogo", on_delete=models.CASCADE, verbose_name="هیرو")
    alt = models.CharField(max_length=255, verbose_name="متن جایگزین")
    link = models.FileField(verbose_name="لینک لوگو بدن")

    class Meta:
        verbose_name = "لوگو بدن هیرو"
        verbose_name_plural = "لوگوهای بدن هیرو"

    def __str__(self):
        return self.alt

class Demo(models.Model):
    image = models.ImageField(upload_to='demo/', verbose_name="تصویر")
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.CharField(max_length=255, verbose_name="زیرعنوان")
    description = models.TextField(verbose_name="توضیحات")

    class Meta:
        verbose_name = "دمو"
        verbose_name_plural = "دموها"

    def __str__(self):
        return self.title

class DemoForm(models.Model):
    demo = models.OneToOneField(Demo, related_name='form', on_delete=models.CASCADE, verbose_name="دمو")
    title = models.CharField(max_length=255, verbose_name="عنوان فرم")
    description = models.TextField(verbose_name="توضیحات فرم")

    class Meta:
        verbose_name = "فرم دمو"
        verbose_name_plural = "فرم‌های دمو"

    def __str__(self):
        return self.title

class AboutUs(models.Model):
    image = models.ImageField(upload_to='about/', verbose_name="تصویر")
    title = models.CharField(max_length=255, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"

    def __str__(self):
        return self.title

class AboutProject(models.Model):
    about = models.ForeignKey(AboutUs, related_name='projects', on_delete=models.CASCADE, verbose_name="درباره ما")
    title = models.CharField(max_length=255, verbose_name="عنوان پروژه")
    description = models.TextField(verbose_name="توضیحات پروژه")

    class Meta:
        verbose_name = "پروژه درباره ما"
        verbose_name_plural = "پروژه‌های درباره ما"

    def __str__(self):
        return self.title


from django.db import models

class Footer(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    address = models.CharField(max_length=255, verbose_name="آدرس")
    copyright = models.CharField(max_length=255, verbose_name="کپی رایت")

    class Meta:
        verbose_name = "فوتر"
        verbose_name_plural = "فوترها"

    def __str__(self):
        return self.title


class FooterSocial(models.Model):
    soical_choices = (
        ('اینستاگرام', 'instagram'),
        ('تلگرام', 'telegram'),
        ('واتساپ', 'whatsapp'),
        ('تویتر', 'twitter')
    )
    soical = models.CharField(max_length=100, choices=soical_choices, unique=True, verbose_name="شبکه اجتماعی")
    footer = models.ForeignKey(Footer, related_name="socials", on_delete=models.CASCADE, verbose_name="فوتر")
    link = models.URLField(verbose_name="لینک")

    class Meta:
        verbose_name = "شبکه اجتماعی فوتر"
        verbose_name_plural = "شبکه‌های اجتماعی فوتر"

    def __str__(self):
        return self.alt


class FooterEmail(models.Model):
    footer = models.ForeignKey(Footer, related_name="emails", on_delete=models.CASCADE, verbose_name="فوتر")
    email = models.EmailField(verbose_name="ایمیل")

    class Meta:
        verbose_name = "ایمیل فوتر"
        verbose_name_plural = "ایمیل‌های فوتر"

    def __str__(self):
        return self.email


class FooterPhone(models.Model):
    footer = models.ForeignKey(Footer, related_name="phones", on_delete=models.CASCADE, verbose_name="فوتر")
    phone = models.CharField(max_length=30, verbose_name="شماره تلفن")

    class Meta:
        verbose_name = "تلفن فوتر"
        verbose_name_plural = "تلفن‌های فوتر"

    def __str__(self):
        return self.phone
