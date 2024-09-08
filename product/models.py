from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام")
    description = models.TextField(verbose_name="توضیحات")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name="دسته‌بندی والد")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        # Return the full breadcrumb path for the category
        full_path = [self.name]
        parent = self.parent
        while parent is not None:
            full_path.append(parent.name)
            parent = parent.parent
        return ' > '.join(full_path[::-1])

#TODO handle updateing with empty feature and detail
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام محصول")
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, allow_unicode=True, verbose_name='نام یکتا')
    description = models.TextField(verbose_name="توضیحات محصول")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته‌بندی")
    main_photo = models.ImageField(upload_to=f'fproduct/main_photos', verbose_name="عکس اصلی")  
    secend_photo = models.ImageField(upload_to=f'fproduct/secend_photos', verbose_name='عکس دوم صفحه ی محصولات')
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


class Detail(models.Model):
    product = models.ForeignKey(Product, related_name='details', on_delete=models.CASCADE, verbose_name='محصول')
    detail_text = models.CharField(max_length=100, verbose_name='متن جزیات', blank=True)

    class Meta:
        verbose_name = "جز"
        verbose_name_plural = "جزیات"

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
    
    