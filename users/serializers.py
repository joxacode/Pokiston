from rest_framework import serializers
from . import models


class SignInSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)


class BranchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Branch
        fields = (
            'id',
            'name',
        )


class BranchUserListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    branch = BranchListSerializer()

    class Meta:
        model = models.UserBranch
        fields = (
            'id',
            'branch',
            'user',
        )


class BranchNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Branch
        fields = ('id', 'name',)


class ResetPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate(self, data):
        new_password1 = data.get('new_password1')
        new_password2 = data.get('new_password2')

        if new_password1 != new_password2:
            raise serializers.ValidationError("New passwords must match.")


        return data


class ForgotPasswordSerializer(serializers.Serializer):
    new_password1 = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate(self, data):
        new_password1 = data.get('new_password1')
        new_password2 = data.get('new_password2')

        if new_password1 != new_password2:
            raise serializers.ValidationError("New passwords must match.")

        return data


class GetUserNameSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)


class UserBranchSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = models.UserBranch
        fields = ('user', 'branch')


