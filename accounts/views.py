from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, response, status
from .models import UserAccount, Diroctor, Vendor, Baker, Client
from .serializers import (
                    UserAccountSerializer, 
                    DiroctorSerializer, 
                    VendorSerializer, 
                    BakerSerializer, 
                    ClientSerializer,
                    LoginSerializer,
                    UserChangePasswordSerializer
                )
from rest_framework.views import APIView
from rest_framework.response import Response
from .email import send_code_email
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken


class RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            serializer = UserAccountSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            send_code_email(serializer.data['email'])
            return Response(data={
                'status': 200,
                'message': f'registration successfull check email',
                'data':serializer.data
            })
        except Exception as e:
            print(e)


class LoginAPIView(generics.GenericAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = LoginSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return response.Response(serializer.validated_data, status=status.HTTP_200_OK)


# Diroctor for ViewSet
class DiroctorViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    def get_queryset(self):
        queryset = Diroctor.objects.all()
        return queryset
    
    def get_serializer_class(self):
        serializer = DiroctorSerializer
        return serializer


# Vendor for ViewSet
class VendorViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    def get_queryset(self):
        queryset = Vendor.objects.all()
        return queryset
    
    def get_serializer_class(self):
        serializer = VendorSerializer
        return serializer
    

# Baker for ViewSet
class BakerViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    def get_queryset(self):
        queryset = Baker.objects.all()
        return queryset
    
    def get_serializer_class(self):
        serializer = BakerSerializer
        return serializer


# Client for ViewSet
class ClientViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    def get_queryset(self):
        queryset = Client.objects.all()
        return queryset

    def get_serializer_class(self):
        serializer = ClientSerializer
        return serializer


class UserChangePasswordAPIView(generics.UpdateAPIView):
    serializer_class = UserChangePasswordSerializer
    model = UserAccount
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)