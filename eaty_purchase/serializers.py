from django.contrib.auth.models import User, Group
from rest_framework import serializers, status
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
    # user = UserSerializer(required=True)
    class Meta:
        model = Session
        fields = ('id','coffe','cake','user')

    # def create(self, validated_data):
    #     """
    #     Overriding the default create method of the Model serializer.
    #     :param validated_data: data containing all the details of student
    #     :return: returns a successfully created student record
    #     """
    #     user_data = validated_data.pop('user')
    #     user = UserSerializer.create(UserSerializer(), validated_data=user_data)
    #     student, created = Session.objects.update_or_create(user=user,
    #                         coffe=validated_data.pop('coffe'),
    #                         cake=validated_data.pop('cake'))
    #     return student

    