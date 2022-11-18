from django.db import models

class AbcractModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    uspdate = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        abstract = True


class Category(AbcractModel):
    name = models.CharField(max_length=128, unique=True)
    parent = models.ForeignKey('self', 
                        on_delete=models.CASCADE, 
                        null=True, blank=True, 
                        related_name='child',
                        limit_choices_to={"is_deleted":False}
                    )
    creator = models.ForeignKey(
                        'accounts.Staff', 
                        on_delete=models.SET_NULL, 
                        null=True, blank=True, 
                        related_name='category'
                    )
    
    def __str__(self):
        return self.name
    

