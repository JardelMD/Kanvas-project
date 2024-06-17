from accounts.models import Account
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ["id", "email", "username", "password", "is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_email(self, email_exists):
        if Account.objects.filter(email=email_exists).exists():
            raise ValidationError(
                "user with this email already exists.", status.HTTP_400_BAD_REQUEST
            )
        return email_exists

    def validate_username(self, username_exists):
        if Account.objects.filter(username=username_exists).exists():
            raise ValidationError(
                "A user with that username already exists.", status.HTTP_400_BAD_REQUEST
            )
        return username_exists

    def create(self, validated_data: dict):
        return Account.objects.create_user(**validated_data)
