from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('email', 'password', 'confirm_password')

    def validate(self, attrs):
        # 1. Verify passwords match
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields did not match."})

        # 2. Enforce strong password rules (Argon2 / Length / Complexity)
        validate_password(attrs['password'])

        return attrs

    def create(self, validated_data):
        # Remove confirm_password before creating the user
        validated_data.pop('confirm_password')
        
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        # Authenticate user using the Custom User Model
        user = authenticate(
            request=self.context.get('request'),
            email=email,
            password=password
        )

        # Security Best Practice: Return generic error message for both cases
        if not user:
            raise serializers.ValidationError({"detail": "Invalid email or password."})

        attrs['user'] = user
        return attrs