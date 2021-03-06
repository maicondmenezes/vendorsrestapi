from django.db import models
from django.urls import reverse

from model_utils.models import TimeStampedModel
from localflavor.br.models import BRCNPJField


class AvailableManager(models.Manager):
    """
    Custom manager to filter only active products
    """

    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class Vendor(TimeStampedModel):
    """
    Model to resgistrate a vendor in database;
    Note that if you delete a vendor from database by default all related products are remove
    """

    name = models.CharField(max_length=200)
    cnpj = BRCNPJField(unique=True)
    city = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "vendor"
        verbose_name_plural = "vendors"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalogue:vendor-detail", kwargs={"pk": self.pk})


class Product(TimeStampedModel):
    """
    Model to resgistrate a product linked only a single vendor in database;
    Note that if you delete a vendor from database by default all related products are remove
    """

    vendor = models.ForeignKey(
        Vendor, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True)
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = (
            "name",
            "price",
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):

        return reverse("catalogue:product-detail", kwargs={"pk": self.pk})
