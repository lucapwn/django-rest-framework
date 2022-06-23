from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.api import serializers
from users.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated,)
