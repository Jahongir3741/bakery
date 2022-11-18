from django.contrib.auth.models import BaseUserManager
from .enums import UserRole

  
class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        user = self.model(
            email = self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
      
    def create_superuser(self , username , password, email):
        user = self.create_user(
            username=username, 
            password=password,
            email=email
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user


class DiroctorManager(UserManager):
    def get_queryset(self , *args,  **kwargs):
        print(UserRole.DIRECTOR.value)
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(role=UserRole.DIRECTOR.name)
        return queryset


class BakerManager(UserManager):    
    def get_queryset(self , *args,  **kwargs):
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(role = UserRole.BAKER.name)
        return queryset


class VendorManager(UserManager):
    def get_queryset(self , *args,  **kwargs):
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(role = UserRole.VENDOR.name)
        return queryset


class ClientManager(UserManager):
    def get_queryset(self , *args,  **kwargs):
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(role = UserRole.CLIENT.name)
        return queryset


class StaffManager(UserManager):
    def get_queryset(self):
        return super(StaffManager, self).get_queryset().filter(
                    role__in=(
                        UserRole.DIRECTOR.name, 
                        UserRole.BAKER.name,
                        UserRole.VENDOR.name,
                    )
                )
