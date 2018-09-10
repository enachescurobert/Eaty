from django.contrib.auth.models import User, Group
from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers, status
from eaty_purchase.models import Session


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        id = serializers.IntegerField(required=False)
        model = User
        fields = ('id','first_name','last_name', 'username', 'email','groups')
        # read_only_fields=('username',)

        # read_only_fields=('username',)
        # depth = 1
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()],
            }
}


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
        # exclude = ('permissions',)
        # read_only_fields=('permissions',)
        # depth = 1

class SessionSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=True)
    # user = UserSerializer(required=True)
    # user = UserSerializer(read_only=True)
    # user = UserSerializer()
    user = UserSerializer()
    class Meta:
        model = Session
        fields = ('id','coffe','cake','user')
        read_only_fields=('first_name','last_name','username')

        # fields = "__all__"
        # depth = 1   
   
   
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

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
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

        # for session in sessions:
        #     session_id = session.get('id', None)
        #     if session_id:
        #         inv_session = Session.objects.get(id=session_id, invoice=instance)
        #         inv_session.coffe = session.get('coffe', inv_session.coffe)
        #         inv_session.cake = session.get('cake', inv_session.cake)
        #         inv_session.save()
        #     else:
        #         Session.objects.create(account=instance, **session)

        return instance