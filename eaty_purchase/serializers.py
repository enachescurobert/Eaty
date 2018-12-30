from django.contrib.auth.models import User, Group
from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers, status
from eaty_purchase.models import Session
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = "__all__" 

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class SessionSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    class Meta:
        model = Session
        fields = ('id','coffe','cake','user')
        read_only_fields=('first_name','last_name','username')


    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        student, created = Session.objects.update_or_create(user=user,
                            coffe=validated_data.pop('coffe'),
                            cake=validated_data.pop('cake'))
        return student


    def update(self, instance, validated_data):
        instance.coffe = validated_data.get('coffe', instance.coffe)
        instance.cake = validated_data.get('cake', instance.cake)

        instance.save()

        sessions = validated_data.get('sessions')

        return instance