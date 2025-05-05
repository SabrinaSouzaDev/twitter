from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.accounts.serializers import CustomTokenObtainPairSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

User = get_user_model()

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    @method_decorator(cache_page(60 * 5))
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    #   @method_decorator(cache_page(60 * 5))
    # def get(self, request, *args, **kwargs):
    #     return Response({
    #         'username': request.user.username,
    #         'email': request.user.email,
    #         'first_name': request.user.first_name,
    #         'last_name': request.user.last_name,
    #         'bio': request.user.bio
    #     })

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()  # Alteração aqui
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()  # Alteração aqui
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CustomTokenRefreshView(TokenRefreshView):
    pass
