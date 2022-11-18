from django.db import models
from .enums import UserRole
from django.contrib.auth.models import  AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from .manager import (  UserManager, 
                        DiroctorManager,
                        BakerManager,
                        VendorManager,
                        ClientManager,
                        StaffManager
                )


class UserAccount(AbstractUser):
    username = models.CharField(max_length=256, unique=True)      
    role = models.CharField(max_length=8, choices = UserRole.choices(), default=UserRole.CLIENT.value)
    email = models.EmailField(max_length=200, unique = True)
    phone = PhoneNumberField(null = True, blank = True)
    is_director = models.BooleanField(default = False)
    is_baker = models.BooleanField(default = False)
    is_vendor = models.BooleanField(default = False)
    is_client = models.BooleanField(default = False)
    is_email_verify = models.BooleanField(default=False)
    code = models.CharField(max_length=6, null=True, blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['password', 'email']

    objects = UserManager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name = 'Bitta director',
                fields = ['role'],
                condition = models.Q(role = UserRole.DIRECTOR.value)
            )
        ]
    
    def __str__(self):
        return self.username


class Diroctor(UserAccount):
    objects = DiroctorManager()

    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        self.set_password(self.password)
        self.type = UserRole.DIRECTOR.value
        self.is_director = True
        self.is_superuser = True
        self.is_staff = True
        return super(Diroctor, self).save(*args, **kwargs)
    

class Vendor(UserAccount):
    objects = VendorManager()

    class Meta :
        proxy = True
      
    def save(self , *args , **kwargs):
        self.set_password(self.password)
        self.type = UserRole.VENDOR.value
        self.is_teacher = True
        return super(Vendor, self).save(*args , **kwargs)


class Baker(UserAccount):
    objects = BakerManager()

    class Meta : 
        proxy = True
      
    def save(self , *args , **kwargs):
        self.set_password(self.password)
        self.type = UserRole.BAKER.value
        self.is_baker = True
        return super(Baker, self).save(*args , **kwargs)


class Client(UserAccount):
    objects = ClientManager()

    class Meta : 
        proxy = True
      
    def save(self , *args , **kwargs):
        self.set_password(self.password)
        self.type = UserRole.CLIENT.value
        self.is_student = True
        return super(Client,self).save(*args , **kwargs)
    
    def __str__(self):
        return self.username


class Staff(UserAccount):
    objects = StaffManager()

    class Meta:
        proxy = True
