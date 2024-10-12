from django.db import models


class RequestDemo(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    phone_number = models.CharField(max_length=15, verbose_name="شماره تلفن")
    company_name = models.CharField(max_length=100, verbose_name="نام شرکت")
    message = models.TextField(verbose_name="پیام", blank=True, null=True)
    module_name = models.CharField(max_length=100, verbose_name="نام ماژول")
    requested_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ درخواست")

    class Meta:
        verbose_name = "درخواست دمو"
        verbose_name_plural = "درخواست‌های دمو"

    def __str__(self):
        return f"درخواست دمو از {self.full_name} - {self.company_name}"


class ContactUs(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    subject = models.CharField(max_length=150, verbose_name="موضوع")
    message = models.TextField(verbose_name="پیام")
    contacted_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ تماس")

    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "تماس‌های دریافت‌شده"

    def __str__(self):
        return f"تماس از {self.full_name} - {self.subject}"


class EndPointSendContactUs(models.Model):
    request_link = models.URLField(verbose_name='لینک پست ارتباط با ما')
    full_name = models.BooleanField(verbose_name="ارسال نام", help_text='ارسال با کلید full_name')
    email = models.BooleanField(verbose_name="ارسال ایمیل", help_text='ارسال با کلید email')
    subject = models.BooleanField(verbose_name="ارسال موضوع", help_text='ارسال با کلید subject')
    message = models.BooleanField(verbose_name="ارسال پیام", help_text='ارسال با کلید message')
    contacted_at = models.BooleanField(verbose_name="ارسال تاریخ تماس", help_text='ارسال با کلید contacted_at')
    class Meta:
        verbose_name = 'لینک پست تیکت تماس با ما'
        verbose_name_plural = 'لینک های پست تیکت تماس با ما'
    def __str__(self):
        return self.request_link


class EndPointSendRequestDemo(models.Model):
    request_link = models.URLField(verbose_name='لینک پست درخواست دمو')
    full_name = models.BooleanField(verbose_name="ارسال نام", help_text='ارسال با کلید full_name')
    email = models.BooleanField(verbose_name="ارسال ایمیل", help_text='ارسال با کلید email')
    phone_number = models.BooleanField(verbose_name="ارسال شماره تلفن", help_text='ارسال با کلید phone_number')
    company_name = models.BooleanField(verbose_name="ارسال نام شرکت", help_text='ارسال با کلید company_name')
    message = models.BooleanField(verbose_name="ارسال پیام", help_text='ارسال با کلید message')
    module_name = models.BooleanField(verbose_name="ارسال نام ماژول", help_text='ارسال با کلید module_name')
    requested_at = models.BooleanField(verbose_name="ارسال تاریخ درخواست", help_text='ارسال با کلید requested_at')

    class Meta:
        verbose_name = 'لینک پست درخواست دمو'
        verbose_name_plural = 'لینک های پست درخواست دمو'

    def __str__(self):
        return self.request_link

class LogTicket(models.Model):
    status_code = models.CharField(max_length=10, blank=True, null=True)
    request_body = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    exception = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.status_code

