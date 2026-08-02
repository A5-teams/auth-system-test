from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.throttling import ScopedRateThrottle
from axes.decorators import axes_dispatch
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied

class RegisterView(APIView):
    """
    API endpoint for handling secure user registration.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully."},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(axes_dispatch, name='dispatch')
class LoginView(APIView):
    """
    Secure API endpoint for handling user authentication with HttpOnly Cookies and Account Lockout.
    """
    permission_classes = [AllowAny]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'login_attempts'

    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                user = serializer.validated_data['user']
                
                # Generate JWT tokens
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)

                response = Response(
                    {"message": "Login successful."},
                    status=status.HTTP_200_OK
                )

                # Security Hardened HttpOnly Cookie Setup
                response.set_cookie(
                    key='access_token',
                    value=access_token,
                    httponly=True,       # Prevents XSS token theft
                    secure=False,        # Set to True in HTTPS production
                    samesite='Lax',      # Prevents CSRF attacks
                    max_age=15 * 60      # Expires in 15 minutes
                )

                response.set_cookie(
                    key='refresh_token',
                    value=refresh_token,
                    httponly=True,
                    secure=False,
                    samesite='Lax',
                    max_age=24 * 60 * 60 # Expires in 1 day
                )

                return response

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except PermissionDenied:
            # django-axes አካውንቱን ሲቆልፈው የሚመጣ Exception
            return Response(
                {"detail": "Too many failed login attempts. Account temporarily locked for 15 minutes."},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )