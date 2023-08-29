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
