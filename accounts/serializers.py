from rest_framework import serializers
from .models import UserAccount, Diroctor, Vendor, Baker, Client
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _


class UserChangePasswordSerializer(serializers.Serializer):
    model = UserAccount

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)


    def validate(self, attrs):
        new = attrs.get('new_password')
        new1 = attrs.get('new_password1')
        if new1 == new:
            raise serializers.ValidationError("Xatolik! Yangi parollar ikki xil kiritildi!")
        return attrs


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    token_class = RefreshToken

    default_error_messages = {
        "no_active_account": _("No active account found with the given credentials")
    }

    def validate(self, attrs):
        authenticate_kwargs = {
            'username': attrs['username'],
            "password": attrs["password"],
        }
        try:
            authenticate_kwargs["request"] = self.context["request"]
        except KeyError:
            pass

        user = authenticate(**authenticate_kwargs)
        refresh = self.get_token(user)

        attrs["refresh"] = str(refresh)
        attrs["access"] = str(refresh.access_token)

        del attrs['usrname'], attrs['password']

        return attrs

    @classmethod
    def get_token(cls, user):
        return cls.token_class.for_user(user)


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id','username', 'email']
        extra_kwargs = {
            'password':{'write_only':True}
        }


class DiroctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diroctor
        fields = ['id','username', 'email', 'password', 'type']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    
    def validate_type(self, value):
        user = Diroctor.objects.all()
        
        if user is not None:
            raise ValidationError({"msg":"Bizda director bor?"})
        return value


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id','username', 'email']
        extra_kwargs = {
            'password':{'write_only':True}
        }


class BakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baker
        fields = ['id','username', 'email']
        extra_kwargs = {
            'password':{'write_only':True}
        }


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id','username', 'email']
        extra_kwargs = {
            'password':{'write_only':True}
        }