from itertools import product

from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام")
    description = models.TextField(verbose_name="توضیحات")
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, allow_unicode=True,
                            verbose_name='نام یکتا')
    show_count_in_main = models.BooleanField(default=False, verbose_name='نمایش در صفحه ی اصلی',
                                             help_text="در صورت روشن بودن این فیلد در پایین صفحه ی خانه تعداد محصولات این دسته بندی نمایش داده میشود ")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        if self.slug:
            return self.slug
        else:
            return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._slug_generate()

        super().save(*args, **kwargs)

    def _slug_generate(self):
        initial_slug = slugify(self.name)
        slug = initial_slug
        count = 1
        while Category.objects.filter(slug=slug).exists():
            slug = f"{initial_slug}-{count}"
            count += 1
        return  slug


#TODO handle updateing with empty feature and detail
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام محصول")
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, allow_unicode=True,
                            verbose_name='نام یکتا')
    meta_title = models.CharField(max_length=30, verbose_name='متا تایتل')
    meta_description = models.TextField(verbose_name='متا تگ دسکریپشن')
    meta_keyword = models.TextField(help_text='لطفا با کاما وارد کنید', verbose_name='متا تگ کیورد')
    description = models.TextField(verbose_name="توضیحات محصول")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته‌بندی")
    thumbnail = models.ImageField(upload_to=f'fproduct/main_photos', verbose_name="عکس اصلی")
    product_icon_photo = models.ImageField(upload_to=f'fproduct/icons', verbose_name='عکس ایکون لیست محصولات')


    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_slug()
        super().save(*args, **kwargs)

    def _generate_slug(self):
        initial_slug = slugify(self.name, allow_unicode=True)
        slug = initial_slug
        count = 1
        while Product.objects.filter(slug=slug).exists():
            slug = f"{initial_slug}-{count}"
            count += 1
        return slug


class Slide(models.Model):
    product = models.ForeignKey(Product, related_name='slides', on_delete=models.CASCADE, verbose_name='محصول')
    image = models.ImageField(upload_to="product_slides/", verbose_name="تصویر")
    description = models.TextField(verbose_name="توضیحات")

    def __str__(self):
        return self.product.name + self.image.name


class Capability(models.Model):
    product = models.ForeignKey(Product, related_name='capability', on_delete=models.CASCADE, verbose_name='محصول')
    detail_text = models.CharField(max_length=100, verbose_name='قابلیت', blank=True)

    class Meta:
        verbose_name = "قابلیت"
        verbose_name_plural = "قابلیت ها"

    def __str__(self):
        return f"{self.product}: {self.detail_text[:30]}"


class Feature(models.Model):
    product = models.ForeignKey(Product, related_name='features', on_delete=models.CASCADE, verbose_name='محصول')
    feature_text = models.TextField(verbose_name='ویژگی', blank=True)

    class Meta:
        verbose_name = "ویژگی"
        verbose_name_plural = "ویژگی‌ها"

    def __str__(self):
        return f"{self.product}: {self.feature_text[:30]}"
