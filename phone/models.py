from django.db import models
from slugify import slugify 

class Phone(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерируем slug только если он пустой
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
