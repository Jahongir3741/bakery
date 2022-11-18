from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .utils import bread_url
from accounts.models import Diroctor
from django.core.exceptions import ValidationError

class AbcractModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    uspdate = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Bakery(AbcractModel):
    creator = models.ForeignKey(
                        'accounts.Staff', 
                        on_delete=models.SET_NULL, 
                        null=True, blank=True, 
                        related_name='bakeries'
                )
    owner = models.ForeignKey(Diroctor, on_delete=models.CASCADE, related_name='owner_bakery')
    name = models.CharField(max_length=128)
    location =models.CharField(max_length=128, unique=True)
    phone = PhoneNumberField(unique=True)
    is_active = models.BooleanField(default=True)
    open_at = models.TimeField()
    close_at = models.TimeField()
    is_deleted = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'location'],
                name='location'
            )
        ]
    
    def __str__(self):
        return self.name


class Bread(AbcractModel):
    creator = models.ForeignKey(
                        'accounts.Staff', 
                        on_delete=models.SET_NULL, 
                        null=True, blank=True, 
                        related_name='breans'
                )
    name = models.CharField(max_length=128)
    category = models.ForeignKey('category.Category', on_delete=models.PROTECT, related_name='categories')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    text = models.TextField()
    image = models.URLField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name='name_and_category_unique',
                fields=['name', 'category'],
                )
        ]

    def __str__(self):
        return self.name
    

class BreadItem(AbcractModel):
    creator = models.ForeignKey(
                        'accounts.Staff', 
                        on_delete=models.SET_NULL, 
                        null=True, blank=True, 
                        related_name='breaditems'
                )
    bread = models.ForeignKey(Bread, on_delete=models.CASCADE, related_name="breads")
    count = models.PositiveIntegerField()

    def counts(self, value):
        if self.count < value:
            raise ValidationError({"msg":f"Kichirasiz bizda { self.count } ta non qoldin"})
        self.count -= value
        self.save()

    def __str__(self):
        return f"{self.bread} {self.count}"
    