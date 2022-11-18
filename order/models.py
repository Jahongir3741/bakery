from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .enums import Status


class AbcractModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    uspdate = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        abstract = True


class Order(AbcractModel):
    client = models.ForeignKey('accounts.Client', on_delete=models.PROTECT)
    location = models.CharField(max_length=200)
    phone = PhoneNumberField()
    status = models.CharField(max_length=12, choices=Status.choices(), default=Status.NEW.value)
    time = models.TimeField(auto_now_add=True)

    def confirmed(self):
        self.status = Status.CONFIRMED.name
        self.save()
    
    def cancel(self):
        self.status = Status.CANCELLED.name
        self.save()
    
    def success(self):
        self.status = Status.SUCCESS.name
        self.save()


class OrderItem(AbcractModel):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='orders')
    bread_item = models.ForeignKey('bakery.BreadItem', on_delete=models.SET_NULL, null=True, related_name='breadss')
    count = models.PositiveIntegerField()

    def get_total_price(self):
        return self.count * self.bread_item.count
