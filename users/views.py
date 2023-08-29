from django.db.models import Q
from rest_framework.views import APIView
from . import serializers
from . import models
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import generics

class SignInAPIView(APIView):
    serializer_class = serializers.SignInSerializers

    def post(self, request, *args, **kwargs):
        serializer = serializers.SignInSerializers(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = models.User.objects.filter(Q(username=username))

        if not user.exists():
            raise ValidationError(
                detail={'msg': 'user not found'},
                code=400
            )
        user = user.first()
        if not user.check_password(password):
            raise ValidationError(
                detail={'msg': 'You entered a wrong password'},
                code=400
            )
        attrs = {
            'username': username,
        }
        attrs.update(user.tokens())
        return Response(
            data={
                'success': True,
                'auth_status': user.auth_status,
                "access": user.tokens()['access'],
                "refresh": user.tokens()['refresh'],
            },
            status=200
        )


class BranchListAPIView(generics.ListAPIView):
    serializer_class = serializers.BranchListSerializer
    queryset = models.Branch.objects.all()


class UserBranchSerializer(generics.ListAPIView):
    serializer_class = serializers.BranchUserListSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = models.UserBranch.objects.filter(user=user)
        return queryset
