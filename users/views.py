from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserDetailSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['username', 'email', 'profile__hometown', 'profile__age', 'profile__gender']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetailSerializer
        return UserSerializer