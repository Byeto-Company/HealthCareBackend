from accounts.serializers import UserSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User

class UserView(APIView):

    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        user = request.user
        user_ser = UserSerializer(user)
        return Response(user_ser.data, status=status.HTTP_200_OK)
    def put(self, request):
        user = request.user
        user_ser = UserSerializer(instance=user, data=request.data)
        if user_ser.is_valid():
            user_ser.save()
            return Response(user_ser.data, status=status.HTTP_200_OK)
        return Response(user_ser.errors, status=status.HTTP_400_BAD_REQUEST)