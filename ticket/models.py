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