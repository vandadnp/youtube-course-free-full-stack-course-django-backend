from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres import fields as PostgresFields


class ProductCategory(models.Model):
    name = models.CharField(max_length=256)
    icon_url = models.URLField(blank=True)
    description = models.TextField()
    parent_category = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="children_categories",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Maker(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Currency(models.TextChoices):
        SWEDISH_CROWN = ("SEK", _("Swedish Crown"))
        AMERICAN_DOLLAR = ("USD", _("American Dollar"))
        EURO = ("EUR", _("Euro"))
        POUND_STERLING = ("GBP", _("Pound Sterling"))
        YEN = ("JPY", _("Yen"))
        AUSTRALIAN_DOLLAR = ("AUD", _("Australian Dollar"))

    title = models.CharField(max_length=512)
    subtitle = models.CharField(max_length=512)

    maker = models.ForeignKey(
        Maker,
        on_delete=models.CASCADE,
        related_name="products",
        blank=True,
        null=True,
    )

    image1_url = models.URLField(blank=True, null=True)
    image2_url = models.URLField(blank=True, null=True)
    image3_url = models.URLField(blank=True, null=True)
    image4_url = models.URLField(blank=True, null=True)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.AMERICAN_DOLLAR,
    )

    variation_product_ids = PostgresFields.ArrayField(
        models.IntegerField(null=True, blank=True),
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.title} - {self.subtitle} - {self.maker}"
