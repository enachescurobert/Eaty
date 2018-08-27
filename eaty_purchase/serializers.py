from django.contrib.auth.models import User, Group
from rest_framework import serializers
from eaty_purchase.models import Session


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class SessionSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Session
        fields = ('id','coffe','cake','user')