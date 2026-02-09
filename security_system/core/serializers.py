from rest_framework import serializers
from .models import Application, UserApplicationAccess, User

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'name', 'code']

class UserAccessSerializer(serializers.ModelSerializer):
    application = ApplicationSerializer()

    class Meta:
        model = UserApplicationAccess
        fields = ['application']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'role']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data.get('role', 'NORMAL')
        )
        return user